# Write a function that accepts a list of integers and returns a new list containing only the even numbers.
def even_numbers(n):
    new_list=[]
    for i in n:
        if i%2==0:
            new_list.append(i)
    return new_list

n=[2,4,1,6,7,9,10]
print(even_numbers(n))

