array = [1,2,3,4,5,6,7,8,9,10]
value = 8

def search(array, value):
    for i in range(0, len(array)):
        if value == array[i] :
            return i
    return None
print(f"Value on position {search(array,value)}")