========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/sample_pylibrary/badge/?style=flat
    :target: https://readthedocs.org/projects/sample_pylibrary
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/Wenyue-Sun/sample_pylibrary.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/Wenyue-Sun/sample_pylibrary

.. |requires| image:: https://requires.io/github/Wenyue-Sun/sample_pylibrary/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/Wenyue-Sun/sample_pylibrary/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/Wenyue-Sun/sample_pylibrary/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/Wenyue-Sun/sample_pylibrary

.. |version| image:: https://img.shields.io/pypi/v/sample_pylibrary.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/sample_pylibrary

.. |wheel| image:: https://img.shields.io/pypi/wheel/sample_pylibrary.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/sample_pylibrary

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/sample_pylibrary.svg
    :alt: Supported versions
    :target: https://pypi.org/project/sample_pylibrary

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/sample_pylibrary.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/sample_pylibrary

.. |commits-since| image:: https://img.shields.io/github/commits-since/Wenyue-Sun/sample_pylibrary/v0.1.0.svg
    :alt: Commits since latest release
    :target: https://github.com/Wenyue-Sun/sample_pylibrary/compare/v0.1.0...master



.. end-badges

Sample python package created from cookiecutter-pylibrary

* Free software: MIT license

Installation
============

::

    pip install sample_pylibrary

You can also install the in-development version with::

    pip install https://github.com/Wenyue-Sun/sample_pylibrary/archive/master.zip


Documentation
=============


https://sample_pylibrary.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
