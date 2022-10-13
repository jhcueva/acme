from typing import Dict, List

from utils import splitHourMinutes, splitTimeFrame

INPUT_FILE = r'testInput.txt'


def read_file(file_path: str) -> List[str]:
    """
    Read the data and store the information in an array

    Args:
        file_path (str): The file path of the data file

    Returns:
        List[str]: Each element of the array represents a line on the data file
    """
    fileData = []
    with open(file_path, 'r', encoding='utf-8') as inputFile:
        for line in inputFile:
            removeJumpLine = line.replace("\n", "")
            trimSpaces = removeJumpLine.replace(" ", "")
            fileData.append(trimSpaces)

    return fileData


def employeesSchedule(employeesScheduleData: List[str]) -> Dict[str, str]:
    """
    Structures the data as a dictionary with the name 
    of the employee as a key and his schedule as value 

    Args:
        workersScheduleData (List[str]): Raw data

    Returns:
        Dict[str, List]: Data structured as a dictionary with name of the employee as key and the schedule as the value
    """
    employeesSchedule = {}

    for schedule in employeesScheduleData:
        split_employee_schedule = schedule.split('=')
        employee, schedule = split_employee_schedule[0], split_employee_schedule[1].split(
            ',')
        employeesSchedule[employee] = schedule

    return employeesSchedule


def employeesCombination(employees: List[str], pairingNumber: int = 2) -> List:
    """
    Compute the possible employees combination in couples 

    Get the list of employees and returns a list with 
    the possible combinations of pairs of employees

    Args:
        workers (List[str]): List of the employees
        pairingNumber (int, optional): Number of employees combination Defaults to 2.

    Returns:
        List: List with the different workers combination 
    """
    if pairingNumber == 0:
        return [[]]

    possibleCombinations = []

    for i in range(0, len(employees)):
        firstItem = employees[i]
        adjacentItems = employees[i+1:]
        for p in employeesCombination(adjacentItems, pairingNumber-1):
            possibleCombinations.append([firstItem]+p)

    return possibleCombinations


def employeesCoincidedOffice(employeesCombination: List, employeesSchedule: Dict[str, List]):
    for i in range(len(employeesCombination)):
        employeeCombination = employeesCombination[i]
        scheduleOne = employeesSchedule[employeeCombination[0]]
        scheduleTwo = employeesSchedule[employeeCombination[1]]
        coincidedOffice = sameTimeFrame(scheduleOne, scheduleTwo)
        print(
            f'{employeeCombination[0]}-{employeeCombination[1]}:{len(coincidedOffice)}')


def isStartlessthanEndd(startOne: str, endOne: str, startTwo: str, endTwo: str) -> bool:
    hourStartOne, minuteStartOne = splitHourMinutes(startOne)
    hourEndOne, minuteEndOne = splitHourMinutes(endOne)
    hourStartTwo, minuteStartTwo = splitHourMinutes(startTwo)
    hourEndTwo, minuteEndTwo = splitHourMinutes(endTwo)

    startOne_endTwo = isStartlessthanEnd(
        hourStartOne,
        hourEndTwo,
        minuteStartOne,
        minuteEndTwo
    )
    startTwo_endOne = isStartlessthanEnd(
        hourStartTwo,
        hourEndOne,
        minuteStartTwo,
        minuteEndOne
    )

    if startOne_endTwo and startTwo_endOne:
        return True
    else:
        return False


def isStartlessthanEnd(hourStart, hourEnd, minuteStart, minuteEnd):
    if hourStart == hourEnd:
        if minuteStart <= minuteEnd:
            return True
        else:
            return False
    elif hourStart < hourEnd:
        return True
    else:
        return False


def isTimeFrameIntersection(timeFrameOne, timeFrameTwo):
    timeFrameIntersection = isStartlessthanEndd(
        timeFrameOne[0],
        timeFrameOne[1],
        timeFrameTwo[0],
        timeFrameTwo[1]
    )

    return timeFrameIntersection


def sameTimeFrame(scheduleOne: List[str], scheduleTwo: List[str]) -> List[str]:
    """_summary_

    Args:
        scheduleOne (List[str]): Schedule of the first employee
        scheduleTwo (List[str]): Schedule of the second employee

    Returns:
        List[str]: Schedule where the employees share the same time frame
    """

    weekOne, weekTwo = {day[:2]: day[2:] for day in scheduleOne}, {
        day[:2]: day[2:] for day in scheduleTwo}
    weekDaysOne, weekDaysTwo = list(weekOne.keys()), list(weekTwo.keys())

    daysIntersection = list(set(weekDaysOne).intersection(set(weekDaysTwo)))

    sameTimeFrame = []

    for day in daysIntersection:
        timeFrameOne, timeFrameTwo = splitTimeFrame(
            weekOne[day]), splitTimeFrame(weekTwo[day])
        timeFrameIntersection = isTimeFrameIntersection(
            timeFrameOne, timeFrameTwo)

        if timeFrameIntersection:
            sameTimeFrame.append(day)

    return sameTimeFrame


if __name__ == '__main__':
    raw_data = read_file(file_path=INPUT_FILE)
    structured_data = employeesSchedule(raw_data)
    combinations = employeesCombination(list(structured_data.keys()), 2)
    results = employeesCoincidedOffice(combinations, structured_data)
