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

def general_cosine(M, a, sym: bool = True) -> Untyped: ...
def boxcar(M, sym: bool = True) -> Untyped: ...
def triang(M, sym: bool = True) -> Untyped: ...
def parzen(M, sym: bool = True) -> Untyped: ...
def bohman(M, sym: bool = True) -> Untyped: ...
def blackman(M, sym: bool = True) -> Untyped: ...
def nuttall(M, sym: bool = True) -> Untyped: ...
def blackmanharris(M, sym: bool = True) -> Untyped: ...
def flattop(M, sym: bool = True) -> Untyped: ...
def bartlett(M, sym: bool = True) -> Untyped: ...
def hann(M, sym: bool = True) -> Untyped: ...
def tukey(M, alpha: float = 0.5, sym: bool = True) -> Untyped: ...
def barthann(M, sym: bool = True) -> Untyped: ...
def general_hamming(M, alpha, sym: bool = True) -> Untyped: ...
def hamming(M, sym: bool = True) -> Untyped: ...
def kaiser(M, beta, sym: bool = True) -> Untyped: ...
def kaiser_bessel_derived(M, beta, *, sym: bool = True) -> Untyped: ...
def gaussian(M, std, sym: bool = True) -> Untyped: ...
def general_gaussian(M, p, sig, sym: bool = True) -> Untyped: ...
def chebwin(M, at, sym: bool = True) -> Untyped: ...
def cosine(M, sym: bool = True) -> Untyped: ...
def exponential(M, center: Untyped | None = None, tau: float = 1.0, sym: bool = True) -> Untyped: ...
def taylor(M, nbar: int = 4, sll: int = 30, norm: bool = True, sym: bool = True) -> Untyped: ...
def dpss(
    M,
    NW,
    Kmax: Untyped | None = None,
    sym: bool = True,
    norm: Untyped | None = None,
    return_ratios: bool = False,
) -> Untyped: ...
def lanczos(M, *, sym: bool = True) -> Untyped: ...
def get_window(window: Untyped, Nx: Untyped, fftbins: bool = True) -> Untyped: ...
