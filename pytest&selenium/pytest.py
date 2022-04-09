import logging
import time
import pytest

logging.basicConfig(filename='pytestt.log' ,level=logging.DEBUG, datefmt='|%Y-%m-%d|%H:%M:%S|', format='%(asctime)s::%(levelname)-6s [%(filename)s:%(lineno)d]--->%(message)s')

def add(a, b):
    try:
        return a+b
    except:
        logging.exception("something worng with add function")

def sub(a, b):
    try:
        return a-b
    except:
        logging.exception("something worng with sub function")

def mul(a, b):
    try:
        return a*b
    except:
        logging.exception("something worng with mul function")

def div(a, b):
    try:
        if b == 0:
            print("ERROR: you can't div 0")
        return a/b
    except:
        logging.exception("something worng with div function")

def div_evenlly(a, b):
    try:
        if b == 0:
            print("ERROR: you can't div 0")
        return a//b
    except:
        logging.exception("something worng with div_evenlly function")


def modulo(a, b):
    try:
        if b == 0:
            print("ERROR: you can't div 0")
        return a%b
    except:
        logging.exception("something worng with modulo function")


def sqrt(a):
    try:
        if a > 0:
            print("the answer is complex")
        return a**0.5
    except:
        logging.exception("something worng with sqrt function")

@pytest.mark.parametrize(('x', 'y'), [(5, 5), (5, 6)])
def test_functions0(x ,y):
    assert add(x, y) == 10

@pytest.mark.parametrize(('x', 'y'), [(5, 5), (5, 6)])
def test_functions1(x ,y):
    assert sub(x, y) == 0

@pytest.mark.parametrize(('x', 'y'), [(5, 5), (5, 6)])
def test_functions2(x ,y):
    assert mul(x, y) == 25

@pytest.mark.parametrize(('x', 'y'), [(5, 5), (5, 6)])
def test_functions3(x ,y):
    assert div(x, y) == 1

@pytest.mark.parametrize(('x', 'y'), [(5, 5), (5, 6)])
def test_functions4(x ,y):
    assert div_evenlly(x, y) == 1

@pytest.mark.parametrize(('x', 'y'), [(5, 5), (5, 6)])
def test_functions5(x ,y):
    assert modulo(x, y) == 0

@pytest.mark.parametrize(('x'), [(9), (6)])
def test_functions6(x):
    assert sqrt(x) == 3

