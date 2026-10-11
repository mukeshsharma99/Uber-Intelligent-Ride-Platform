def find_best_driver(drivers, ride):
    """
    Find the best driver for a ride.
    """

    if not drivers:
        return None

    # Simple matching for now:
    # choose the closest available driver
    available_drivers = [
        driver for driver in drivers
        if driver["available"]
    ]

    if not available_drivers:
        return None

    best_driver = min(
        available_drivers,
        key=lambda driver: driver["distance"]
    )

    return best_driver