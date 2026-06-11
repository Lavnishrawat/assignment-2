#Answer 1
my_tuple=(10,20,30,40,50)
print(my_tuple[0])
print(my_tuple[4])
print(len(my_tuple))
print(my_tuple[1:4])
#Answwer 2
fruits=("apple","banana","mango","orange")
print(fruits[1])
print(fruits[2:4])
print(len(fruits))
#Answer 3
numbers={10,20,30,40,50}
print(numbers)
print(len(numbers))
if(30 in numbers):
    print("30 is oresent here")
else:
    print("30 is not present here")
#Answer 4
set1={1,2,3,4}
set2={3,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))
#Answer 5
student={"name":"lavnish",
         "age":19,
         "course":"python"
}
print(student)
print(student["name"])
print(student["age"])
#student course creating a list
numbers = [12,45,7,23,56,89,34]
print(max(numbers))
numbers.sort()
print(numbers[-2])
#Answer 6
arr=[10,20,30,40,50,60]
print(arr[::-1])
#Answer 7 
data=(5,10,15,20,25,30,35)
count = 0
for i in data:
    if i %5 == 0:
        count += 1
print(count)
print(sum(data))
print("average:",sum(data)/len(data))
#Answer 8 
students = {"aman":78,
            "ria":92,
            "kirti":88,
            "rahul":95
}
print(max(students.values()))
print(min(students.values()))
for name, marks in students.items():
    if marks > 85:
        print(name)
#Answer 9 
arr = [1, 2, 2, 3, 1, 4, 2] 
def count_frequency(arr):
    checked = []

    for i in arr:
        if i not in checked:
            print(i, "=", arr.count(i), "times")
            checked.append(i)

arr = [1, 2, 2, 3, 1, 4, 2]
count_frequency(arr)
#Answer 10
arr = [10, 20, 30, 20, 40, 10, 50, 30] 
def find_duplicates(arr):
    print("Duplicate elements are:")

    for i in arr:
        if arr.count(i) > 1:
            print(i)

arr = [10, 20, 30, 20, 40, 10, 50, 30]
find_duplicates(arr)
