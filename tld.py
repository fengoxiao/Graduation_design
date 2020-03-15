N,K=[int(x) for x in input().split(' ')]
result=str(K)
for x in range(K-1,K-3,-1):
    if x>0:
        result = '%d %s' % (x, result)
    else:
        break
if K-3>0:
    result = '%d %s %s' % (1,'...',result)
'''
if K-1>0:
    result = '%d %s'%(K - 1,result)
    if K - 2> 0:
        result = '%d %s'%(K - 2,result)
        if K-3>0:
            result = '%d %s %s' % (1,'...',result)
'''
if K<N:
    result = '%s %d'%(result,K + 1)
    if K + 1<N:
        result = '%s %d'%(result,K + 2)
        if K+2<N:
            result = '%s %s %d' % (result,'...', N)
print(result)
