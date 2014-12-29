import inspect
import six


class ChoicesMeta(type):
    def __new__(cls, name, bases, attrs):
        ch = list()
        updated_attrs = dict()
        for name, value in six.iteritems(attrs):
            if not name.startswith('_'):
                try:
                    index, label = value
                except ValueError:
                    index = label = value
                ch.append((index, label))
                updated_attrs[name] = index
        attrs.update(updated_attrs)
        attrs['choices'] = sorted(ch, key=lambda c: c[0])
        return super(ChoicesMeta, cls).__new__(cls, name, bases, attrs)


@six.add_metaclass(ChoicesMeta)
class Choices(object):
    pass


if __name__ == '__main__':
    class Ch(Choices):
        A = 1, 'a'
        C = 3, 'c'
        B = 2, 'b'
    assert Ch.choices == [(1, 'a'), (2, 'b'), (3, 'c')]
    assert Ch.A == 1

    class Ch(Choices):
        A = 'X'
        B = 'Y'
        C = 'Z'
    assert Ch.choices == [('X', 'X'), ('Y', 'Y'), ('Z', 'Z')]
    assert Ch.C == 'Z'

