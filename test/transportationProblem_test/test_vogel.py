import unittest
from checkData.Loader import Loader
from transportationProblem.Vogel import Vogel
from model.Contract import Contract


class TestVogel(unittest.TestCase):

    def test_should_load_contracts(self):
        # before
        file = open('data1.txt', 'r')
        loader = Loader('test_data1.txt' + '_result')
        loader.load_data(file)
        file.close()
        vogel = Vogel(loader)
        # when
        contract1 = Contract(0, 0, 800, 70.5)
        contract2 = Contract(0, 1, 600, 70.0)
        contract3 = Contract(2, 0, 900, 80.0)
        vogel.load_contracts()
        # then
        self.assertEqual(contract1, vogel.matrix[0][0])
        self.assertEqual(contract2, vogel.matrix[1][0])
        self.assertEqual(contract3, vogel.matrix[0][2])

    def test_should_find_mins(self):
        # before
        file = open('data1.txt', 'r')
        loader = Loader('test_data1.txt' + '_result')
        loader.load_data(file)
        file.close()
        # when
        vogel = Vogel(loader)
        vogel.load_contracts()
        min_c = [0.5, 10.0, 10.0]
        min_r = [9.5, 10.0, 20.99]
        # then
        self.assertEqual(min_c, vogel.get_min_c())
        self.assertEqual(min_r, vogel.get_min_r())

    def test_should_update_rows_mins(self):
        # before
        file = open('data1.txt', 'r')
        loader = Loader('test_data1.txt' + '_result')
        loader.load_data(file)
        file.close()
        # when
        vogel = Vogel(loader)
        vogel.load_contracts()
        contract1 = Contract(2, 1, 400, 50)
        vogel.matrix[1][2] = contract1
        vogel.update_rows_mins()
        min_r = [9.5, 20.0, 20.99]
        min_c = [0.5, 10.0, 10.0]
        # then
        self.assertEqual(min_r, vogel.get_min_r())
        self.assertEqual(min_c, vogel.get_min_c())

    def test_should_update_columns_mins(self):
        # before
        file = open('data1.txt', 'r')
        loader = Loader('test_data1.txt' + '_result')
        loader.load_data(file)
        file.close()
        # when
        vogel = Vogel(loader)
        vogel.load_contracts()
        contract1 = Contract(2, 1, 400, 50)
        vogel.matrix[1][2] = contract1
        vogel.update_columns_mins()
        min_r = [9.5, 10.0, 20.99]
        min_c = [0.5, 10.0, 30.0]
        # then
        self.assertEqual(min_c, vogel.get_min_c())
        self.assertEqual(min_r, vogel.get_min_r())

    def should_fill_pharmacy(self):
        # before
        file = open('data1.txt', 'r')
        loader = Loader('test_data1.txt' + '_result')
        loader.load_data(file)
        file.close()
        vogel = Vogel(loader)
        # when
        vogel.load_contracts()
        vogel.fill_pharmacy()
        # then
        self.assertEqual(2, len(vogel.matrix))
        self.assertEqual(3, len(vogel.matrix[0]))

if __name__ == '__main__':
    unittest.main()
