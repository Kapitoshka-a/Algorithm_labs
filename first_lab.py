import unittest


# variant 3 , level 3
def find_left_peak_part(array, peaks):
    left_part = []
    start = sum([len(i) for i in peaks]) - 1 if peaks else 0
    for i in range(start, len(array) - 1):
        if array[i] < array[i + 1]:
            left_part.append(array[i])
        else:
            if left_part:
                left_part.append(array[i])
                break
    return left_part if len(left_part) >= 1 else None


def find_right_peak_part(left_part, array, peaks):
    right_part = []
    start = sum([len(i) for i in peaks]) + len(left_part) - 1
    for i in range(start, len(array) - 1):
        if array[i - 1] > array[i]:
            right_part.append(array[i])
        else:
            if right_part:
                break
    return right_part if len(right_part) >= 1 else None


def find_longest_peak(array):
    if len(array) < 3:
        return None

    peaks = []
    peak_found = True
    while peak_found:
        peak_found = False
        left_peak_part = find_left_peak_part(array, peaks)
        if left_peak_part:
            right_peak_part = find_right_peak_part(left_peak_part, array, peaks)
            if right_peak_part:
                peaks.append(left_peak_part + right_peak_part)
                peak_found = True

    longest_peak = max(peaks, key=len, default=None)
    return longest_peak


class TestLongestPeak(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(find_longest_peak([1, 2, 3, 4, 5, 6]), None)

    def test_case_2(self):
        self.assertEqual(find_longest_peak([6, 5, 4, 3, 2, 1]), None)

    def test_case_3(self):
        self.assertEqual(find_longest_peak([1, 3, 5, -2, 1, 10, 15, 0, -1, -4, 4, 5, 4]),
                         [-2, 1, 10, 15, 0, -1, -4])

    def test_case_4(self):
        self.assertEqual(find_longest_peak([1, 4, 2, 10, 20, 30, 40]), [1, 4, 2])


if __name__ == '__main__':
    unittest.main()