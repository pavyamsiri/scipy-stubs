from typing import Any, Literal, TypeAlias, overload

import numpy as np
import optype.numpy as onp
from scipy._typing import Falsy, Truthy
from ._bsplines import BSpline
from ._fitpack_impl import bisplev, bisplrep, splprep, splrep

__all__ = ["bisplev", "bisplrep", "insert", "spalde", "splantider", "splder", "splev", "splint", "splprep", "splrep", "sproot"]

_Float: TypeAlias = float | np.float64
_Float1D: TypeAlias = onp.Array1D[np.float64]
_Float2D: TypeAlias = onp.Array2D[np.float64]
_FloatND: TypeAlias = onp.ArrayND[np.float64]

_Ext: TypeAlias = Literal[0, 1, 2, 3]

_TCK1D: TypeAlias = tuple[_Float1D, _Float1D, int]
_TCK2D: TypeAlias = tuple[_Float1D, list[_Float1D], int]
_ToTCK: TypeAlias = tuple[onp.ToFloat1D, onp.ToFloat1D | onp.ToFloat2D, onp.ToInt]
_ToTCK1D: TypeAlias = tuple[onp.ToFloat1D, onp.ToFloatStrict1D, onp.ToInt]
_ToTCK2D: TypeAlias = tuple[onp.ToFloat1D, onp.ToFloatStrict2D, onp.ToInt]

###

# NOTE: These functions (except spalde) also accept `BSpline` instances, unlike their duals in `_fitpack_impl`.

#
@overload  # tck: BSpline
def splev(x: onp.ToFloatND, tck: BSpline, der: int = 0, ext: _Ext = 0) -> _FloatND: ...
@overload  # tck: 1-d
def splev(x: onp.ToFloatND, tck: _ToTCK1D, der: int = 0, ext: _Ext = 0) -> _FloatND: ...
@overload  # tck: 2-d
def splev(x: onp.ToFloatND, tck: _ToTCK2D, der: int = 0, ext: _Ext = 0) -> list[_FloatND]: ...
@overload  # tck: ?-d
def splev(x: onp.ToFloatND, tck: _ToTCK, der: int = 0, ext: _Ext = 0) -> _FloatND | list[_FloatND]: ...

#
@overload  # tck: BSpline, full_output: falsy
def splint(a: onp.ToFloat, b: onp.ToFloat, tck: BSpline, full_output: Falsy = 0) -> _Float | _Float1D: ...
@overload  # tck: BSpline, full_output: truthy
def splint(a: onp.ToFloat, b: onp.ToFloat, tck: BSpline, full_output: Truthy) -> tuple[_Float | _Float1D, _Float1D]: ...
@overload  # tck: 1-d, full_output: falsy
def splint(a: onp.ToFloat, b: onp.ToFloat, tck: _ToTCK1D, full_output: Falsy = 0) -> _Float: ...
@overload  # tck: 2-d, full_output: falsy
def splint(a: onp.ToFloat, b: onp.ToFloat, tck: _ToTCK2D, full_output: Falsy = 0) -> list[_Float]: ...
@overload  # tck: ?-d, full_output: falsy
def splint(a: onp.ToFloat, b: onp.ToFloat, tck: _ToTCK, full_output: Falsy = 0) -> _Float | list[_Float]: ...
@overload  # tck: 1-d, full_output: truthy
def splint(a: onp.ToFloat, b: onp.ToFloat, tck: _ToTCK1D, full_output: Truthy) -> tuple[_Float, _Float1D]: ...
@overload  # tck: 2-d, full_output: truthy
def splint(a: onp.ToFloat, b: onp.ToFloat, tck: _ToTCK2D, full_output: Truthy) -> tuple[list[_Float], _Float1D]: ...
@overload  # tck: ?-d, full_output: truthy
def splint(a: onp.ToFloat, b: onp.ToFloat, tck: _ToTCK, full_output: Truthy) -> tuple[_Float | list[_Float], _Float1D]: ...

