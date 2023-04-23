# Write a python script to sort(ascending and descending) a dictionary by value
x = {4:4,1:2,3:4,2:4}
y = sorted(x.items())
print(y)
z = y[::-1]
print(z)

      
# Given a list of integers, write a function that returns the smallest element in the list.
def numbers(nums):
    nums.sort()
    return nums[0]
  
print(numbers([7,4,5,6,2,1]))



#Write a function that takes in a list of integers and returns the longest consecutive subsequence of the list. 
# For example, given [1, 2, 3, 5, 6, 7, 8], the function should return [5, 6, 7, 8].
def list_ints(nums):
    # for num in nums:
        nums.sort()
        return nums[2:5] 
print(list_ints([20,40,30,10,50]))

# Write a python program to append new item to the end of the array

def fruits(arr):
      arr.append("mango")
      return arr
print(fruits(["apple","oranges","melon"]))

# Write a python program to reverse the order of items in an array
def fruits(arr):
      arr.reverse()
      return arr
print(fruits(["apple","oranges","melon"]))

# Turn every item of a list into its square
def empty_Arr(arr):
      empty_List = []
      for x in arr:
            empty_List.append(x**2)
      return empty_List      
print(empty_Arr([2,4,6,8]))

# Turn every item of a list into its square root
def empty_Arr(arr):
      empty_List = []
      for x in arr:
            empty_List.append(x**0.5)
      return empty_List      
print(empty_Arr([2,4,6,8]))

# Remove all  occurences of a specified item from a list
def empty_Arr(nums):
      empty_List = []
      for x in nums:
            if x not in empty_List:
                empty_List.append(x)
      return empty_List      
print(empty_Arr(["draw","paint","draw"]))
      












        
    