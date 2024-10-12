import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

import numpy as np
from PIL import Image

import matplotlib.cm as cm

from utilities import MIN_PIXEL, MAX_PIXEL, HEIGHT, WIDTH, NEW_WIDTH
from custom_logger import logger

def create_frame_from_pixels(pixels, width=WIDTH, height=HEIGHT):
    """
    Create an image frame from pixel data.

    Args:
        pixels (np.array): Array of pixel values.
        width (int, optional): Width of the image. Defaults to 200.
        height (int, optional): Height of the image. Defaults to 1.

    Returns:
        Image: PIL Image object created from the pixel data.
    """
    min_val, max_val = np.min(pixels), np.max(pixels)
    if min_val < MIN_PIXEL or max_val > MAX_PIXEL:
        logger.warning(f"Pixel values out of range: min={min_val}, max={max_val}")

    if not np.allclose(pixels, np.round(pixels)):
        logger.warning("Non-integer pixel values detected")

    pixels_clipped = np.clip(pixels, MIN_PIXEL, MAX_PIXEL)
    frame_array = np.round(pixels_clipped).astype(np.uint8)
    frame_array = frame_array.reshape((height, width))
    return Image.fromarray(frame_array)


def resize_frame(frame, new_width=NEW_WIDTH):
    """
    Resize an image frame to a new width while maintaining aspect ratio.

    Args:
        frame (Image): PIL Image object to resize.
        new_width (int, optional): New width for the image. Defaults to 150.

    Returns:
        Image: Resized PIL Image object.
    """
    width, height = frame.size
    scaling_factor = new_width / width
    new_height = int(round(height * scaling_factor))
    return frame.resize((new_width, new_height), Image.LANCZOS)


def apply_colormap(frame):
    """
    Apply a colormap to a grayscale image frame.

    Args:
        frame (Image): PIL Image object to apply colormap to.

    Returns:
        Image: PIL Image object with colormap applied.
    """
    colormap = cm.get_cmap("jet")
    frame_array = np.array(frame)
    normalized_array = frame_array / MAX_PIXEL
    colored_array = colormap(normalized_array)
    colored_frame = (colored_array[:, :, :3] * MAX_PIXEL).astype(np.uint8)
    return Image.fromarray(colored_frame)
