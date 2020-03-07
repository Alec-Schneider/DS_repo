def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls +=1
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@counter
def write(x):
    if writers.calls > 1:
        write.calls = 0
        print('write calls', write.calls)
    print('write calls', write.calls)
    return x*x

@counter
def writers(y):
    print(y)
    write(y)
    print('writers calls', writers.calls)
    return y


writers(3)
writers(10)
writers(2)