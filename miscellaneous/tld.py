svo_list=[['a','b','c'],['a','b','c'],['a','b','d']]
result=[]
for svo_i in svo_list:
    flag=True
    for svo in result:
        if svo[1]==svo_i[1] and svo[0]==svo_i[0] and svo[2]==svo_i[2]:
            flag=False
            break
    if flag:
        result.append(svo_i)

print(result)