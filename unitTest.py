import unittest
from cuaternion import Cuaternion 
#Esta clase realiza el unit test del tipo cuaternion 
#Se verifican las operaciones, los cuaterniones que resultan de ellas y si funciona de manera correcta incluso 
#en casos en los que se introducen letras en lugar de numeros
class Testing(unittest.TestCase):
    def testOperations(self):
        c = Cuaternion(2,3,4,5)
        self.assertEqual(c+2, Cuaternion(4,3,4,5))
        self.assertEqual(2+c, Cuaternion(4,3,4,5))
        self.assertEqual(c*2, Cuaternion(4,3,4,5))
        self.assertEqual(2*c, Cuaternion(4,3,4,5))
        a = Cuaternion(1,2,3,4)
        b = Cuaternion(5,6,7,8)
        self.assertEqual(a+b, Cuaternion(6,8,10,12))
        self.assertEqual(b+a, Cuaternion(6,8,10,12))
        self.assertEqual(-a, Cuaternion(1,-2,-3,-4))
        self.assertEqual(~a, Cuaternion(1,-2,-3,-4))
        d = Cuaternion(1,1,1,1)
        self.assertEqual(d*d, Cuaternion(-2,2,2,2))
        f = Cuaternion(3,5,2,6)
        self.assertTrue(+f)
        self.assertTrue(b+c)
        self.assertTrue(a*b+c)
        self.assertTrue((b + b) * (c + ~a))
        self.assertTrue(+(c*b))
        self.assertTrue(b+3)
        self.assertTrue(a*3.0+7.0)
        self.assertTrue((b+b)*+c)
        self.assertTrue(Cuaternion("a","b","c","d"))
        self.assertTrue(Cuaternion("a",1,2,3))
        
unittest.main()
