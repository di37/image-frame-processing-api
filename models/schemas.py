from pydantic import BaseModel, Field
from typing import Optional


class DepthRangeRequest(BaseModel):
    depth_min: Optional[float] = Field(
        None, ge=0, description="Minimum depth value (must be non-negative)"
    )
    depth_max: Optional[float] = Field(
        None, gt=0, description="Maximum depth value (must be greater than 0)"
    )
