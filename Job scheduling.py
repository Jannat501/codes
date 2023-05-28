#!/usr/bin/env python
# coding: utf-8

# In[12]:


# profit = [15, 27, 10, 100, 150]
# jobs = ["j1", "j2", "j3", "j4", "j5"]
# deadline = [2, 3, 3, 3, 4]

profitNJobs = sorted(zip(profit, jobs, deadline), reverse=True)

slot = [0] * len(jobs)
total_profit = 0
scheduled_jobs = [0] * len(jobs)

for job in profitNJobs:
    for j in range(job[2], -1, -1):
        if slot[j] == 0:
            scheduled_jobs[j] = job[1]
            total_profit += job[0]
            slot[j] = 1
            break

print("Jobs scheduled:", scheduled_jobs[0:])
print("Total Profit:", total_profit)


# In[ ]:





# In[ ]:





# In[13]:


# profit = [50,15,45,80,11]
# jobs= ["J1","J2","J3","J4","J5"]
# deadline = [2,4,3,1,4]


profit = [15, 27, 10, 100, 150]
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadline = [2, 3, 3, 3, 4]
profitNjobs = sorted(zip(profit,jobs,deadline),reverse = True)


slot = [0] *len(jobs)
schedule = [0] * len(jobs)

total_prof = 0

for job in profitNjobs:
    for j in range(job[2],-1,-1):
        if slot[j] == 0:
            schedule[j] = job[1]
            slot[j] = 1
            total_prof += job[0]
            break
print("Job Scheduling ....",schedule[0:])
print("total profit :",total_prof)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




