def linear_search(list,target): 
    
    for i in range(0,len(list)):
        if target == list[i]:
            return i
            

numbers = [ 1, 5, 6, 9, 2, 3, 5 ] 
result = linear_search(numbers,3)
print(result)

