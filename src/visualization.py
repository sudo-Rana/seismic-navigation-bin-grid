import matplotlib.pyplot as plt


def plot_fold_map(fold_df):
    plt.figure(figsize=(8, 6))
    sc = plt.scatter(
        fold_df["Bin_X"],
        fold_df["Bin_Y"],
        c=fold_df["Fold"],
        cmap="viridis",
        s=20
    )
    plt.colorbar(sc, label="Fold")
    plt.xlabel("Inline Bin")
    plt.ylabel("Crossline Bin")
    plt.title("3D Seismic Fold Coverage Map")
    plt.show()
