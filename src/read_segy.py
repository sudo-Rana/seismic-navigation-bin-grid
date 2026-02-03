import segyio
import pandas as pd


def apply_scalar(value, scalar):
    if scalar == 0 or scalar is None:
        return value
    if scalar > 0:
        return value * scalar
    return value / abs(scalar)


def read_segy_navigation(segy_file):
    """
    Read seismic navigation from SEG-Y headers with scalar handling
    """
    records = []

    with segyio.open(segy_file, "r", ignore_geometry=True) as f:
        for tr in range(f.tracecount):
            hdr = f.header[tr]

            scalar = hdr.get(segyio.TraceField.SourceGroupScalar, 1)

            sx = hdr.get(segyio.TraceField.SourceX)
            sy = hdr.get(segyio.TraceField.SourceY)
            gx = hdr.get(segyio.TraceField.GroupX)
            gy = hdr.get(segyio.TraceField.GroupY)

            if None in (sx, sy, gx, gy):
                continue

            records.append({
                "SX": apply_scalar(sx, scalar),
                "SY": apply_scalar(sy, scalar),
                "GX": apply_scalar(gx, scalar),
                "GY": apply_scalar(gy, scalar)
            })

    return pd.DataFrame(records)
