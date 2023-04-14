from typing import Optional, Iterable, List, Dict, Callable

from funtion import filter_query, unique_query, limit_query, map_query, sort_query, regex_get


CMD_TO_FUNCTIONS: Dict[str, Callable] = {
    'filter': filter_query,
    'unique': unique_query,
    'limit': limit_query,
    'map': map_query,
    'sort': sort_query,
    'regex': regex_get,
}


def read_file(file_name: str) -> Iterable[str]:
    with open(file_name) as f:
        for line in f:
            yield line


def configur(cmd: str, value: str, file_name: str, data: Optional[Iterable[str]]) -> List[str]:
    if data is None:
        prepr_date: Iterable[str] = read_file(file_name)
    else:
        prepr_date = data

    return list(CMD_TO_FUNCTIONS[cmd](value=value, data=prepr_date))
