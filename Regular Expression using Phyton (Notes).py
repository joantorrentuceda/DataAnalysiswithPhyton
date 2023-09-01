#!/usr/bin/env python
# coding: utf-8

# # Re Module + Regex Methods

# In[4]:


import re


# In[5]:


quote = "There's only one thing I hate more than lying: skim milk. Which is water that's lying about being milk. - Ron Swanson"


# In[6]:


re.search("milk",quote).group()


# In[7]:


re.findall("milk",quote)


# In[8]:


len(re.findall("milk",quote))


# In[9]:


re.split("\.",quote)


# In[10]:


quote = "There's only one thing I hate more than lying: skim milk. Which is water that's lying about being milk. - Ron Swanson"


# In[11]:


re.sub("milk", "dairy", quote, count = 1)


# # Regex Meta-Characters

# In[12]:


import re


# In[13]:


string = 'I like the mountains in the spring. 234098'


# In[14]:


re.findall('[a-zA-Z0-9]',string)


# In[15]:


string = 'I have 123,456 koalas!'


# In[16]:


re.findall('[0-4]', string)


# In[17]:


string = 'You can see sea shells by the sea shore. sba'

re.findall('s.a', string)


# In[18]:


string = "Well well well... if it isn't Will Wilmer"

re.findall('W.{2}l', string)


# In[19]:


# ^

string = 'Happy birthday to you. Happy birthday to you. Happy birthday dear Alex, happy birthday to you.'

re.findall('^you', string)


# In[20]:


re.findall('^Happy', string)


# In[21]:


# $

re.findall('you.$', string)


# In[22]:


# * - zero or more
# + - one or more
# ? -zero or one


# In[23]:


string = 'This Thing called a Thimble has Thrice hurt me'

re.findall('Thi.*e', string)


# In[24]:


string = 'This Thing called a Thimble has Thrice hurt me'

re.findall('Thi.+e', string)


# In[25]:


string = 'This Thing called a Thimble ha Thrice hurt me'

re.findall('Thi.{3}?e', string)


# In[27]:


# |

string = 'I hate that I love balloon animals. They are beautiful.'

re.findall('love|beautiful', string)


# In[28]:


string = 'I hate that I love balloon animals. They are beautiful.'

re.findall('lovely|beautiful', string)


# In[29]:


string = 'I like cats. You like cats? We all like cats.'

re.findall('\?',string)


# # Regular Expression Use Cases

# In[30]:


import re

random_text = '''
My name is Mr. Neo. My phone number is 123-456-7890. My email is ChosenOne@gmail.com
My name is Mr. Morphius. My phone number is 413-234-2568. My email is CoolGuy@yahoo.com. 
My name is Mrs. Trinity. My phone number is 285-036-8215. My email is ChosenOnesGirl1@apple.com.
'''


# In[31]:


re.findall('@([a-z]+)',random_text)


# In[32]:


re.findall('@[a-z]+',random_text)


# In[33]:


re.findall('@([\w\.]+)',random_text)


# In[34]:


re.findall('@[\w\.]+',random_text)


# In[35]:


re.findall('[\w+]+@[\w\.]+',random_text)


# In[36]:


re.findall('\d{3}-\d{3}-\d{4}',random_text)


# In[37]:


# Normally, data is not given as a text string. We have to apply regular expression, for example, to a list:

my_list = ['ChosenOne@gmail.com', 'CoolGuy@yahoo.com.', 'ChosenOnesGirl1@apple.com.']


# In[39]:


for email in my_list:
    print(re.findall('@[\w\.]+',email))


# In[41]:


# If we also want the output as a list: 

domain_list = [re.findall('@[\w\.]+',email)[0] for email in my_list]

print(domain_list)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




