"""
Create a function to take a two Dimentionals Matrix, Input N is given find 
if N occurs in all of the rows in the matrix 
[[1,2,3,4,5],
 [9,5,4,2,1],
 [5,1,9,0,8],
 [0,3,4,7,8]]
output  = 5

"""
from collections import defaultdict 

M = 4 #rows
N = 5 # col

def findcommon(mat):
    global M, N

    cnt = dict()
    cnt =defaultdict(lambda: 0,cnt)
    i=0 #rows
    j=0 # col
    #itterate through the rows
    while(i < M):
        cnt[mat[i][0]]= cnt[mat[i][0]]+1
        j=1
        while(j< N):
            if(mat[i][j] != mat[i][j-1]):
                cnt[mat[i][j]] = cnt[mat[i][j]]+1

            j=j+1
        i=i+1
    for ele in cnt:
        if(cnt[ele]==M):
            return ele
    return -1


mat =[[1,2,3,4,5],
 [2,4,5,8,10],
 [3,5,7,9,11],
 [1,3,5,7,9],]
result = findcommon(mat)
if(result == -1):
    print("No common Element found")
else:
    print(result)


