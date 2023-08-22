def binary_search(list, target):

    first_i = 0
    last_i = len(list)-1

    while first_i <= last_i:
        mid_i = (first_i+last_i)//2

        if target == list[mid_i]:
            return mid_i
        elif target > list[mid_i]:
            first_i = mid_i + 1
        else:
            last_i = mid_i - 1

sorted_list = [ 5,9,13,19,31,46,80]
result = binary_search(sorted_list, 1)
print(result)
