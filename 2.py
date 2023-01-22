from replit import db
db["key1"]="李吉峰,新年快乐！祝你生日快乐！新的一年(2023)就让replit去accompany you."
print(db["key1"])
class node:
  def __init__(self,a=0,b=0,i=0,s= 0):
    self.x= a
    self.y= b
    self.i= i
    self.step= s
class Solution:
  def getBoard(self,grid):
    direction=[[1,0],[-1,0],[0,1],[0,-1]]
    n=len(grid)
    m= len(grid[0])
    visit=[[[0 for i in range(2)]for i in range(m)]for i in range(n)]
    p= []
    if(grid[0][0]==0):
      new= node(0,0,0,0)
      visit[0][0][0]=1
    else:
      new= node(0,0,1,0)
    p.append(new)
    flag=-1
    visit[0][0][-1]= 1
    cnt= 0
    while cnt<len(p):
      a= p[cnt]
      cnt+= 1
      if a.x==n-1 or a.y== n-1:
        flag= a.step
        break
      else:
        for i in range(0,4):
          new_x=a.x+direction[i][0]
          new_y=a.y+direction[i][1]
          if new_x<=n-1 and new_x>= 0 and new_y<=n-1 and new_y>= 0:
            if grid[new_x][new_y]== 0 and visit[new_x][new_y][a.i]== 0:
              visit[new_x][new_y][a.i]=1
              visit[new_x][new_y][1]= 1
              p.append(node(new_x,new_y,a.i,a.step+1))
        if grid[new_x][new_y]== 1 and a.i== 0 and visit[new_x][new_y][1]== 0:
          visit[new_x][new_y][1]=1
          p.append(node(new_x,new_y,1,a.step+1))
    return flag
      
if __name__== "__main__":
  a= [[0,1,0,0,0],[0,0,0,1,0],[1,1,0,1,0],[1,1,1,1,0]]
 # print("地图是: ",a)
  s= Solution()
 # print("最少要走: ",s.getBoard(a))

class Solution:
  def multiply(self,A,B):
    n=len(A)
    m=len(A[0])
    k= len(B)
    C=[[0 for _ in range(k)]for i in range(n)]
    for i in range(n):
      for j in range(m):
        if A[i][j]!=0:
          for l in range(k):
            C[i][l]+= A[i][j]*B[j][l]
    return C
    
if __name__== "__main__":
  A=[[1,0,0],[-1,0,3]]
  B=[[7,0,0],[0,0,0],[0,0,1]]
  s=Solution()
 # print("输入的两个数组是:A= ",A,"B= ",B)
  #print("输出的结果是: ",s.multiply(A,B))

class Solution:
  def largestRectangleArea(self,heights):
    indices_stack=[]
    area= 0
    for index ,height in enumerate(heights+[0]):
      while indices_stack and heights[indices_stack[-1]]>=height:
        popped_index= indices_stack.pop()
        left_index= indices_stack[-1] if indices_stack else -1
        width=index-left_index-1
        area= max(area,width*heights[popped_index])
      indices_stack.append(index)
    return area     
        
if __name__== "__main__":
  heights=[2,1,5,6,2,3]
  s= Solution()
  #print("输入每个直方图的高度: ",heights)
  #print("找到的直方图的最大面积: ",s.largestRectangleArea(heights))

class Solution:
  def maximalRectangle(self,matrix):
    if not matrix:
      return 0
    max_rectangle=0
    heights=[0]*len(matrix[0])
    for row in matrix:
      for index,num in enumerate(row):
        heights[index]=heights[index]+1 if num else 0
      max_rectangle=max(max_rectangle,self.find_max_rectangle(heights))
    return max_rectangle
  def find_max_rectangle(self,heights):
    indices_stack= []
    max_rectangle= 0
    for index,heights in enumerate(heights+[-1]):
      while indices_stack and heights[indices_stack[-1]]>=heights:
        popped=indices_stack.pop(-1)
        left_bound=  indices_stack[-1]if indices_stack else -1
        indices_stack.append(index)  #indices_stack.append(index) 
   # return max_rectangle
      max_rectangle=max(max_rectangle,(index-left_bound-1)*heights[popped])
      indices_stack.append(index)
    return max_rectangle  
    #max(max_rectangle,(index-left_bound-1)*heights[popped])
