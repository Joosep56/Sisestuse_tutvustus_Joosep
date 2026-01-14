class Numbrid:
    def __init__(self, text):
        self.text = text

    def get_results(self):
        results = []
        results.append(f"Sisestasid: {self.text}")

        if self.is_number():
            number = float(self.text)

            # Positiivne / negatiivne / 0
            if number > 0:
                results.append("• Positiivne number")
            elif number < 0:
                results.append("• Negatiivne number")
            else:
                results.append("• Number on 0")

            # Täisarv või murdarv
            if number.is_integer():
                results.append("• Täisarv")
                int_number = int(number)

                # Paaris või paaritu
                if int_number % 2 == 0:
                    results.append("• Paaris arv")
                else:
                    results.append("• Paaritu arv")

                # Jagub kolmega
                if int_number % 3 == 0:
                    results.append("• Jagub kolmega")
                else:
                    results.append("• Ei jagu kolmega")

                # Ümmargune number
                if str(abs(int_number)).endswith(("0", "5")):
                    results.append("• Ümmargune number")
                else:
                    results.append("• Ei ole ümmargune number")
            else:
                results.append("• Murdarv")
        else:
            results.append("• Ei ole number")

        return "\n".join(results)

    def is_number(self):
        try:
            float(self.text)
            return True
        except ValueError:
            return False
