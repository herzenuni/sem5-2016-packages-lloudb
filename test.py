import unittest
import program





class TestMain(unittest.TestCase):

    def testAdding(self):
        before = len(book.__dict__["participants"])
        program.Partisipant.Adding('Robert',
                                   'Zainitdinov',
                                   19,
                                   'lloudb@gmail.com')
        after = len(program.Partisipant.__dict__["participants"])
        self.failIfEqual(after,before)

    def testDelete(self):
        before = len(book.__dict__["participants"])
        program.Partisipant.Adding('Robert',
                                   'Zainitdinov',
                                   19,
                                   'lloudb@gmail.com')
        program.Partisipant.Delete('Robert')
        after = len(program.Partisipant.__dict__["participants"])
        self.assertEqual(after, before)

    def testRecorder(self):
        import os
        if not os.path.exists('./file.json'):
            assert ('Файл не существует')

if __name__ == '__main__':
    unittest.main()
