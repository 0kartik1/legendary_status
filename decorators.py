def log_keeper(function):
    def arg_logger(*args,**kwargs):
        counter = 1
        for a in args:
            print(f'Argument {counter} : {a}')
            counter += 1
        ans = function(*args,**kwargs)
        print('LOGGING COMPLETE')
        return ans
    return arg_logger

def testing_deco(func):
    def just_a_wrapper(*args,**kwargs):
        func()
    return just_a_wrapper

@log_keeper
def adding_func(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

# decorator stacking


print(adding_func(10,20,30,40))