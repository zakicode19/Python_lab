import datetime
import random


class HumanJD():
    """
    A class to represent a specific human named John Doe.
  """
    firstName = "John"
    lastName = "Doe"


class Human():
    """
    A class to represent a specific human
  ...

    Attributes
    ----------
    firstname : str
        first name of the person
    lastname : str
        family name of the person
    age : int
        age of the person

    Methods
    -------
    bornIn():
        return the year of birth of the human.
  """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old. He is born in {self.bornIn()}'

    def bornIn(self):
        """
    return the year of birth
    """
        return datetime.datetime.now().year - self.age


class Student:
    """
      Student class
      Provide information about name, age, section
    """

    def __init__(self, name, age, section):

        # initialization
        # Self is the keyword we use to refers to the class object
        self.name = name
        self.age = age
        self.section = section

        # Good case need to have if, elif, else
        if self.section == 'DS':
            self.strength = "Machine Learning"
        elif self.section == 'DE':
            self.strength = "Coding"
        else:
            self.strength = "Something else"

    def __str__(self):
        """
        Print function, allows to access every attribute
        """
        return f"Name: {self.name}\nAge: {self.age}\nSection: {self.section}\nStrength: {self.strength}"

    def get_str(self):
        """
        Print function, allows to access every attribute
        """
        return f"Name: {self.name}\nAge: {self.age}\nSection: {self.section}\nStrength: {self.strength}"

    def get_age(self):
        """
        return the age of a student
        """
        return self.age

    def is_ready(self, exam_name=''):
        """
        return true if the student is ready for the given exam
            false if not
        """
        if self.section == "DE" and exam_name == 'math':
            return False
        elif self.section == "DS" and exam_name == 'math':
            return True
        else:
            return random.choice([True, False])
