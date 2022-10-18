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
  
4. The function **sameTimeFrame** take the schedules of two employees and structure each schedule in a dictionary using the day as the key and the schedule as the value. Then take the days that each of the employees works, compare them and create a list with the days that the two workers coincide.

   Input work days employee one: ```["MO", "TH", "FR", "SA"]```
   
   Input work days employee two: ```["WE", "TH", "FR", "SU"]```
   
   Output: ```["TH", "FR"]```

<div align="center">
  <a href="url"><img src="https://user-images.githubusercontent.com/15198470/196300945-1573dac8-6f34-48da-b70d-0114d64bf7d5.jpg" width="360" height="280" class="center" /></a>
</div>


  Then iterates over the days on which the two employees coincide, read the schedule of the day and divide it into check-in and check-out times.
  
  To fing out if two employees have been in the office within the same time frame compares employee one's check-in time with employee two's check-out time and employee two's check-in time with employee one's check-out time.
  If employee one's check-in time is less than employee two's check-out time and employee two's check-in time is less than employee one's check-out time the two employees have been in the office within the same time frame. Otherwise they haven't been.
  
<p align="center">
    employeeOneCheckIn < employeeTwoCheckOut <b>and</b> employeeTwoCheckIn < employeeOneCheckOut 
</p>
  
<div align="center">
    <a href="url"><img src="https://user-images.githubusercontent.com/15198470/196445823-d4efd2e2-a6b0-41c2-b223-81e278557048.jpg" width="1060"               height="260"   class="center" /></a>
    <a href="url"><img src="https://user-images.githubusercontent.com/15198470/196445840-935dfe6d-b007-463a-8afe-c92da1ad0e6f.jpg" width="480"               height="220"   class="center" /></a>
</div>

   
  Finally it stores the days that both have been in the office within the same time frame in an array


5. The function **employeesCoincidedOffice** iterates over each of the possible combinations of employees, takes their schedules and passes them as arguments to the **sameTimeFrame** function, which returns an array with the days on which the employees have been in the office within the same time frame. Finally print the pairs of employees in alphabetical order and how often they have coincided in the office

## Run

  Make sure to be in the root folder

  Run code

    python3 main.py <TXT PATH FILE>

  To run tests first install dependencies
  
    pip install -r requirements.txt
    
  Run tests

    pytest -v
