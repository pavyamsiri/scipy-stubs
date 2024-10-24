from collections.abc import Callable
from typing import Literal, TypeAlias

import numpy as np
import numpy.typing as npt
import optype.numpy as onpt
from numpy._typing import _ArrayLikeFloat_co, _ArrayLikeInt_co
from scipy._typing import AnyReal, Seed, Untyped

__all__ = ["gaussian_kde"]

_BWMethod: TypeAlias = Literal["scott", "silverman"] | AnyReal | Callable[[gaussian_kde], AnyReal]

class gaussian_kde:
    dataset: onpt.Array[tuple[int, int], np.float64 | np.float32]
    d: int
    n: int
    factor: np.float64
    covariance: onpt.Array[tuple[int, int], np.float64 | np.float32]

    @property
    def weights(self) -> npt.NDArray[np.float64 | np.float32]: ...
    @property
    def inv_cov(self) -> onpt.Array[tuple[int, int], np.float64 | np.float32]: ...
    @property
    def neff(self) -> int: ...
    def __init__(
        self,
        /,
        dataset: _ArrayLikeFloat_co,
        bw_method: _BWMethod | None = None,
        weights: _ArrayLikeFloat_co | None = None,
    ) -> None: ...
    def __call__(self, /, points: _ArrayLikeFloat_co) -> onpt.Array[tuple[int], np.float64 | np.float32]: ...
    evaluate = __call__
    def pdf(self, /, x: _ArrayLikeFloat_co) -> onpt.Array[tuple[int], np.float64 | np.float32]: ...
    def logpdf(self, /, x: _ArrayLikeFloat_co) -> onpt.Array[tuple[int], np.float64 | np.float32]: ...
    def integrate_gaussian(self, /, mean: _ArrayLikeFloat_co, cov: _ArrayLikeFloat_co) -> np.float64 | np.float32: ...
    def integrate_box_1d(self, /, low: AnyReal, high: AnyReal) -> np.float64 | np.float32: ...
    def integrate_box(
        self,
        /,
        low_bounds: _ArrayLikeFloat_co,
        high_bounds: _ArrayLikeFloat_co,
        maxpts: int | None = None,
    ) -> np.float64 | np.float32: ...
    def integrate_kde(self, /, other: gaussian_kde) -> np.float64 | np.float32: ...
    def resample(
        self,
        /,
        size: int | None = None,
        seed: Seed | None = None,
    ) -> onpt.Array[tuple[int, int], np.float64 | np.float32]: ...
    def scotts_factor(self, /) -> np.float64: ...
    def silverman_factor(self, /) -> np.float64: ...
    def covariance_factor(self, /) -> np.float64: ...
    def set_bandwidth(self, /, bw_method: _BWMethod | None = None) -> None: ...
    def marginal(self, /, dimensions: _ArrayLikeInt_co) -> Untyped: ...
