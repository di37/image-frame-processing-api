# Database Module - `database`

This module handles all database operations for the image processing project using an object-oriented approach with a singleton-like pattern.

## Contents

- `__init__.py`: Exports the `ImageDatabase` class and a pre-instantiated `image_database` object
- `image_database.py`: Contains the `ImageDatabase` class with core database functionality

## Key Methods

The `ImageDatabase` class provides the following key methods:

- `initialize_database()`: Sets up the database schema and populates it with image frames from CSV data
- `get_db_connection()`: Provides a context-managed database connection
- `get_image_frames(depth_min, depth_max)`: Retrieves image frames within a specified depth range
- `store_image_frame(conn, depth, frame)`: Stores a processed image frame in the database
- `get_db_version()` and `set_db_version(version)`: Manage database versioning

## Usage

Import the pre-instantiated `image_database` object from the module:

```python
from database import image_database

# Initialize the database
image_database.initialize_database()

# Retrieve image frames
frames = image_database.get_image_frames(9015.1, 9015.4)
```

The `image_database` object is a singleton-like instance of the `ImageDatabase` class. It handles SQLite database operations, including initialization, connection management, and querying of image frame data. This approach ensures that a single database connection is shared across the application.

For most use cases, the pre-instantiated `image_database` object should be sufficient and is the recommended way to interact with the database module.
