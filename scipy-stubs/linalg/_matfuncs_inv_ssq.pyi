import numpy as np

class LogmRankWarning(UserWarning): ...
class LogmExactlySingularWarning(LogmRankWarning): ...
class LogmNearlySingularWarning(LogmRankWarning): ...
class LogmError(np.linalg.LinAlgError): ...
class FractionalMatrixPowerError(np.linalg.LinAlgError): ...
