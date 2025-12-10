from functools import reduce

#testing lambda functions
mult = lambda x,y,z=1:x*y*z
print(mult(5,6))

#testing map function
#applies function given to each value in iterable
list_of_nums = [1,2,3,4,5]
squared_list = list(map(lambda x: x*x, list_of_nums))
print(squared_list)

#map func with multiple iterables
cubed_list = list(map(lambda x,y: x*y,list_of_nums,squared_list))
print(cubed_list)

#testing reduce functionality
combined_ans = reduce(lambda x,y:str(x) + ' ' + str(y),list_of_nums,'0')
print(combined_ans)