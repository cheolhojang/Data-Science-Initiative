
# coding: utf-8

# In[1]:


from datascience import *
import numpy as np
# These lines set up graphing capabilities.
import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import warnings
warnings.simplefilter('ignore', FutureWarning)


# In[2]:


# HIDDEN
from datascience import *
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import math
from scipy import stats
import numpy as np


# In[3]:


from IPython.display import Image
from IPython.core.display import HTML 
Image(url= "https://cdn.businessformtemplate.com/samples/Eviction_Notice.png")


# # PLAN FOR DATA JUSTICE IN EVICTION
# 
# 
# Data provided by 
# 
# http://www.antievictionmappingproject.net
# 
# https://www.immigrationadvocates.org/nonprofit/legaldirectory/search?&state=CA&national=0&county=&legalArea=&legalService=&nonLegalService=&interestArea=&population=&legalNetwork=&language=&detentionFacility=&text=&zip=&interpreting=0&map=1 
# 
# 
# ## EVICTION
# 
# - Eviction is a very serious issue in today's society. People are getting evicted from their homes and houses at an alarming rate and there is very little data about what happens after they become evicted or what options they had financially. We're going to examine the eviction data with other places in the United States and compare the two. But before that, we need an accurate picture and an intuitive understanding of just how bad eviction has become.
# 
# - The Eviction data I worked with is from a website called AntiEvictionMappingProject. The Oakland Map specifically is what we're going to be examining. There is ample eviction data all across the Bay Area, but we're only taking a look at a tiny part of it to understand the bigger picture. To minimize the deviation from the complete data set, we're going to look at 3 different sample sizes; 
# 
# - First, we're going to look at a tiny street corner with less than 5 evictions, Second, we're going to examine a moderate size street called Alcatraz Avenue which has about 10 evictions.
# ## RESOURCES
# - Once we get a good understanding of the eviction situation in Oakland, we're going to take a look at some of the resources available to immigrants and people that have been evicted from their homes in the East Bay and compare it to other areas, such as San Francisco, Los Angeles, and various areas in between. 

# In[4]:


import datetime
#Relative day between the constraints of the graph
def yearconversion(year,month,day):
    begin = datetime.date(2015, 11, 30);
    end = datetime.date(2005, 1, 1);
    deltad = (begin - end);
    current = datetime.date(year,month,day) - end;
    proportionoftime = current/deltad
    return proportionoftime


# In[5]:


#Returns an array of the year converted proportions to be applied to a table
def proportioncollector(table):
    emp = make_array()
    for i in np.arange(len(table.column(0))):
        singlerow = table.row(i)
        emp = np.append(emp, yearconversion(singlerow.item(2),singlerow.item(3),singlerow.item(4)))
    return emp


# In[6]:


smallstreet = Table.read_table('62ndStreet.csv')


# In[7]:


((smallstreet.sort('Eviction Day',descending = True)).sort('Eviction Month', descending = True)).sort('Eviction Year', descending = True)


# In[8]:


resources = Table.read_table('resources.csv')
resources


# In[9]:


eastbay = resources.where(' Area', are.equal_to(' East Bay'))
eastbay


# In[10]:


losangeles = resources.where(' Area', are.equal_to(' Los Angeles'))
losangeles


# In[11]:


gilroy = resources.where(' Area', are.equal_to(' Gilroy'))
gilroy


# In[12]:


watsonville = resources.where(' Area', are.equal_to(' Watsonville'))
watsonville


# In[15]:


fresno = resources.where(' Area', are.equal_to(' Fresno'))
fresno


# In[17]:


bakersfield = resources.where(' Area', are.equal_to(' Bakersfield'))
bakersfield


# In[9]:


ordered = resources.sort(' Area', descending = True)
ordered


# In[18]:


areabar = resources.group(' Area')
pre = areabar.sort('count', descending = True)
pre.barh(' Area')


# In[19]:


orderedresources = Table.read_table('orderedresources.csv')
areabar = orderedresources.group(' Area')
pre = areabar.sort('count', descending = True)
pre.barh(' Area')


# In[39]:


stations = Table.read_table('furthereast.csv')
stations


# In[41]:


Marker.map_table(stations.select('lat', 'long', 'color'))

