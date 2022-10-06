import fib

'''print("Inside test_fib.py:", __name__)

print(fib.fib(20))'''

x = "x-global"
def toplevel():
    global x
    print(x)
    x = "x-local"
    print(x)
print(x)
toplevel()
print(x)