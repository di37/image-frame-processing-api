import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

import pandas as pd

from utilities import IMAGE_FRAMES_CSV_PATH
from custom_logger import logger


def analyze_csv():
    """
    Analyze the CSV file containing image data.

    This function reads the CSV file, logs information about its structure,
    and calculates the minimum and maximum pixel values.
    """
    df = pd.read_csv(IMAGE_FRAMES_CSV_PATH)
    logger.info(f"CSV analysis:")
    logger.info(f"Shape: {df.shape}")
    logger.info(f"Columns: {df.columns}")
    logger.info(f"Data types: \n{df.dtypes}")
    logger.info(f"NA values: \n{df.isna().sum()}")

    pixel_data = df.drop("depth", axis=1)
    min_val = pixel_data.min().min()
    max_val = pixel_data.max().max()

    logger.info(f"Minimum pixel value: {min_val}")
    logger.info(f"Maximum pixel value: {max_val}")
