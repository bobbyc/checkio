import unittest

def checkio(elf):
	n = 0
	for i in range(3):
		n += elf[i]
	return n


class CheckIo(unittest.TestCase):
    def testSum(self):
    	self.assertEqual(checkio([1,2,3,4,5,6]), 6)
        
if __name__ == "__main__":
    unittest.main()

    
