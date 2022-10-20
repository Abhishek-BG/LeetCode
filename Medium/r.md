 <!-- Integer j
integer arr[2][2] = {(6,0),(1,2)}
arr[0][0] = arr[0][1]& arr[1][0]
arr[0][1]=(arr[1][1]+4)^arr[0][1]
if(1+3)<(7-arr[1][1])
    arr[0][1]=(arr[0][1]+4)+arr[0][1]
else
  arr[0][1]=(8+11)&arr[1][1]
end if
print(arr[1][1]+arr[0][1]+arr[1][0]) -->

<!-- 
Integer p,q,r
set p=2,q=5,r=9
if(q+9)<p|| (q&p)<p
 r=(p&q)+q
 else
 p=r+p
end if 
r= q+p
print p+q+r -->

<!-- Integer a,b,c
set a=7,b=56,c=12
if((4+5)<(6+b)||1)
   b=c&a
   a=c*(a+b)<(4&a)
   c=a&b
end if
print(a+b+C) -->

<!-- Integer p,q,r
set p=9, q=8,r=6,s=8
for(each r from 0 to 5)
s=p&r
q =1+r+s
    if(6>p || (4+8)<(8+q-s))
        q=2+r+s
    end if
end for 
print p+q*s -->
<!-- 
Integer p,q,r,
set p=1,q=4,r=10
if((2+8)(6-p))
p=(5+7)+r
q=r+p
q=(r+q)+p
end if
print p+q+r -->

<!-- 
Integer funn(integer a, integer ,integer c)
if((b+a)>(a-b))
a=a+c
b=(10+10)+c
c=a^b
end if
return a+b+c
#2,7,7 -->

<!--  -->
<!-- 
Integer funn(int a,int b)
if(a+b <10)
return 1+funn(a+1,b+1)
else
return 2
end if
#7,2 -->
<!-- 
4,9,2
Integer fun(int a,int b,int c)
if(a>b && a>0 || c < a)
return a+b+fun(b-1,a-1,a)
end if 
return a+b+c -->


<!-- integer p,q,r
set p=7,q=3,r=8
for(each r from 3to 7)
    p=(5+11)^q
    if((q+r)>(r-q))
        q=(7+9)+r
        p=(p+q)+r
    else
        q=(11^11)+q
        jump out of loop
    end if 
end for
print p+q -->






