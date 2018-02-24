def funx():
    x=5
    def funy():
        nonlocal x
        x *=x
        return x
    return funy
print(funx()())
