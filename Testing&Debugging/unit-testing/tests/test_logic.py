import pytest 
from app.logic import is_eligible_for_loan


def test_elible_user():
    assert is_eligible_for_loan(30,60000,"employed") == True

def test_underage_user():
    assert is_eligible_for_loan(18,60000,"employed") == False

def test_low_income():
    assert is_eligible_for_loan(30,40000,"employed") == False

def test_unemployed_user():
    assert is_eligible_for_loan(30,60000,"unemployed") == False    

def test_boundary_case():
    assert is_eligible_for_loan(21,50000,"employed") == True