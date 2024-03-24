import unittest

from HumanMove import Student

class HumanMoveTest(unittest.TestCase):
    def test_normal_1(self):
        result_1 = Student('Andrey')
        for i in range(10):
            result_1.walk()
        self.assertEqual(result_1.distance, 50, 'Дистанции не равны [дистанция человека(Andrey)] != 500')
        return result_1.distance

    def test_normal_2(self):
        result_2 = Student('Petr')
        for i in range(10):
            result_2.run()
        self.assertEqual(result_2.distance, 100, 'Дистанции не равны [дистанция человека(Petr)] != 1000')
        return result_2.distance


    def test_normal_3(self):
        self.assertLess(self.test_normal_1(), self.test_normal_2(), 'Petr должен преодолеть дистанцию больше, чем Andrey')

if __name__ == '__main__':
    unittest.main()