#!/usr/bin/env python
# coding: utf-8

# In[29]:


def days_to_units(num_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{num_of_days} days are {num_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{num_of_days} days are {num_of_days * 24 * 60} minutes"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dictionary):
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered a 0, please enter a valid positive number")
        else:
            print("you entered a negative number, no conversion for you!")
    except ValueError:
        print("your input is not a valid number. Don't ruin my program!")
        
class User:
    #constructors
    def __init__(self, email, name, password, cur_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = cur_job_title
    #changing new password
    def change_password(self, new_password):
        self.password = new_password
        return 'New password: ', self.password
        # do somth
        
    # changing job title
    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title
        return 'New Job Title is', self.current_job_title
    def get_user_info(self):
        print(f'User {self.name} currently works as a {self.current_job_title}. You can contact then at {self.email}')

# In[ ]:





# In[9]:


ff = {'f': 5, 'h':66}
#print(ff['f'])


# In[ ]:




