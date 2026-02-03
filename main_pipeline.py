from src.read_segy import read_segy_navigation
from src.validation import validate_navigation
from src.geometry import compute_cmp
from src.binning import generate_bin_grid
from src.qc import navigation_spacing_qc
from src.visualization import plot_fold_map


SEGY_FILE = "data/raw/synthetic_3d.sgy"


def main():
    print("Reading SEG-Y navigation...")
    df = read_segy_navigation(SEGY_FILE)

    print("Validating navigation...")
    validate_navigation(df)

    print("Computing CMPs...")
    df = compute_cmp(df)

    print("Generating bin grid...")
    df, fold = generate_bin_grid(df, bin_size_x=25, bin_size_y=25)

    print("Running navigation QC...")
    flags = navigation_spacing_qc(df, threshold=300)
    df["QC_Flag"] = flags

    print("Plotting fold map...")
    plot_fold_map(fold)

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    main()
