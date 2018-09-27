###### this is the first .py file ###########
n=int(input("enter the value of rows n :"))
m=int(input("enter the value of coloumn m:"))
patt = []

# loop to create matrix
for i in range(n):
	t = list(input())
	patt = patt + [t]
print(patt)


for i in range(n):
	for j in range(m):
		#print(i,j,patt[i][j])
	
		if patt[i][j]=='S'and patt[i][j+1]=='S' and patt[i][j-1]=='S': # loop to print a pattern of 9
			if patt[i+1][j]=='S'and patt[i+1][j-1]=='D' and patt[i+1][j+1]=='D':
				if patt[i+2][j-2]=='S' and patt[i+2][j+2]=='S' and patt[i+2][j+1]=='S' and patt[i+2][j-1]=='S'and patt[i+2][j]=='S': 
					if patt[i+3][j]=='S'and patt[i+3][j-1]=='D' and patt[i+3][j+1]=='D':
						if patt[i+4][j]=='S'and patt[i+4][j+1]=='S' and patt[i+4][j-1]=='S':	
							print("9")
		
		elif patt[i][j]=='S' and patt[i][j-1]=='D' and patt[i][j+1]=='D' and i<=n-1 :# loop to print a pattern of 5
			if patt[i+1][j]=='S' and patt[i+1][j+1]=='S' and patt[i+1][j-1]=='S':
				if patt[i+2][j]=='S' and patt[i][j-1]=='D'and patt[i][j+1]=='D': 
						print("5")
		elif patt[i][j]=='S' and patt[i][j-1]=='D' and patt[i][j+1]=='D' and i<=n-1 :# loop to print a pattern of 1
			if patt[i+1][j]=='D'and patt[i+1][j-1]=='D' and patt[i+1][j+1]=='D':
				if patt[i+2][j]=='D'and patt[i+2][j-1]=='D' and patt[i+2][j+1]=='D':
					print("1")
			
			
		
			
####### write your code here ##########
