def find_driver():
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
            "distance": 0.8
        }
    ]

    available_drivers = [
        driver for driver in drivers
        if driver["available"]
    ]

    if not available_drivers:
        return None

    nearest_driver = min(
        available_drivers,
        key=lambda driver: driver["distance"]
    )

    return nearest_driver