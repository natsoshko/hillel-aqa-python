print("hello world")

my_int = 10
my_float = 20.3
my_string = "hello world"
my_list = [1, 2, 5.9, True, [1,0], 5]
my_tuple = (1, 2, "hello", None)
my_set = {1, 2, False}
my_dict = {"key": "value", "key2": {"sub_key": "sub_value"}}
my_bool = True
my_none = None

my_variable = None
print(my_variable)
# ctrl+/
'''
print('test multi rows')
'''



my_variable = my_int + my_float
print(my_variable)

# snake_case - для найменування змінних
# CamelCase - для найменування класів
# UPPER_SNAKE - для найменування констант

#ctrl + Alt + L
sum_ = 5 + 10
diff = 15 - 5
mult = 3*15
div = 15/3

print(sum_)
print(diff)
print(mult)
print(div)

# = - оператор присвоєння
# == - оператор порівняння, повертає True, False

if sum_ == 15:
    print("sum_ is equal to 15")

my_name = "Alex"
print("Hello", my_name, sep="_")
print("Hello", my_name, end="")
print("Hello", my_name)

print("Hello, my name is", my_name, ". My age is", 10+20)

first_int = 10
second_int = 20
print(id(first_int), id(second_int))
second_int = first_int
print(id(first_int), id(second_int))

my_name1, my_age1 = ("Alex", 10)
print(my_name1, my_age1)
my_name2, my_age2 = "Max", 20
print(my_name2, my_age2)
copy_name, copy_age = my_name2, my_age2
print(copy_name, copy_age)



