from Classes.Quantities import Quantities
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from Constants import (TABLE_INTRODUCTION, PLT_TITLE, G_LAT, G_RESULT, POSITIVE_RESULT_MSG, NEGATIVE_RESULT_MSG,
                       M_ZERO_MSG, PLT_XLABEL, PLT_YLABEL)


class Results:
    values_table = {}
    mean_table = {}
    uncert_table = {}
    g_calc = None

    @classmethod
    def calculate_g(cls, lat):
        return 9.7803267714 * (1 + 0.00193185138639 * np.sin((lat / 180) * np.pi) ** 2) / (
            np.sqrt((1 - 0.00669437999013 * np.sin((lat / 180) * np.pi) ** 2)))

    @classmethod
    def table_printer(cls):
        for i in range(1, Quantities.diff_l_numb + 1):

            Results.values_table[f"{i}"] = {
                "Length [m]": Quantities.length_dict[f"{i}"]["values_str"],
                "10⋅T [s]": Quantities.period_dict[f"{i}"]["values_str"],
                "": f"Length number {i}",
                "Measurm. id": range(1, max([Quantities.l_rep_numb, Quantities.t_rep_numb]) + 1)
            }

            Results.mean_table[f"{i}"] = {
                "Length [m]": Quantities.length_dict[f"{i}"]["mean_str"],
                "10⋅T [s]": Quantities.period_dict[f"{i}"]["mean_str"],
                "": f"Length number {i}",
                "Measurm. id": "x_mean"
            }

            Results.uncert_table[f"{i}"] = {
                "Length [m]": Quantities.length_dict[f"{i}"]["uncertainty_str"],
                "10⋅T [s]": Quantities.period_dict[f"{i}"]["uncertainty_str"],
                "": f"Length number {i}",
                "Measurm. id": "u(x)"
            }

            df_val = pd.DataFrame(dict([(key, pd.Series(value)) for key, value in Results.values_table[f"{i}"].items()]))
            df_val.replace(np.nan, "", inplace=True)
            df_mean = pd.DataFrame(Results.mean_table[f"{i}"], index=["x_mean"])
            df_unc = pd.DataFrame(Results.uncert_table[f"{i}"], index=["u(x)"])
            df_temp = pd.concat([df_val, df_mean, df_unc])
            df_temp[""] = f"Length number {i}"
            df_temp = df_temp.set_index(["", "Measurm. id"])

            if i == 1:
                df_all = df_temp
            else:
                df_all = pd.concat([df_all, df_temp])

        pd.set_option('display.colheader_justify', 'center')
        pd.set_option('display.max_rows', None)
        print(TABLE_INTRODUCTION, df_all)

    @classmethod
    def graph_printer(cls):
        x = np.array([Quantities.length_dict[f"{i}"]["mean_float"] for i in range(1, Quantities.diff_l_numb + 1)])
        y = np.array([(Quantities.period_dict[f"{i}"]["mean_float"] / 10) ** 2 for i in range(1, Quantities.diff_l_numb + 1)])
        x_err = np.array([Quantities.length_dict[f"{i}"]["uncertainty_float"] for i in range(1, Quantities.diff_l_numb + 1)])
        y_err = np.array([(Quantities.period_dict[f"{i}"]["mean_float"] / 50) * Quantities.period_dict[f"{i}"]["uncertainty_float"] for i in range(1, Quantities.diff_l_numb + 1)])
        model = sm.OLS(y, sm.add_constant(x))
        results = model.fit()
        m = results.params[1]
        b = results.params[0]
        u_m = results.bse[1]

        if m != 0:
            g = Quantities(None)
            g.mean_float = (4 * np.pi ** 2) / m
            g.mean_str = str(g.mean_float)
            g.uncertainty_float = (4 * np.pi**2 * u_m) / m**2
            g.uncertainty_str = g.round_to_sig_fig(g.uncertainty_float)
            g.round_to_uncertainty()

            print(G_LAT, f"{Results.g_calc}")

            print(G_RESULT, f"{g.mean_str} ± {g.uncertainty_str}")

            if g.mean_float - g.uncertainty_float < Results.g_calc < g.mean_float + g.uncertainty_float:
                print(POSITIVE_RESULT_MSG)
            else:
                print(NEGATIVE_RESULT_MSG)

        else:
            print(M_ZERO_MSG)

        plt.errorbar(x, y, fmt="bo", xerr=x_err, yerr=y_err, elinewidth=0.9, label="Measurement points")
        xx = np.linspace(x[0], x[-1])
        yy = m*xx + b
        plt.plot(xx, yy, label="least squares fit, $y = mx + b$")
        plt.xlabel(PLT_XLABEL)
        plt.ylabel(PLT_YLABEL)
        plt.title(PLT_TITLE)
        plt.legend(framealpha=1, shadow=True)
        plt.grid(alpha=0.25)

        plt.show()

