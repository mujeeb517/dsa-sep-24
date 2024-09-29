# Even:  A number that's fully divisble (reminder) by 2
# Prime Number: 2, 3, 5, 7, 11
# Billions 25 12am
# Ex: 2,4,6,8,10..
# Ex: 1,3,5,7
# Edge case
def printNumbers(n):
    for i in range(1, n+1):
        print(i)

# def printEven(n):
#     for i in range(1,n+1):
#         if i%2 == 0:
#             print(i)


# signature
# def printEven(n):
#     for i in range(1,n+1):
#         if(i%2!=0): 
#            continue
#         else:
#             print(i)


def printEven(n):
    for i in range(1,1000000000):
        if(i%2==0):
            print(i)
        
        if(i==n):
            break


printEven(100)