from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database import Base


class AssetCategory(Base):
    __tablename__ = "asset_categories"

    id = Column(Integer, primary_key=True, index=True)

    category_name = Column(String(100), unique=True, nullable=False)

    description = Column(Text, nullable=True)

    assets = relationship(
        "Asset",
        back_populates="category"
    )
