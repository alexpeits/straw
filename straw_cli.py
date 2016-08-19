try:
    from IPython import embed

    def repl(context):
        embed()
except ImportError:
    from code import interact

    def repl(context):
        interact(local=context)

from straw.straw import Pipe


class Cat(Pipe):
    def run(self):
        return ' ' .join(self.args)


class Upper(Pipe):
    def run(self, pipe_in):
        return pipe_in.upper()


if __name__ == '__main__':
    repl(globals())
