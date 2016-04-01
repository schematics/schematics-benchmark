
Schematics benchmark suite
==========================

Tests that measure and detect regressions in performance of the
`Schematics <https://github.com/schematics/schematics>`_ library.


Setup
-----

The benchmarks are run with the `asv <https://github.com/spacetelescope/asv>`_
utility and requires also ```virtualenv```.

To install asv::

    pip install virtualenv git+https://github.com/spacetelescope/asv

To run the suite::

    sh run.sh

Refer to the `asv documentation <https://asv.readthedocs.org/>`_ for more info.
