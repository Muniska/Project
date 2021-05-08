#!/usr/bin/env python
# coding: utf-8

# In[33]:


def  exponential(a,b):
     c = (1+a)**b
     print(c)
     return c
exponential(99,11)


# In[11]:


print(1000**1/3 >= 10)
print(12**2 == 154-9)
print(10/(100**1/2) < 1)


# In[32]:


x=input() 
x=253**1/y
y=int(y)  
print(float(y))

if y%2==0:
    print("even")
if y%2==1:
    print("odd")


# In[33]:


print('insert x')
x = input()
print('insert y')
y = input()

if y > x:
    print("y is greater than x")
elif y == x:
    print("y is equal to x")
else:
    print("y is not greater than x")


    
    


# In[8]:


# Nd - number of cases on a given day
# E - average number of people someone infected is exposed to each day
# p - probability of each exposure becoming an infection

def number_of_cases_next_day (E,p,Nd):
    N=(1+E*p)*Nd
    print(int(N))
    return(int(N))
number_of_cases_next_day (3,0.3,7)
    
    




# In[3]:


def Celsuis_to_Fahrenheit(t):
    F=9/5*t+32
    print(F)
Celsuis_to_Fahrenheit(45)


# In[24]:


temp = eval(input('Enter a temperature in Celsius: '))
f_temp = 9/5*temp+32
print('In Fahrenheit, that is', f_temp)

if f_temp > 120:
    print('Let us swim.')
if f_temp < 60:
    print('Let us stay at home.')
else:
    print('Let us go for travelling')


# In[5]:


# a - current assets
# l - current liabilities


a = eval(input('current assets:'))
l = eval(input('current liabilities:'))
    
print('Current ratio', a / l)
    

if a/l > 2:
    print("ratio is robust")
elif a/l ==1.5:
    print("y is equal to x")
else:
    print("business is unhealthy")





# In[33]:


def statistics(marriages_count, happily_married, divorced, lat):
    print(f"There were {marriages_count} marriages")
    print(f"From them {happily_married} are happily married")
    print(f"Divorced are {divorced}")
    print('The rest are living apart but together', marriages_count - happily_married - divorced)


print("Statistics of families for 2020:")
marriages_count = 36000
happily_married = 14000
divorced = 12000
statistics(marriages_count, happily_married, divorced, lat)


# In[36]:


w = eval(input('Enter your weight in kg: ')) 
h = eval(input('Enter your height in m: ')) 
print('BMI', w/h**2)

if w/h**2<18.5: 
    print('underweight') 
    
elif 25>=w/h**2>18.5: 
    print('healthy') 
    
elif 40>=w/h**2>25: 
    print('overweight') 
    
else: 
    print('You are too fat. Stop eating!')


# In[12]:


x = '\u0394'
y = "Hadicha"
z=78
r=len(y)
print(x)
print(type(x))
print(len(y))
print(type(z))
print(z+r)


# In[ ]:





# In[ ]:





# In[ ]:




