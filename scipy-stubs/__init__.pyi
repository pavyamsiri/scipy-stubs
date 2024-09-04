from collections.abc import Sequence
from typing import Final, Literal
from typing_extensions import LiteralString

from . import (
    cluster,
    constants,
    datasets,
    fft,
    fftpack,
    integrate,
    interpolate,
    io,
    linalg,
    misc,
    ndimage,
    odr,
    optimize,
    signal,
    sparse,
    spatial,
    special,
    stats,
)
from .__config__ import show as show_config
from ._lib._ccallback import LowLevelCallable
from ._lib._testutils import PytestTester

__all__ = [
    "LowLevelCallable",
    "__version__",
    "cluster",
    "constants",
    "datasets",
    "fft",
    "fftpack",
    "integrate",
    "interpolate",
    "io",
    "linalg",
    "misc",
    "ndimage",
    "odr",
    "optimize",
    "show_config",
    "signal",
    "sparse",
    "spatial",
    "special",
    "stats",
    "test",
]
__version__: Final[LiteralString]
np_minversion: Final[LiteralString]
np_maxversion: Final[LiteralString]

test: Final[PytestTester]

submodules: Final[
    Sequence[
        Literal[
            "cluster",
            "constants",
            "datasets",
            "fft",
            "fftpack",
            "integrate",
            "interpolate",
            "io",
            "linalg",
            "misc",
            "ndimage",
            "odr",
            "optimize",
            "signal",
            "sparse",
            "spatial",
            "special",
            "stats",
        ]
    ]
]
