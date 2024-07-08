#!/usr/bin/env python
# coding: utf-8

# # Bank Statement Analysis

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


data = pd.read_excel(r"C:\Users\lenovo\Downloads\DS-Assignment Dataset and instructions\DS-Assignment Dataset and instructions\P1- BankStatements (2) - Copy.xlsx")
data.head()


# In[3]:


data.dtypes


# In[4]:


data.shape


# # Transaction Analysis

# - What is the total number of transactions made over the year?

# In[5]:


data["valueDate"] = pd.to_datetime(data["valueDate"])
data["transactionTimestamp"] = pd.to_datetime(data["transactionTimestamp"])


# In[6]:


data["year"] = data["valueDate"].dt.year


# In[7]:


no_of_trans = data.groupby("year").size()


# In[8]:


no_of_trans


# In[9]:


no_of_trans.plot(kind="bar")
plt.xticks(rotation=0)
plt.show()


#    - What is the distribution of transaction amounts (e.g., small vs. large transactions)?(define small and large transactions by yourself)

# In[10]:


data["amount"].mean()


# - let transactions amaount < 850 be "Small"
# - let transactions amaount >= 850 be "Large"

# In[11]:


small_trans = data[data["amount"] < 850]["amount"].count()
large_trans = data[data["amount"] >= 850]["amount"].count()


# In[12]:


print("Number of small transactions:", small_trans)
print("Number of large transactions:", large_trans)


# In[13]:


labels = ['Small Transactions (< 850)', 'Large Transactions (>= 850)']
sizes = [small_trans, large_trans]
colors = ['blue', 'red']
explode = (0.1, 0) 

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True)
plt.title('Distribution of Transaction Amounts')
plt.show()


#    - Analyze the frequency of different transaction types (debit vs. credit).

# In[14]:


type_counts = data['type'].value_counts()
type_counts


# In[15]:


type_counts.plot(kind='bar', color=['blue', 'green'])
plt.title('Frequency of Transaction Types')
plt.xlabel('Transaction Type')
plt.ylabel('Frequency')
plt.xticks(rotation=0)
plt.show()


# # Balance Analysis

#    - What is the trend of the account balance over time?

# In[16]:


plt.plot(data["valueDate"], data["currentBalance"] , color='y')
plt.title("Current Balance Trend")
plt.xlabel("time period")
plt.ylabel("Amount")
plt.show()


# The current balance trend shows significant fluctuations, characterized by a sharp increase in November 2023 followed by a pronounced decrease in December 2023.

# # Spending Patterns

# - What are the main categories of expenses (e.g., fuel, Ecommerce, food, shopping, ATM withdrawals, UPI transactions)?

# In[17]:


data.groupby("type")["mode"].value_counts()


# In[18]:


spending = data[data["type"] == "DEBIT"].groupby(["type","mode"]).size()


# In[19]:


spending


# In[20]:


type(spending)


#   - Analyze the frequency and amount of spending in each category.

# In[21]:


colors = ['blue', 'red','yellow']
explode = (0.5,0,0)

plt.pie(spending, colors=colors,explode =explode, autopct='%1.1f%%', shadow=True,labels=spending.keys())
plt.title('Distribution of Spending')
plt.legend()
plt.show()


# - UPI is the most commonly used method for spending

# # Income Analysis

# - What are the main sources of income (e.g., salary, UPI credits)?
# 

# In[22]:


Income = data[data["type"] == "CREDIT"].groupby("mode").size()


# In[23]:


Income


# - Identify any patterns in the timing and amount of income received.

# In[24]:


plt.pie(Income ,colors=colors ,explode = explode ,autopct = "%1.1f%%" ,shadow = True ,labels = Income.keys())
plt.legend()
plt.show()


# - Only 0.3% of the total payments received are cash Payments 

# # Alert Generation 
# 

# 
#    - Generate alerts for low balance or high expenditure periods.
# 

# In[25]:


low_bal_threshold = 10
low_bal_alerts = data[data["amount"] < low_bal_threshold]
low_bal_alerts = low_bal_alerts[["amount","type","mode","currentBalance","valueDate"]]


# In[26]:


print("Low Balance Alerts:")
print(low_bal_alerts)


# In[27]:


high_bal_threshold = 15000
high_bal_alerts = data[data["amount"] > high_bal_threshold]
high_bal_alerts = high_bal_alerts[["amount","type","mode","currentBalance","valueDate"]]


# In[28]:


print("High Balance Alerts:")
print(high_bal_alerts)


#    - Identify any unusual or suspicious transactions.

# In[29]:


susp_threshold = 25000
susp_alerts = data[data["amount"] > susp_threshold]
susp_alerts = susp_alerts[["amount","type","mode","currentBalance","valueDate"]]


# In[30]:


print("Suspicious Transactions:")
print(susp_alerts)


# In[ ]:





# In[ ]:





# In[ ]:




