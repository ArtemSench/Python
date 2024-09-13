import unittest
from tests_12_2 import TournamentTest
from tests_12_1 import RunnerTest

# Создание TestSuite
test_suite = unittest.TestSuite()

# Добавление тестов
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
test_suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))

# Выполнение тестов с verbosity=2
if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)