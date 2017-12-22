# Created by: luca.ienzi
# Created on: dec 2017
# Created for: ICS3U
# this program display the day and the numebr of day in the week it is
from emumm import Enum

Day = Enum('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
print (len(Day)) 
print(Day.Saturday.index) 
print(Day[6]) 
print(Day.Saturday)
print('Saturday' in Day) 
Day_selected = 'Saturday'
if Day_selected in Day:
    print (Day_selected + 'is a valid day') 
else:
    print('That is not a day')     
    Day_selected = int(input('Enter your favorite day #:'))     
    print(Day[Day_selected])
print("what is your favorite day?")
