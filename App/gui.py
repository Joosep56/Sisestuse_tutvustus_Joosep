import tkinter as tk
from tkinter import ttk
#from Arvutused.arvutamine import Arvutamine

from Arvutused.sonad import Sonad
from Arvutused.numbrid import Numbrid


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Minu projekt – GUI")
        self.geometry("520x420")

        # Veidike stiilsemaks seda GUI
        style = ttk.Style(self)
        style.configure("TEntry", fieldbackground="#e6f2ff")  # sisestuskast
        style.configure("TText", background="#ffffe0")  # tulemuste kast
        style.configure("TLabel", background="#f0f8ff")  # labelid
        self.configure(bg="#f0f8ff")  # akna taust

        self._build_ui()

    def _build_ui(self):
        ttk.Label(self, text="Sisesta midagi:").pack(anchor="w", padx=10, pady=(10, 0))

        self.entry = ttk.Entry(self)
        self.entry.pack(fill="x", padx=10, pady=5)

        buttons = ttk.Frame(self)
        buttons.pack(fill="x", padx=10, pady=5)

        ttk.Button(buttons, text="Näita", command=self.show).pack(side="left")
        ttk.Button(buttons, text="Puhasta", command=self.clear).pack(side="left", padx=10)

        ttk.Label(self, text="Tulemused:").pack(anchor="w", padx=10, pady=(10, 0))

        self.output = tk.Text(self, height=12)
        self.output.pack(fill="both", expand=True, padx=10, pady=(0, 10))

    def show(self):
        user_input = self.entry.get()

        try:
            float(user_input)
            calc = Numbrid(user_input)
        except ValueError:
            calc = Sonad(user_input)

        result_text = calc.get_results()

        self.output.delete("1.0", "end")
        self.output.insert("end", result_text)

        self.entry.delete(0, "end")

    def clear(self):
        self.output.delete("1.0", "end")
        self.entry.delete(0, "end")






