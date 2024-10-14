# Image Processing Module - `image_processing`

This module contains functions for processing and manipulating image frames for the project.

## Contents

- `__init__.py`: Exports main functions for external use
- `image_frame_utils.py`: Contains core image processing functionality

## Key Functions

- `create_frame_from_pixels(pixels, width, height)`: Creates a PIL Image object from pixel data
- `resize_frame(frame, new_width)`: Resizes an image frame while maintaining aspect ratio
- `apply_colormap(frame)`: Applies a colormap to a grayscale image frame

## Usage

Import required functions from the module:

```python
from image_processing import create_frame_from_pixels, resize_frame, apply_colormap
```

## Features

- Creates image frames from pixel arrays
- Handles pixel value validation and clipping
- Resizes images using the LANCZOS algorithm for high-quality results
- Applies a 'jet' colormap to grayscale images

This module works in conjunction with the `utilities` module for `constants` and the `custom_logger` for logging warnings and errors during image processing.