#
@overload  # tck: BSpline
def sproot(tck: BSpline, mest: int = 10) -> _Float1D | _Float2D: ...
@overload  # tck: 1-d
def sproot(tck: _ToTCK1D, mest: int = 10) -> _Float1D: ...
@overload  # tck: 2-d
def sproot(tck: _ToTCK2D, mest: int = 10) -> list[_Float1D]: ...
@overload  # tck: ?-d
def sproot(tck: _ToTCK, mest: int = 10) -> _Float1D | list[_Float1D]: ...

#
@overload  # x: 0-d, tck: 1-d
def spalde(x: onp.ToFloat, tck: _ToTCK1D) -> _Float1D: ...
@overload  # x: 0-d, tck: 2-d
def spalde(x: onp.ToFloat, tck: _ToTCK2D) -> list[_Float1D]: ...
@overload  # x: 0-d
def spalde(x: onp.ToFloat, tck: _ToTCK) -> _Float1D | list[_Float1D]: ...
@overload  # x: 1-d, tck: 1-d
def spalde(x: onp.ToFloatStrict1D, tck: _ToTCK1D) -> list[_Float1D]: ...
@overload  # x: 1-d, tck: 1-d
def spalde(x: onp.ToFloatStrict1D, tck: _ToTCK2D) -> list[list[_Float1D]]: ...
@overload  # x: 1-d, tck: ?-d
def spalde(x: onp.ToFloatStrict1D, tck: _ToTCK) -> list[_Float1D] | list[list[_Float1D]]: ...
@overload  # x: 2-d, tck: 1-d
def spalde(x: onp.ToFloatStrict2D, tck: _ToTCK1D) -> list[list[_Float1D]]: ...
@overload  # x: 2-d, tck: 2-d
def spalde(x: onp.ToFloatStrict2D, tck: _ToTCK2D) -> list[list[list[_Float1D]]]: ...
@overload  # x: 2-d, tck: ?-d
def spalde(x: onp.ToFloatStrict2D, tck: _ToTCK) -> list[list[_Float1D]] | list[list[list[_Float1D]]]: ...
@overload  # catch-all
def spalde(x: onp.ToFloatND, tck: _ToTCK) -> _Float1D | list[_Float1D] | list[list[_Float1D]] | list[list[list[Any]]]: ...

#
@overload  # tck: BSpline
def insert(x: onp.ToFloat, tck: BSpline, m: int = 1, per: onp.ToBool = 0) -> BSpline[np.float64]: ...
@overload  # tck: 1-d
def insert(x: onp.ToFloat, tck: _ToTCK1D, m: int = 1, per: onp.ToBool = 0) -> _TCK1D: ...
@overload  # tck: 2-d
def insert(x: onp.ToFloat, tck: _ToTCK2D, m: int = 1, per: onp.ToBool = 0) -> _TCK2D: ...
@overload  # tck: ?-d
def insert(x: onp.ToFloat, tck: _ToTCK, m: int = 1, per: onp.ToBool = 0) -> _TCK1D | _TCK2D: ...

#
@overload  # tck: BSpline
def splder(tck: BSpline, n: int = 1) -> BSpline[np.float64]: ...
@overload  # tck: 1-d
def splder(tck: _ToTCK1D, n: int = 1) -> _TCK1D: ...
@overload  # tck: 2-d
def splder(tck: _ToTCK2D, n: int = 1) -> _TCK2D: ...
@overload  # tck: ?-d
def splder(tck: _ToTCK, n: int = 1) -> _TCK1D | _TCK2D: ...

#
@overload  # tck: BSpline
def splantider(tck: BSpline, n: int = 1) -> BSpline[np.float64]: ...
@overload  # tck: 1-D
def splantider(tck: _ToTCK1D, n: int = 1) -> _TCK1D: ...
@overload  # tck: 2-D
def splantider(tck: _ToTCK2D, n: int = 1) -> _TCK2D: ...
@overload  # tck: ?-D
def splantider(tck: _ToTCK, n: int = 1) -> _TCK1D | _TCK2D: ...
