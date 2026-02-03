import segyio
import pandas as pd


def read_segy_navigation(segy_file):
    """
    Read seismic navigation from SEG-Y headers
    Returns a DataFrame with source, receiver, and CMP coordinates
    """
    records = []

    with segyio.open(segy_file, "r", ignore_geometry=True) as f:
        for tr in range(f.tracecount):
            hdr = f.header[tr]

            sx = hdr.get(segyio.TraceField.SourceX, None)
            sy = hdr.get(segyio.TraceField.SourceY, None)
            gx = hdr.get(segyio.TraceField.GroupX, None)
            gy = hdr.get(segyio.TraceField.GroupY, None)

            if None in (sx, sy, gx, gy):
                continue

            records.append({
                "SX": sx,
                "SY": sy,
                "GX": gx,
                "GY": gy
            })

    df = pd.DataFrame(records)
    return df
