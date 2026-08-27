# Binnacle of project: Student_Control_System

## 📅 Session: Friday (07/08/26)
** Status: 
** Module 'main' works well, i worked on the option 1 capabilities. Already call the function of the module 'data' and 'actions'. Beside the program can save the data on the .csv file. 
_Also, i worked on the menu option 2. It brings the report with all students inside the .csv file. 
_Also, I did the report for the menu option 4, it brings a report by student.

** Module 'menu'have all the options to manage the program and I made a AIIC design with the program's name and the version.


-** Blocks or doubts: **
-**📌 To do: ** 
[] to work on the option 3. Try to get the top 3 data of the avg notes and sort. I think that, maybe could be a good idea to make a new call from the .csv file and sort the data from the avg note, and then, make a function that show me the first 3 data.
[] to work on the option 5. Works on a report with a student filter. I think that, i could make a extra menu on this part, and bring the option to choice while kind of data the user would choice. For example, filter by name or second name or other filter by section.

## 📅 Session: Monday (10/08/26)
** Agenda:
[X] to work on the option 3. Try to get the top 3 data of the avg notes and sort. I think that, maybe could be a good idea to make a new call from the .csv file and sort the data from the avg note, and then, make a function that show me the first 3 data.
** STATUS
    _I did the function 'avg_sort_read_file', this function read the .csv file and then it sort the data by avg_note and then filter the first three students. I used the method .sort() and found extra features that give me the possibility to order the list without fails results like 'none'and allows float result.
                    sort_list.sort(key=lambda x: float(x['avg_note']), reverse=True)

**📌 To do: **                    
[] to work on the option 5. Works on a report with a student filter. I think that, i could make a extra menu on this part, and bring the option to choice while kind of data the user would choice. For example, filter by name or second name or other filter by section.
[] Create option 7. Find a student by name and section. Aks to confirm before to delete.

** Blocks or doubts: **
    _ I am not sure about how find data with 2 criteria. I am thinking to use a extra key. Like name + section. I should to search something about that.
    _ Maybe I will should to combine the option 5 and 7. I think that they makes the same function.


## 📅 Session: Tuesday (11/08/26)