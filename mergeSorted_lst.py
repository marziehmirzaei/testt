lst_1=[1,2,4,88]
lst_2=[1,3,4,95,120]
lst_3=[]
i=0
j=0
for k in range(len(lst_1)+len(lst_2)):
    if (lst_1[i]<= (lst_2[j])):      
        lst_3.append(lst_1[i])        
        if (i>=len(lst_1)-1):
            if j<=(len(lst_2)-1):
                lst_3.append(lst_2[j])
                if j<len(lst_2)-1:
                    j+=1
                else:
                    break
            else:
                    break
        else:
            i+=1    
    else:
        if j<len(lst_2)-1:
            lst_3.append(lst_2[j])
            j+=1
        else:
            break
print(lst_3)
i = j = 0
for index in range(len(lst_1)):
    if lst_1[i] == lst_2[j]:
        lst_3.append([lst_1[i],lst_2[j]])
        i = i + 1
        j = j + 1
    elif lst_1[i] > lst_2[j]:
        lst_3.append(lst_2[j])
        j= j + 1
    elif lst_2[j] > lst_1[i]:
        lst_3.append(lst_1[i])
        i = i + 1
    
        