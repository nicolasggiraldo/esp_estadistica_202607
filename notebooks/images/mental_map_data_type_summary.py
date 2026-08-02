from matplotlib.patches import FancyBboxPatch

def caja(ax, xy, texto, color="#4C72B0", ancho=2.2, alto=0.9, fontsize=9):
    x, y = xy
    box = FancyBboxPatch(
        (x - ancho / 2, y - alto / 2), ancho, alto,
        boxstyle="round,pad=0.08,rounding_size=0.08",
        linewidth=1.5, edgecolor=color, facecolor=color, alpha=0.15,
    )
    ax.add_patch(box)
    ax.text(x, y, texto, ha="center", va="center", fontsize=fontsize, color="black")

def flecha(ax, origen, destino):
    ax.annotate("", xy=destino, xytext=origen,
                arrowprops=dict(arrowstyle="-|>", color="gray", lw=1.2, shrinkA=0, shrinkB=0))

fig, ax = plt.subplots(figsize=(11, 6.5))
ax.set_xlim(0, 12)
ax.set_ylim(0, 7)
ax.axis("off")

# Nivel 0: raíz
caja(ax, (6, 6.6), "Data types", color="#333333", ancho=2.6)

# Nivel 1
caja(ax, (3, 5.1), "Qualitative\n(categorical)", color="#DD8452")
caja(ax, (9, 5.1), "Quantitative\n(numeric)", color="#55A868")
flecha(ax, (6, 6.15), (3.4, 5.55))
flecha(ax, (6, 6.15), (8.6, 5.55))

# Nivel 2
caja(ax, (1.5, 3.6), "Nominal\nno order\ne.g.: gender", color="#DD8452", ancho=2.4)
caja(ax, (4.5, 3.6), "Ordinal\nordered\ne.g.: education level", color="#DD8452", ancho=2.4)
caja(ax, (7.5, 3.6), "Discrete\ncount\ne.g.: # purchases", color="#55A868", ancho=2.4)
caja(ax, (10.5, 3.6), "Continuous\nmeasurement\ne.g.: spending $", color="#55A868", ancho=2.4)

flecha(ax, (2.6, 4.65), (1.9, 4.05))
flecha(ax, (3.4, 4.65), (4.1, 4.05))
flecha(ax, (8.6, 4.65), (7.9, 4.05))
flecha(ax, (9.4, 4.65), (10.1, 4.05))

# Separador visual
ax.plot([0.3, 11.7], [2.35, 2.35], color="lightgray", lw=1, linestyle="--")
ax.text(6, 2.05, "Stevens\' levels of measurement (increasing information)",
        ha="center", fontsize=9, style="italic", color="dimgray")

# Nivel 3: escalera de Stevens
escalones = ["Nominal", "Ordinal", "Interval", "Ratio"]
detalles = ["mode", "+ order", "+ distances", "+ absolute zero"]
xs = [1.5, 4.5, 7.5, 10.5]
for x, nombre, detalle in zip(xs, escalones, detalles):
    caja(ax, (x, 1.0), f"{nombre}\n({detalle})", color="#8172B2", ancho=2.4, alto=1.0)
for x1, x2 in zip(xs[:-1], xs[1:]):
    flecha(ax, (x1 + 1.25, 1.0), (x2 - 1.25, 1.0))

plt.tight_layout()
plt.savefig(
    "images/mental_map_data_type_summary.png",
    dpi=200,
    bbox_inches="tight",
)