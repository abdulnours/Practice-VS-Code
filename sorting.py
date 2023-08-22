def pls_sort_this(list):

    '''
    for i in range(0,len(list)-1):
    maximum = max(list)
    minimum = min(list)
    '''   

    count=1
    
    while count:
        count = 0
        for i in range(0, len(list)-1):
            if list[i] > list[i+1]:
                count=1
                a = list[i]
                # print(a)
                b = list[i+1]
                # print(b)
                list[i] = b
                # print(list)
                list[i+1] = a
                # print(list)
        print(count)
        print(list)
    return list

unsorted_list = [ 69,1,2,3,4,5,6,7,8,9 ]

my_sorted_list = pls_sort_this(unsorted_list)
# print(my_sorted_list)


