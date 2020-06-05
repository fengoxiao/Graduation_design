class Solution:
    def reorganizeString(self, S: str) -> str:
        S_long=len(S)
        dic_str={}
        for s in S:
            if s not in dic_str:
                dic_str[s]=1
            else:
                dic_str[s]+=1
        result=['']*S_long
        sort_list=sorted(dic_str.items(), key=lambda item: item[1],reverse = True)
        star=0
        if sort_list[0][1]  S_long:
            return ''
        for x in sort_list:
            key,value=x
            while result[star]:
                star+=1
            for i in range(value):
                result[star+i*2]=key
        return ''.join(result)