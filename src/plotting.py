from matplotlib_venn import venn2
import matplotlib.pyplot as plt

def plot_venn(A, B, AB, outfile="venn.png"):
    solo_A = A - AB
    solo_B = B - AB

    venn2(
        subsets=(solo_A, solo_B, AB),
        set_labels=("GO-Homología", "GO-FANTASIA")
    )
    plt.title("Solape GO entre métodos")
    plt.savefig(outfile, dpi=300, bbox_inches="tight")
