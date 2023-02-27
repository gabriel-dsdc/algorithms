def study_schedule(permanence_period: list[tuple[int, int]], target_time: int):
    if type(target_time) != int or any(
        [
            type(period[0]) != int or type(period[1]) != int
            for period in permanence_period
        ]
    ):
        return None
    return len(
        [
            period
            for period in permanence_period
            if period[0] <= target_time <= period[1]
        ]
    )
