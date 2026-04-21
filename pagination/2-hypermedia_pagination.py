#!/usr/bin/env python3


"""
function should return a tuple of size two containing a start
index and an end index corresponding to the range of indexes to
return in a list for those particular pagination parameters
"""

import csv
from typing import List, Dict
from math import trunc


def index_range(page: int, page_size: int) -> tuple:
    """
    return a tuple with the start index and end index
    """
    starting_index = (page - 1) * page_size
    ending_index = starting_index + page_size
    start_end = (starting_index, ending_index)
    return start_end


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get page from the dataset
        """
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)

        row = []
        page_index = index_range(page, page_size)
        starting_index, ending_index = page_index[0], page_index[1]

        for i in range(starting_index, ending_index):
            try:
                row.append(self.dataset()[i])
            except IndexError:
                return []

        return row

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get the hypermedia pagination
        """
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)

        total_pages = len(self.dataset()) / page_size
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page + 1 <= total_pages else None
        hyper_dict = {
            "page_size": len(self.get_page(page, page_size)),
            "page": page,
            "data": self.get_page(page, page_size),
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": trunc(total_pages)
            if total_pages == trunc(total_pages) else trunc(total_pages + 1)
            }
        return hyper_dict
