# Tech Discovery Club Scheduler Tool
# CLICK RUN (GREEN BUTTON)
# WORKS Best on PC

print("Welcome to the Tech Discovery Club")
print("-"*80)
print("This simple program will help us figure out the best times to meet bi-weekly!\nIt shouldn't take longer than 3-4 minutes but make sure to have your schedule and student ID ready!")
print("-"*80)
print("First to add you officially, please answer these short 5 questions.")


# simple 3-2-1 countdown timer
def countdown(t):
    import time
    print('Loading...')
    while t >= 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
    print("Let's go! \n \n \n \n \n")

t=3
countdown(t)
# imports date Module
from datetime import date

import gspread
# keys here




# Lists for each weekday google sheet time slot cell number
monList = ['C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','C19','C20','C21','C22','C23','C24']
tueList = ['D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','D14','D15','D16','D17','D18','D19','D20','D21','D22','D23','D24']
wedList = ['E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12','E13','E14','E15','E16','E17','E18','E19','E20','E21','E22','E23','E24']
thurList = ['F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','F20','F21','F22','F23','F24']
friList = ['G2','G3','G4','G5','G6','G7','G8','G9','G10','G11','G12','G13','G14','G15','G16','G17','G18','G19','G20','G21','G22','G23','G24']
satList = ['H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','H14','H15','H16','H17','H18','H19','H20','H21','H22','H23','H24']
sunList = ['I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12','I13','I14','I15','I16','I17','I18','I19','I20','I21','I22','I23','I24']


today = date.today()
insertRow = []
insertRow.append(str(today))
name = input("What is your full name?\n")
insertRow.append(name)
insertRow.append(input("What is your student ID?\n"))
insertRow.append(input("What is your phone number?\n"))
insertRow.append(input("What is your primary field of interest?\n[What you think you want to do for work]\n"))
insertRow.append(input("What would you like to see in the club?\ne.g. Pizza\n"))

newRow = int(wks2.acell('H1').value)  # keeps row going - most recent at the top
wks2.insert_row(insertRow, (newRow))


#--------------------------------MONDAY--------------------------------------
# TIME SLOTS PRINT
print("="*80)
print("                                 TIME SLOTS 1-22")
print("="*80)
print("1.) 9:00am-9:30am   2.) 9:30am-10:00am\n3.) 10:00am-10:30am 4.) 10:30am-11:00am\n5.) 11:00am-11:30am 6.) 11:30am-12:00am\n7.) 12:00am-12:30pm 8.) 12:30pm-1:00pm\n9.) 1:00pm-1:30pm   10.) 1:30pm-2:00pm\n11.) 2:00pm-2:30pm  12.) 2:30pm-3:00pm\n13.) 3:00pm-3:30pm  14.) 3:30pm-4:00pm\n15.) 4:00pm-4:30pm  16.) 4:30pm-5:00pm\n17.) 5:00pm-5:30pm  18.) 5:30pm-6:00pm\n19.) 6:00pm-6:30pm  20.) 6:30pm-7:00pm\n21.) 7:00pm-7:30pm  22.) 7:30pm-8:00pm")
print("="*80)
#------------- Updates Google Sheets 'Monday' Cells If *NOT* Completely Free  ------------
answer = input("Are you typically free on Mondays? (Can meet anytime) [Y/N]\ntype in 'y' or 'n'\n")
if answer in ['n', 'N', 'no', 'No', 'NO']:
    print("\nWhat time ranges (shown above) can you absolutely not meet on Monday?\n    [List as whole numbers seperated by commas]\n        -----[e.g. 1,2,7,16,20,21,22]-----\n")
    monInput = [int(x) for x in input().split(",")] # Prompts user for input of numbers. Splits per comma. Changes to INT list.
    print("Loading...")
    for num in monInput:
        wks.update(monList[num-1], (int(wks.acell(monList[num-1]).value)+1))
print("Input Successful")


#--------------------------------TUESDAY--------------------------------------
# TIME SLOTS PRINT
print("="*80)
print("                                 TIME SLOTS 1-22")
print("="*80)
print("1.) 9:00am-9:30am   2.) 9:30am-10:00am\n3.) 10:00am-10:30am 4.) 10:30am-11:00am\n5.) 11:00am-11:30am 6.) 11:30am-12:00am\n7.) 12:00am-12:30pm 8.) 12:30pm-1:00pm\n9.) 1:00pm-1:30pm   10.) 1:30pm-2:00pm\n11.) 2:00pm-2:30pm  12.) 2:30pm-3:00pm\n13.) 3:00pm-3:30pm  14.) 3:30pm-4:00pm\n15.) 4:00pm-4:30pm  16.) 4:30pm-5:00pm\n17.) 5:00pm-5:30pm  18.) 5:30pm-6:00pm\n19.) 6:00pm-6:30pm  20.) 6:30pm-7:00pm\n21.) 7:00pm-7:30pm  22.) 7:30pm-8:00pm")
print("="*80)
#------------- Updates Google Sheets 'Tuesday' Cells If *NOT* Completely Free  ------------
answer = input("Are you typically free on Tuesdays? (Can meet anytime) [Y/N]\ntype in 'y' or 'n'\n")
if answer in ['n', 'N', 'no', 'No', 'NO']:
    print("\nWhat time ranges (shown above) can you absolutely not meet on Tuesday?\n    [List as whole numbers seperated by commas]\n        -----[e.g. 1,2,7,16,20,21,22]-----\n")
    tueInput = [int(x) for x in input().split(",")] # Prompts user for input of numbers. Splits per comma. Changes to INT list.
    print("Loading...")
    for num in tueInput:
        wks.update(tueList[num-1], (int(wks.acell(tueList[num-1]).value)+1))
print("Input Successful")

#--------------------------------WEDNESDAY--------------------------------------
# TIME SLOTS PRINT
print("="*80)
print("                                 TIME SLOTS 1-22")
print("="*80)
print("1.) 9:00am-9:30am   2.) 9:30am-10:00am\n3.) 10:00am-10:30am 4.) 10:30am-11:00am\n5.) 11:00am-11:30am 6.) 11:30am-12:00am\n7.) 12:00am-12:30pm 8.) 12:30pm-1:00pm\n9.) 1:00pm-1:30pm   10.) 1:30pm-2:00pm\n11.) 2:00pm-2:30pm  12.) 2:30pm-3:00pm\n13.) 3:00pm-3:30pm  14.) 3:30pm-4:00pm\n15.) 4:00pm-4:30pm  16.) 4:30pm-5:00pm\n17.) 5:00pm-5:30pm  18.) 5:30pm-6:00pm\n19.) 6:00pm-6:30pm  20.) 6:30pm-7:00pm\n21.) 7:00pm-7:30pm  22.) 7:30pm-8:00pm")
print("="*80)
#------------- Updates Google Sheets 'Wednesday' Cells If *NOT* Completely Free  ------------
answer = input("Are you typically free on Wednesdays? (Can meet anytime) [Y/N]\ntype in 'y' or 'n'\n")
if answer in ['n', 'N', 'no', 'No', 'NO']:
    print("\nWhat time ranges (shown above) can you absolutely not meet on Wednesday?\n    [List as whole numbers seperated by commas]\n        -----[e.g. 1,2,7,16,20,21,22]-----\n")
    wedInput = [int(x) for x in input().split(",")] # Prompts user for input of numbers. Splits per comma. Changes to INT list.
    print("Loading...")
    for num in wedInput:
        wks.update(wedList[num-1], (int(wks.acell(wedList[num-1]).value)+1))
print("Input Successful")

#--------------------------------THURSDAY--------------------------------------
# TIME SLOTS PRINT
print("="*80)
print("                                 TIME SLOTS 1-22")
print("="*80)
print("1.) 9:00am-9:30am   2.) 9:30am-10:00am\n3.) 10:00am-10:30am 4.) 10:30am-11:00am\n5.) 11:00am-11:30am 6.) 11:30am-12:00am\n7.) 12:00am-12:30pm 8.) 12:30pm-1:00pm\n9.) 1:00pm-1:30pm   10.) 1:30pm-2:00pm\n11.) 2:00pm-2:30pm  12.) 2:30pm-3:00pm\n13.) 3:00pm-3:30pm  14.) 3:30pm-4:00pm\n15.) 4:00pm-4:30pm  16.) 4:30pm-5:00pm\n17.) 5:00pm-5:30pm  18.) 5:30pm-6:00pm\n19.) 6:00pm-6:30pm  20.) 6:30pm-7:00pm\n21.) 7:00pm-7:30pm  22.) 7:30pm-8:00pm")
print("="*80)
#------------- Updates Google Sheets 'Thursday' Cells If *NOT* Completely Free  ------------
answer = input("Are you typically free on Thursdays? (Can meet anytime) [Y/N]\ntype in 'y' or 'n'\n")
if answer in ['n', 'N', 'no', 'No', 'NO']:
    print("\nWhat time ranges (shown above) can you absolutely not meet on Thursday?\n    [List as whole numbers seperated by commas]\n        -----[e.g. 1,2,7,16,20,21,22]-----\n")
    thurInput = [int(x) for x in input().split(",")] # Prompts user for input of numbers. Splits per comma. Changes to INT list.
    print("Loading...")
    for num in thurInput:
        wks.update(thurList[num-1], (int(wks.acell(thurList[num-1]).value)+1))
print("Input Successful")

