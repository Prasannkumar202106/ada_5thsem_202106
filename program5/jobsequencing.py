#job sequencing problem with deadline
#initialize the statment
def printJobSequencing(arr,u):
              n=len(arr)
              for i in range(n):
                  for j in range(n-1-i):
                      if(arr[j][2]<arr[j+1][2]):
                          arr[j],arr[j+1]=arr[j+1],arr[j]
              result = [False]*u
              job = ['-1']*u
              for i in range(len(arr)):
                  for j in range(min(u-1,arr[i][1]-1),-1,-1):
                      if(result[j] is False):
                          result[j] = True
                          job[j] = arr[i][0]
                          break
              print(job)
              #driver code to get the result of job with maximum profit
arr =           [['j1',4,80],
                ['j2',7,100],
                ['j3',5,60],
                ['j4',3,10],
                ['j5',1,20]]    
print("the maximum profit sequence of jobs")
printJobSequencing(arr,5)

#here first input is job name,second one is deadline and third one is profit