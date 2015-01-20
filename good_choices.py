import inspect
import six


__all__ = ['Choices', 'VERSION']

VERSION = (1, 1)


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

    def __iter__(self):
        for index, label in self.choices:
            yield index


@six.add_metaclass(ChoicesMeta)
class Choices(object):
    pass

