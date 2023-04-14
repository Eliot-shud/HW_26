from typing import Iterable


def filter_query(value: str, data: Iterable[str]):
    return filter(lambda item: value in item, data)


def unique_query(data, *args, **kwargs):
    return set(data)


def limit_query(value, data):
    limit = int(value)
    return list(data)[:limit]


def map_query(value, data):
    column = int(value)
    return map(lambda item: item.split(' ')[column], data)


def sort_query(value, data):
    reverse = value == 'desc'
    return sorted(data, reverse=reverse)