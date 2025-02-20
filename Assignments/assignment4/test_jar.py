import pytest

from jar import Jar

def test_init(): #test the jar's capacity at the start
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(3)
    assert jar.capacity == 3
    with pytest.raises(ValueError): Jar(-10)

def test_str(): #test if the output is correct
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar = Jar()
    jar.deposit(0)
    assert str(jar) == ""

def test_deposit(): #test if the size attribute tracks the correct number of cookies
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    jar = Jar()
    jar.deposit(0)
    assert jar.size == 0

def test_withdraw(): #test if the size attribute tracks the correct number of cookies after withdrawal
    jar = Jar()
    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2
    jar = Jar()
    jar.deposit(3)
    with pytest.raises(ValueError): jar.withdraw(6)

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()

if __name__ == "__main__":
    main()

