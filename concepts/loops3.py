# Nested loops

'''
 1 * 1  = 1
 1 * 2  = 2

 5 * 1 = 5
 5 * 2 = 10
'''


def printMulTbl():
    for i in range(1,6): # 5  5 * 5 = 25
        for j in range(1,11000000): # 5
            if(j==11): 
                break
            res = str(i) + ' * ' + str(j) + ' = '+ str(i*j)
            print(res)
        print()
    

printMulTbl()