def combined_list(list_1, list_2):
    result_list = list ()

    for i in list_1:
        if i in list_2: 

            result_list += [i] 

            print (result_list)



combined_list ([1,2,3,4], [3,4,5,6])
