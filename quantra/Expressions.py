
# coding: utf-8

# In[1]:


PV = 1000


# In[2]:


r = 0.05
n = 1

FV = PV * ((1+r)**n)
print(FV)


# In[3]:


FV = 1050
r = 0.05
n = 1

PV = FV / ((1+r)**n)
print(PV)


# In[4]:


PV = 1000
r = 0.05
n = 2
t = 1

FV = PV * ((1+(r/n))**(n*t))
print(FV)


# In[5]:


r = 0.1
n = 3
PV = 0
FV = 9476.96

AP = (FV * r) / ( ((1+r)**n) - 1) 
print(AP)


# In[6]:


r = 0.1
n = 5
AP = 2500

PV = (AP * (1-( (1+r)**-n) )) / r
print(PV)


# In[7]:


r = 0.08
n = 45
AP1 = 30000

PV = (AP1 * (1 - ((1+r)**-n) )) / r
print(PV)


# In[8]:


FV = 363252.0450945144
n = 25
r = 0.15

AP = (FV * r) / (((1+r)**n) - 1)
print(AP)