#--------------------------------FRIDAY--------------------------------------
# TIME SLOTS PRINT
print("="*80)
print("                                 TIME SLOTS 1-22")
print("="*80)
print("1.) 9:00am-9:30am   2.) 9:30am-10:00am\n3.) 10:00am-10:30am 4.) 10:30am-11:00am\n5.) 11:00am-11:30am 6.) 11:30am-12:00am\n7.) 12:00am-12:30pm 8.) 12:30pm-1:00pm\n9.) 1:00pm-1:30pm   10.) 1:30pm-2:00pm\n11.) 2:00pm-2:30pm  12.) 2:30pm-3:00pm\n13.) 3:00pm-3:30pm  14.) 3:30pm-4:00pm\n15.) 4:00pm-4:30pm  16.) 4:30pm-5:00pm\n17.) 5:00pm-5:30pm  18.) 5:30pm-6:00pm\n19.) 6:00pm-6:30pm  20.) 6:30pm-7:00pm\n21.) 7:00pm-7:30pm  22.) 7:30pm-8:00pm")
print("="*80)
#------------- Updates Google Sheets 'Friday' Cells If *NOT* Completely Free  ------------
answer = input("Are you typically free on Fridays? (Can meet anytime) [Y/N]\ntype in 'y' or 'n'\n")
if answer in ['n', 'N', 'no', 'No', 'NO']:
    print("\nWhat time ranges (shown above) can you absolutely not meet on Friday?\n    [List as whole numbers seperated by commas]\n        -----[e.g. 1,2,7,16,20,21,22]-----\n")
    friInput = [int(x) for x in input().split(",")] # Prompts user for input of numbers. Splits per comma. Changes to INT list.
    print("Loading...")
    for num in friInput:
        wks.update(friList[num-1], (int(wks.acell(friList[num-1]).value)+1))
print("Input Successful")

#--------------------------------SATURDAY--------------------------------------
# TIME SLOTS PRINT
print("="*80)
print("                                 TIME SLOTS 1-22")
print("="*80)
print("1.) 9:00am-9:30am   2.) 9:30am-10:00am\n3.) 10:00am-10:30am 4.) 10:30am-11:00am\n5.) 11:00am-11:30am 6.) 11:30am-12:00am\n7.) 12:00am-12:30pm 8.) 12:30pm-1:00pm\n9.) 1:00pm-1:30pm   10.) 1:30pm-2:00pm\n11.) 2:00pm-2:30pm  12.) 2:30pm-3:00pm\n13.) 3:00pm-3:30pm  14.) 3:30pm-4:00pm\n15.) 4:00pm-4:30pm  16.) 4:30pm-5:00pm\n17.) 5:00pm-5:30pm  18.) 5:30pm-6:00pm\n19.) 6:00pm-6:30pm  20.) 6:30pm-7:00pm\n21.) 7:00pm-7:30pm  22.) 7:30pm-8:00pm")
print("="*80)
#------------- Updates Google Sheets 'Saturday' Cells If *NOT* Completely Free  ------------
answer = input("Are you typically free on Saturdays? (Can meet anytime) [Y/N]\ntype in 'y' or 'n'\n")
if answer in ['n', 'N', 'no', 'No', 'NO']:
    print("\nWhat time ranges (shown above) can you absolutely not meet on Saturday?\n    [List as whole numbers seperated by commas]\n        -----[e.g. 1,2,7,16,20,21,22]-----\n")
    satInput = [int(x) for x in input().split(",")] # Prompts user for input of numbers. Splits per comma. Changes to INT list.
    print("Loading...")
    for num in satInput:
        wks.update(satList[num-1], (int(wks.acell(satList[num-1]).value)+1))
print("Input Successful")

#--------------------------------SUNDAY--------------------------------------
# TIME SLOTS PRINT
print("="*80)
print("                                 TIME SLOTS 1-22")
print("="*80)
print("1.) 9:00am-9:30am   2.) 9:30am-10:00am\n3.) 10:00am-10:30am 4.) 10:30am-11:00am\n5.) 11:00am-11:30am 6.) 11:30am-12:00am\n7.) 12:00am-12:30pm 8.) 12:30pm-1:00pm\n9.) 1:00pm-1:30pm   10.) 1:30pm-2:00pm\n11.) 2:00pm-2:30pm  12.) 2:30pm-3:00pm\n13.) 3:00pm-3:30pm  14.) 3:30pm-4:00pm\n15.) 4:00pm-4:30pm  16.) 4:30pm-5:00pm\n17.) 5:00pm-5:30pm  18.) 5:30pm-6:00pm\n19.) 6:00pm-6:30pm  20.) 6:30pm-7:00pm\n21.) 7:00pm-7:30pm  22.) 7:30pm-8:00pm")
print("="*80)
#------------- Updates Google Sheets 'Sunday' Cells If *NOT* Completely Free  ------------
answer = input("Are you typically free on Sundays? (Can meet anytime) [Y/N]\ntype in 'y' or 'n'\n")
if answer in ['n', 'N', 'no', 'No', 'NO']:
    print("\nWhat time ranges (shown above) can you absolutely not meet on Sunday?\n    [List as whole numbers seperated by commas]\n        -----[e.g. 1,2,7,16,20,21,22]-----\n")
    sunInput = [int(x) for x in input().split(",")] # Prompts user for input of numbers. Splits per comma. Changes to INT list.
    print("Loading...")
    for num in sunInput:
        wks.update(sunList[num-1], (int(wks.acell(sunList[num-1]).value)+1))
print("Input Successful")

print("="*80)
print(f"Thank you {name} for taking the time to fill this out!")
print("We will have our meeting dates announced soon!")


print("-"*80)
print("goodbye... for now")

