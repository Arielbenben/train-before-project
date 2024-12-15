from dataclasses import dataclass
from datetime import datetime


@dataclass
class Relationship:
    relationship_type: str
    enrollment_date: datetime