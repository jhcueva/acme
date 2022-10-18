from typing import Tuple


def isTimeFrameIntersection(timeFrameOne: Tuple[str, str], timeFrameTwo: Tuple[str, str]) -> bool:
    """
    Take the time frame of the employees and return True if they share time frame
    and return False when not

    Args:
        timeFrameOne (Tuple[str, str]): Time frame employee One
        timeFrameTwo (Tuple[str, str]): Time frame employee Two

    Returns:
        bool: Return True when the employees share time frame 
    """
    timeFrameIntersection = isIntersection(
        timeFrameOne[0],
        timeFrameOne[1],
        timeFrameTwo[0],
        timeFrameTwo[1]
    )
    return timeFrameIntersection


def isIntersection(startOne: str, endOne: str, startTwo: str, endTwo: str) -> bool:
    """
    Take the start time and the end time of the employee One and the start time
    and the end time of the employee two. 

    When the start time of the employee One is less than the end time of the employee 
    Two and when the start time of the employee Two is less than the end time of the 
    employee One is a time frame intersection and returns True 

    Args:
        startOne (str): Start time of the employee One
        endOne (str): End time of the employee One
        startTwo (str): Start time of the employee Two
        endTwo (str): End time of the employee Two

    Returns:
        bool: Returns True when the time frame of the employeeOne intersects whit the employee two
    """
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
        Tuple[int, int]: Return time between hour and minutes
    """
    hour, minutes = time.split(":")
    return int(hour), int(minutes)
