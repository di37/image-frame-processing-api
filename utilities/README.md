# Utilities Module - `utilities`

This module provides utility functions and constants used across the project.

## Contents

- `__init__.py`: Exports constants and utility functions
- `constants.py`: Defines project-wide constants
- `csv_analyzer.py`: Contains utility functions for CSV analysis

## Constants

- `IMAGE_FRAMES_CSV_PATH`: Path to the raw CSV data file
- `DATABASE_PATH`: Path to the SQLite database
- `MIN_PIXEL`, `MAX_PIXEL`: Pixel value range (0-255)
- `HEIGHT`, `WIDTH`: Dimensions of original image frames
- `NEW_WIDTH`: Target width for resized images
- `IMAGE_FORMAT`: Format for storing images (PNG)

## Utility Functions

- `analyze_csv()`: Analyzes the structure and content of the image data CSV file

## Usage

Import constants and functions as needed:

```python
from utilities import IMAGE_FRAMES_CSV_PATH, DATABASE_PATH, analyze_csv
```

## Features

- Centralized storage for project-wide constants
- Environment variable support for file paths
- CSV analysis function for data inspection

## Dependencies

- Pandas (for CSV analysis)
- custom_logger (for logging analysis results)

This module is designed to be imported by other modules in the project to access shared constants and utility functions. It helps maintain consistency across the project and provides useful general functions that are frequently used for data analysis.
