import os
import random

import tabula
import requests
import pandas as pd


def say_hello():
    """
  print "hello world""
  :return: None
  """
    print('Hello World!')


def get_first_name(name: str):
    """
    This function gets the first name and prints it
  """
    # Different ways to print
    print("First Name: ", name)
    print("First name: %s" % name)
    print(f'First name: {name}')


# Function with default value
def get_first_name2(name: str = 'Ana'):
    """
  print 3 time the name
  :param name: a string
  :return: None
  """
    print("First Name: ", name)
    print("First name: %s" % name)
    print(f'First name: {name}')


def download(url: str):
    """
  download a file from an URL
  :param url: the url of the needed file
  :return: None
  """
    req = requests.get(url)
    url_content = req.content
    csv_file = open('iris.csv', 'wb')
    csv_file.write(url_content)
    csv_file.close()


def get_data_url(url: str):
    """
  download a file from an URL
  :param url: the url of the needed file
  :return: a pandas file
  """
    res = pd.read_csv(url, header=None)
    return res


# Count the number of words in a sentence
def count_words(sentence: str) -> int:
    """
  Count the number of word (define base on the space) in string
  :param sentence: a string
  :return: the count as integer
  """
    counter = 0
    if type(sentence) == type(str):
        words = sentence.split()  # default split by space

        for i in words:
            counter += 1
    else:
        raise Exception

    return counter


# Count the number of words in a sentence whose length is greater than k
def count_words_k(sentence: str, k: int) -> int:
    """
  This function returns the number of words in a sentence whose length is
  greater than a given parameter 'k'
  """
    # declare the return variable and initialize it to 0
    counter = 0

    # Check the type of the param 'sentence' is of type 'string'
    if type(sentence) == str:
        words = sentence.split()  # default split by space

        # Iterate throw the list of words
        for word in words:
            # Check the length of each word
            if len(word) > k:  # if the length is greater than 'k', count 1
                counter += 1

    # if 'sentence' is not a string raise a ValueError Exception
    else:
        raise ValueError

    # return the final counter of words whose length is greater than k
    return counter


# Rewrite function with try except clause
def get_data_url(url: str):
    """
  get data from an url using try except
  :param url:  the url of the data as CSV
  :return: a pandas dataframe
  """
    res = None
    flag = False
    try:
        res = pd.read_csv(url, header=None)
    except Exception as e:
        flag = True
        print(e)

    if flag:  # Check if 'res' has not value None
        raise Exception  # Block the code
    else:
        return res


# renaming file function
def name_file_rename(path, sep):
    """
  The function verify if file exists, rename the file, substitutes the empty spaces by the defined separator and replace the file
  path = old file path
  sep = define the separator
    """
    # verify if file exists
    assert os.path.exists(path), "Path does not exist."

    # split path and filename
    mydir, f = os.path.split(path)

    # replace empty spaces with sep
    new_name = f.replace(' ', sep)

    # join path and new file name
    new_path = os.path.join(mydir, new_name)

    # replace file
    os.rename(path, new_path)

    # return the new_path
    return new_path


# function to convert pdf in cvs
def pdf2csv(path):
    """
  convert pdf to csv
  """
    # rename is the file getting renamed, pre is the part of file name before extension and ext is current extension
    pre, ext = os.path.splitext(path)
    output = pre + '.csv'
    print(output)
    tabula.convert_into(path, output, output_format="csv", pages='all')
    return output


# count the number of lines
def count_lines(filename):
    """
  return the number of lines in a csv file
  """
    try:
        with open(filename) as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print("No such file, please check the file path name.")
    else:
        return len(lines)


def student_is_ready(student, exam_name=''):
    """
    input: a student and tha exam_name
    return true if the student is ready for the given exam
        false if not
    """
    if student.section == "DE" and exam_name == 'math':
        return False
    elif student.section == "DS" and exam_name == 'math':
        return True
    else:
        return random.choice([True, False])