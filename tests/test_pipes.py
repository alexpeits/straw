import unittest

from straw.straw import Pipe


class Cat(Pipe):
    def run(self):
        return ' '.join(self.args)


class Upper(Pipe):
    def run(self, pipe_in):
        return pipe_in.upper()


class Join(Pipe):
    def run(self, pipe_in):
        delimiter = self.kwargs.get('delimiter', '-')
        return delimiter.join(pipe_in.split())


class TestPipes(unittest.TestCase):

    def test_one(self):
        out = Cat('asdf') | Upper()
        self.assertEqual(out, 'ASDF')
        out = Cat('one two') | Join()
        self.assertEqual(out, 'one-two')
        out = Cat('one two') | Join(delimiter='*')
        self.assertEqual(out, 'one*two')

    def test_multiple(self):
        out = Cat('one two') | Upper() | Join()
        self.assertEqual(out, 'ONE-TWO')

    def test_string_first(self):
        out = 'one two' | Upper()
        self.assertEqual(out, 'ONE TWO')
        out = 'one two' | Upper() | Join(delimiter='*')
        self.assertEqual(out, 'ONE*TWO')


if __name__ == '__main__':
    unittest.main()
