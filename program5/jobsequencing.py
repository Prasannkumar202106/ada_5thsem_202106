#job sequencing problem with maxixmum profit and time deadline
def jobsequencing(arr: list, m: int) -> list:
    
    
    arr = sorted(arr, key=lambda i: i[1], reverse=True) 
    print(arr)
    count = 0 # for counting jobs added to sequence
    job_sequence=[None]*m
    for item in arr:
        if count >= m:
            break
        i=0
        for i in range(item[2]-1,-1,-1):
            if job_sequence[i] == None:
                job_sequence[i] = (item[0],item[1])
                count+=1
                break
    
    return job_sequence

# Driver code:
jobs = input("Enter jobs : ")   #taking  input (seperated by ",")
jobs = list(jobs.split(','))  # creating list 

profits = input("Enter profits : ") # taking profits input
profits = list(profits.split(','))
profits = [int(i) for i in profits]  #creating list

deadlines = input("Enter deadlines :") # taking deadlines
deadlines = list(deadlines.split(','))
deadlines = [int(i) for i in deadlines] #creating list 


# a data model arr to store list of tuples of jobs , profits , deadlines
arr = [(jobs[i], profits[i], deadlines[i]) for i in range(len(jobs))]

print(jobsequencing(arr, max(deadlines))) # calling the function jobsequencing..