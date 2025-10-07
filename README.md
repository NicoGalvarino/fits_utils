# fits_utils

Utilities for working with FITS files and pandas DataFrames.

## Installation
Clone or download this repository and navigate to its directory on the terminal. Then:
  * Install:

  ```bash
  pip install .
  ```

  * Or, install in editable mode for development:

  ```bash
  pip install -e .
  ```

## Usage

```python
import fits_utils

# Read a FITS file into a pandas DataFrame
df = fits_utils.pandas_from_fits('data.fits')

# Save a pandas DataFrame to FITS format
fits_utils.save_to_fits(df, 'output.fits')

# Generate spectrum names
name = fits_utils.spec_name(row, mgii=True)
```

## Functions

- `pandas_from_fits(filepath)`: Read FITS file into pandas DataFrame
- `save_to_fits(df, filepath, meta=None)`: Save pandas DataFrame to FITS file
- `spec_name(row, mgii=False)`: Generate spectrum filename from row data
- `format_pd_for_fits(df)`: Format pandas DataFrame for FITS compatibility
- `cols_format_dict(format_dict, dataframe)`: Get matching column formats
