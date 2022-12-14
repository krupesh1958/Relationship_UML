# Association in python 

class Student:

    def __init__ (self, pay, amount):
        self.pay = pay
        self.amount = amount


class Collage:

    def __init__ (self, amount):
        self.amount = amount

    def value (self, valu):
        return valu - self.amount

obj = Collage(15)
print(obj.value(Student(10,50).amount))

# Aggregation in python

class Student:

    def __init__ (self,pay):
        self.pay = pay

    def value (self):
        return self.pay

class Collage:

    def __init__ (self, pay, amount):
        self.pay = pay
        self.amount = amount

    def value (self):
        return self.amount + self.pay.value()

obj = Collage(Student(10),50)
print(obj.value())

# Composition in python

class Student:
    
    def __init__ (self,pay,amount):
        self.pay = pay
        self.amount = amount

    def value (self):
        return self.pay - self.amount


class Collage:

    def __init__ (self, pay, amount):
        self.amount = Student(pay,amount).value()
    
    def final_value (self):
        return self.amount

obj = Collage(100,50)
print(obj.final_value())
    
# get all versions perticular library

import json
import sys
from urllib import request    
from pkg_resources import parse_version    
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def versions(pkg_name):
    url = f'https://pypi.python.org/pypi/{pkg_name}/json'
    releases = json.loads(request.urlopen(url).read())['releases']
    return sorted(releases, key=parse_version, reverse=True)    


if __name__ == '__main__':
    print(*versions(sys.argv[1]), sep='\n')

# Terminal :: python <file_name> <library_name>
