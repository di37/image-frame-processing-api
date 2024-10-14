import os
from fastapi import FastAPI, HTTPException, Body
import base64

from database import image_database
from utilities import analyze_csv
from custom_logger import logger

from models import DepthRangeRequest

app = FastAPI()


@app.on_event("startup")
def startup_event():
    """
    Perform startup tasks for the FastAPI application.

    This function is called when the FastAPI server starts up.
    It analyzes the CSV file and initializes the database.
    """
    # Ensure that the 'data' directory exists in the current working directory
    os.makedirs("data", exist_ok=True)
    os.makedirs("data/processed", exist_ok=True)
    analyze_csv()
    image_database.initialize_database()


@app.post("/image_frames/by_depth_range")
def get_image_frames_by_depth_range(depth_range: DepthRangeRequest):
    """
    Endpoint to retrieve image frames within a specified depth range.

    Args:
        data (dict): Request body containing depth_min and depth_max.
        db_conn (sqlite3.Connection): Database connection object.

    Returns:
        dict: Dictionary containing a list of image frames.

    Raises:
        HTTPException: If depth_min or depth_max are missing, or if no frames are found.
    """
    depth_min = depth_range.depth_min
    depth_max = depth_range.depth_max

    logger.info(f"Received request with depth_min={depth_min}, depth_max={depth_max}")

    if depth_min is None or depth_max is None:
        raise HTTPException(
            status_code=400, detail="depth_min and depth_max are required."
        )

    try:
        frames = image_database.get_image_frames(depth_min, depth_max)
    except Exception as e:
        logger.error(f"Error retrieving image frames: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

    if not frames:
        raise HTTPException(status_code=404, detail="Image frames not found")

    frame_list = []
    for depth, frame_data in frames:
        try:
            encoded_frame = base64.b64encode(frame_data).decode("utf-8")
            frame_list.append({"depth": depth, "frame_data": encoded_frame})
        except Exception as e:
            logger.error(f"Error processing frame at depth {depth}: {str(e)}")
            # Skip this frame and continue with the next one

    logger.info(f"Returning {len(frame_list)} frames")
    return {"image_frames": frame_list}
