#!/usr/bin/env python3

import csv
import math
from typing import List

"""Simple helper function for pagination"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Calculate the start and end indices for a given page and page size.

Args:
    page (int): The page number (starting from 1)
    page_size (int): The number of items per page

Returns:
    Tuple[int, int]: A tuple containing the start index
    and end index for the given page.
"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        """
        Get a specific page of the dataset.
        
        Args:
            page (int): The page number (starting from 1)
            page_size (int): The number of items per page
            
        Returns:
            List[List]: The requested page of data or empty list if out of range
        """
        # Assert that both arguments are integers greater than 0
        assert isinstance(page, int) and page > 0, "page must be an integer greater than 0"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be an integer greater than 0"
        
        # Get the dataset
        dataset = self.dataset()
        
        # Use index_range to find the correct indexes
        start_index, end_index = index_range(page, page_size)
        
        # Check if the requested page is out of range
        if start_index >= len(dataset):
            return []
        
        # Return the appropriate page of the dataset
        return dataset[start_index:end_index]