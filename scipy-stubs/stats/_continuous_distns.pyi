from collections.abc import Sequence
from typing import Any, ClassVar, Final, TypeAlias
from typing_extensions import LiteralString, deprecated, override

import numpy as np
import numpy.typing as npt
import optype.numpy as onpt
from scipy._typing import Seed
from ._distn_infrastructure import _rv_continuous_0, rv_continuous

__all__ = [
    "alpha",
    "alpha_gen",
    "anglit",
    "anglit_gen",
    "arcsine",
    "arcsine_gen",
    "argus",
    "argus_gen",
    "beta",
    "beta_gen",
    "betaprime",
    "betaprime_gen",
    "bradford",
    "bradford_gen",
    "burr",
    "burr12",
    "burr12_gen",
    "burr_gen",
    "cauchy",
    "cauchy_gen",
    "chi",
    "chi2",
    "chi2_gen",
    "chi_gen",
    "cosine",
    "cosine_gen",
    "crystalball",
    "crystalball_gen",
    "dgamma",
    "dgamma_gen",
    "dweibull",
    "dweibull_gen",
    "erlang",
    "erlang_gen",
    "expon",
    "expon_gen",
    "exponnorm",
    "exponnorm_gen",
    "exponpow",
    "exponpow_gen",
    "exponweib",
    "exponweib_gen",
    "f",
    "f_gen",
    "fatiguelife",
    "fatiguelife_gen",
    "fisk",
    "fisk_gen",
    "foldcauchy",
    "foldcauchy_gen",
    "foldnorm",
    "foldnorm_gen",
    "gamma",
    "gamma_gen",
    "gausshyper",
    "gausshyper_gen",
    "genexpon",
    "genexpon_gen",
    "genextreme",
    "genextreme_gen",
    "gengamma",
    "gengamma_gen",
    "genhalflogistic",
    "genhalflogistic_gen",
    "genhyperbolic",
    "genhyperbolic_gen",
    "geninvgauss",
    "geninvgauss_gen",
    "genlogistic",
    "genlogistic_gen",
    "gennorm",
    "gennorm_gen",
    "genpareto",
    "genpareto_gen",
    "gibrat",
    "gibrat_gen",
    "gompertz",
    "gompertz_gen",
    "gumbel_l",
    "gumbel_l_gen",
    "gumbel_r",
    "gumbel_r_gen",
    "halfcauchy",
    "halfcauchy_gen",
    "halfgennorm",
    "halfgennorm_gen",
    "halflogistic",
    "halflogistic_gen",
    "halfnorm",
    "halfnorm_gen",
    "hypsecant",
    "hypsecant_gen",
    "invgamma",
    "invgamma_gen",
    "invgauss",
    "invgauss_gen",
    "invweibull",
    "invweibull_gen",
    "irwinhall",
    "irwinhall_gen",
    "jf_skew_t",
    "jf_skew_t_gen",
    "johnsonsb",
    "johnsonsb_gen",
    "johnsonsu",
    "johnsonsu_gen",
    "kappa3",
    "kappa3_gen",
    "kappa4",
    "kappa4_gen",
    "ksone",
    "ksone_gen",
    "kstwo",
    "kstwo_gen",
    "kstwobign",
    "kstwobign_gen",
    "laplace",
    "laplace_asymmetric",
    "laplace_asymmetric_gen",
    "laplace_gen",
    "levy",
    "levy_gen",
    "levy_l",
    "levy_l_gen",
    "loggamma",
    "loggamma_gen",
    "logistic",
    "logistic_gen",
    "loglaplace",
    "loglaplace_gen",
    "lognorm",
    "lognorm_gen",
    "loguniform",
    "lomax",
    "lomax_gen",
    "maxwell",
    "maxwell_gen",
    "mielke",
    "mielke_gen",
    "moyal",
    "moyal_gen",
    "nakagami",
    "nakagami_gen",
    "ncf",
    "ncf_gen",
    "nct",
    "nct_gen",
    "ncx2",
    "ncx2_gen",
    "norm",
    "norm_gen",
    "norminvgauss",
    "norminvgauss_gen",
    "pareto",
    "pareto_gen",
    "pearson3",
    "pearson3_gen",
    "powerlaw",
    "powerlaw_gen",
    "powerlognorm",
    "powerlognorm_gen",
    "powernorm",
    "powernorm_gen",
    "rayleigh",
    "rayleigh_gen",
    "rdist",
    "rdist_gen",
    "recipinvgauss",
    "recipinvgauss_gen",
    "reciprocal",
    "reciprocal_gen",
    "rel_breitwigner",
    "rel_breitwigner_gen",
    "rice",
    "rice_gen",
    "rv_histogram",
    "semicircular",
    "semicircular_gen",
    "skewcauchy",
    "skewcauchy_gen",
    "skewnorm",
    "skewnorm_gen",
    "studentized_range",
    "studentized_range_gen",
    "t",
    "t_gen",
    "trapezoid",
    "trapezoid_gen",
    "trapz",
    "trapz_gen",
    "triang",
    "triang_gen",
    "truncexpon",
    "truncexpon_gen",
    "truncnorm",
    "truncnorm_gen",
    "truncpareto",
    "truncpareto_gen",
    "truncweibull_min",
    "truncweibull_min_gen",
    "tukeylambda",
    "tukeylambda_gen",
    "uniform",
    "uniform_gen",
    "vonmises",
    "vonmises_gen",
    "vonmises_line",
    "wald",
    "wald_gen",
    "weibull_max",
    "weibull_max_gen",
    "weibull_min",
    "weibull_min_gen",
    "wrapcauchy",
    "wrapcauchy_gen",
]

