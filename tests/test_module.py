import unittest
import pandas as pd
from src.time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

class TestTimeSeriesVisualizer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Cargar el DataFrame una sola vez para todos los tests
        cls.df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

    def test_draw_line_plot(self):
        try:
            draw_line_plot(self.df)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)

    def test_draw_bar_plot(self):
        try:
            draw_bar_plot(self.df)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)

    def test_draw_box_plot(self):
        try:
            draw_box_plot(self.df)
            result = True
        except Exception:
            result = False
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()