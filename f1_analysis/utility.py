# pyright: reportMissingTypeStubs=false
import pandas as pd  # type: ignore
import numpy as np  # type: ignore

def set_dark(ax, facecolor='#222222', text_color='white', spine_color='#bbbbbb'):
    """_summary_

    Args:
        ax (_type_): ax object or array of ax objects
        facecolor (str, optional): backgroud color. Defaults to '#222222'.
        text_color (str, optional): texts color. Defaults to 'white'.
        spine_color (str, optional): axes color. Defaults to '#bbbbbb'.
    """
    # Handle both single axes and array of axes
    if isinstance(ax, np.ndarray):
        axes_list = ax.flatten()
    elif hasattr(ax, '__iter__') and not isinstance(ax, str):
        axes_list = list(ax)
    else:
        axes_list = [ax]
    
    # Set figure background color once (from the first axes)
    if len(axes_list) > 0:
        axes_list[0].figure.patch.set_facecolor(facecolor)
    
    # Apply dark theme to each axes
    for ax_item in axes_list:
        # background color
        ax_item.set_facecolor(facecolor)
        
        # texts color
        ax_item.tick_params(colors=text_color)
        
        # axes color 
        for spine in ax_item.spines.values():
            spine.set_color(spine_color)
        
        ax_item.xaxis.label.set_color(text_color)
        ax_item.yaxis.label.set_color(text_color)
        ax_item.title.set_color(text_color)


def time_gap(driver_1_laps: pd.DataFrame, driver_1_name, driver_2_laps: pd.DataFrame, driver_2_name) -> pd.DataFrame:
    """_summary_
    Return the gap DataFrame between the two drivers.
    
    Args:
        driver_1_laps: pd.DataFrame, chasing driver 
        driver_1_name: str
        driver_2_laps: pd.DataFrame, chased driver
        driver_2_name: str
    """
    driver_1_laps['CumulativeTime'] = driver_1_laps['LapTimeSec'].cumsum()
    driver_2_laps['CumulativeTime'] = driver_2_laps['LapTimeSec'].cumsum()
    
    gap = pd.merge(driver_1_laps[['LapNumber', 'CumulativeTime']],
                   driver_2_laps[['LapNumber', 'CumulativeTime']],
                   on='LapNumber',
                   suffixes=(f'_{driver_1_name}', f'_{driver_2_name}'))
    gap['TimeGap'] = gap[f'CumulativeTime_{driver_1_name}'] - gap[f'CumulativeTime_{driver_2_name}']
    
    return gap