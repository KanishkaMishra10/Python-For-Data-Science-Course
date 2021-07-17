#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os             #os module to interact with the functionality of the operating system
from PIL import Image
from IPython.display import IFrame

Here 'r' is the response object, it has information about the request, like the status of the request.
# In[2]:


url='http://www.ibm.com/'
r=requests.get(url)


# In[3]:


r.status_code


# In[4]:


print(r.request.headers)


# In[5]:


print("request body: ", r.request.body)


# In[6]:


header=r.headers
print(r.headers)


# In[7]:


header['date']


# In[8]:


header['Content-Type']


# In[9]:


r.encoding


# In[10]:


#to view the first 100 characters
r.text[0:100]

To load the non-text requests, like images.
# In[11]:


url='https://gitlab.com/ibm/skills-network/courses/placeholder101/-/raw/master/labs/module%201/images/IDSNlogo.png'


# In[12]:


#make a get request
r=requests.get(url)
print(r.headers)


# In[13]:


r.headers['Content-Type']


# In[14]:


#An image is a response object that contains the image as a bytes-like object. As a result, we must save it using a file object. First, we specify the file path and name

path=os.path.join(os.getcwd(),'image.png')
path


# In[15]:


#to save the file 

with open(path,'wb') as f:
    f.write(r.content)


# In[16]:


Image.open(path)  


# In[17]:


url_get='http://httpbin.org/get'


# In[18]:


payload={"name":"Joseph","ID":"123"}


# In[19]:


r=requests.get(url_get,params=payload)


# In[20]:


r.url


# In[21]:


print("request body:", r.request.body)
print(r.status_code)
print(r.text)
r.headers['Content-Type']


# In[22]:


r.json()         #to return the python dictionary


# In[23]:


r.json()['args']


# # Post Request
Like a GET request, a POST is used to send data to a server, but the POST request sends the data in a request body. In order to send the Post Request in Python, in the URL we change the route to POST:
# In[24]:


url_post='http://httpbin.org/post'


# In[25]:


r_post=requests.post(url_post,data=payload)


# In[26]:


print("POST request URL:",r_post.url )
print("GET request URL:",r.url)


# In[27]:


print("POST request body:",r_post.request.body)
print("GET request body:",r.request.body)


# In[28]:


r_post.json()['form']


# In[ ]:




