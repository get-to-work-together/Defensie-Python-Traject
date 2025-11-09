
def repeat_decorator(fn):
    def inner():
        for _ in range(5):
            fn()
    return inner

def trace(fn):
    def inner(*args, **kwargs):
        print(f'Entering function {fn.__name__}')
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        fn(*args, **kwargs)
        print('Done')
    return inner


@trace
def print_iets(s, n=1):
    print(f's => {s}', n)


print_iets('abracadabra', n=3)