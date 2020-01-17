import ast
import dis


def fixer(func):
    def wrapper():
        co = func.__code__
        return func()
    return wrapper



@fixer
def hello_world():
    print('hello world!')



hello_world()
