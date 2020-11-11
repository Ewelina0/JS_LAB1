def sort_list(unsorted_list):
    unsorted_list.sort(key=lambda x: (x[1], x[2]))
    print(unsorted_list)


if __name__ == '__main__':
    list_to_sort = [[3, 2, 3], [2, 0, 2], [3, 0, 1]]
    list_to_sort_2 = [[3, 2, 3], [2, 0, 2], [3, 0, 1], [3, 1, 0]]

    sort_list(list_to_sort)
    sort_list(list_to_sort_2)
