def pls_sort_this(list):

    '''
    for i in range(0,len(list)-1):
    maximum = max(list)
    minimum = min(list)
    '''   
    
    for n in range(0,len(list)-1):
        for i in range(0,len(list)-1):
            if list[i] > list[i+1]:
                a = list[i]
                #print(a)
                b = list[i+1]
                #print(b)
                list[i] = b
                #print(list)
                list[i+1] = a
        # print(count)
        print(list)

    return list

unsorted_list = [10,9,8,7,6,5,4,3,2,1]

my_sorted_list = pls_sort_this(unsorted_list)
# print(my_sorted_list)


