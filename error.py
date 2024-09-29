def div_internal2(a,b):
    return a/b

def div_internal(a,b):
    return a/b

# Exception handling
def div(a,b):
    try:
        # open a file
        return div_internal(a,b)
    except:
        print('Invalid input')
    finally:
        # clean up
        # file.close()
        print('finally')

res = div(10,0)
print(res)



