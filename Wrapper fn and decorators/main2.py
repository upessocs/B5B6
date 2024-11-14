# write a function to evaluate expression "res = i * 10" for all values between 0 to n, function is taking one input argument "n"
import time

n = 10000000

def testfn(n):
    for i in range(0,n):
        res = i * 10

def wrapper(func,*args,**kwargs):
    def wrapped(*args,**kwargs):
        start_time = time.time() * 1000# recording timein milli sec
        #execute function
        func(*args,**kwargs)

        end_time = time.time() * 1000
        diff = end_time - start_time

        print(f"execution time for n = {n} is \n {diff} milli sec")

    # wrapped(*args,**kwargs)
    return(wrapped)

newWarppedFn = wrapper(testfn,n)

newWarppedFn(n)