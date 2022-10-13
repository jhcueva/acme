# Technical Test

The company ACME offers their employees the flexibility to work the hours they want. But due to some external circumstances they need to know what employees have been at the office within the same time frame

The goal of this exercise is to output a table containing pairs of employees and how often they have coincided in the office.

## Example

**Input**: The name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our examples below

**Output**: Table containing pairs of employees and how often they have coincided in the office.

|  	| **Case 1** 	| **Case 2** 	|  	
|---	|---	|---	|
| **Input** 	| RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00- 21:00<br>ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00<br>ANDRES=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00 	| ASTRID-RENE:2<br>ASTRID-ANDRES: 3<br>RENE-ANDRES: 2 	|  
| **Output** 	| RENE=MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00<br>ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00 	| RENE-ASTRID: 3 	|  	
