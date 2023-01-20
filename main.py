import os

print("Hello world from ...")
os.system("python --version")

class Solution:
  def __init__(self,x):
    
   if (x%9== 8)and(x%8== 7)and(x%6==5)and(x%5== 4)and(x%4== 3)and(x%2==1):
    print(x)
  
  