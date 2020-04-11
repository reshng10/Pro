import unittest

from soz_analizi.sekilci import isim_animals


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)


    def testMethod(self):

     if (isim_animals.animals.__contains__('Adadovşanı')):
         result=True

     expected=True
     self.assertEqual(result,expected)





if __name__ == '__main__':
    unittest.main()
