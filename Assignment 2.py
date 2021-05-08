#!/usr/bin/env python
# coding: utf-8

# In[1]:


shopping_list = """
My shopping list:
\t* Groceries \n\t\tApples\n\t\tBananas"""


def print_two(*apples):
    red_apples, green_apples = apples
red_apples = 1 # $ per kg
green_apples = 1.5 # $ per kg
apples_color1 = 'red'
apples_color2 = 'green'

def print_two(*bananas):
    raw_bananas, ripe_bananas = bananas
raw_bananas = 0.75 # per kg
ripe_bananas = 1 # per kg
bananas_color1 = 'raw'
bananas_color2 ='ripe'


print(shopping_list)

print('What do you wish to buy?')
item1 = input()
print(f"red apples $: {red_apples}, green apples $: {green_apples}")
print(f"would you like {apples_color1} or {apples_color2}?")
color = input()
print("How much do you need {} ".format(color) + item1 + " ?")
item1_quantity = int(input())
item1_price = int(item1_quantity * red_apples)
print(f"Total $: {item1_price}")

print('What else do you wish to buy?')
item2 = input()
print(f"raw bananas $: {raw_bananas}, ripe bananas $: {ripe_bananas}")
print(f"would you like {bananas_color1} or {bananas_color2}?")
color = input()
print("How much do you need {} ".format(color) + item2 + " ?")
item2_quantity = int(input())
item2_price = int(item2_quantity * ripe_bananas)
print(f"Total $: {item2_price}")
total = item1_price + item2_price
print (f"total: $  {total}")


# In[ ]:




