# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




def houseHunting(annual_salary, portion_saved, total_cost):
    current_savings = 0
    portion_down_payment = 0.25
    r = 0.04
    months = 0
    while (current_savings < (portion_down_payment * total_cost)):
        current_savings += current_savings * (r/12) + portion_saved *(annual_salary / 12)
        months += 1
    return "Number of months: "+ str(months)
        
def inputValue(messages):
    while True:
        value = input(messages)
        try:
            val = int(value)
            return val
        except ValueError:
            try:
                val = float(value)
                return val
            except ValueError:
                print("")


annual_salary = inputValue("Enter your annual salary: ")
portion_saved = inputValue("Enter the percent of your salary to save, as a decimal: ")
total_cost = inputValue("Enter the cost of your dream home: ")
print(houseHunting(annual_salary, float(portion_saved),total_cost))


