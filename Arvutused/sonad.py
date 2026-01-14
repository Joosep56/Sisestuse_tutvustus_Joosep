class Sonad:
    def __init__(self, text):
        self.text = text

    def get_results(self):
        results = []
        results.append(f"Sisestatud väärtus: {self.text}")

        # Tühi või mitte
        if self.text == "":
            results.append("• Sisend on tühi")
        else:
            results.append("• Sisend ei ole tühi")

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

        return "\n".join(results)