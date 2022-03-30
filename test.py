import unittest

Target = __import__("302PairProg")
Wife_tax=Target.Wife_Tax
Husband_tax=Target.Husband_Tax
Joint_tax=Target.Joint_Tax
clear=Target.clear

class TestTax(unittest.TestCase):
	def testCase1(self):
    	"""
    	Test that it can calculate the Total Tax
    	"""
    	W_Personal_Income = 1000000
    	H_Personal_Income = 200000
    	clear()
    	Wresult = round(Wife_tax(W_Personal_Income),0)
    	Hresult = round(Husband_tax(H_Personal_Income),0)
    	Jresult = round(Joint_tax(),0)
    	self.assertEqual(Wresult, 126500)
    	self.assertEqual(Hresult, 1480)
    	self.assertEqual(Jresult, 136360)
   	 
	def testCase2(self):
    	"""
    	Test that it can calculate the Total Tax
    	"""
    	W_Personal_Income = 123123
    	H_Personal_Income = 123123
    	clear()
    	Wresult = Wife_tax(W_Personal_Income)
    	Hresult = Husband_tax(H_Personal_Income)
    	Jresult = Joint_tax()
    	self.assertEqual(Wresult, "Nill")
    	self.assertEqual(Hresult, "Nill")
    	self.assertEqual(Jresult, 10,"Should be 0")
   	 
	def testCase3(self):
    	"""
    	Test whether negative numbers can be input
    	"""
    	W_Personal_Income = -123123
    	H_Personal_Income = -123123
    	clear()
    	Wresult = Wife_tax(W_Personal_Income)
    	Hresult = Husband_tax(H_Personal_Income)
    	Jresult = Joint_tax()
    	self.assertEqual(Wresult,"Nill")
    	self.assertEqual(Hresult, "Nill")
    	self.assertEqual(Jresult, "Should be Nill")


if __name__ == '__main__':
	unittest.main()

