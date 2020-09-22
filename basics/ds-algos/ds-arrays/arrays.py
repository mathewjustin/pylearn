array = [2,3,5,7,1]

print(array[0]) # index based access , indexes will be starging with 0

print(array[0:2]) #returns from index 0 to index 2 exclusive

print(array[:-1])  # all expect last 1

array2 = [10.0,3,'Justin']  # In python array can mix the types


# linear serch O(N)
max=array[0]
for num in array:
    if num>max:
        max=num

print(max)