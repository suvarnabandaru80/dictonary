# Create a dictionary from two lists:
# a.	keys = ['id', 'name', 'age']
# b.	values = [101, 'John', 25
# a= ['id', 'name', 'age']
# b= [101, 'John', 25]
# c=dict(zip(a,b))
# print(c)

#2.	Create a dictionary to store student name and age.
# k={}
# k['name']=input("Enter your name:")
# k['age']=int(input("enter your age:"))
# print(k)


#Create an empty dictionary and add key-value pairs one by one.
# k={}
# k["name"]=input("enter your name:")
# k["age"]=input("enter your age:")
# k["city"]=input("enter your city:")
# print(k)

#loop 
# res=[]
# for i in range(3):
#     k={}
#     print({i+1})
#     k["name"]=input("enter your name:")
#     k["age"]=input("enter your age:")
#     k["city"]=input("enter your city:")
#     res.append(k)
# print("\ncollected Data:")    
# for person in res:
#     print(person)

# Get the value of key "salary" from this dictionary:
# EX: employee = {'name': 'John', 'age': 30, 'salary': 50000}
# employee = {'name': 'John', 'age': 30, 'salary': 50000}
# print(employee['salary'])

#Remove the last inserted key-value pair from the dictionary using an appropriate method
# employee = {'name': 'John', 'age': 30, 'salary': 50000}
# employee.popitem()
# print(employee)

#Define packing and unpacking in Python. Also, provide one example for both packing and unpacking.
# Packing :
# This packing is nothing but grouping n no.of elements into a single variable is called packing .
# ex:res=[123.3.134,True,"suv"]
# Unpacking :
# This is nothing but gettting the elemnts from the single variable and assiging diffrent variables to the elemnts is called unpacking .
# EX:res=[123.3.134,True,"suv"]
# a,b,c=res
# print(a)
# print(b)
# print(c)
# print(a,*b)