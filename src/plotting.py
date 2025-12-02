from matplotlib_venn import venn2
import matplotlib.pyplot as plt

def diagrama_venn(gos_totales_h: float, gos_totales_f: float, total_solapados: float):
    A = gos_totales_h
    B = gos_totales_f
    AB = round(total_solapados, 1)

    solo_A = round(A - AB, 1)
    solo_B = round(B - AB, 1)

    venn2(subsets=(solo_A, solo_B, AB), set_labels=("GO-Homología", "GO-Fantasia"))
    plt.title("Venn de los téminos GO anotados con FANTASIA vs anotación por homología, para la lista de especies analizadas")
    plt.show()

    fig = plt.gcf()
    fig.set_size_inches(5, 5)
    plt.savefig("venn.png", dpi=300, bbox_inches="tight")