if __name__== "__main__":
   matrix=[[1,1,0,0,1],[0,1,0,0,1],[0,0,1,1,1],[0,0,1,1,1],[0,0,0,0,1]]
   #s=Solution()
  # print("输入的布尔类型的二维矩阵是: ",matrix)
   #print("最大矩阵的面积是: ",s.maximalRectangle(matrix))
#error

class Solution:
  def kthSmallest(self,matrix,k):
    if not matrix or not matrix[0] or k== 0:
      return None
    while len(matrix)>1:
      matrix.append(self.merge(matrix.pop(0),matrix.pop(0)))
    return matrix[0][k-1]
  def merge(self,nums1,nums2):
    res,index1,index2=[],0,0
    while index1<len(nums1)or index2<len(nums2):
      if index1>=len(nums1):
        res.append(nums2[index2])
        index2+= 1
      elif index2>=len(nums2):
        res.append(nums1[index1])
        index1+= 1
      elif nums1[index1]<nums2[index2]:
        res.append(nums1[index1])
        index1+= 1
      else:
        res.append(nums2[index2])
        index2 += 1
    return res
if __name__== "__main__":
  arr=[[1,5,7],[3,7,8],[4,8,9]]
  index= 4
  s= Solution()
  #print("输入的数组: ",arr)
 # print("运行后的结果是: ",s.kthSmallest(arr,index))

import sys
class Solution:
  def maxSubArray(self,nums):
    min_sum,max_sum=0,-sys.maxsize
    prefix_sum= 0
    for num in nums:
      prefix_sum+= num
      max_sum=max(max_sum,prefix_sum-min_sum)
      min_sum=min(min_sum,prefix_sum)
    return max_sum

if __name__== "__main__":
  s= Solution()
  nums1=[-1,-2,3,4,2,2,4,3,-6]
  nums2=[4,2,1,4,-1,2,7,4,-3]
  #print(str(s.maxSubArray(nums1)))
  #print(str(s.maxSubArray(nums2)))

class Solution:
  def maxTwoSubArray(self,nums):
    n=len(nums)
    a=nums[:]
    aa=nums[:]
    for i in range(1,n):
      a[i]=max(nums[i],a[i-1]+nums[i])
      aa[i]=max(a[i],a[i-1])
    b=nums[:]
    bb=nums[:]
    for i in range(n-2,-1,-1):
      b[i]=max(b[i+1]+nums[i],nums[i])
      bb[i]=max(b[i],bb[i+1])
    mx=-65535
    for i in range(n-1):
      mx=max(aa[i]+b[i+1],mx)
    return mx

if __name__== "__main__":
  s=Solution()
  n1=[6,5,4,3,2]
  n2=[2,1,2,1,2,1]
  #print(str(s.maxTwoSubArray(n1)))
  #print(str(s.maxTwoSubArray(n2)))

class Solution:
  def maxSubArray(self,nums,k):
    MIN=-2**32
    n=len(nums)
    array=[0]
    for num in nums:
      array.append(num)
    ans1= [[MIN for i in range(k+1)]for j in range(n+1)]
    ans2= [[MIN for i in range(k+1)]for j in range(n+1)]
    for i in range(1,n+1):
      for j in range(1,k+1):
        ans1[i][j]=max(ans1[i-1][j]+array[i],ans1[i-1][j-1]+array[i],ans2[i-1][j-1]+array[i])
        ans2[i][j]=max(ans1[i-1][j],ans2[i-1][j])
    return max
if __name__== "__main__":
   nums=[-1,4,-2,3,-2,3]
   k=2
   s=Solution()  
  # print("不重叠的数组和: ",s.maxSubArray(nums,k))
