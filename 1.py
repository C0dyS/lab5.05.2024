import time
import json
import os


#другие классы не нашел, нашел этот

class Calculator:

    @classmethod
    def add(cls,x,y):
        return x + y
    @classmethod
    def subtract(cls,x,y):
        return x - y
    @classmethod
    def multiply(cls,x,y):
        return x * y
    @classmethod
    def divide(cls,x,y):
        if y == 0:
            raise ValueError("Division by zero is not allowed")
        else:
            return x / y


    @staticmethod
    def file_dump(result):
        filename = 'calc_results.json'
        if os.path.isfile(filename):
            with open(filename, 'r') as file:
                data = json.load(file)
        else:
            data = []

        data.append(result)

        with open(filename, 'w') as file:
            json.dump(data, file)

    @classmethod
    def __call__(cls,operation_type,a,b):
        if operation_type == 'add':
            result = cls.add(a,b)
            cls.file_dump(result)
            return result
        elif operation_type == 'subtract':
            result = cls.subtract(a,b)
            cls.file_dump(result)
            return result
        elif operation_type == 'multiply':
            result = cls.multiply(a,b)
            cls.file_dump(result)
            return result
        elif operation_type == 'divide':
            result = cls.divide(a,b)
            cls.file_dump(result)
            return result
        else:
            raise ValueError('Wrong operation type')


