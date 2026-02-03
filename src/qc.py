import numpy as np


def navigation_spacing_qc(df, threshold=200):
    """
    Detect abnormal CMP spacing
    """
    dx = np.diff(df["CMP_X"].values)
    dy = np.diff(df["CMP_Y"].values)

    dist = np.sqrt(dx**2 + dy**2)
    flags = dist > threshold

    return flags
