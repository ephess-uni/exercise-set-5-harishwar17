""" ex_5_2.py
This module contains an entry point that

- loads data from a file `ex_5_2-data.csv` into a numpy array
- shifts and scales the data such that the resulting mean
        is 0 and the standard deviation is 1.
- writes the processed data to a file called `ex_5_2-processed.csv`
"""
import numpy as np
import os
try:
    from src.util import get_repository_root
except ImportError:
    from util import get_repository_root


if __name__ == "__main__":

    # Use these predefined input / output files
    root_dir = get_repository_root()
    INFILE = root_dir / "data" / "ex_5_2-data.csv"
    OUTFILE = root_dir / "outputs" / "ex_5_2-processed.csv"

    os.makedirs(root_dir / "outputs", exist_ok=True)
    read = np.loadtxt(INFILE)
    mean_of_data = np.mean(read)
    mean_of_data_zero = read - mean_of_data
    _std = np.std(mean_of_data_zero)
    processed = mean_of_data_zero / _std
    np.savetxt(OUTFILE, processed,fmt='%.2e')