class Solution:
  def maxDiffSubArray(self,nums):
    n=len(nums)
    mx1=[0]*n
    mx1[0]=nums[0]
    forward=[mn1[0],mx1[0]]
    array_f=[0]*n
    array_f[0]=forward[:]
    for i in range(1,n):
      mx1[i]=max(mx1[i-1]+nums[i],nums[i])
      mx1[i]=min(mx1[i-1]+nums[i],nums[i])
      forward=[min(mn1[i],forward[0]),max(mx1[i],forward[1])]
      array_f[i]=forward[:]
    mx2=[0]*n
    mx2[n-1]=nums[n-1]
    mn2=[0]*n
    mn2[n-1]=nums[n-1]
    backward=[mn2[n-1],mx2[n-1]]
    array_b=[0]*n
    array_b[i]=backward[:]
    result=-65535
    #for i in range(n-1):
    #result=max(result,abs(array_f[i][0]-array_b[i+1][1]),abs(array_f[i][1]-array_b[i+1][0]))
  # return result
if __name__== "__main__":
  s=Solution()
  n1=[5,3,1,-4]
  n2=[3,-1,6,2]
  #print(str(s.maxDiffSubArrays(n1)))
class Solution:
  def intersection(self,nums1,nums2):
    return list(set(nums1)&set(nums2))
if __name__== "__main__":
  s= Solution()
  l1=[1,2,3,4] 
  l2=[2,4,6,8]
  #print(str(s.intersection(l1,l2)))
import collections
class Solution:
  def intersection(self,nums1,nums2):
    counts=collections.Counter(nums1)
    result= []
    for num in nums2:
      if counts[num]>0:
        result.append(num)
        counts[num]-= 1
    return result
if __name__== "__main__":
  s= Solution()
  l1=[1,2,3,4,5,6]
  l2=[2,4,6,8,10]
  #print(str(s.intersection(l1,l2)))
from collections import deque
class Solution:
  def thanK(self,nums,k):
    if not nums:
      return 0
    ans,product,index= 0,1,0
    queue=deque()
    while index<len(nums):
      product*= nums[index]
      queue.append(nums[index])
      while product>=k and queue:
        remove=queue.popleft()
        product/=remove
      if queue:
        ans+= len(queue)
      index+= 1
    return ans
if __name__== "__main__":
  s= Solution()
  l1= [8,4,3,6,10]
  num= 100
  #print(str(s.thanK(l1,num)))
class Solution:
  def minSubArray(self,nums):
    sum= 0
    minSum= nums[0]
    maxSum= 0
    for num in nums:
      sum+= num
      if sum-maxSum<minSum:
        minSum=sum-maxSum
      if sum>maxSum:
        maxSum=sum
    return minSum
if __name__== "__main__":
  s= Solution()
  l1=[1,-1,-2,1]
  l2=[3,-2,2,1]    
  #print(str(s.minSubArray(l1)))
  #print(str(s.minSubArray(l2)))
class Solution:
  def continuousSubArray(self,A):
    ans=-0x7ffffff
    sum= 0
    start,end= 0,-1
    result=[-1,-1]
    for x in A:
      if sum<0:
        sum= x
        start=end+1
        end=start
      else:
        sum+= x
        end+= 1
      if sum>ans:
        ans=sum
        result=[start,end]
    return result
if __name__== "__main__":
  nums=[-3,1,3,-3,4]
  s=Solution()
  #print(s.continuousSubArray(nums))    
class Solution:
  def subarraySum(self,nums):
    prefix_hash={0:-1}
    prefix_sum=0
    for i,num in enumerate(nums):
      prefix_sum+= num
      if prefix_sum in prefix_hash:
        return prefix_hash[prefix_sum]+1,i
      prefix_hash[prefix_sum]= i
    return -1,-1
if __name__== "__main__":
  nums= [-3,1,2,-3,4]
  s=Solution()
  #print(s.subarraySum(nums))
class Solution:
  def partitionArray(self,nums,k):
    start,end=0,len(nums)-1
    while start<= end:
      while start<= end and nums[start]<k:
       start+= 1
      while start<=end and nums[end]>= k:
       end-= 1
      if start<end:
         #nums[start],nums[end]=nums[end],nums[start]
        nums[start],nums[end]=nums[end],nums[start]
        start+= 1
        end-= 1
    return start
