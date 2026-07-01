import unittest

from calculator import add, subtract


class CalculatorTest(unittest.TestCase):
    def test_add_returns_sum_of_two_numbers(self):
        # add(2, 3)은 2와 3을 더한 값인 5를 돌려줘야 합니다.
        result = add(2, 3)

        self.assertEqual(result, 5)

    def test_subtract_returns_difference_of_two_numbers(self):
        # subtract(7, 4)는 7에서 4를 뺀 값인 3을 돌려줘야 합니다.
        result = subtract(7, 4)

        self.assertEqual(result, 3)


if __name__ == "__main__":
    # 이 파일을 직접 실행하면 위에 작성한 테스트들이 실행됩니다.
    unittest.main()
