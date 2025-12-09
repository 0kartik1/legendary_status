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

@log_keeper
def adding_func(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(adding_func(10,20,30,40))