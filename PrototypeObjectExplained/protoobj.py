class CustomObj:
    def __init__(self, idx, title):
        self.idx = idx
        self.title = title
        self.sameattr = 'sameattr'

    def __repr__(self):
        suprep = super().__repr__()
        return '<{}{}>'.format(self.idx, suprep)

    def __len__(self):
        """
        called by: len()
        """
        return 12345

    def __eq__(self, other):
        """
        called by: ==
        """
        return self.sameattr == other.sameattr



if __name__ == '__main__':
    pass

    obj1 = CustomObj(idx=1, title='one')
    obj2 = CustomObj(idx=2, title='two')

    objs = [obj1, obj2]

    print(':: help on object:')
    print(help(object))

    print('\n:: print obj')
    print(obj1)

    print('\n:: print objs')
    print(objs)

    print('\n:: len()')
    print(len(obj1))

    print('\n:: ==')
    print(obj1 == obj2)
