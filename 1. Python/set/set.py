# Set Python ka ek collection data type hai jo unique values store karta hai.

# Duplicate values automatically remove ho jati hain.
# Indexing nahi hoti.
# Unordered collection hai (items ka order fixed nahi hota).
# Mutable hai (add/remove kar sakte hain).

numbers = {10, 20, 30, 20, 10}

#print(numbers) # 20 10 30 (order change ho sakta hai) Duplicate Values Allowed Nahi Hai
#numbers.add(40)
#print(numbers) # 20 10 30 40 (add karta hai) mutable Hai
# print(numbers[0]) #index nahi hota

...

# Empty Set Banana
s = {} #dictionary hai
s={1}#set hai 
s={1,}#set hai
# s = set() #set hai
#print(type(s))

#set Mein Item Add karna
#add()
fruits={"Apple","Mango","ram"}
fruits.add("kiwi")
#print(fruits)
fruits.add("pineapple")
print(fruits)
fruits.update(["ram", "mohit"])
# fruits.remove("App") #give error if not exists in set 
# fruits.discard("Orange") #remove (Error Nahi Deta) 
# fruits.pop() #remove
# fruits.clear() #remove all items

#print(fruits)

#loop in set
fruits ={"Apple","Mango","Banana"}
# print(fruits)

# for fruit in fruits:
    # print(fruit)