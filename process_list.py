from typing import List


def process_list(input_list: List[int]) -> List[int]:
    """
    Process a list of integers

    Parameters:
    input_list: List[int]
        A list of integers. Length must be a multiples of 10.

    Returns:
    List[int]
        The input list with items at indexes that are multiples of 2 or 3
        removed. Note, indexing starts from zero.

    Raises:
    ValueError:
        If the length of the input_list is not a multiple of 10.
    """
    if len(input_list) % 10 != 0:
        raise ValueError("List length must be a multiple of 10")

    return [
        item
        for index, item in enumerate(input_list)
        if index == 0 or (index % 2 != 0 and index % 3 != 0)
    ]


def test_invalid_length():
    try:
        input_list = list(range(1, 10))
        process_list(input_list)
        assert False, "test_invalid_length failed."
    except ValueError as e:
        assert str(e) == "List length must be a multiple of 10"


def test_filtering():
    expected = [0, 1, 5, 7]
    actual = process_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    assert actual == expected, f"Got: {actual}, Expected: {expected}"

    expected = [0, 1, 5, 7, 11, 13, 17, 19]
    actual = process_list(list(range(0,20)))

    assert actual == expected, f"Got: {actual}, Expected: {expected}"



if __name__ == "__main__":
    test_invalid_length()
    test_filtering()
    print("All tests passed!")
