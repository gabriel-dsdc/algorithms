def study_schedule(
    permanence_period: list[tuple[int, int]], target_time: int
) -> int | None:
    if type(target_time) != int:
        return None

    counter = 0
    for period in permanence_period:
        if type(period[0]) != int or type(period[1]) != int:
            return None

        if period[0] <= target_time <= period[1]:
            counter += 1
    return counter
