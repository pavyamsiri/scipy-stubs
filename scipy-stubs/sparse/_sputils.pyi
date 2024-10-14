from typing import Any, Literal

import numpy as np
import scipy.sparse as sp
from scipy._lib._util import np_long as np_long, np_ulong as np_ulong
from scipy._typing import Untyped, UntypedArray

supported_dtypes: Untyped

def upcast(*args) -> Untyped: ...
def upcast_char(*args) -> Untyped: ...
def upcast_scalar(dtype, scalar) -> Untyped: ...
def downcast_intp_index(arr) -> Untyped: ...
def to_native(A) -> Untyped: ...
def getdtype(dtype, a: Untyped | None = None, default: Untyped | None = None) -> Untyped: ...
def getdata(obj, dtype: Untyped | None = None, copy: bool = False) -> UntypedArray: ...
def get_index_dtype(arrays=(), maxval: Untyped | None = None, check_contents: bool = False) -> Untyped: ...
def get_sum_dtype(dtype: np.dtype[np.generic]) -> np.dtype[np.generic]: ...
def isscalarlike(x) -> bool: ...
def isintlike(x) -> bool: ...
def isshape(x, nonneg: bool = False, *, allow_1d: bool = False) -> bool: ...
def issequence(t) -> bool: ...
def ismatrix(t) -> bool: ...
def isdense(x) -> bool: ...
def validateaxis(axis) -> None: ...
def check_shape(args, current_shape: Untyped | None = None, *, allow_1d: bool = False) -> tuple[int, ...]: ...
def check_reshape_kwargs(kwargs) -> Untyped: ...
def is_pydata_spmatrix(m) -> bool: ...
def convert_pydata_sparse_to_scipy(arg: Any, target_format: Literal["csc", "csr"] | None = None) -> Any | sp.spmatrix: ...
def matrix(*args, **kwargs) -> Untyped: ...
def asmatrix(data, dtype: Untyped | None = None) -> Untyped: ...
