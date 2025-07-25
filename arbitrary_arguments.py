def label(*args, **kwargs):
    for arg in args:
        print(arg, end = " ")
    print()
    for key, value in kwargs.items():
        print(value, end="\n")

label("Dr.", "Henry", "Mark",
      street= "123",
      apt= "detroit",
      zip ='000')











# def address(**kwargs):
#     # print(type(kwargs))
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")

# address(street='123 nothing', apt='44456', city= 'nope', state= "ewew", zip='w3455')




# def disp(*args):
#     for arg in args:
#         print(arg, end=' ')

# disp("Mark", "Henry")




# def sum(*args):
#     total = 0 
#     for arg in args:
#         total += arg
#     return total

# print(sum(1,2,3,5))