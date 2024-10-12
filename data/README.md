# Data Folder - `data`

This folder contains both raw and processed data for the image processing project.

## Structure

- `raw/`: Contains the original data files
  - `image_data.csv`: CSV file with depth and pixel data
- `processed/`: Stores processed data files
  - `image_data.db`: SQLite database (generated from raw data)

## Raw Data Format (image_data.csv)

- First column: `depth` (float values representing depth)
- Columns 2-201: `col1` to `col200` (integer values 0-255 representing pixel intensities)
- Each row represents a single 1-pixel high image with 200 pixels width

Note: The `image_data.db` database in the `processed` folder is generated from this raw CSV data and should not be edited directly.
