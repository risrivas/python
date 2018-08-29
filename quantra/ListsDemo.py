
# coding: utf-8

# In[1]:


new_list = []
type(new_list)


# In[2]:


new_list=[10,20,30,40]
type(new_list)


# In[3]:


new_list=[10,20.2,"thirty",40]
type(new_list)


# In[4]:


new_list=[[10,20,30,40], [10.2,11.5,4.5,7.8], ["ten", "Rishi"]]
type(new_list)


# In[5]:


new_list=[10,[20.2,["thirty",[40]]]]
type(new_list)


# In[6]:


new_list=[10,20,30,40]
print(new_list)


# In[7]:


new_list.append(50)
print(new_list)


# In[8]:


new_list.extend([60,70,80,90])
print(new_list)


# In[9]:


new_list.insert(0,0)
print(new_list)


# In[10]:


new_list.remove(0)
print(new_list)


# In[11]:


new_list.pop()


# In[12]:


print(new_list)


# In[13]:


new_list.pop(4)


# In[14]:


print(new_list)


# In[15]:


new_list.index(60)


# In[16]:


new_list.count(20)


# In[17]:


print(new_list)


# In[18]:


new_list.reverse()
print(new_list)


# In[19]:


new_list.sort()
print(new_list)

