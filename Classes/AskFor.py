class AskFor:
    @classmethod
    def float(cls, question, values=False):
        while True:
            answer = input(question)
            try:
                answer_float = float(answer)
                if answer_float > 0:
                    if values:
                        return answer_float, answer

                    return answer_float
                else:
                    print("Value needs to be greater than 0!")

            except ValueError:
                try:
                    answer_float = float(answer.replace(",", "."))
                    if values:
                        return answer_float, answer
                    return answer_float

                except ValueError:
                    print("Wrong value!")

    @classmethod
    def integer(cls, question):
        while True:
            try:
                answer_int = int(input(question))
                if answer_int > 0:
                    return answer_int
                else:
                    print("Value needs to be greater than 0!")

            except ValueError:
                print("Wrong value!")

    @classmethod
    def int_from_list(cls, question, int_range):
        while True:
            try:
                answer_int = int(input(question).strip())
                if answer_int in int_range:
                    return answer_int
                else:
                    print("Value out of range!")
            except ValueError:
                print("Wrong value!")

