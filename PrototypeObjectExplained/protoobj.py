def print_methodinfo(method):
    def wrapper(*args, **kwargs):
        # print('\t[CALL] {}'.format(method.__name__))
        result = method(*args, **kwargs)
        return result
    return wrapper



class CustomType(type):
    pass



class CustomObj(metaclass=CustomType):
    @print_methodinfo
    def __init__(self, idx, title):
        self.idx = idx
        self.title = title
        self.sameattr = 'sameattr'

    @print_methodinfo
    def __repr__(self):
        suprep = super().__repr__()
        return '<{}{}>'.format(self.idx, suprep)

    @print_methodinfo
    def __len__(self):
        """
        called by: len()
        """
        return 12345

    @print_methodinfo
    def __eq__(self, other):
        """
        called by: "=="
        """
        return self.sameattr == other.sameattr

    @print_methodinfo
    def __lt__(self, other):
        """
        less than, called by: "<"
        """
        return self.idx < other.idx


    @print_methodinfo
    def __new__(cls, *args, **kwargs):
        """
        called before __init__. Can be used to create
        singletons.
        """
        instance = super().__new__(cls)
        return instance


    @print_methodinfo
    def __getattribute__(self, attr):
        """
        1st call on attribute access.
        """
        value = super().__getattribute__(attr)
        return value


    @print_methodinfo
    def __getattr__(self, attr):
        """
        2nd call on attribute access.
        called when attr is missing.
        """
        value = 'generated value'
        return value


    @print_methodinfo
    def __contains__(self, value):
        """
        called by: "in"
        """
        return True


    @print_methodinfo
    def __iter__(self):
        self.iterstart = 0
        return self



    @print_methodinfo
    def __next__(self):
        while self.iterstart < 5:
            self.iterstart += 1

            return 'iter: {}'.format(self.iterstart)

        raise StopIteration



    @print_methodinfo
    def __getitem__(self, index):
        return 'a'




DynamicClass = type('DynamicClass', (), {})
DynamicClassWithMeta = CustomType('DynamicClassWithMeta', (), {})






if __name__ == '__main__':
    pass

    print(dir(type))
    print(dir(object))

    instanceX = DynamicClass()
    instanceY = DynamicClassWithMeta()

    obj1 = CustomObj(idx=1, title='one')
    obj2 = CustomObj(idx=2, title='two')

    objs = [obj1, obj2]

    len(obj1)
    obj1 == obj2
    obj1 < obj2
    getattr(obj1, 'idx')
    obj1.title
    obj1.missing
    obj1[7]
    'a' in obj1

    for item in obj1:
        print(item)

    print('obj1: ', obj1)
    print('objs: ', objs)
