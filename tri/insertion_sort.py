unsorted_array = [2018, 1998, 1986, 2020, 2006]


def insertion_sort(array_to_sort):
    for index in range(1, len(array_to_sort)):
        current_item = array_to_sort[index]
        current_left_index = index - 1
        while current_left_index >= 0 and array_to_sort[current_left_index] > current_item:
            array_to_sort[current_left_index + 1] = array_to_sort[current_left_index]
            current_left_index -= 1
        array_to_sort[current_left_index + 1] = current_item
    return array_to_sort


if __name__ == '__main__':
    print(insertion_sort(unsorted_array))
