import sys
from typing import Dict, List, Union

from utils import isTimeFrameIntersection, splitTimeFrame


def readFile(file_path: str) -> List[str]:
    """
    Read the data, remove jump lines and spaces. Finally store the information in an array

    Args:
        file_path (str): The file path

    Returns:
        List[str]: Each element of the array represents a line on the data file
    """
    fileData = []

    try:
        with open(file_path, 'r', encoding='utf-8') as inputFile:
            for line in inputFile:
                removeJumpLine = line.replace("\n", "")
                trimSpaces = removeJumpLine.replace(" ", "")
                fileData.append(trimSpaces)            

        return fileData

    except FileNotFoundError:
        print("Oops! No such file or directory")
        sys.exit(1)
    except IsADirectoryError:
        print("Oops! The path you enter is a directory, you have to enter a file path")
        sys.exit(1)
        
        

        
def employeesSchedule(employeesScheduleData: List[str]) -> Dict[str, List[str]]:
    """
    Structures the data as a dictionary with the name 
    of the employee as a key and his schedule as value 

    Args:
        workersScheduleData (List[str]): Raw data

    Returns:
        Dict[str, List[str]]: Data structured as a dictionary with name of the employee as key and the schedule as the value
    """
    employeesSchedule = {}
    for schedule in employeesScheduleData:
        employee, schedule = schedule.split('=')
        employeesSchedule[employee] = schedule.split(',')
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
        List: List with the different employees combination 
    """
    if pairingNumber == 0:
        return [[]]

    possibleCombinations = []

    for i in range(0, len(employees)):
        firstItem = employees[i]
        adjacentItems = employees[i+1:]
        for j in employeesCombination(adjacentItems, pairingNumber-1):
            possibleCombinations.append([firstItem]+j)
    return possibleCombinations        
        

def sameTimeFrame(scheduleOne: List[str], scheduleTwo: List[str]) -> List[str]:
    """_summary_

    Args:
        scheduleOne (List[str]): Schedule of the first employee
        scheduleTwo (List[str]): Schedule of the second employee

    Returns:
        List[str]: Days where the employees share the same time frame
    """

    weekOne = {day[:2]: day[2:] for day in scheduleOne}
    weekTwo = {day[:2]: day[2:] for day in scheduleTwo}
    weekDaysOne, weekDaysTwo = list(weekOne.keys()), list(weekTwo.keys())
    daysIntersection = list(set(weekDaysOne).intersection(set(weekDaysTwo)))

    sameTimeFrame = []

    for day in daysIntersection:
        timeFrameOne = splitTimeFrame(weekOne[day])
        timeFrameTwo = splitTimeFrame(weekTwo[day])
        timeFrameIntersection = isTimeFrameIntersection(timeFrameOne, timeFrameTwo)

        if timeFrameIntersection:
            sameTimeFrame.append(day)

    return sameTimeFrame

    
def employeesCoincidedOffice(employeesCombination: List, employeesSchedule: Dict[str, List[str]]):
    for i in range(len(employeesCombination)):
        employeeCombination = employeesCombination[i]
        scheduleOne = employeesSchedule[employeeCombination[0]]
        scheduleTwo = employeesSchedule[employeeCombination[1]]
        coincidedOffice = sameTimeFrame(scheduleOne, scheduleTwo)
        print(f'{employeeCombination[0]}-{employeeCombination[1]}: {len(coincidedOffice)}')


def run(args):
    if len(args) == 1:
        print("You need enter the path of the .txt file")
    else:
        raw_data = readFile(file_path=args[1])
        structured_data = employeesSchedule(raw_data)
        combinations = employeesCombination(list(structured_data.keys()), 2)
        employeesCoincidedOffice(combinations, structured_data)


if __name__ == '__main__':        
    run(sys.argv)