_Scalar_f8_in: TypeAlias = np.float64 | np.float32 | np.float16 | np.integer[Any] | np.bool_
_AnyArray_f8_in: TypeAlias = float | onpt.CanArray[tuple[int, ...], np.dtype[_Scalar_f8_in]] | Sequence[_AnyArray_f8_in]

# without shape params
class anglit_gen(_rv_continuous_0): ...
class arcsine_gen(_rv_continuous_0): ...
class cauchy_gen(_rv_continuous_0): ...
class cosine_gen(_rv_continuous_0): ...
class expon_gen(_rv_continuous_0): ...
class gibrat_gen(_rv_continuous_0): ...
class gumbel_l_gen(_rv_continuous_0): ...
class gumbel_r_gen(_rv_continuous_0): ...
class halfcauchy_gen(_rv_continuous_0): ...
class halflogistic_gen(_rv_continuous_0): ...
class halfnorm_gen(_rv_continuous_0): ...
class hypsecant_gen(_rv_continuous_0): ...
class kstwobign_gen(_rv_continuous_0): ...
class laplace_gen(_rv_continuous_0): ...
class levy_gen(_rv_continuous_0): ...
class levy_l_gen(_rv_continuous_0): ...
class logistic_gen(_rv_continuous_0): ...
class maxwell_gen(_rv_continuous_0): ...
class moyal_gen(_rv_continuous_0): ...

class norm_gen(_rv_continuous_0):
    @override
    def fit(  # type: ignore[override]  # pyright: ignore[reportIncompatibleMethodOverride]
        self,
        /,
        data: _AnyArray_f8_in,
        floc: _Scalar_f8_in | None = None,
        fscale: _Scalar_f8_in | None = None,
        **kwds: _Scalar_f8_in,
    ) -> tuple[np.float64, np.float64]: ...

class rayleigh_gen(_rv_continuous_0): ...
class semicircular_gen(_rv_continuous_0): ...
class uniform_gen(_rv_continuous_0): ...
class wald_gen(_rv_continuous_0): ...

