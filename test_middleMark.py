import pytest
import main

@pytest.mark.parametrize("expected, actual", main.returnList())
class TestClass:
       def test_final(self, expected, actual):
              assert expected == actual

