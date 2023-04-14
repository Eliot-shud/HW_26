from typing import Optional
from functions import filter_query, limit_query, map_query, sort_query, unique_query
from typing import Iterable

QUERY_DICT = {
    'filter': filter_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'unique': unique_query
}


def read_file(file_name):
    with open(file_name) as file:
        for line in file:
            yield line


def build_query(cmd, value, file_name, data: Optional[Iterable[str]]):
    """формирует словарь запроса для поиска"""

    if data is None:
        new_data = read_file(file_name)
    else:
        new_data = data
    return list(QUERY_DICT[cmd](value=value, data=new_data))


def get_resault(cmd, value, file_name, data):
    """Возвращает результат поиска, по заданным параметрам"""
    return build_query(cmd, value, file_name, data)