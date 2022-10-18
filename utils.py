from typing import Tuple


def isTimeFrameIntersection(timeFrameOne: Tuple[str, str], timeFrameTwo: Tuple[str, str]) -> bool:
    """
    Take the time frame of the employees. When the start time of the employee One 
    is less than the end time of the employee Two and when the start time of the 
    employee Two is less than the end time of the employee One is a time frame 
    intersection and returns True otherwise returns False

    Args:
        timeFrameOne (Tuple[str, str]): Time frame employee One
        timeFrameTwo (Tuple[str, str]): Time frame employee Two

    Returns:
        bool: Return True when the employees share time frame otherwise False
    """

    hourStartOne, minuteStartOne = splitHourMinutes(timeFrameOne[0])
    hourEndOne, minuteEndOne = splitHourMinutes(timeFrameOne[1])
    hourStartTwo, minuteStartTwo = splitHourMinutes(timeFrameTwo[0])
    hourEndTwo, minuteEndTwo = splitHourMinutes(timeFrameTwo[1])
    
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
    """
    Compares if the start time less than the end time and return true
    if start time it's less than end time.

    Args:
        hourStart (int): Hour start
        hourEnd (int): Hour end
        minuteStart (int): Minute start
        minuteEnd (int): Minute end

    Returns:
        bool: Returns True when start time is less than end time.
    """
    if hourStart == hourEnd:
        if minuteStart < minuteEnd:
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
        Tuple[int, int]: Return time in hour and minutes
    """
    hour, minutes = time.split(":")
    return int(hour), int(minutes)
