
"""
Benchmarks for iteration loops.
"""

from schematics.models import Model
from schematics.types import IntType
from schematics.types.compound import ModelType, DictType, ListType
try:
    from schematics.iterations import atoms
except ImportError:
    from schematics.transforms import atoms


class Foo(Model):
    intfield = IntType(max_value=2)
    matrixfield = ListType(ListType(IntType))
    dictfield = DictType(IntType)
    modelfield = ModelType('Foo')

data = {
    'intfield': '1',
    'dictfield': dict(a=1, b=2),
    'modelfield': {
        'intfield': '2',
        'matrixfield': [[0, 0, 0], [1, 1, 1], [2, 2, 2]],
        'dictfield': dict(a=11, b=22),
        'modelfield': {
            'intfield': '3',
            'dictfield': dict(a=111, b=222)}}}


def atoms_loop():
    return [(field_name, field, value) for field_name, field, value in atoms(Foo, data)]


class TimeValidationSuite:

    def time_atoms_iteration(self):
        atoms_loop()


class MemValidationSuite:

    def peakmem_atoms_iteration(self):
        for i in xrange(10000):
            atoms_loop()
