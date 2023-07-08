def sorted_array(array):
    new_array=[]
    for i in range(len(array)):
        new_array.append(array[i]**2)
    new_array.sort()
    return new_array
print(sorted_array(list(map(int,input().split()))))
       