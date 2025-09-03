# Package metadata
__version__ = "0.1.0"
__author__ = "Nicolas Guerra Varas"
__email__ = "nicolas.guerravaras@eso.org"

# Import main functions to make them available at package level
from .fits_utils import (
    pandas_from_fits,
    save_to_fits,
    spec_name,
    format_pd_for_fits,
    cols_format_dict,
    col_format_all_S17,
    col_units
)

__all__ = [
    'pandas_from_fits',
    'save_to_fits', 
    'spec_name',
    'format_pd_for_fits',
    'cols_format_dict',
    'col_format_all_S17',
    'col_units'
]
