from collections.abc import Callable
from typing_extensions import TypeVar

import optype as op

__all__ = [
    "doc_replace",
    "docformat",
    "extend_notes_in_docstring",
    "filldoc",
    "indentcount_lines",
    "inherit_docstring_from",
    "replace_notes_in_docstring",
    "unindent_dict",
    "unindent_string",
]

_F = TypeVar("_F", bound=Callable[..., object])

def docformat(docstring: str, docdict: dict[str, str] | None = None) -> str: ...
def inherit_docstring_from(cls: type | object) -> Callable[[_F], _F]: ...
def extend_notes_in_docstring(cls: type | object, notes: str) -> Callable[[_F], _F]: ...
def replace_notes_in_docstring(cls: type | object, notes: str) -> Callable[[_F], _F]: ...
def indentcount_lines(lines: op.CanIter[op.CanNext[str]]) -> int: ...
def filldoc(docdict: dict[str, str], unindent_params: bool = True) -> Callable[[_F], _F]: ...
def unindent_dict(docdict: dict[str, str]) -> dict[str, str]: ...
def unindent_string(docstring: str) -> str: ...
def doc_replace(obj: object, oldval: str, newval: str) -> Callable[[_F], _F]: ...
