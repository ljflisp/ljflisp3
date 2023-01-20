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
  print(str(s.maxSubArray(nums1)))
  print(str(s.maxSubArray(nums2)))