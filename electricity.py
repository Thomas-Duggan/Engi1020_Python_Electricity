# Copyright (c) 2025 Thomas Duggan
# This work is licensed under CC BY-SA 4.0


############### Input Request ###############

energy = input("Energy usage per day in kWh: ")
if energy == '':
    loop = False 	# if user presses enter, loop will not go through
    energy_usage = [0] 		#Prevents error of "energy_usage" being unassigned
    
if energy != '':
    loop = True 
    energy_usage = [float(energy)] #converts number into float for list
    # 			 ^ initial defintion of energy_usage

while loop == True:	# if user does not press enter, it will repeat
   
    print("Press 'Enter' to continue")
    energy = input("Energy usage per day in kWh: ")
    if energy == '':
        loop = False
    if energy != '':
        # loop being true is removed because it is assumed
        energy_usage += [float(energy)] #add to list instead of redefining it
        
        # print(energy_usage) # !!! testing purposes only
    

############### Month Request ###############

loop2 = True
month_number = 101

while loop2 == True:
    month_count = 0
    month = input("Starting month (in full): ")
    for month_test in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
        month_count += 1 				# for each month, this variable increases by one regardless of if its the month we want
        if month_test == month:
            month_number = month_count 	# sets month number when month count when month is equal to listed item
            loop2 = False

    if (month_count == 12) and (month_number == 101):
        print ("Try again. Here are some examples: January , February, March")


############### Day Request ###############

while True:
    day = int(float(input("Starting day of month: ")))
 
    # There must be an easier way to do this section. This method is incredibly exessive.
    if (month_number == 1 or month_number == 3 or month_number == 5 or month_number == 7 or month_number == 8 or month_number == 10 or month_number == 12):
        if day > 31:
            print("Invalid Number, try again. Day should be less than 32")
        elif day < 1:
            print("Invalid Number, try again. Day should be more than 0") # Commented below. This is identical.
        else:
            day_number = day
            break
   
    if (month_number == 4 or month_number == 6 or month_number == 9 or month_number == 11): # month_number is from previous section
        if day > 30:
            print("Invalid Number, try again. Day should be less than 31")	# For these months, days are always from 1-31.
        elif day < 1:
            print("Invalid Number, try again. Day should be more than 0") 	# Prevents user from inputing a negative number.
        else:
            day_number = day	# reassigns the inputed number to another variable. I don't know why I did this, but it works.
            break
   
    if month_number == 2:
        if day > 28:
            print("Invalid Number, try again. Day should be less than 29") # Commented above. This is identical.
        elif day < 1:
            print("Invalid Number, try again. Day should be more than 0")
        else:
            day_number = day
            break
        


############### TESTING PURPOSES ONLY ###############

#print("Energy Usage:",energy_usage) # shows energy list
#print("Month Number:",month_number) # shows month number
#print("Day Number:",day_number)   	 # shows day number


############### Math ###############

# Notes:
# energy_usage is the list associated with daily energy usage
# month_number is the int number associated to the month
    # January = 1, December = 12, etc
# day_number is the starting day of the month

cost = 0
for temp_val in energy_usage:
    cost += temp_val * 0.14237 # temp_val is a value used for temporary number storage in complex math equations below
    
# print("Price Before Recursion:",cost) # !!! for testing only

temp_val = 0 # Resets temp_val to be reused later on

recursive_period = day_number + len(energy_usage)

# print(recursive_period) 								# < !!! for testing only
# print("Recursive Period Before:",recursive_period)	# < 

recursive_times = 1
repeat = 1

month_lengths = [31,28,31,30,31,30,31,31,30,31,30,31]
while recursive_period > month_lengths[month_number-repeat]:	# Tests if the number of days flow into the following month.
    recursive_period -= month_lengths[month_number-repeat] 		# This should work for over a months worth of numbers, but this hasnt been tested.
    recursive_times += 1										# Variable "recursive_times" and "repeat" might be able to be both a single variable, 
    repeat += 1													# but I dont want to ruin the program.
                
# print("Recursive Period After:",recursive_period)		# < !!! for testing only
# print("Recursive Times:",recursive_times)				# <

cost += (recursive_times * 15.79)
cost = round(cost,2) 	# Can i haz bonus mark plz???

print("Total cost:","$"+str(cost))


############### ISSUES ###############

# Only works in 2025
# User can input negative numbers in enery usage

