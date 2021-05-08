#!/usr/bin/env python
# coding: utf-8

# In[1]:


usernames=['Malika', 'Marhabo', 'Mohiniso', 'Munira','Admin']
a=input('Please enter your name:')
for users in usernames:
    if a in usernames and a != 'Admin':
        print(f'Hello {a} thank you for logging in again.')
        break
    elif a =='Admin':
        print(f'Hello {a}, would you like to see a status report?')
        break


# In[2]:


current_users=['Malika', 'Marhabo', 'Mohiniso', 'Munira','Admin']
new_users=['Malika', 'Marhabo', 'Javlon', 'Jahongir','Abdunabi']
new_user=input('Please enter your name:')
for users in new_users:
    if new_user in new_users =='Malika' or 'Marhabo':
        print('That username has been already used, enter a new username:', end='')
    a=input()
    if a in new_users and a != 'Malika' or 'Marhabo' :
        print('This username is available')
        break   
    else:
        print('That username does not exit')


# In[14]:


import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
while guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break    # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))


# In[ ]:




