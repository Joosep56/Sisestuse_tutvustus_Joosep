
class Arvutamine:
    def __init__(self, user_input):
        self.text = user_input

    def get_results(self):
        results = f"Sisestasid: {self.text}"

        # Sisendi näitamine
        results= []
        results.append(f"Sisestasid: {self.text}")

        # Tühi või mitte
        if self.text == "":
            results.append("• Sisend on tühi")
        else:
            results.append("• Sisend ei ole tühi")

        # Tekstiga seotud kontrollid
        if self.text != "":
            # Algab suure tähega
            if self.text[0].isupper():
                results.append("• Algab suure tähega")
            else:
                results.append("• Ei alga suure tähega")

            # Sisaldab numbrit
            if any(char.isdigit() for char in self.text):
                results.append("• Sisaldab numbrit")
            else:
                results.append("• Ei sisalda numbrit")

            # Üks või mitu sõna
            if len(self.text.split()) > 1:
                results.append("• Sisaldab mitut sõna")
            else:
                results.append("• Sisaldab ühte sõna")

            # Palindroom
            cleaned = self.text.lower().replace(" ", "")
            if cleaned == cleaned[::-1]:
                results.append("• On palindroom")
            else:
                results.append("• Ei ole palindroom")

        # Numbrilised kontrollid
        if self.is_number():
            number = float(self.text)

            # Positiivne / negatiivne
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