if __name__== "__main__":
   s= Solution()
   l1= [5,1,4,2,3]  
   num= 2 
   #print(str(s.partitionArray(l1,num)))
class Solution:
  def findPair(self,nums,k):
    if k>0:
      return len(set(nums)&set(n+k for n in nums))
    if k== 0:
      return sum(v>1 for v in collections.Counter(nums).values())
    return 0
if __name__== "__main__":
  s= Solution()
  l1=[6,3,4,2,5,1]
  num= 2
  #print(str(s.findPair(l1,num))) 
class Solution:
  def removeDuplicates(self,A):
    if A== []:
      return 0
    index= 0
    for i in range(1,len(A)):
      if A[index]!= A[i]:
        index+= 1
        A[index]+= A[i]
    return index+1
if __name__== "__main__":
  s= Solution()
  l1= [1,2,3]
  l2= [2,5,1,3]
  #print(str(s.removeDuplicates(l2)))
class Solution:
  def minimumSize(self,nums,s):
    if nums is None or len(nums)== 0:
      return -1
    n=len(nums)
    minLength=n+1
    num= 0
    j= 0
    for i in range(n):
      while j<=n and sum<s:
        sum+= nums[j]
        j+= 1
      if sum>=s:
        minLength= min(minLength,j-i)
        sum-= nums[i]
    if minLength== n+1:
      return -1
    return minLength

if __name__== "__main__":
  s= Solution()
  l1= [1,2,3,4,5]
  nums1= 10
  #print(str(s.minimumSize(l1,nums1)))
class Solution:
  def maxAverage(self,nums,k):
    if not nums:
      return 0
    start,end=min(nums),max(nums)
    while end-start>1e-5:
      mid=(start+end)/2
      if self.check_subarray(nums,k,mid):
         start=end
      else:
         end= mid
    return start
  def check_subarray(self,nums,k,average):
    prefix_sum=[0]
    for num in nums:
      prefix_sum.append(prefix_sum[-1]+num-average)
    min_prefix_sum= 0
    for i in range(k,len(nums)+1):
      if prefix_sum[i]-min_prefix_sum>= 0:
        return True
      min_prefix_sum= min(min_prefix_sum,prefix_sum[i-k+1])
    return False
if __name__== "__main__":
  s= Solution()
  nums=[5,3,-4,6,-7,2,-1]
  k=5
  #print(str(s.maxAverage(nums,k)))
class Solution:
  def findMin(self,nums):
    if not nums:
      start,end=0,len(nums)-1
      target=nums[-1]
      while start+1<end:
        mid=(start+end)//2
        if nums[mid]<=target:
          end= mid
        else:
          start= mid
      return min(nums[start],nums[end])
if __name__== "__main__":
  s= Solution()
  l1= [1,2,3,4,5]   
  #print(str(s.findMin(l1)))
class Solution:
  def findMin(self,num):
    min= num[0]
    start,end=0,len(num)-1
    while start<end:
      mid= (start+end)//2
      if num[mid]>num[end]:
        start= mid+1
      elif num[mid]<num[end]:
        end=mid
      else:
        end=end-1
    return num[start]
if __name__== "__main__":
  s= Solution()
  l1= [1,2,4,5,6,7,8]  
  #print(str(s.findMin(l1)))
class Solution:
  def search(self,A,target):
    if not A:
      return -1
    start,end= 0,len(A)-1
    while start+1<end:
      mid= (start+end)//2
      if A[mid]>=A[start]:
        if A[start]<=target<=A[mid]:
          end=mid
        else:
          start= mid
      else: 
          end= mid
    if A[start]== target:
      return start
    if A[end]== target:
      return end
    return -1
if __name__== "__main__":
  s= Solution()
  l1= [1,2,3,4,5]
  k= 5
  #print(str(s.search(l1,k)))
class Solution:
  def search(self,A,target):
    for num in A:
      if num== target:
        return True
    return False
if __name__== "__main__":
  s= Solution()
  l1= [1,2,3,4,5,6,7,8]
  target= 5
  #print(str(s.search(l1,target)))
