import re
from Classes.AskFor import AskFor
import numpy as np
import scipy.stats


class Quantities:
    diff_l_numb = None
    l_rep_numb = None
    t_rep_numb = None
    l_resolution = None
    t_resolution = None
    length_dict = {}
    period_dict = {}

    def __init__(self, rep_numb):
        # Values
        self.values_float = []
        self.values_str = []
        self.mean_float = None
        self.mean_str = None
        self.rep_numb = rep_numb

        # Uncertainty
        self.uncertainty_A = None
        self.uncertainty_B = None
        self.uncertainty_exp = None
        self.uncertainty_float = None
        self.uncertainty_str = None

    def get_values_list(self):
        i = 0
        while i < self.rep_numb:
            value_float, value_str = AskFor.float(f"Insert value number {i + 1} : ", values=True)
            self.values_float.append(value_float)
            self.values_str.append(value_str)
            i += 1

    def get_average(self):
        if len(set(self.values_float)) > 1:
            self.mean_float = np.mean(self.values_float)
        else:
            self.mean_float = self.values_float[0]

    def get_uncertainty(self, quantity):
        if quantity == "length":
            self.uncertainty_B = Quantities.l_resolution / np.sqrt(3)
        else:
            self.uncertainty_B = Quantities.t_resolution / np.sqrt(3)

        if len(set(self.values_float)) > 1:
            std_dev = np.std(self.values_float, ddof=1)
            self.uncertainty_A = std_dev / np.sqrt(self.rep_numb)
            self.uncertainty_exp = np.sqrt(self.uncertainty_A ** 2 + self.uncertainty_B ** 2)
            self.uncertainty_float = self.uncertainty_exp * scipy.stats.t.ppf(1 - 0.05 / 2, self.rep_numb - 1)

        else:
            self.uncertainty_A = 0
            self.uncertainty_float = self.uncertainty_B

        self.uncertainty_str = self.round_to_sig_fig(self.uncertainty_float)

    def round_to_sig_fig(self, numb, sig_fig=None):
        if not sig_fig:
            return f'{float(f"{numb:.{2}g}"):g}'
        else:
            return f'{float(f"{numb:.{sig_fig}g}"):g}'

    def round_to_uncertainty(self):
        if "." in self.uncertainty_str:
            round_digits = (len(re.search(r"^\d+\.(\d+)$", self.uncertainty_str).group(1)))
            self.mean_str = f"{self.mean_float:.{round_digits}f}"
        else:
            round_digits = len(self.uncertainty_str)
            if round_digits <= len(self.mean_str):
                self.mean_str = str(round(self.mean_float, -round_digits))
            else:
                self.mean_str = self.round_to_sig_fig(self.mean_float, 3)

    def measurement_dict_append(self, n, quantity):
        if quantity == "length":
            Quantities.length_dict[f"{n}"] = {
                "values_float": self.values_float,
                "values_str": self.values_str,
                "mean_float": self.mean_float,
                "mean_str": self.mean_str,
                "uncertainty_float": self.uncertainty_float,
                "uncertainty_str": self.uncertainty_str
            }
        else:
            Quantities.period_dict[f"{n}"] = {
                "values_float": self.values_float,
                "values_str": self.values_str,
                "mean_float": self.mean_float,
                "mean_str": self.mean_str,
                "uncertainty_float": self.uncertainty_float,
                "uncertainty_str": self.uncertainty_str
            }
