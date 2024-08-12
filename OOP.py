class StudentInfo:
    """
    # INSTANCE VARIABLES
        - ALWAYS STORES DATA WITHIN DIFFERENT METHODS, USUALLY WITHIN THE CONSTRUCTOR, THE __init__ METHOD

    __init__ method This is used to create multiple instances, calling the class later on and passing down the
    arguments after self. The self statement every time creates a new instance, lets say for eg, we pass down
    info ('Pipal Deka', 621, 7896607723, "pd@gmail.com") as data, syntax being -

    stud_1 = StudentInfo('Pipal Deka', 621, 7896607723, "pd@gmail.com")
      |
    creates instance stud_1, passes down the info through self.

    this self is to be only used inside the class,

    # CLASS VARIABLES
        - ITS SAME FOR THE WHOLE CLASS.
        - ITS DEFINED ONLY ONCE, FOR THE WHOLE CLASS.

    #CLASSMETHODS AND STATIC-METHODS
    """

    class_name = "2024-B.Tech"    # Class Variable.

    def __init__(self, first, last, admin_no, phone, email):
        self.First = first
        self.Last = last
        self.admin_no = admin_no
        self.phone = phone
        self.email = email

    def display_name(self):
        return '{}{}'.format(self.First, self.Last)

    def display_info(self):
        return 'Name: {}{} \n'.format(self.First, self.Last), f'Class: {self.class_name}\n', f'Phone NO: {self.phone}\n'


'''creating an instances into the class - stud_1 is an attribute of the class now. They are class variables created 
via self, they can be used by other methods when needed without being defined again.
'''

stud_1 = StudentInfo('Pipal ', 'Deka', 621, 7896602733, "pipal21.deka@gmail.com")

# ways to call a method
print(stud_1.display_name())  # calling directly from the instance
print(StudentInfo.display_name(stud_1))  # calling the method from the class with passing the instance as an argument

"""
We can access CLASS VARIABLES via different methods. 
We can use the CLASS, aswell as CLASS INSTANCES to call a CLASS VARIABLE outside the class. 

    - StudentInfo.class_name --- accessing via CLASS 
    - stud_1.class_name --- accessing via CLASS INSTANCES
    
We can also change the CLASS VARIABLE for each instances, as shown below. 
        # print(stud_1.class_name)
        # stud_1.class_name = "2024-B.tech CSE"
        # print(stud_1.class_name)
        Output: 
            2024-B.Tech
            2024-B.tech CSE

"""
print(StudentInfo.class_name)
print(stud_1.class_name)
stud_1.class_name = "2024-B.tech CSE"
print(stud_1.class_name)
# print(stud_1.__dict__)

print(stud_1.display_info())


