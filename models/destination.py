from sqlalchemy import Column, String, Float, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid

from core.config import settings # Placeholder if needed for base

# Note: In a real app, you'd use a Base class from a db module
# This is just a stub to show directory structure usage
class Destination:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, index=True)
    lat = Column(Float)
    lng = Column(Float)
    base_vibe = Column(JSON)
