from pydantic import BaseModel

class PropertyDetails(BaseModel):
    postcode: str
    recent_trends: str
    fuuture: str
    growth_rate: str