#   * * * * *
for i in range(5):
    print("*",end='')
print()

#many "str method"
for i in range(5):#row ranges
    print("* "*10)#multiples
print("*"*5)#multiples
print()

#while_loop 
row = 1
while row<=5:
    for col in range(5):
        print(row,end =' ')
    print()
    row+=1
print()
#for_loop 
for row in range(1,6):#------->its outer for loop rows cntrl
    for col in range(1,6):#---->its inner for loop col cntrl (responsibility end="")
        print(row,end =' ')
    print()
print()
#type3
for row in range(1,6):#------->its outer for loop rows cntrl
    for col in range(1,6):#---->its inner for loop col cntrl (responsibility end="")
        print(row*col,end =' ')
    print()
print()     

#reversed
for row in range(5,0,-1):
    for col in range(5,0,-1):
        print(row,end=' ')
    print()   
print() 
#loop repeated mistake dont try this method***********************
#  1    2   3   4   
for col in range(1,5):
    print(col,end=' ')
print()
#  1    2   3
for col in range(1,4):
    print(col,end=' ')
print()
#  1    2 
for col in range(1,3):
    print(col,end=' ')
print()
#  1
for col in range(1,2):
    print(col,end=' ')
print()
print()

#loop repeated mistake dont try this method Rightway------------>
for row in range(6,1,-1):
    for col in range(1,row):
        print(col,end=' ')
    print()
print()
print()
#type----2
row=7        #for row in range(6,1,-1)
while row>=0:#unwanted line
    for col in range(1,row):
        print(row,end=' ')
    print()
    row-=1 #unwantedline


row =5
no=1
for row in range(5,0,-1):
    for  col in range(row):
        print(no,end= " ")
    print()
    no+=1
    #slice
word = 'nellai'
count= len(word)
for row in range(count,0,-1):
    for col in range(row):
        print(word[col],end = '')
    print()



for row in range(1,0,6):
    for col in range(row):
        print('*',end=' ')
    print()


for row in range(3,-1,-1):
    for col in range(row):
        print('_',end=' ')
    print("*",end=' ')
    print()

for row in range(3,-1,-1):
    for col in range(row):
        print(' ',end=' ')
    for col in range(4-row):
         print("*",end=' ')
    print()
