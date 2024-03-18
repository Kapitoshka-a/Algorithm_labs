import unittest
from src.avl_queue_priority import AVL_Priority_Queue


class TestAVLPriorityQueue(unittest.TestCase):
    def test_empty_queue(self):
        pq = AVL_Priority_Queue()
        self.assertEqual(pq.display(), None)

    def test_insert_and_display(self):
        pq = AVL_Priority_Queue()
        pq.insert(10, 'A')
        pq.insert(20, 'B')
        pq.insert(5, 'C')
        pq.insert(15, 'D')
        pq.insert(25, 'E')
        pq.insert(30, 'F')

        expected_output = ['F', 'E', 'B', 'D', 'A', 'C']
        self.assertEqual(pq.display(), expected_output)

    def test_same_priority(self):
        pq = AVL_Priority_Queue()
        pq.insert(10, 'A')
        pq.insert(20, 'B')
        pq.insert(20, 'C')
        pq.insert(10, 'D')

        expected_output = ['B', 'C', 'A', 'D']
        self.assertEqual(pq.display(), expected_output)


if __name__ == "__main__":
    unittest.main()
