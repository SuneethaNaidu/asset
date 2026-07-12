from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.asset import AssetCreate

from app.services.asset_service import (
    create_asset,
    get_assets,
    get_asset_by_id,
    delete_asset
)

router = APIRouter(
    prefix="/assets",
    tags=["Assets"]
)


@router.get("/")
def list_assets(db: Session = Depends(get_db)):
    return get_assets(db)


@router.get("/{asset_id}")
def asset_details(asset_id: int, db: Session = Depends(get_db)):
    asset = get_asset_by_id(db, asset_id)

    if asset is None:
        raise HTTPException(
            status_code=404,
            detail="Asset not found"
        )

    return asset


@router.post("/")
def register_asset(
    asset: AssetCreate,
    db: Session = Depends(get_db)
):
    return create_asset(db, asset)


@router.delete("/{asset_id}")
def remove_asset(
    asset_id: int,
    db: Session = Depends(get_db)
):
    asset = delete_asset(db, asset_id)

    if asset is None:
        raise HTTPException(
            status_code=404,
            detail="Asset not found"
        )

    return {
        "message": "Asset deleted successfully"
    }