import sys
class Solution:
  def subarraySumClosest(self,nums):
    prefix_sum=[(0,-1)]
    for i,num in enumerate(nums):
      prefix_sum.append((prefix_sum[-1][0]+num,i))
    prefix_sum.sort()
    closest,answer=sys.maxsize,[]
    for i in range(1,len(prefix_sum)):
      if closest>prefix_sum[i][0]-prefix_sum[i-1][0]:
        closest=prefix_sum[i][0]-prefix_sum[i-1][0]
        left=min(prefix_sum[i-1][1],prefix_sum[i][1])+1
        right=max(prefix_sum[i-1][1],prefix_sum[i][1])
        answer=[left,right]
    return answer
if __name__== "__main__":
  s= Solution()
  nums=[-3,1,1,-3,5]
  #print(s.subarraySumClosest(nums))
class Solution:
  def smallestDifference(self,A,B):
    C= []
    for x in A:
      C.append((x,'A'))
    for x in B:
      C.append((x,'B'))
    C.sort()
    diff= 0x7ffffff
    cnt=len(C)
    for i in range(cnt-1):
      if C[i][1]!=C[i+1][1]:
        diff=min(diff,C[i+1][0]-C[i][0])
    return diff
if __name__== "__main__":
  l1= [5,6,4,2,3]
  l2= [1,1,1,1,1]
  s= Solution()
  #print(str(s.smallestDifference(l1,l2)))
class Solution:
  def sameNumber(self,nums,k):
    vis= {}
    n= len(nums)
    for i in range(n):
      x= nums[i]
      if x in vis:
        if i-vis[x]<k:
          return "YES"
      vis[x]=i
    return "NO"
if __name__== "__main__":
  nums= [1,2,3,1,5,9,3]
  k= 4
  s= Solution()
  #print(s.sameNumber(nums,k))
class Solution:
  def reverseArray(self,nums):
    start= 0
    end= -1
    for _ in range(len(nums)//2):
      nums[start],nums[end]= nums[end],nums[start]
      start+= 1
      end-= 1
    return nums
if __name__== "__main__":
  s= Solution()
  nums= [1,2,5]
 # print(s.reverseArray(nums))

class Solution:
  def partitonalArray(self,nums):
    start,end= 0,len(nums)-1
    while start<end:
      while start<end and nums[start]%2== 1:
        start+= 1
      while start<end and nums[end]%2== 0:
        end-= 1
      if start<end:
        nums[start],nums[end]=nums[end],nums[start]
        start+= 1
        end-= 1
    return nums
if __name__== "__main__":
  s= Solution()
  nums= [1,2,3,4]
  #print(s.partitonalArray(nums))
class Solution:
  def isUnique(self,str):
    if len(str)>len(set(str)):
      return False
    else:
      return True
if __name__== "__main__":
  str= "abc"
  s=Solution()
  #print(s.isUnique(str))

class Solution:
  def lengthOfLongestSubstring(self,s):
    unique_chars=set([])
    j= 0
    n= len(s)
    longest= 0
    for i in range(n):
      while j<n and s[j] not in unique_chars:
        unique_chars.add(s[j])
        j+= 1
        longest= max(longest,j-i)
        unique_chars.remove(s[i])
    return longest
if __name__== "__main__":
  s= Solution()
  s1= "abccd"
  s2= "hahah"
  #print(str(s.lengthOfLongestSubstring(s1)))
  #print(str(s.lengthOfLongestSubstring(s2)))
class Solution:
  def longestPalindrome(self,s):
    if not s:
       return ""
    longest= ""
    for middle in range(len(s)):
      sub= self.find_palindrome_from(s,middle,middle)
      if len(sub)>len(longest):
        longest= sub
        sub.find_palindrome_from(s,middle,middle)
        if len(sub)>len(longest):
           longest= sub
    return longest
  def find_palindrome_from(self,string,left,right):
    while left>= 0 and right<len(string) and string[left]== string[right]:
      left-= 1
      right+= 1
    return string[left+1:right]
if __name__== "__main__":
  s= Solution()
  string1= "abcdedcb"
  #print(str(s.longestPalindrome(string1)))