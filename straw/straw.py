class Pipe(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __or__(self, nxt):
        if not hasattr(self, 'out'):
            self._out = self.run()
        nxt._out = nxt.run(self._out)
        return nxt

    def __ror__(self, other):
        self._out = self.run(other)
        return self

    def run(self, pipe_in=None):
        raise NotImplementedError()

    def __repr__(self):
        if not hasattr(self, 'out'):
            self._out = self.run()
        return self._out

    def __eq__(self, other):
        return self.__repr__() == other
