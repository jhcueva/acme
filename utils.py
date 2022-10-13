from typing import Tuple


def splitTimeFrame(timeFrame: str) -> Tuple[str, str]:
    """Split the time frame between the time frame start and time frame end

    Args:
        timeFrame (str): Time frame Example: 10:00-12:00

    Returns:
        Tuple[str, str]: Return time frame between the time frame start and time frame end
    """
    timeFrameStart, timeFrameEnd = timeFrame.split("-")
    return timeFrameStart, timeFrameEnd


def splitHourMinutes(time: str) -> Tuple[str, str]:
    """Split time between hour and minutes

    Args:
        time (str): Time

    Returns:
        Tuple[str, str]: Return time between hour and minutes
    """
    hour, minutes = time.split(":")
    return hour, minutes
