from sqlalchemy.orm import Session

from app.models.asset import Asset
from app.utils.asset_tag import generate_asset_tag


def get_assets(db: Session):
    return db.query(Asset).all()


def get_asset_by_id(db: Session, asset_id: int):
    return db.query(Asset).filter(Asset.id == asset_id).first()


def create_asset(db: Session, asset_data):
    asset = Asset(
        asset_tag="TEMP",
        asset_name=asset_data.asset_name,
        serial_number=asset_data.serial_number,
        acquisition_date=asset_data.acquisition_date,
        acquisition_cost=asset_data.acquisition_cost,
        location=asset_data.location,
        condition=asset_data.condition,
        category_id=asset_data.category_id,
        shared_bookable=asset_data.shared_bookable,
        status="Available"
    )

    db.add(asset)
    db.commit()
    db.refresh(asset)

    asset.asset_tag = generate_asset_tag(asset.id)

    db.commit()
    db.refresh(asset)

    return asset


def delete_asset(db: Session, asset_id: int):
    asset = get_asset_by_id(db, asset_id)

    if asset:
        db.delete(asset)
        db.commit()

    return asset
