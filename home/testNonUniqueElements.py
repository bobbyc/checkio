import unittest


def checkio(data):

    from collections import Counter
    count = Counter(data)
    print count

    ret = [ x for x in data if count[x] > 1 ]
    return ret


def checkio_speed(data):
    from collections import Counter
    nonunique = Counter(data) - Counter(set(data))
    return [x for x in data if x in nonunique]


class CheckIo(unittest.TestCase):

    def testSum(self):
        res = checkio([10, 9, 10, 9, 8])
        self.assertEqual(res, [10, 9, 10, 9])

if __name__ == "__main__":
    unittest.main()
