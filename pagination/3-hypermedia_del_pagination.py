#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get hypermedia pagination information for a specific index.

        Args:
            index (int): The start index of the return page (None for 0)
            page_size (int): The number of items per page

        Returns:
            Dict: Dictionary containing pagination metadata and data
        """
        # Set default index to 0 if None
        if index is None:
            index = 0

        # Assert that index is in valid range
        indexed_dataset = self.indexed_dataset()
        assert 0 <= index < len(indexed_dataset), "Index out of range"

        # Get the data for the current page
        data = []
        current_index = index
        next_index = index

        # Collect data for the current page
        for i in range(page_size):
            # Find the next available index
            while (current_index < len(indexed_dataset) and
                   current_index not in indexed_dataset):
                current_index += 1

            if current_index < len(indexed_dataset):
                data.append(indexed_dataset[current_index])
                next_index = current_index + 1
                current_index += 1
            else:
                break

        # Return the hypermedia dictionary
        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
