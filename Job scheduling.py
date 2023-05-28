
profit = [15, 27, 10, 100, 150]
jobs = ["j1", "j2", "j3", "j4", "j5"]
deadline = [2, 3, 3, 3, 4]

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
