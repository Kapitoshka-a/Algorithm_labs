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
    for i in range(start, len(array)):
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


if __name__ == '__main__':
    print(find_longest_peak([1, 2, 3, 4, 2, 5, 6, 7, 0, -11]))
