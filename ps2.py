###### this is the second .py file ###########
#rotate 
def reverse(lt,a):
    copy = list(lt)
    for i in range(len(lt)):
        if a<0:
            lt[i+a] = copy[i]
        else:
            lt[i] = copy[i-a]


#grouping
g1="abcdefghi"
g2="jklmnopqr"
g3="stuvwxyz_"

m1 =[]
m2 =[]
m3 =[]
index1=[]
index2=[]
index3=[]


k1,k2,k3 = list(map(int,input().split()))

#strings
msg = input()
msgl = list(msg)


#compare
for i in range(0,len(msg)):
    if msgl[i] in g1:
        m1.append(msgl[i])
        index1.append(i)
       
    elif msgl[i] in g2:
        m2.append(msgl[i])
        index2.append(i)
    elif msgl[i] in g3:
        m3.append(msgl[i])
        index3.append(i)



#rotate c1,c2,c3
reverse(m1,k1)
reverse(m2,k2)
reverse(m3,k3)



#get decrypted 
a1=0
a2=0
a3=0
for i in range(0,len(msg)+1):
    if i in index1:
        msgl[i]=m1[a1]
        a1+=1
    elif i in index2:
        msgl[i]=m2[a2]
        a2+=1
    elif i in index3:
        msgl[i]=m3[a3]
        a3+=1   

for i in msgl[:]:
    print (i, end ='')




####### write your code here ##########
