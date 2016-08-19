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
