#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.


# In[2]:


fin = open('words.txt')  


def make_dict():
    d = dict()
    for line in fin:
        word = line.strip()
        d[word] = word
    return d

       
      
    
    


# In[3]:


make_dict()


# In[ ]:





# In[ ]:




