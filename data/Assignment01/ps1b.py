#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 00:15:47 2021

@author: thanhnhut
"""
def houseHunting(annual_salary, portion_saved, total_cost, semi_annual_raise):
    current_savings = 0
    portion_down_payment = 0.25
    r = 0.04
    save_of_month = annual_salary / 12
    months = 0
    while (current_savings < (portion_down_payment * total_cost)):
        
        if months % 6 == 0 and months > 0:
            save_of_month += save_of_month * semi_annual_raise
            
        current_savings += current_savings * (r/12) + portion_saved * save_of_month
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
                

annual_salary = inputValue("Enter your starting annual salary: ")
portion_saved = inputValue("Enter the percent of your salary to save, as a decimal: ")
total_cost = inputValue("Enter the cost of your dream home: ")
semi_annual_raise = inputValue("Enter the semi­annual raise, as a decimal: ")
print(houseHunting(annual_salary, float(portion_saved),total_cost, semi_annual_raise))
                
