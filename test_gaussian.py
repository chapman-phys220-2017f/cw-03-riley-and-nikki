#!/usr/bin/env python3

"""Gaussian Module Unit Tests"""

import nose
import math
import gaussian

def test_g():
    """Tests g with following trials:
        - g(0) ?= 1.0/sqrt(2pi)
    """
    # Pre-computed correct value of g(0)
    actual = 1.0/math.sqrt(2*math.pi)
    # Testing implementation
    trial = gaussian.g(0)
    # Debug messages like this are only printed if the test fails
    print("Testing g(0): ",actual," ?= ",trial)
    # an assert command is the actual test
    # for floats, be sure to use assert_almost_equal instead (here to 4 digits)
    nose.tools.assert_almost_equal(actual, trial, 4)

def test_interval():
    """Tests interval with the following trials:
    """
    result = gaussian.interval(gaussian.add,1,5,1)
    actual = [2,3,4,5,6]
    assert result == actual
    
def test_integrate():
    """Tests integrate with the following trials"""
    def const_func(x):
        return 5
    
    i = gaussian.integrate(const_func,0,10,1)
    result = gaussian.integrate(i,1)
    
    
    
    
    
    
    