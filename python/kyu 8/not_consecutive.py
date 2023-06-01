'''
num = [1,2,3,4,6,7,8]

def first_consecutive(list):
    for i,j in enumerate(list,list[0]):
        if i!=j:
            print(i)
        else:
            print(None)

first_consecutive(num)
'''

def non_consecutive(arr):
    prev = arr[0]
    first = None
    for num in arr[1:]:
        if (prev + 1) != num:
            first = num
            break
        prev += 1
    return first


print(non_consecutive([1,2,3,4,5,6,7,8,9]))

### Reference

# Finding first non-consecutive number