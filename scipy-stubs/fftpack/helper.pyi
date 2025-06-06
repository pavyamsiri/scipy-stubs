# This module is not meant for public use and will be removed in SciPy v2.0.0.
import sys
from typing import Final
from typing_extensions import deprecated

__all__ = ["fftfreq", "fftshift", "ifftshift", "next_fast_len", "rfftfreq"]

__MESSAGE: Final = "will be removed in SciPy v2.0.0"

if sys.version_info >= (3, 13):
    # `device` was added in numpy 2
    @deprecated(__MESSAGE)
    def fftfreq(n: object, d: object = ..., device: object = ...) -> object: ...
else:
    @deprecated(__MESSAGE)
    def fftfreq(n: object, d: object = ...) -> object: ...

@deprecated(__MESSAGE)
def fftshift(x: object, axes: object = ...) -> object: ...
@deprecated(__MESSAGE)
def ifftshift(x: object, axes: object = ...) -> object: ...
@deprecated(__MESSAGE)
def next_fast_len(target: object) -> object: ...
@deprecated(__MESSAGE)
def rfftfreq(n: object, d: object = ...) -> object: ...
