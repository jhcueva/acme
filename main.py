from typing import List, Dict


INPUT_FILE = r'testInput.txt'

def read_file(file_path: str) -> List[str]:
    """Read the data and store the information in an array

    Args:
        file_path (str): The file path of the data file

    Returns:
        List[str]: Each element of the array represents a line on the data file
    """
    fileData = []
    with open(file_path, 'r', encoding='utf-8') as inputFile:
        for line in inputFile:
            removeJumpLine = line[:-1]
            fileData.append(removeJumpLine)

    return fileData
            
def clean_data(workersScheduleData: List[str]) -> Dict[str, List]:
    """_summary_

    Args:
        workersScheduleData (List[str]): _description_

    Returns:
        Dict[str, List]: _description_
    """
    workersSchedule = {}
    
    for workerSchedule in workersScheduleData:
        split_employee_schedule = workerSchedule.split('=')
        employee, schedule = split_employee_schedule[0], split_employee_schedule[1].split(',')
        workersSchedule[employee]=schedule
    return workersSchedule


def workersCombination(workers: List[str], pairingNumber: int = 2) -> List:
    """_summary_

    Args:
        workers (List[str]): _description_
        pairingNumber (int, optional): _description_. Defaults to 2.

    Returns:
        List: _description_
    """
    if pairingNumber==0:
        return [[]]
    
    possibleCombinations=[]
    
    for i in range(0,len(workers)):
        firstItem=workers[i]
        adjacentItems=workers[i+1:]
        for p in workersCombination(adjacentItems,pairingNumber-1):
            possibleCombinations.append([firstItem]+p)
            
    return possibleCombinations


if __name__ == '__main__':
    combinations = workersCombination(['RENE', 'ANDRES', 'ASTRID'], 2)
    print(combinations)