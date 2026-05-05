from typing import Dict, List, Optional
from pydantic import BaseModel

class UserPersona(BaseModel):
    preferences: Dict[str, float]
    constraints: List[str]
    mood: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "preferences": {"adventure": 0.8, "relaxation": 0.2},
                "constraints": ["max_budget: 2000", "wheelchair_access"],
                "mood": "seeking solitude"
            }
        }
