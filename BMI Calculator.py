#!/usr/bin/env python
# coding: utf-8

# In[45]:


def your_bmi (): 
    
    name = input ('Enter your name:  ')
    name_capitalize = name.capitalize() 
        
    weight_choice = 'WRONG'
    acceptable_range = range(1,650)
    within_range = False
    
    while weight_choice.isdigit() == False or within_range == False:
        weight_choice = input('Enter your weight in kg:  ')
    
        if weight_choice.isdigit() == False:
            print('Sorry, that is not a digit.' )
        if weight_choice.isdigit() == True:
            if int(weight_choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print('Sorry, you are out of range 1-650')
   

    height_choice = 'WRONG'
    acceptance_range_height = range (1,260)
    within_range_height = False
    
    while height_choice.isdigit()==False or within_range_height == False:
        height_choice = input('Enter your height in cm: ')
        
        if height_choice.isdigit()==False:
            print('Sorry, that is not a digit')
        if height_choice.isdigit()==True:
            if int(height_choice) in acceptance_range_height:
                within_range_height = True
            else:
                within_range_height = False
                print('Sorry, you are out of range 1,260')
  
    BMI = int(weight_choice)/((int(height_choice)/100)*(int(height_choice)/100))

    print(round(BMI,2))

    if BMI > 0:
        if(BMI<16):
            print(name_capitalize  +  ', you are starved.')
        elif (BMI <=16.99):
            print(name_capitalize  + ', you are in hypothermia.')
        elif (BMI <=18.49):
            print(name_capitalize +  ', you are underweight.')
        elif (BMI<=24.99):
            print(name_capitalize  +  ', you are in normal weight.')
        elif (BMI<=29.99):
            print( name_capitalize +  ', you are overweight.')
        elif (BMI <=34.99):
            print(name_capitalize +  ', you have 1st obesity.')
        elif (BMI<=39.99):
            print(name_capitalize +  ', you have 2st obesity.')
        elif (BMI >40):
            print (name_capitalize +  ', you are severely obese.')
        else:
            print(name_capitalize +  ', you are morbidly obese.')
    else:
        print('Enter valid input.')


# In[47]:


your_bmi()


# In[9]:


your_bmi()


# In[16]:


your_bmi ()


# In[21]:


your_bmi1()


# In[25]:


your_bmi()


# In[ ]:




