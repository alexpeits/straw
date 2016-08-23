=====
Straw
=====

-----------------------------
Unix-like pipelines in Python
-----------------------------


*Usage:*

Declare some data pipelines:

.. code-block:: python

    from straw import Pipe


    class Cat(Pipe):
        def run(self):
            return ' '.join(self.args)


    class Upper(Pipe):
        def run(self, pipe_in):
            return pipe_in.upper()


    class FirstWord(Pipe):
        def run(self, pipe_in):
            return pipe_in.split()[0]


    class Join(Pipe):
        def run(self, pipe_in):
            delimiter = self.kwargs.get('delimiter', '-')
            return delimiter.join(pipe_in.split())


Use them:

.. code-block:: python

    >>> print 'upper' | Upper()
    'UPPER'
    >>> print Cat('upper') | Upper()
    'UPPER'
    >>> print Cat('one two three') | FirstWord()
    'one'
    >>> print Cat('one two three') | Join()
    'one-two-three'
    >>> print Cat('one two three') | Join(delimiter='*')
    'one*two*three'


Or, if you prefer writing plain functions:

.. code-block:: python

    from straw import pipe


    @pipe
    def cat(pipe_in, *args):
        return ' '.join(args)


    @pipe
    def upper(pipe_in):
        return pipe_in.upper()


    @pipe
    def first_word(pipe_in):
        return pipe_in.split()[0]


    @pipe
    def join(pipe_in, delimiter='-'):
        return delimiter.join(pipe_in.split())


Usage:

.. code-block:: python

    >>> print 'upper' | upper()
    'UPPER'
    >>> print cat('upper') | upper()
    'UPPER'
    >>> print cat('one two three') | firstWord()
    'one'
    >>> print cat('one two three') | join()
    'one-two-three'
    >>> print cat('now with functions') | upper() | join(delimiter='_')
    'NOW_WITH_FUNCTIONS'
