#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 00:51:25 2021

@author: thanhnhut
"""

def haveTheAbilityToPay(annual_salary, portion_saved, total_cost, semi_annual_raise):
    current_savings = 0
    portion_down_payment = 0.25
    r = 0.04
    save_of_month = annual_salary / 12
    
    
    for i in range(0,36):
        if i % 6 == 0 and i > 0:
            save_of_month += save_of_month * semi_annual_raise
        current_savings += current_savings * (r/12) + portion_saved * save_of_month
        if current_savings >= (total_cost * portion_down_payment):
            return i
    return False

def houseHunting(annual_salary):
   
    total_cost = 1000000
    semi_annual_raise = 0.07
    
    for i in range(1, 10001):
        if haveTheAbilityToPay(annual_salary, i/10000, total_cost, semi_annual_raise) != False:
            return "Best savings rate: "+ str(i/10000)
    return "It is not possible to pay the down payment in three years"
    
    
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
        
               

            
print(houseHunting(inputValue("Enter the starting salary: ")))



  