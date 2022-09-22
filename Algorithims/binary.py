content = [1,2,3,4,5,6,7,8,9]
item = 10
start = 0
end = (len(content) -1)
search = 8

while start <= end :
    mid = (start + end)//2
    if search == content[mid] :
        print("Content found")
        break
    elif start == end :
        print("Content NOT found")
        break
    else:
        if item < content[mid] :
            end = mid -1
        elif item > content[mid] :
            start = mid +1