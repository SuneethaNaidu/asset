from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import ForeignKey
from sqlalchemy import Date
from sqlalchemy import String

from app.database import Base


class AssetAllocation(Base):

    __tablename__ = "asset_allocations"

    id = Column(Integer, primary_key=True)

    asset_id = Column(
        Integer,
        ForeignKey("assets.id")
    )

    employee_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    allocated_date = Column(Date)

    expected_return = Column(Date)

    returned_date = Column(Date)

    status = Column(
        String(30),
        default="Allocated"
    )
