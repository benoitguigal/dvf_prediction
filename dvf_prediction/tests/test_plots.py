from unittest import TestCase

from ..plots import plot_valeur_fonciere_hist, plot_map


class PlotTestCase(TestCase):

    def test_plot_valeur_fonciere_hist(self):
        plot_valeur_fonciere_hist('paris')

    def test_plot_map(self):
        towns = [
            ('paris', 30000),
            ('marseille', 10000),
            ('lyon', 13000),
            ('nantes', 10000),
            ('bordeaux', 13000),
            ('toulouse', 10000)
        ]
        plot_map('paris')

