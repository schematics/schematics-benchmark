
"""
Benchmarks for validation loops.
"""

from schematics.models import Model
from schematics.types import StringType, IntType
from schematics.validate import validate


class Foo(Model):
    s = StringType()
    i = IntType()

data = {'s': 'schematics', 'i': 42}


class TimeValidationSuite:

    def time_validate_dictionary(self):
        validate(Foo, data)

    def time_validate_model(self):
        Foo(data, validate=True)


class MemValidationSuite:

    def peakmem_validate_dictionary(self):
        for i in xrange(10000):
            validate(Foo, data)

    def peakmem_validate_model(self):
        for i in xrange(10000):
            Foo(data, validate=True)

    def mem_model_instance(self):
        return Foo(data, validate=True)
