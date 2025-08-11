import pandas as pd
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

def main():
    # Load the dataset
    df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    # Generate visualizations
    draw_line_plot(df)
    draw_bar_plot(df)
    draw_box_plot(df)

if __name__ == "__main__":
    main()