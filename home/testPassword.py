import unittest

def checkio(data):

    import re
    #replace this for solution
    return True if re.search(r'[A-Z]',data) and re.search(r'[a-z]',data) and re.search(r'[0-9]',data) and len(data) >= 10 else False

class CheckIo(unittest.TestCase):

    def test(self):

        self.assertEqual( checkio(u'A1213pokl'), False)
        self.assertEqual( checkio(u'bAse730onE4') ,True)
        self.assertEqual( checkio(u'asasasasasasasaas') , False)
        self.assertEqual( checkio(u'QWERTYqwerty'), False)
        self.assertEqual( checkio(u'123456123456'), False )
        self.assertEqual( checkio(u'QwErTy911poqqqq'), True)

if __name__ == "__main__":
    unittest.main()


