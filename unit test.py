import unittest
from main import GetUsername
from main import bubblesort

class MyTestCase(unittest.TestCase):
    def test_PlayerUsername(self):
        username, restriction = GetUsername('284fc0cc-20c6-47ab-b889-b2fff388678c')  # This is my account's uuid
        self.assertEqual(username,"TacoDelMar314")  # This is my username
        self.assertEqual(restriction,2)  # The two shows that I'm recognized as a player
    def test_CarpetBot(self):
        username, restriction = GetUsername('b876ec32-e396-476b-a115-8438d83c67d4')  # This is not a player on my server, this is a youtuber, who's account is used as a bot on our server, in tribute to his death
        self.assertEqual(username, "Bot - Technoblade")
        self.assertEqual(restriction, 1)  # The one shows that he's recognized as a bot from the Carpet mod
    def test_blank(self):
        username, restriction = GetUsername('2aef9ede-35dc-3d95-a068-9b41ba59e267')  # This is a bot that we use, but the actual uuid isn't tied to a username yet, so it's considered a 'known blank'
        self.assertEqual(username, "Known blank")
        self.assertEqual(restriction, 0)  # The zero shows the lowest value, that being a bot with no username tied.

    def test_SmallSort(self):
        arr1=[1,2,3]
        arr2=[10,20,30]
        outarr1,outarr2 = bubblesort(arr1,arr2)
        self.assertEqual(outarr1,[3,2,1])
        self.assertEqual(outarr2,[30,20,10])
    def test_SmallNoSort(self):  # These lists don't need to be sorted, arr1 is already in reverse order
        arr1=[3,2,1]
        arr2=[5,6,7]
        outarr1,outarr2 = bubblesort(arr1,arr2)
        self.assertEqual(outarr1,[3,2,1])
        self.assertEqual(outarr2,[5,6,7])
    def test_BigSort(self):  # Remember, these two arrays are parallel, and so I only need arr1 sorted into reverse order.
        arr1=[3,2,8,9,5,6,4,7,1]
        arr2=[1,2,3,4,5,6,7,8,9]
        outarr1,outarr2 = bubblesort(arr1,arr2)
        self.assertEqual(outarr1,[9,8,7,6,5,4,3,2,1])
        self.assertEqual(outarr2,[4,3,8,6,5,7,1,2,9])
if __name__ == '__main__':
    unittest.main()
