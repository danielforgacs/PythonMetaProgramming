import ast
import dis


def fixer(func):
    def wrapper():
        co = func.__code__
        # print(dir(co))
        # print(co.co_code)
        # print(co.co_consts)

        # co.co_consts = (None, 'LH')
        # dis.dis(co)
        # func.__code__.co_contsts = ('1', '2')
        # dis.dis(co.co_code)
        # ast.NodeVisitor().visit(func)
        # ast.NodeVisitor().visit(co)
        return func()
    return wrapper



@fixer
def hello_world():
    print('hello world!')



hello_world()

