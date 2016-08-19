from straw import Pipe


class Cat(Pipe):
    def run(self, pipe_in):
        return ' '.join(self.args)

class Upper(Pipe):
    def run(self, pipe_in):
        return pipe_in.upper()


class FirstWord(Pipe):
    def run(self, pipe_in):
        return pipe_in.split()[0]


class Join(Pipe):
    def run(self, pipe_in):
        if self.args:
            delimiter = self.args[0]
        else:
            delimiter = self.kwargs.get('delimiter', '-')
        return delimiter.join(pipe_in.split())


class Replace(Pipe):
    def run(self, pipe_in):
        _from = self.args[0]
        _to = self.args[1]
        return pipe_in.replace(_from, _to)


def test_pipe():
    print Cat('upper') | Upper()
    print Cat('one two three') | FirstWord()
    print Cat('one two three') | Join()
    print Cat('one two three') | Join('*')
    print Cat('one two three') | Replace('one', 'one hundred') | Upper() | Join('_')


if __name__ == '__main__':
    test_pipe()
