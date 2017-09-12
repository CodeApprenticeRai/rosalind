
# coding: utf-8

# In[1]:


#Used pprint for testing
import pprint
pp = pprint.PrettyPrinter(indent=4)

#Opened the file
with open("rosalind_gc.txt", "r") as f:
	data = f.read()

#Cleaning data
data = data.split('>')
data.remove('')
data = [d.replace('\n','') for d in data]

data_dict = {}

#Creates a dictionary, 'label':[DNA_string, GC_content]
for d in data:
    data_dict[d[0:13]] = [d[13:]]
    data_dict[d[0:13]].append( 100*((d.count('C')+d.count('G'))/ len(d[13:])) )

#Sorts for largest GC-content in the dict
biggest = 0
for key in data_dict:
    if  data_dict[key][1] > biggest:
        b_key = key
        biggest = data_dict[key][1]
        


# In[2]:


#Result
print(b_key, round(data_dict[b_key][1],6), sep="\n")


# In[3]:





# In[4]:





# In[ ]:




