from pydantic import BaseModel


class AssetCategoryCreate(BaseModel):

    category_name: str

    description: str | None = None


class AssetCategoryResponse(BaseModel):

    id: int

    category_name: str

    description: str | None

    class Config:
        from_attributes = True
