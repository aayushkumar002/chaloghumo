from typing import Any, Dict, List
from pydantic import BaseModel

class RecommendationBase(BaseModel):
    destination_id: str
    match_score: float
    reasoning_chain: List[str]
    context_snapshot: Dict[str, Any]

class RecommendationCreate(RecommendationBase):
    pass

class Recommendation(RecommendationBase):
    class Config:
        from_attributes = True
