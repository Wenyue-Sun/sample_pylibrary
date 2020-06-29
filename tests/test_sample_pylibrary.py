
from sample_pylibrary import longest
from sample_pylibrary.cli import main


def test_main():
    main([])


def test_longest():
    assert longest([b'a', b'bc', b'abc']) == b'abc'
