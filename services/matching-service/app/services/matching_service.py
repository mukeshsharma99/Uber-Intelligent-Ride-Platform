from app.database.redis import redis_client


def initialize_drivers():
    redis_client.delete("available_drivers")

    redis_client.sadd(
        "available_drivers",
        1,
        2,
    )


def find_driver():
    drivers = redis_client.smembers("available_drivers")

    if not drivers:
        return None

    driver_data = [
        {
            "id": 1,
            "name": "Driver 1",
            "distance": 2.5,
        },
        {
            "id": 2,
            "name": "Driver 2",
            "distance": 1.2,
        },
    ]

    available_drivers = [
        driver
        for driver in driver_data
        if str(driver["id"]) in drivers
    ]

    if not available_drivers:
        return None

    return min(
        available_drivers,
        key=lambda driver: driver["distance"],
    )