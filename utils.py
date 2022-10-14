from typing import Tuple


def isTimeFrameIntersection(timeFrameOne: Tuple[str, str], timeFrameTwo: Tuple[str, str]) -> bool:
    timeFrameIntersection = isIntersection(
        timeFrameOne[0],
        timeFrameOne[1],
        timeFrameTwo[0],
        timeFrameTwo[1]
    )
    return timeFrameIntersection


def isIntersection(startOne: str, endOne: str, startTwo: str, endTwo: str) -> bool:
    hourStartOne, minuteStartOne = splitHourMinutes(startOne)
    hourEndOne, minuteEndOne = splitHourMinutes(endOne)
    hourStartTwo, minuteStartTwo = splitHourMinutes(startTwo)
    hourEndTwo, minuteEndTwo = splitHourMinutes(endTwo)

    startOne_endTwo = isStartTimelessthanEndTime(
        hourStartOne,
        hourEndTwo,
        minuteStartOne,
        minuteEndTwo
    )
    startTwo_endOne = isStartTimelessthanEndTime(
        hourStartTwo,
        hourEndOne,
        minuteStartTwo,
        minuteEndOne
    )

    if startOne_endTwo and startTwo_endOne:
        return True
    else:
        return False
    
    
def isStartTimelessthanEndTime(hourStart: int, hourEnd: int, minuteStart: int, minuteEnd: int) -> bool:
    if hourStart == hourEnd:
        if minuteStart <= minuteEnd:
            return True
        else:
            return False
    elif hourStart < hourEnd:
        return True
    else:
        return False


def splitTimeFrame(timeFrame: str) -> Tuple[str, str]:
    """Split the time frame between the start time and end time

    Args:
        timeFrame (str): Time frame Example: 10:00-12:00

    Returns:
        Tuple[str, str]: Return start time and end time
    """
    timeFrameStart, timeFrameEnd = timeFrame.split("-")
    return timeFrameStart, timeFrameEnd


def splitHourMinutes(time: str) -> Tuple[int, int]:
    """Split time between hour and minutes

    Args:
        time (str): Time

    Returns:
        Tuple[int, int]: Return time between hour and minutes
    """
    hour, minutes = time.split(":")
    return int(hour), int(minutes)
