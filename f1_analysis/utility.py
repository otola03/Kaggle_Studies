def set_dark(ax, facecolor='#222222', text_color='white', spine_color='#bbbbbb'):
    """_summary_

    Args:
        ax (_type_): ax object
        facecolor (str, optional): backgroud color. Defaults to '#222222'.
        text_color (str, optional): texts color. Defaults to 'white'.
        spine_color (str, optional): axes color. Defaults to '#bbbbbb'.
    """
    # background color
    ax.set_facecolor(facecolor)
    ax.figure.patch.set_facecolor(facecolor)
    
    # texts color
    ax.tick_params(colors=text_color)
    
    # axes color 
    for spine in ax.spines.values():
        spine.set_color(spine_color)
    
    ax.xaxis.label.set_color(text_color)
    ax.yaxis.label.set_color(text_color)
    ax.title.set_color(text_color)