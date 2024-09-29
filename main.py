from Classes.Quantities import Quantities
from Classes.AskFor import AskFor
from Classes.Results import Results
from Constants import QUESTION_LATITUDE, LATITUDE_INT_RANGE, QUESTION_L_REP, QUESTION_T_REP, QUESTION_RESOLUTION_L, \
    QUESTION_RESOLUTION_T, QUESTION_MEAS_NUMB, T_MEASUREMENTS_LOOP, L_MEASUREMENTS_LOOP


def main():
    # Calculate gravitational acceleration from latitude
    Results.g_calc = round(Results.calculate_g(AskFor.int_from_list(QUESTION_LATITUDE, LATITUDE_INT_RANGE)), 2)

    # Get properties of the measurements and measuring devices that don't change
    Quantities.diff_l_numb = AskFor.integer(QUESTION_MEAS_NUMB)
    Quantities.l_rep_numb = AskFor.integer(QUESTION_L_REP)
    Quantities.t_rep_numb = AskFor.integer(QUESTION_T_REP)
    Quantities.l_resolution = AskFor.float(QUESTION_RESOLUTION_L)
    Quantities.t_resolution = AskFor.float(QUESTION_RESOLUTION_T)

    # Through one iteration of the following loop all the important values regarding one length of the pendulum are gathered
    for i in range(1, Quantities.diff_l_numb + 1):
        print("\n" + f"Data regarding length number {i} of the pendulum: \n")

        print(L_MEASUREMENTS_LOOP)

        length = Quantities(Quantities.l_rep_numb)
        length.get_values_list()
        length.get_uncertainty(quantity="length")
        length.get_average()
        length.round_to_uncertainty()
        length.measurement_dict_append(i, "length")

        print(T_MEASUREMENTS_LOOP)
        period = Quantities(Quantities.t_rep_numb)
        period.get_values_list()
        period.get_uncertainty(quantity="period")
        period.get_average()
        period.round_to_uncertainty()
        period.measurement_dict_append(i, "period")

    Results.table_printer()
    Results.graph_printer()


if __name__ == "__main__":
    main()
