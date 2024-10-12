import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

import pandas as pd
import io
import sqlite3

from image_processing import create_frame_from_pixels, resize_frame, apply_colormap
from utilities import DATABASE_PATH, IMAGE_FRAMES_CSV_PATH, IMAGE_FORMAT
from custom_logger import logger


def get_db_version():
    """
    Retrieve the current version of the database.

    Returns:
        int: The current version number of the database.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("PRAGMA user_version")
    version = cursor.fetchone()[0]
    conn.close()
    return version


def set_db_version(version):
    """
    Set the version of the database.

    Args:
        version (int): The version number to set for the database.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA user_version = {version}")
    conn.commit()
    conn.close()


def store_image_frame(conn, depth, frame):
    """
    Store an image frame in the database.

    Args:
        conn (sqlite3.Connection): Database connection object.
        depth (float): Depth value associated with the frame.
        frame (Image): PIL Image object to store.
    """
    cursor = conn.cursor()
    frame_byte_arr = io.BytesIO()
    frame.save(frame_byte_arr, format=IMAGE_FORMAT)
    frame_byte_arr = frame_byte_arr.getvalue()

    cursor.execute(
        """
        INSERT OR REPLACE INTO image_frames (depth, frame) VALUES (?, ?)
    """,
        (depth, frame_byte_arr),
    )
    conn.commit()


def initialize_database():
    """
    Initialize the database if it hasn't been initialized already.

    This function checks the database version, creates the necessary table,
    and populates it with image frames from the CSV file if needed.
    """
    current_version = get_db_version()
    if current_version == 1:  # 1 is our current version
        logger.info(
            "Database already initialized and up to date. Skipping initialization."
        )
        return

    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS image_frames (
            depth REAL PRIMARY KEY,
            frame BLOB
        )
    """
    )
    conn.commit()

    df = pd.read_csv(IMAGE_FRAMES_CSV_PATH)
    df = df.fillna(0)
    pixel_columns = df.columns.drop("depth")
    df[pixel_columns] = df[pixel_columns].astype(int)

    depths = df["depth"].values
    pixel_data = df[pixel_columns].values

    for i, (depth, pixels) in enumerate(zip(depths, pixel_data)):
        try:
            logger.info(f"Processing image frame at depth {depth}")
            frame = create_frame_from_pixels(pixels)
            frame = resize_frame(frame)
            frame = apply_colormap(frame)
            store_image_frame(conn, depth, frame)
            if i % 100 == 0:  # Log progress every 100 rows
                logger.info(f"Processed {i} image frames")
        except Exception as e:
            logger.error(f"Error processing image frame at depth {depth}: {str(e)}")

    conn.close()
    set_db_version(1)  # Set to version 1 after successful initialization
    logger.info("Database initialization completed")


def get_image_frames(db_conn, depth_min, depth_max):
    """
    Retrieve image frames from the database within a specified depth range.

    Args:
        db_conn (sqlite3.Connection): Database connection object.
        depth_min (float): Minimum depth value.
        depth_max (float): Maximum depth value.

    Returns:
        list: List of tuples containing depth and frame data.
    """
    cursor = db_conn.cursor()
    cursor.execute(
        """
        SELECT depth, frame FROM image_frames WHERE depth BETWEEN ? AND ?
        ORDER BY depth
    """,
        (depth_min, depth_max),
    )
    return cursor.fetchall()


def get_db_connection():
    """
    Create and yield a database connection.

    Yields:
        sqlite3.Connection: Database connection object.
    """
    db_conn = sqlite3.connect(DATABASE_PATH)
    try:
        yield db_conn
    finally:
        db_conn.close()
