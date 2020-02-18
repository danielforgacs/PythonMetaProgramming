class CustomObj:
    def __init__(self, idx, title):
        print('::[__init__]')
        self.idx = idx
        self.title = title
        self.sameattr = 'sameattr'

    def __repr__(self):
        print('::[__repr__]')
        suprep = super().__repr__()
        return '<{}{}>'.format(self.idx, suprep)

    def __len__(self):
        """
        called by: len()
        """
        print('::[__len__]')
        return 12345

    def __eq__(self, other):
        """
        called by: "=="
        """
        print('::[__eq__]')
        return self.sameattr == other.sameattr

    def __lt__(self, other):
        """
        less than, called by: "<"
        """
        print('::[__lt__]')
        return self.idx < other.idx


    def __new__(cls, *args, **kwargs):
        """
        called before __init__. Can be used to create
        singletons.
        """
        print('::[__new__]')
        instance = super().__new__(cls)
        return instance


    def __getattribute__(self, attr):
        """
        1st call on attribute access.
        """
        print('::[__getattribute__]')
        value = super().__getattribute__(attr)
        return value


    def __getattr__(self, attr):
        """
        2nd call on attribute access.
        called when attr is missing.
        """
        print('::[__getattr__]')
        value = 'generated value'
        return value




if __name__ == '__main__':
    pass

    print(':: help on object:')
    print(help(object))
    print(':: --------------:')

    obj1 = CustomObj(idx=1, title='one')
    obj2 = CustomObj(idx=2, title='two')

    objs = [obj1, obj2]

    print(obj1)
    print(objs)
    print(len(obj1))
    print(obj1 == obj2)
    print(obj1 < obj2)
    print(getattr(obj1, 'idx'))
    print(obj1.title)
    print(obj1.missing)