# with shape params
class ksone_gen(rv_continuous): ...
class kstwo_gen(rv_continuous): ...
class alpha_gen(rv_continuous): ...
class beta_gen(rv_continuous): ...
class betaprime_gen(rv_continuous): ...
class bradford_gen(rv_continuous): ...
class burr_gen(rv_continuous): ...
class burr12_gen(rv_continuous): ...
class fisk_gen(burr_gen): ...
class chi_gen(rv_continuous): ...
class chi2_gen(rv_continuous): ...
class dgamma_gen(rv_continuous): ...
class dweibull_gen(rv_continuous): ...
class exponnorm_gen(rv_continuous): ...
class exponweib_gen(rv_continuous): ...
class exponpow_gen(rv_continuous): ...
class fatiguelife_gen(rv_continuous): ...
class foldcauchy_gen(rv_continuous): ...
class f_gen(rv_continuous): ...
class foldnorm_gen(rv_continuous): ...
class weibull_min_gen(rv_continuous): ...
class truncweibull_min_gen(rv_continuous): ...
class weibull_max_gen(rv_continuous): ...
class genlogistic_gen(rv_continuous): ...
class genpareto_gen(rv_continuous): ...
class genexpon_gen(rv_continuous): ...
class genextreme_gen(rv_continuous): ...
class gamma_gen(rv_continuous): ...
class erlang_gen(gamma_gen): ...
class gengamma_gen(rv_continuous): ...
class genhalflogistic_gen(rv_continuous): ...
class genhyperbolic_gen(rv_continuous): ...
class gompertz_gen(rv_continuous): ...
class gausshyper_gen(rv_continuous): ...
class invgamma_gen(rv_continuous): ...
class invgauss_gen(rv_continuous): ...
class geninvgauss_gen(rv_continuous): ...
class norminvgauss_gen(rv_continuous): ...
class invweibull_gen(rv_continuous): ...
class jf_skew_t_gen(rv_continuous): ...
class johnsonsb_gen(rv_continuous): ...
class johnsonsu_gen(rv_continuous): ...
class laplace_asymmetric_gen(rv_continuous): ...
class loggamma_gen(rv_continuous): ...
class loglaplace_gen(rv_continuous): ...
class lognorm_gen(rv_continuous): ...
class mielke_gen(rv_continuous): ...
class kappa4_gen(rv_continuous): ...
class kappa3_gen(rv_continuous): ...
class nakagami_gen(rv_continuous): ...
class ncx2_gen(rv_continuous): ...
class ncf_gen(rv_continuous): ...
class t_gen(rv_continuous): ...
class nct_gen(rv_continuous): ...
class pareto_gen(rv_continuous): ...
class lomax_gen(rv_continuous): ...
class pearson3_gen(rv_continuous): ...
class powerlaw_gen(rv_continuous): ...
class powerlognorm_gen(rv_continuous): ...
class powernorm_gen(rv_continuous): ...
class rdist_gen(rv_continuous): ...

class reciprocal_gen(rv_continuous):
    fit_note: ClassVar[LiteralString] = ...

class rice_gen(rv_continuous): ...
class irwinhall_gen(rv_continuous): ...
class recipinvgauss_gen(rv_continuous): ...
class skewcauchy_gen(rv_continuous): ...
class skewnorm_gen(rv_continuous): ...
class trapezoid_gen(rv_continuous): ...

@deprecated("will be removed in SciPy 1.16.0.")
class trapz_gen(trapezoid_gen): ...

class triang_gen(rv_continuous): ...
class truncexpon_gen(rv_continuous): ...
class truncnorm_gen(rv_continuous): ...
class truncpareto_gen(rv_continuous): ...
class tukeylambda_gen(rv_continuous): ...
class vonmises_gen(rv_continuous): ...
class wrapcauchy_gen(rv_continuous): ...
class gennorm_gen(rv_continuous): ...
class halfgennorm_gen(rv_continuous): ...
class crystalball_gen(rv_continuous): ...
class argus_gen(rv_continuous): ...

class rv_histogram(rv_continuous):
    def __init__(
        self,
        histogram: tuple[npt.NDArray[np.floating[Any]], npt.NDArray[np.inexact[Any]]],
        *args: float | LiteralString | Seed,
        density: bool | None = None,
        **kwargs: float | LiteralString | Seed,
    ) -> None: ...

class studentized_range_gen(rv_continuous): ...
class rel_breitwigner_gen(rv_continuous): ...

