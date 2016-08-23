import unittest

from straw.straw import pipe


@pipe
def cat(pipe_in, *args):
    return ' '.join(args)


@pipe
def upper(pipe_in):
    return pipe_in.upper()


@pipe
def join(pipe_in, delimiter='-'):
    return delimiter.join(pipe_in.split())


class TestPipeDecorator(unittest.TestCase):

    def test_one(self):
        out = cat('asdf') | upper()
        self.assertEqual(out, 'ASDF')
        out = cat('one two') | join()
        self.assertEqual(out, 'one-two')
        out = cat('one two') | join(delimiter='*')
        self.assertEqual(out, 'one*two')

    def test_multiple(self):
        out = cat('one two') | upper() | join()
        self.assertEqual(out, 'ONE-TWO')

    def test_string_first(self):
        out = 'one two' | upper()
        self.assertEqual(out, 'ONE TWO')
        out = 'one two' | upper() | join(delimiter='*')
        self.assertEqual(out, 'ONE*TWO')


if __name__ == '__main__':
    unittest.main()

