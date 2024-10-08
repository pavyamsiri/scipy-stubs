from typing_extensions import override

import numpy as np
from scipy._typing import Untyped
from ._trustregion import BaseQuadraticSubproblem

class CGSteihaugSubproblem(BaseQuadraticSubproblem):
    @override
    def solve(self, trust_radius: float | np.float64) -> Untyped: ...
