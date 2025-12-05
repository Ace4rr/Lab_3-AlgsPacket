import pytest
from argparser import build_parsers

@pytest.fixture
def parser():
    return build_parsers()

def test_fact_parsing(parser):
    args=parser.parse_args(["fact", "10"])
    assert args.command=="fact"
    assert args.n==10
    assert args.handler is not None
    assert args.mode=="iter"

def test_factr_parsing(parser):
    args=parser.parse_args(["factr", "7"])
    assert args.command=="factr"
    assert args.n==7
    assert args.mode=="rec"

def test_fib_parsing(parser):
    args=parser.parse_args(["fib", "15"])
    assert args.command=="fib"
    assert args.n==15
    assert args.mode=="iter"

def test_fibr_parsing(parser):
    args=parser.parse_args(["fibr", "8"])
    assert args.command=="fibr"
    assert args.n==8
    assert args.mode=="rec"

def test_sort_parsing(parser):
    args=parser.parse_args(["sort", "quick", "5", "3", "1"])
    assert args.command=="sort"
    assert args.algo=="quick"
    assert args.nums==[5.0, 3.0, 1.0]
    assert args.handler is not None

def test_stack_push_parsing(parser):
    args=parser.parse_args(["stack", "push", "42"])
    assert args.command=="stack"
    assert args.action=="push"
    assert args.value==42
    assert args.handler is not None

def test_stack_pop_parsing(parser):
    args=parser.parse_args(["stack", "pop"])
    assert args.command=="stack"
    assert args.action=="pop"
    assert args.value is None

def test_invalid_command(parser):
    with pytest.raises(SystemExit):
        parser.parse_args(["unknown", "cmd"])