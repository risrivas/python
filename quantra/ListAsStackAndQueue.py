
# coding: utf-8

# In[1]:


my_stack = [10, 20, 30, 40, 50]
my_stack.append(60)
print(my_stack)


# In[2]:


my_stack.pop()
print(my_stack)


# In[3]:


from collections import deque

my_queue = deque(["Federer", "Nadal", "Djokovic", "Agassi" , "Sampras"])
my_queue.append("Becker")
print(my_queue)


# In[4]:


type(my_queue)


# In[5]:


my_queue.popleft()


# In[6]:


print(my_queue)


# In[8]:


my_queue.pop()
print(my_queue)

