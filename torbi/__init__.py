###############################################################################
# Configuration
###############################################################################


# Default configuration parameters to be modified
from .config import defaults

# Modify configuration
import yapecs
yapecs.configure('torbi', defaults)

# Import configuration parameters
from .config.defaults import *
import torbi
del torbi.defaults # remove unnecessary module
from .config.static import *


###############################################################################
# Module imports
###############################################################################

import torch

# Import decode function first to avoid circular import
from .viterbi import decode

# Import C extension
from . import _C

# Import all functions from core
from .core import *

# Import other modules
from .chunk import chunk
from . import data
from . import evaluate
from . import partition
from . import reference
