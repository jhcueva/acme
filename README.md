# Technical Test

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

## Example

**Input**: The name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below

**Output**: Table containing pairs of employees and how often they have coincided in the office.

|  	| **Case 1** 	| **Case 2** 	|  	
|---	|---	|---	|
| **Input** 	| RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00<br>ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00<br>ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00 	| ASTRID-RENE: 2<br>ASTRID-ANDRES: 3<br>RENE-ANDRES: 2 	|  
| **Output** 	| RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00<br>ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00 	| RENE-ASTRID: 3 	|  	

## Solution

My solution is composed of five main functions:
- **readFile:** Read the file indicated in the path, remove line breaks and whitespace. Store each line of the file in an array
- **employeesSchedule:** Structures the employee's schedule in a dictionary, taking the employee's name as the key and the employee's schedule as the value
- **employeesCombination:** Calculate the different ways in which employees can be grouped in pairs
- **sameTimeFrame:** Compare if a pair of employees share working hours in a same day
- **employeesCoincidedOffice:** Return a pair of employees and how often they have coincided in the office.

When the code is executed ```python3 main.py <TXT PATH FILE>``` a series of steps are started:

1. First the function **readFile** takes as an argument the path of the file that is sent when executing the program. Loop through each line of the file, remove whitespace and line breaks. Finally store each line in a list
2. The result of the function readFile is sent as an argument to the function **employeesSchedule**. It goes through the sent elements and splits between employee and schedule. It stores the data in a dictionary, taking the employee as the key and schedule as the key.


    Example:
  
    Input:
  
    ```["name1=schedule1", "name2=schedule2", ..., "nameN=scheduleN"]```
  
    Output:
    ```
    {
      "name1" : "schedule1",
      "name2" : "schedule2",
      ... ,
      "nameN" : "scheduleN",
    }
    ```
  
3. The function **employeesCombination** takes the list of employees and calculates the possible combinations of the employees in pairs.
  Example:
  
    Input:
  ```["name1", "name2", "name3"]```
  
    Output:
  ```[["name1", "name2"], ["name1", "name3"], ["name2", "name3"]]```
  
5. The function **sameTimeFrame** take the schedules of two employees and structure each schedule in a dictionary using the day as the key and the schedule as the value. Take the days that each of the employees works and create a list with the days that the two workers coincide.

<div align="center">
  <a href="url"><img src="https://user-images.githubusercontent.com/15198470/196300945-1573dac8-6f34-48da-b70d-0114d64bf7d5.jpg" width="360" height="280" class="center" /></a>
</div>


  Iterates over the days on which the two employees coincide, read the schedule of the day and divide it into check-in and check-out times.

1. Step 5

## Run

  Make sure to be in the root folder

  Run code

    python3 main.py <TXT PATH FILE>

  Run tests

    pytest -v
