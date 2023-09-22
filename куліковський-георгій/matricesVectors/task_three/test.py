def test_decorator(metod):
    def wrapper(par1, par2):
        if par1 == par2:
            return metod(par1, par2)
        else:
            print("error")
            return 0
    return wrapper

@test_decorator
def new_method(num1, num2):
    print(num1+num2)
    return num1+num2

new_method(10,5)