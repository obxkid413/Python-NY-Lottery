
# coding: utf-8

# In[1]:

import pandas as pd
import matplotlib.pyplot as plt


# open and read file

lotto=pd.read_csv('/Users/jon/Downloads/Lottery_NY_Lotto_Winning_Numbers__Beginning_2001.csv')

#lotto_df=pd.DataFrame(lotto)


# In[2]:

lotto_df=pd.DataFrame(lotto)


# In[3]:

lotto_df.head()


# In[4]:

lst=[]
for index, row in lotto_df.iterrows():
    lst.append(row['Winning Numbers'])
    


# In[5]:

lst=[i.split() for i in lst]


# In[6]:

#make sure the split did what I expected
print lst[0:2]


# In[7]:

#append every individual number to a new list
numbers=[]
for i in lst:
    for k in i:
        numbers.append(k)
        
        


# In[8]:

#create a dictionary that counts every number
counter={}

for i in numbers:
    if i in counter:
        counter[i]+=1
    else:
        counter[i]=1
        


# In[20]:

df_count = pd.Series(counter, name='Freq')
df_count.index.name='Number'
df_count.reset_index()
df_count=pd.DataFrame(df_count)

df_count.sort_values('Freq', ascending=False)
# We can see about 12 percent of all winning tickets contained the number 53. This was the most frequent number in winning tickets.




# In[14]:

import xlsxwriter


# In[18]:

''''export results to Excel if desired
workbook=xlsxwriter.Workbook('/Users/jon/Documents/jons_lottery.xlsx')
worksheet=workbook.add_worksheet('number_freq')

row=1
col=0

for keys in counter.keys():
    worksheet.write(row, col, keys)
    row+=1
    
row=1
col=1

for values in counter.values():
    worksheet.write(row, col, values)
    row+=1
    


# In[23]:

# we can do the same thing for the bonus number
lst_bonus=[]
for index, row in lotto_df.iterrows():
    lst_bonus.append(row['Bonus #'])


# In[24]:

#since there's only a single number, we can just go straight to counting those in the list
counter_bonus={}

for i in lst_bonus:
    if i in counter_bonus:
        counter_bonus[i]+=1
    else:
        counter_bonus[i]=1


# In[30]:

#print counter_bonus
#find max
import operator
max_bonus=max(counter_bonus.iteritems(), key=operator.itemgetter(1))[0:2]

print max_bonus
# We can see the number 51 appeared 48 times which was the most for the bonus numbers


# In[10]:

# We may also want to know if there are pairs of numbers that occur together frequently

from collections import Counter
from itertools import chain, combinations

num_pairs = Counter(chain.from_iterable(combinations(i, 2) for i in lst))



# In[22]:

# Let's get the max from the pairs
import operator
max_pair= max(num_pairs.iteritems(), key=operator.itemgetter(1))[0:2]


# In[23]:

print max_pair
 # We see the pair of (27,50) occurred the most frequently.  This pair occurred in about 2% of all winning tickets.
# We could look at trios too but it would be less than even 2% so we'll stop at pairs for practical reasons.


# In[33]:

#The above max_pair calculation works because all of the sublists are 
# in ascending order, so there isn't a pair of (50, 27) that this function 
# wouldn't be counting here.

foo = lambda x: pd.Series([i for i in reversed(x.split('/'))])
new_df = lotto_df['Draw Date'].apply(foo)
new_df.head()




# In[41]:

new_df=new_df.rename(index=str, columns={0: "Year", 1: "Day", 2: "Month"})


# In[42]:

new_df.head()


# In[44]:

print new_df['Year'].value_counts()


# In[ ]:



