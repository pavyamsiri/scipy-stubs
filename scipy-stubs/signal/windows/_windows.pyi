from scipy._typing import Untyped

__all__ = [
    "barthann",
    "bartlett",
    "blackman",
    "blackmanharris",
    "bohman",
    "boxcar",
    "chebwin",
    "cosine",
    "dpss",
    "exponential",
    "flattop",
    "gaussian",
    "general_cosine",
    "general_gaussian",
    "general_hamming",
    "get_window",
    "hamming",
    "hann",
    "kaiser",
    "kaiser_bessel_derived",
    "lanczos",
    "nuttall",
    "parzen",
    "taylor",
    "triang",
    "tukey",
]

def general_cosine(M: Untyped, a: Untyped, sym: bool = True) -> Untyped: ...
def boxcar(M: Untyped, sym: bool = True) -> Untyped: ...
def triang(M: Untyped, sym: bool = True) -> Untyped: ...
def parzen(M: Untyped, sym: bool = True) -> Untyped: ...
def bohman(M: Untyped, sym: bool = True) -> Untyped: ...
def blackman(M: Untyped, sym: bool = True) -> Untyped: ...
def nuttall(M: Untyped, sym: bool = True) -> Untyped: ...
def blackmanharris(M: Untyped, sym: bool = True) -> Untyped: ...
def flattop(M: Untyped, sym: bool = True) -> Untyped: ...
def bartlett(M: Untyped, sym: bool = True) -> Untyped: ...
def hann(M: Untyped, sym: bool = True) -> Untyped: ...
def tukey(M: Untyped, alpha: float = 0.5, sym: bool = True) -> Untyped: ...
def barthann(M: Untyped, sym: bool = True) -> Untyped: ...
def general_hamming(M: Untyped, alpha: Untyped, sym: bool = True) -> Untyped: ...
def hamming(M: Untyped, sym: bool = True) -> Untyped: ...
def kaiser(M: Untyped, beta: Untyped, sym: bool = True) -> Untyped: ...
def kaiser_bessel_derived(M: Untyped, beta: Untyped, *, sym: bool = True) -> Untyped: ...
def gaussian(M: Untyped, std: Untyped, sym: bool = True) -> Untyped: ...
def general_gaussian(M: Untyped, p: Untyped, sig: Untyped, sym: bool = True) -> Untyped: ...
def chebwin(M: Untyped, at: Untyped, sym: bool = True) -> Untyped: ...
def cosine(M: Untyped, sym: bool = True) -> Untyped: ...
def exponential(M: Untyped, center: Untyped | None = None, tau: float = 1.0, sym: bool = True) -> Untyped: ...
def taylor(M: Untyped, nbar: int = 4, sll: int = 30, norm: bool = True, sym: bool = True) -> Untyped: ...
def dpss(
    M: Untyped,
    NW: Untyped,
    Kmax: Untyped | None = None,
    sym: bool = True,
    norm: Untyped | None = None,
    return_ratios: bool = False,
) -> Untyped: ...
def lanczos(M: Untyped, *, sym: bool = True) -> Untyped: ...
def get_window(window: Untyped, Nx: Untyped, fftbins: bool = True) -> Untyped: ...
