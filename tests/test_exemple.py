# Fonction à tester
def addition(a, b):
    return a + b


# Test avec pytest
def test_addition():
    assert addition(2, 3) == 5 
    assert addition(-1, 1) == 0
