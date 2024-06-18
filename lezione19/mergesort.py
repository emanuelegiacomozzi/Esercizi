def mergeSort(input_list:list):

    if len(input_list) == 1:

        return input_list
    
    mid_point:int = len(input_list) // 2

    mergeSort(input_list=input_list[0:mid_point]) #prendo la prima metà di input_list
    mergeSort(input_list=input_list[mid_point:])  #prendo la seconda metà

def merge(list_1:list[int], list_2:list[int]):

    i, j = 0,0,0

    result: list[int] = [None for _ in range(len(list_1+list_2))]
    
    for k in range (len(result)):

        if list_1[1] > list_2[j]:

            result[k] = list_2[j]

            j += 1
        
        else:

            result[k] = list_1[i]

            i += 1
    
    return result



if __name__ == "__main__":

    input_list: list[int] = [0,1,2,3,4,5,6,7]


    mergeSort(input_list=input_list)

