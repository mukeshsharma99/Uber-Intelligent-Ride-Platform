from fastapi import APIRouter
from app.services.matching_service import find_best_driver

router = APIRouter()


@router.post("/match")
def match_ride(ride: dict):

    drivers = [
        {
            "id": 1,
            "name": "Driver 1",
            "available": True,
            "distance": 2.5
        },
        {
            "id": 2,
            "name": "Driver 2",
            "available": True,
            "distance": 1.2
        },
        {
            "id": 3,
            "name": "Driver 3",
            "available": False,
            "distance": 0.5
        }
    ]

    driver = find_best_driver(drivers, ride)

    if not driver:
        return {
            "message": "No driver available"
        }

    return {
        "message": "Driver matched successfully",
        "driver": driver
    }