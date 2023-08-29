def find_maxima(t_list):
    """Find local maxima of x.

    Input arguments:
    x -- 1D list of real numbers

    Output:
    idx -- list of indices of the local maxima in x
    """
    maxima=[]
    for i in range(len(t_list)):
        if (i == 0):
            if ((t_list[i] >= t_list[i+1])):
                maxima.append(i)

        elif (i == (len(t_list)-1)):
            if ((t_list[i] >= t_list[i-1])):
                maxima.append(i)
        
        elif (i > 0) & (i < len(t_list)-1):
            if (((t_list[i] > t_list[i-1]) & (t_list[i] >= t_list[i+1])) or ((t_list[i] >= t_list[i-1]) & (t_list[i] > t_list[i+1]))):
                maxima.append(i)

    return maxima

#t_list=[1,3,-2,0,2,1]
#print(find_maxima(t_list))

# t_maxima=[1,4]

# maxima=[]
# for i in range(len(t_list)):

#     if (i > 0) & (i < len(t_list)-1):
#         if ((t_list[i] > t_list[i-1]) & (t_list[i] > t_list[i+1])):
#             maxima.append(i)
#     #print(maxima)

# print(maxima)