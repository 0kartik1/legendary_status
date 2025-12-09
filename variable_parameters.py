def tuple_of_args(*argumnets):
    net_sum = 0
    for args in argumnets:
        net_sum += args
    return net_sum

def keyworded_args(**keyworded_arguments):
    print(keyworded_arguments['id'])
    name = None
    last_name = None
    if 'name' in keyworded_arguments:
        name = keyworded_arguments['name']
    if 'last_name' in keyworded_arguments:
        last_name = keyworded_arguments['last_name']
    if name is not None:
            print(name)
    if last_name is not None:
            print(last_name)
    return

get_sum = tuple_of_args(1,2,3,4,5)
print(get_sum)

keyworded_args(name='baigan',id=1)
keyworded_args(last_name='baigan',id='2')