ksone: Final[ksone_gen] = ...
kstwo: Final[kstwo_gen] = ...
kstwobign: Final[kstwobign_gen] = ...
norm: Final[norm_gen] = ...
alpha: Final[alpha_gen] = ...
anglit: Final[anglit_gen] = ...
arcsine: Final[arcsine_gen] = ...
beta: Final[beta_gen] = ...
betaprime: Final[betaprime_gen] = ...
bradford: Final[bradford_gen] = ...
burr: Final[burr_gen] = ...
burr12: Final[burr12_gen] = ...
fisk: Final[fisk_gen] = ...
cauchy: Final[cauchy_gen] = ...
chi: Final[chi_gen] = ...
chi2: Final[chi2_gen] = ...
cosine: Final[cosine_gen] = ...
dgamma: Final[dgamma_gen] = ...
dweibull: Final[dweibull_gen] = ...
expon: Final[expon_gen] = ...
exponnorm: Final[exponnorm_gen] = ...
exponweib: Final[exponweib_gen] = ...
exponpow: Final[exponpow_gen] = ...
fatiguelife: Final[fatiguelife_gen] = ...
foldcauchy: Final[foldcauchy_gen] = ...
f: Final[f_gen] = ...
foldnorm: Final[foldnorm_gen] = ...
weibull_min: Final[weibull_min_gen] = ...
truncweibull_min: Final[truncweibull_min_gen] = ...
weibull_max: Final[weibull_max_gen] = ...
genlogistic: Final[genlogistic_gen] = ...
genpareto: Final[genpareto_gen] = ...
genexpon: Final[genexpon_gen] = ...
genextreme: Final[genextreme_gen] = ...
gamma: Final[gamma_gen] = ...
erlang: Final[erlang_gen] = ...
gengamma: Final[gengamma_gen] = ...
genhalflogistic: Final[genhalflogistic_gen] = ...
genhyperbolic: Final[genhyperbolic_gen] = ...
gompertz: Final[gompertz_gen] = ...
gumbel_r: Final[gumbel_r_gen] = ...
gumbel_l: Final[gumbel_l_gen] = ...
halfcauchy: Final[halfcauchy_gen] = ...
halflogistic: Final[halflogistic_gen] = ...
halfnorm: Final[halfnorm_gen] = ...
hypsecant: Final[hypsecant_gen] = ...
gausshyper: Final[gausshyper_gen] = ...
invgamma: Final[invgamma_gen] = ...
invgauss: Final[invgauss_gen] = ...
geninvgauss: Final[geninvgauss_gen] = ...
norminvgauss: Final[norminvgauss_gen] = ...
invweibull: Final[invweibull_gen] = ...
jf_skew_t: Final[jf_skew_t_gen] = ...
johnsonsb: Final[johnsonsb_gen] = ...
johnsonsu: Final[johnsonsu_gen] = ...
laplace: Final[laplace_gen] = ...
laplace_asymmetric: Final[laplace_asymmetric_gen] = ...
levy: Final[levy_gen] = ...
levy_l: Final[levy_l_gen] = ...
logistic: Final[logistic_gen] = ...
loggamma: Final[loggamma_gen] = ...
loglaplace: Final[loglaplace_gen] = ...
lognorm: Final[lognorm_gen] = ...
gibrat: Final[gibrat_gen] = ...
maxwell: Final[maxwell_gen] = ...
mielke: Final[mielke_gen] = ...
kappa4: Final[kappa4_gen] = ...
kappa3: Final[kappa3_gen] = ...
moyal: Final[moyal_gen] = ...
nakagami: Final[nakagami_gen] = ...
ncx2: Final[ncx2_gen] = ...
ncf: Final[ncf_gen] = ...
t: Final[t_gen] = ...
nct: Final[nct_gen] = ...
pareto: Final[pareto_gen] = ...
lomax: Final[lomax_gen] = ...
pearson3: Final[pearson3_gen] = ...
powerlaw: Final[powerlaw_gen] = ...
powerlognorm: Final[powerlognorm_gen] = ...
powernorm: Final[powernorm_gen] = ...
rdist: Final[rdist_gen] = ...
rayleigh: Final[rayleigh_gen] = ...
loguniform: Final[reciprocal_gen] = ...
reciprocal: Final[reciprocal_gen] = ...
rice: Final[rice_gen] = ...
irwinhall: Final[irwinhall_gen] = ...
recipinvgauss: Final[recipinvgauss_gen] = ...
semicircular: Final[semicircular_gen] = ...
skewcauchy: Final[skewcauchy_gen] = ...
skewnorm: Final[skewnorm_gen] = ...
trapezoid: Final[trapezoid_gen] = ...
trapz: Final[trapz_gen] = ...
triang: Final[triang_gen] = ...
truncexpon: Final[truncexpon_gen] = ...
truncnorm: Final[truncnorm_gen] = ...
truncpareto: Final[truncpareto_gen] = ...
tukeylambda: Final[tukeylambda_gen] = ...
uniform: Final[uniform_gen] = ...
vonmises: Final[vonmises_gen] = ...
vonmises_line: Final[vonmises_gen] = ...
wald: Final[wald_gen] = ...
wrapcauchy: Final[wrapcauchy_gen] = ...
gennorm: Final[gennorm_gen] = ...
halfgennorm: Final[halfgennorm_gen] = ...
crystalball: Final[crystalball_gen] = ...
argus: Final[argus_gen] = ...
studentized_range: Final[studentized_range_gen] = ...
rel_breitwigner: Final[rel_breitwigner_gen] = ...
