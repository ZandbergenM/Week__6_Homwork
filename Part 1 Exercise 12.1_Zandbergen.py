#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Write a function called most_frequent that takes a string and prints the letters decreasing order of frequency.

# Sample String No man is an island Poem by John Donne English
"""No man is an island, Entire of itself,
Every man is a piece of the continent,
A part of the main.
If a clod be washed away by the sea,
Europe is the less.
As well as if a promontory were.
As well as if a manor of thy friend’s
Or of thine own were:
Any man’s death diminishes me,
Because I am involved in mankind,
And therefore never send to know for whom the bell tolls;
It tolls for thee."""

#Spanish
"""Ningún hombre es una isla,
Entero solo,
Cada hombre es un pedazo de un continente,
Una parte de lo completo.
Si el mar arrastrara a un tonto,
Europea sería menos
Exactamente como si arrastrara un promontorio
o arrastrara la casa de tu amigo
o tu propia casa.
La muerte de cualquier hombre me disminuye,
por que me involucro en la humanidad.
Por eso, no preguntes por quien tocan las campanas;
Las tocan por ti."""


# In[2]:


def read_file(filename): # a function to read a file that will later be selected in most_frequet function
    return open(filename).read() #opens the file and reads it


# In[3]:


def make_histogram(s): #a function that will create a histogram for all the letters in the string
    hist = {} #creates an empty dictionary named hist
    for x in s: #from the function make_histogram every letter in the future string
        hist[x] = hist.get(x,0) +1 #adds each letter to the dictionary and assigns a value, plus 1 every time it is identified in the loop
    return hist #returns the dictionary hist


# In[4]:


def most_frequent(s): #function for identifying the most frequent letters in the string
    hist = make_histogram(s) #calls on the function make_histogram from above
    t = [] #creates an empty list 
    for x, freq in hist.items(): # a for loop calling on each letter and the freqeuncy, a key pair tuple
        t.append((freq, x))#appends the tuple to the empty list t
        t.sort(reverse = True)#sorts from high to low
        res = [] #creats an empty list called res
        for freq, x in t:# I'm unsure what these last three lines are for and why they are needed. I don't understand the different between this part and the previous list t
            res.append(x)
    return res
    


# In[5]:


if __name__ == '__main__' :# Never mentioned and I'm not sure how this was expected to be understood...used when importing from another module
    string = read_file('12.1-Spanish.txt')#my text file chosen
    letter_seq = most_frequent(string)#calling the function from above
    for x in letter_seq:#for loop for each letter based on the sequence identified
        print(x) #prints all the letters from high to low


# In[6]:


if __name__ == '__main__' :
    string = read_file('12.1.txt')
    letter_seq = most_frequent(string)
    for x in letter_seq:
        print(x)


# In[ ]:




