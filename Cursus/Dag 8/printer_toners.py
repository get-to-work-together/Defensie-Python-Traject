import matplotlib.pyplot as plt


def toner_levels(levels, printer_name="Printer Cartridge Niveau", ax=None):
    colors = ["cyan", "magenta", "yellow", "black"]
    color_names_nl = ['Cyaan', 'Magenta', 'Geel', 'Zwart']
    
    ax.grid(axis='y', alpha=0.2)
    ax.set_axisbelow(True)
    
    # Volledige staven (100%)
    ax.bar(color_names_nl, [100] * len(colors), color=colors, alpha=0.2, width=0.9)
    
    # Gevulde delen
    ax.bar(color_names_nl, levels, color=colors, width=0.9)
    
    # # Waarden boven de staven
    for i, (level, col) in enumerate(zip(levels, colors)):
        ax.text(i, level+2, f"{level}%", ha="center", color='darkblue', fontsize=12, fontweight='bold')
    
    # Labels en opmaak
    ax.set_ylim(0, 108)
    ax.set_ylabel("Percentage (%)")
    ax.set_title(printer_name)


data = [
    {'name': 'Printer ABC - 134.233.120.001', 'levels': [65, 40, 25, 72]},
    {'name': 'Printer 5 - 134.233.120.011', 'levels': [45, 40, 15, 72]},
    {'name': 'Printer AdBC - 134.233.120.201', 'levels': [85, 40, 25, 72]},
    {'name': 'Printer asssd - 134.233.120.031', 'levels': [75, 40, 25, 72]},
    {'name': 'Printer oiupo - 134.233.120.041', 'levels': [100, 100, 100, 100]},
]


plot_width = 5
plot_height = 5
ncols = 3
nrows = len(data) // ncols
if len(data) % ncols != 0:
    nrows += 1
fig, ax = plt.subplots(nrows, ncols, figsize=(ncols * plot_width, nrows * plot_height), sharey=True, squeeze=False)

for i, d in enumerate(data):
    irow = i // ncols
    icol = i % ncols
    toner_levels(d['levels'], d['name'], ax=ax[irow, icol])

if len(data) % ncols != 0:
    fig.delaxes(ax[nrows-1, ncols-1])

plt.tight_layout()
plt.show()