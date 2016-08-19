class Pipe(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __or__(self, nxt):
        if not hasattr(self, 'out'):
            self.out = self.run()
        nxt.out = nxt.run(self.out)
        return nxt

    def __ror__(self, other):
        self.out = self.run(other)
        return self

    def __repr__(self):
        return self.out

    def __eq__(self, other):
        return self.__repr__() == other

    def run(self, pipe_in=None):
        raise NotImplementedError()
