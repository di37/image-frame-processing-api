# Models

This folder contains Pydantic models used for data validation and serialization in the project.

## Contents

- `__init__.py`: Exports the models for easy import
- `schemas.py`: Defines Pydantic models for request/response schemas

## Models

### DepthRangeRequest

This model is used to validate and serialize the request body for endpoints that require a depth range.

Fields:

- `depth_min`: Optional[float]
  - Description: Minimum depth value (must be non-negative)
  - Validation: Greater than or equal to 0
- `depth_max`: Optional[float]
  - Description: Maximum depth value (must be greater than 0)
  - Validation: Greater than 0

## Usage

To use these models in other parts of the project, import them like this:

```python
from models import DepthRangeRequest

# Example usage in a FastAPI route
@app.post("/get_frames")
async def get_frames(request: DepthRangeRequest):
    depth_min = request.depth_min
    depth_max = request.depth_max
    # ... rest of the route logic
```

## Benefits

- Automatic request validation
- Clear API documentation generation
- Type hinting for better IDE support and code completion
- Centralized definition of data structures used across the application

## Dependencies

- Pydantic: Used for defining the data models and validation

These models help ensure data consistency and provide clear contracts for API interactions throughout the project.
