# Write a function that takes list as an input and returns the sum of the numbers
def sum_list(numbers):
    return sum(numbers)

nums=[1,2,3,4,5,6]
result=sum_list(nums)
print(result)


# Write a function that takes list as an input and returns the max element
def max_list(ele):
    return max(ele)

lst=[10,45,76,21,63]
result1=max_list(lst)
print(result1)


# Write a function which takes list as an input and returns the reverse of the list
def reverse_list(num):
    return num

lst1=[1,2,4,5,7,10]
result2=reverse_list(lst1[::-1])
print(result2)


# Write a function which takes list as an input and returns the sorted list
def sorted_list(sorting):
    for i in range(len(sorting)):
        for j in range(i+1,len(sorting)):
            if sorting[i]>sorting[j]:
                sorting[i],sorting[j]=sorting[j],sorting[i]
    return sorting

lst2=[34,56,78,91,28]
result3=sorted_list(lst2)
print(result3)


# Write a function which takes list as an input and returns the mean
def mean(numbs):
    a=sum(numbs)
    b=len(numbs)
    return a/b

lst3=[4,5,6,8,9]
result4=mean(lst3)
print(result4)


# Write a function which takes list as an input and returns the mode
def mode_list(lst4):
    counts=0
    num=list[0]
    for x in lst4:
        current_freq=lst4.count(x)
        if (current_freq>counts):
            counts=current_freq
            num=x
    return num

lst5=[1,1,4,5,8,8,7,9,4,3,6,1,1,1,8,8,8,8,8]
result5=mode_list(lst5)
print(result5)
    

# Problem Solving
n = int(input("Enter the number of elements: "))
a=[]
for x in range(n):
    j=int(input("Enter the value of array: "))
    a.append(j)
    
k = int(input("Enter the key integer for a k sized-list: "))
b=[]
for i in range(k):
    start = int(input("Enter the start value: "))
    end = int(input("Enter the end value: "))
    sum_start_to_end=int(sum(a[start:end+1]))
    b.append(sum_start_to_end)

print(b)