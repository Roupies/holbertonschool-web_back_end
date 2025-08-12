#!/usr/bin/env python3

def index_range(page, page_size):
    """Simple helper function for pagination

Args:
    page (int): The page number (starting from 1)
    page_size (int): The number of items per page

Returns:
    A tuple containing the start and end indices of the items in the page
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
