FIRST_TIME = True


def get_one_third_section_inaccuracy(min_section, max_section, section):
    n = (max_section - min_section) // 3
    ideal_n = min_section + n
    return abs(section - ideal_n) if section is not None else None


def get_two_third_section_inaccuracy(min_section, max_section, section):
    n = (max_section - min_section) // 3
    ideal_n = min_section + (2 * n)
    return abs(section - ideal_n) if section is not None else None


def get_center_inaccuracy(min_section, max_section, section):
    return abs((section - min_section) + (section - max_section)) if section is not None else None


def get_two_center_sections_and_min_len(min_section, max_section, free_cow_sections, c):
    one_third_section = None
    two_third_section = None
    for section in free_cow_sections:
        section_one_third_accuracy = get_one_third_section_inaccuracy(min_section, max_section, section)
        section_two_third_accuracy = get_two_third_section_inaccuracy(min_section, max_section, section)
        section_one_third_accuracy_main = get_one_third_section_inaccuracy(min_section, max_section, one_third_section)
        section_two_third_accuracy_main = get_two_third_section_inaccuracy(min_section, max_section, two_third_section)
        if section_one_third_accuracy_main is None or section_one_third_accuracy_main > section_one_third_accuracy:
            one_third_section = section
        if section_two_third_accuracy_main is None or section_two_third_accuracy_main >= section_two_third_accuracy:
            two_third_section = section

    c -= 2
    if (one_third_section - min_section < two_third_section - one_third_section and
            one_third_section - min_section < max_section - two_third_section):
        min_len = one_third_section - min_section
    elif (two_third_section - one_third_section < one_third_section - min_section and
          two_third_section - one_third_section < max_section - two_third_section):
        min_len = two_third_section - one_third_section
    else:
        min_len = max_section - two_third_section

    if c > 0:
        get_center_section_and_min_len(min_section, one_third_section, free_cow_sections, c)
        get_center_section_and_min_len(one_third_section, two_third_section, free_cow_sections, c)
        get_center_section_and_min_len(two_third_section, max_section, free_cow_sections, c)

    return min_len


def get_center_section_and_min_len(min_section, max_section, free_cow_section, c):
    global FIRST_TIME
    center_section = None
    free_cow_section = [section for section in free_cow_section if min_section < section < max_section]

    if FIRST_TIME and c % 2 == 0:
        FIRST_TIME = False
        return get_two_center_sections_and_min_len(min_section, max_section, free_cow_section, c)
    else:
        for section in free_cow_section:
            section_accuracy = get_center_inaccuracy(min_section, max_section, section)
            center_section_inaccuracy = get_center_inaccuracy(min_section, max_section, center_section)

            if center_section_inaccuracy is None or section_accuracy < center_section_inaccuracy:
                center_section = section

        c -= 1

        if (center_section - min_section) < (max_section - center_section):
            min_len = center_section - min_section
        else:
            min_len = max_section - center_section

        if c > 0:
            get_center_section_and_min_len(min_section, center_section, free_cow_section, c)
            get_center_section_and_min_len(center_section, max_section, free_cow_section, c)
        return min_len


def find_max_min_length_between_sections(n, c, free_sections):
    min_section = min(free_sections)
    max_section = max(free_sections)

    if c == 2:
        return max_section - min_section

    c -= 2
    return get_center_section_and_min_len(min_section, max_section, free_sections, c)


if __name__ == '__main__':
    N = 8
    C = 4
    free_sections_for_cow = [3, 6, 12, 15, 18, 20, 24, 28]
    print(find_max_min_length_between_sections(N, C, free_sections=free_sections_for_cow))
