from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Date
from sqlalchemy import Boolean
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from app.database import Base


class Asset(Base):

    __tablename__ = "assets"

    id = Column(Integer, primary_key=True, index=True)

    asset_tag = Column(String(30), unique=True, nullable=False)

    asset_name = Column(String(200), nullable=False)

    serial_number = Column(String(100), unique=True)

    acquisition_date = Column(Date)

    acquisition_cost = Column(Float)

    location = Column(String(200))

    condition = Column(String(50))

    status = Column(String(30), default="Available")

    shared_bookable = Column(Boolean, default=False)

    category_id = Column(
        Integer,
        ForeignKey("asset_categories.id")
    )

    category = relationship(
        "AssetCategory",
        back_populates="assets"
    )
