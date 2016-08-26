"""

straw
~~~~~

Simple, UNIX-like pipelining for Python

This was developed strictly for exploring the Python interpreter,
and should definitely not be used in production.

"""


from functools import wraps, partial


class Pipe(object):
    """Enables user-defined functions to be piped together using the | symbol.

    This can be used through the "pipe" decorator, but also by inheriting.
    In the latter case, only the "run" method has to be overriden. Any args and
    kwargs are stored in self.args and self.kwargs, and the only argument in
    "run" (except self) is the pipe input:

    >>> class Join(Pipe):
    ...     def run(self, pipe_in):
    ...         delimiter = self.kwargs.get('delimiter', '-')
    ...         return delimiter.join(pipe_in.split())
    ...
    >>> 'one two three' | Join()
    one-two-three
    >>> 'one two three' | Join(delimiter='*')
    one*two*three

    """

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __or__(self, nxt):
        if not hasattr(self, '_out'):
            self._out = self.run()
        nxt._out = nxt.run(self._out)
        return nxt

    def __ror__(self, other):
        self._out = self.run(other)
        return self

    def run(self, pipe_in=None):
        raise NotImplementedError()

    def __repr__(self):
        if not hasattr(self, '_out'):
            self._out = self.run()
        return self._out

    def __eq__(self, other):
        return self.__repr__() == other


def pipe(func):
    """Decorator that turns a function into a Pipe object.

    The decorated functions MUST be declared with "pipe_in" as the
    first positional argument (the name is not mandatory). Then, in
    the pipeline, this argument is ommited:

    >>> @pipe
    ... def join(pipe_in, delimiter='-'):
    ...     return delimiter.join(pipe_in.split())
    ...
    >>> 'one two three' | join()
    one-two-three
    >>> 'one two three' | join('*')
    one*two*three
    >>> 'one two three' | join(delimiter='$')
    one$two$three

    """

    @wraps(func)
    def decorated(*args, **kwargs):
        _pipe = Pipe(*args, **kwargs)
        def run(self, pipe_in=None):
            return func(pipe_in, *self.args, **self.kwargs)
        _pipe.run = partial(run, _pipe)
        return _pipe

    return decorated
