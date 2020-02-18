class CustomObj:
    def __init__(self, idx, title):
        self.idx = idx
        self.title = title

    def __repr__(self):
        suprep = super().__repr__()
        return '<{}{}>'.format(self.idx, suprep)

    def __len__(self):
        return 12345



if __name__ == '__main__':
    pass

    obj1 = CustomObj(idx=1, title='one')
    obj2 = CustomObj(idx=2, title='two')

    objs = [obj1, obj2]

    print(':: help on object:')
    print(help(object))
    print('\n:: printing obj')
    print(obj1)
    print('\n:: printing obj list')
    print(objs)
    print('\n:: printing obj len')
    print(len(obj1))
