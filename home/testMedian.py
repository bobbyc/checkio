import unittest

def checkio(data):

    data.sort()
    size = len(data)

    ret = ( float(data[size//2]) + data[-(size//2+1)] ) / 2
    return ret

class CheckIo(unittest.TestCase):

    def test(self):
        self.assertEqual( checkio([1, 2, 3, 4, 5]), 3)
        self.assertEqual( checkio([3, 1, 2, 5, 3]), 3)
        self.assertEqual( checkio([1, 300, 2, 200, 1]), 2)
        self.assertEqual( checkio([3, 6, 20, 99, 10, 15]), 12.5)
        self.assertEqual( checkio([1, 10, 2, 9, 3, 8, 4, 7, 5, 6]), 5.5)

if __name__ == "__main__":
    unittest.main()


