# Database Module

This module handles all database operations for the image processing project.

## Contents

- `__init__.py`: Exports main functions for external use
- `helper.py`: Contains core database functionality

## Key Functions

- `initialize_database()`: Sets up the database schema and populates it with image frames from CSV data
- `get_db_connection()`: Provides a context-managed database connection
- `get_image_frames(db_conn, depth_min, depth_max)`: Retrieves image frames within a specified depth range
- `store_image_frame(conn, depth, frame)`: Stores a processed image frame in the database
- `get_db_version()` and `set_db_version(version)`: Manage database versioning

## Usage

Import required functions from the module:

```python
from database import initialize_database, get_db_connection, get_image_frames
```

The module handles SQLite database operations, including initialization, connection management, and querying of image frame data. It works in conjunction with the image processing module to store and retrieve processed image frames.
