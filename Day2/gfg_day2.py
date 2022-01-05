
# Given a positive integer N. You have to find Nth natural number after removing all the numbers containing digit 9.


#User function Template for python3

class Solution:
    def findNth(self,N):
        newn=""
        while(N>0):
            newn=str(N%9)+newn
            N=N//9
        return int(newn)
            
        #code here

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t=int(input())
for i in range(0,t):
    n=int(input())
    obj=Solution()
    s=obj.findNth(n)
    print(s)
# } Driver Code Ends
