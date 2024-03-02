"""
used for scalability
used to pass multiple param values
compulsory convention - function(normal, *args, **kwargs)
The two later are optional arguments
"""


def funcarg(*args, **kwargs):  # No argument can be passed after args**
    # print(list(args))   #it is converted to a tuple
    for i in args:
        print(i)

    for key, value in kwargs.items():
        print(f"{key} is a value {value}")


har = ['Harry', 'Marry', 'Rohan', 'Skillf', 'Shivam']
kw = {"Rohan": "Monitor", "Harry": "Fitness Instructor",
      "The Programmer": "Coordinator", "Shivam": "Cook"}
funcarg(*har, **kw)
