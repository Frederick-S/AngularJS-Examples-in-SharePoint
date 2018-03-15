import unittest
from src.chapter_10.singly_linked_circular_list import SinglyLinkedCircularList


class TestSinglyLinkedCircularList(unittest.TestCase):
    def test_singly_linked_circular_list(self):
        singly_linked_circular_list = SinglyLinkedCircularList()
        singly_linked_circular_list.insert(1)
        singly_linked_circular_list.insert(2)
        singly_linked_circular_list.insert(3)
        self.assertEqual(None, singly_linked_circular_list.search(4))
        self.assertEqual(1, singly_linked_circular_list.search(1).key)

        singly_linked_circular_list.delete(1)
        self.assertEqual(None, singly_linked_circular_list.search(1))

        singly_linked_circular_list.delete(2)
        singly_linked_circular_list.delete(3)
        self.assertTrue(singly_linked_circular_list.is_empty())


if __name__ == '__main__':
    unittest.main()
