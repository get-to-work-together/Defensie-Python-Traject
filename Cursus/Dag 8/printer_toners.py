import matplotlib.pyplot as plt



def plot_toner_levels(levels, printer_name="Printer Cartridge Niveau", ax=None):
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