def dec_fun(fn):
    def inner_fn(n1,n2):
        if n1<n2:
            (n1,n2)=(n2,n1)
            return fn(n1,n2)
    return inner_fn


@dec_fun
def sub(n1,n2):
    return n1-n2

def div(n1,n2):
    return n1/n2

print(sub(10,20))

print(div(10,20))