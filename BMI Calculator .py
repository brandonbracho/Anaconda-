#!/usr/bin/env python
# coding: utf-8

# In[ ]:


name_1=input("What is your name? ")
height_in1=input("What is your height in inches? ")
weight_lbs1= input("What is your weight in lbs ? ")
height_in1=float(height_in1)
weight_lbs1=float(weight_lbs1)

def bmi_calculator(name,height,weight):
    bmi=(weight*703)/(height**2)
    print(f"Bmi: {bmi}")
    if bmi<18.5:
        return name + " is underweight"
    elif bmi<24.9:
        return name + " is at a normal weight"
    else:
        return name + " is overweight"
    

bmi_calculator(name_1, height_in1, weight_lbs1)




# In[ ]:




