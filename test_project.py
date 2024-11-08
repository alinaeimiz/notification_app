
"""
Created on Sun Feb  4 12:37:29 2024

@author: naemiz
"""

import project as nt



def test_title():
    assert isinstance(nt.title(), str) == True
def test_massage():
    assert isinstance(nt.massage(), str) == True
def test_icon():
    assert isinstance(nt.icon(), str) == True
