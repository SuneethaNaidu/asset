from datetime import date

from pydantic import BaseModel


class AssetCreate(BaseModel):

    asset_name: str

    serial_number: str

    acquisition_date: date

    acquisition_cost: float

    location: str

    condition: str

    category_id: int

    shared_bookable: bool = False


class AssetResponse(BaseModel):

    id: int

    asset_tag: str

    asset_name: str

    status: str

    class Config:
        from_attributes = True
