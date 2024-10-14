import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

import pandas as pd
import io
import sqlite3

from image_processing import create_frame_from_pixels, resize_frame, apply_colormap
from utilities import DATABASE_PATH, IMAGE_FRAMES_CSV_PATH, IMAGE_FORMAT
from custom_logger import logger


class ImageDatabase:
    def __init__(
        self,
        database_path=DATABASE_PATH,
        csv_path=IMAGE_FRAMES_CSV_PATH,
        image_format=IMAGE_FORMAT,
    ):
        self.database_path = database_path
        self.csv_path = csv_path
        self.image_format = image_format
        self.logger = logger

    def get_db_version(self):
        """Retrieve the current version of the database."""
        with self.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("PRAGMA user_version")
            return cursor.fetchone()[0]

    def set_db_version(self, version):
        """Set the version of the database."""
        with self.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(f"PRAGMA user_version = {version}")
            conn.commit()

    def store_image_frame(self, conn, depth, frame):
        """Store an image frame in the database."""
        cursor = conn.cursor()
        frame_byte_arr = io.BytesIO()
        frame.save(frame_byte_arr, format=self.image_format)
        frame_byte_arr = frame_byte_arr.getvalue()

        cursor.execute(
            "INSERT OR REPLACE INTO image_frames (depth, frame) VALUES (?, ?)",
            (depth, frame_byte_arr),
        )
        conn.commit()

    def initialize_database(self):
        """Initialize the database if it hasn't been initialized already."""
        current_version = self.get_db_version()
        if current_version == 1:  # 1 is our current version
            self.logger.info(
                "Database already initialized and up to date. Skipping initialization."
            )
            return

        with self.get_db_connection() as conn:
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

            df = pd.read_csv(self.csv_path)
            df = df.fillna(0)
            pixel_columns = df.columns.drop("depth")
            df[pixel_columns] = df[pixel_columns].astype(int)

            depths = df["depth"].values
            pixel_data = df[pixel_columns].values

            for i, (depth, pixels) in enumerate(zip(depths, pixel_data)):
                try:
                    self.logger.info(f"Processing image frame at depth {depth}")
                    frame = create_frame_from_pixels(pixels)
                    frame = resize_frame(frame)
                    frame = apply_colormap(frame)
                    self.store_image_frame(conn, depth, frame)
                    if i % 100 == 0:  # Log progress every 100 rows
                        self.logger.info(f"Processed {i} image frames")
                except Exception as e:
                    self.logger.error(
                        f"Error processing image frame at depth {depth}: {str(e)}"
                    )

        self.set_db_version(1)  # Set to version 1 after successful initialization
        self.logger.info("Database initialization completed")

    def get_image_frames(self, depth_min, depth_max):
        """Retrieve image frames from the database within a specified depth range."""
        with self.get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                SELECT depth, frame FROM image_frames WHERE depth BETWEEN ? AND ?
                ORDER BY depth
                """,
                (depth_min, depth_max),
            )
            return cursor.fetchall()

    def get_db_connection(self):
        """Create and yield a database connection."""
        return sqlite3.connect(self.database_path)

image_database = ImageDatabase()