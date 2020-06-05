dic_str={'s':2,'ss':3}
sort_list=sorted(dic_str.items(), key=lambda item: item[1])
for x in sort_list:
    key, value = x
    print(key)
    print(value)