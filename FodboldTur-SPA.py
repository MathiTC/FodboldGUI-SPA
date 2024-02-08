import tkinter as tk
from tkinter import ttk
import pickle

filename = 'betalinger.pk'

# Prøv at indlæse tidligere data fra pickle-fil, eller opret en tom dictionary
try:
    with open(filename, 'rb') as f:
        betalinger = pickle.load(f)
    print("Data indlæst fra fil.")
except (FileNotFoundError, EOFError):
    betalinger = {}
    print("Ingen tidligere data fundet. Opret ny opsparingsordning.")

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Home Page")
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Register Payment", command=lambda: controller.show_frame("RegisterPayment"))
        button1.pack()

        button2 = tk.Button(self, text="View Payments", command=lambda: controller.show_frame("ListPayments"))
        button2.pack()

        button3 = tk.Button(self, text="View Worst Payers", command=lambda: controller.show_frame("WorstPayers"))
        button3.pack()


class RegisterPayment(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.medlem_navn_label = tk.Label(self, text="Indtast medlemmets navn:")
        self.medlem_navn_label.pack(pady=5)

        # Entry widget for member's name
        self.medlem_navn_var = tk.StringVar()
        self.medlem_navn_entry = tk.Entry(self, textvariable=self.medlem_navn_var)
        self.medlem_navn_entry.pack(pady=5)
        self.medlem_navn_entry.bind("<KeyRelease>", self.autocomplete)

        # Listbox to display autocomplete suggestions
        self.autocomplete_listbox = tk.Listbox(self)
        self.autocomplete_listbox.pack(pady=5)
        self.autocomplete_listbox.bind("<Double-Button-1>", self.select_autocomplete)

        self.belob_label = tk.Label(self, text="Indtast beløb:")
        self.belob_label.pack(pady=5)

        self.belob_entry = tk.Entry(self)
        self.belob_entry.pack(pady=5)

        self.registrer_button = tk.Button(self, text="Registrer Betaling", command=self.registrer_betalinger)
        self.registrer_button.pack(pady=10)

        self.back_button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        self.back_button.pack()

    def autocomplete(self, event=None):
        # Get the text typed by the user
        typed_text = self.medlem_navn_var.get()

        # Clear the listbox
        self.autocomplete_listbox.delete(0, tk.END)

        # Display autocomplete suggestions
        for medlem_navn in betalinger.keys():
            if typed_text.lower() in medlem_navn.lower():
                self.autocomplete_listbox.insert(tk.END, medlem_navn)

    def select_autocomplete(self, event=None):
        # Get the selected item from the listbox
        selected_item = self.autocomplete_listbox.get(tk.ACTIVE)

        # Update the Entry widget with the selected item
        self.medlem_navn_var.set(selected_item)

    def registrer_betalinger(self):
        medlem_navn = self.medlem_navn_entry.get()
        belob = float(self.belob_entry.get())

        if medlem_navn in betalinger:
            betalinger[medlem_navn] += belob
        else:
            betalinger[medlem_navn] = belob

        print(f"{medlem_navn} har nu indbetalt i alt {betalinger[medlem_navn]:.2f} kr.")

        # Clear entry fields after registration
        self.medlem_navn_entry.delete(0, tk.END)
        self.belob_entry.delete(0, tk.END)

class ListPayments(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="View Payments Page")
        label.pack(pady=10, padx=10)

        # Create the table
        self.table = ttk.Treeview(self)
        self.table["columns"] = ("Medlem", "Indbetalt", "Mangler")
        self.table.heading("#0", text="Medlem")
        self.table.heading("Medlem", text="Medlem")
        self.table.heading("Indbetalt", text="Indbetalt")
        self.table.heading("Mangler", text="Mangler")
        self.table.pack(fill="both", expand=True)

        # Populate the table
        self.update_table()

        button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        button.pack()

    def update_table(self):
        for medlem, indbetalt in betalinger.items():
            mangler = max(0, 4500 - indbetalt)
            self.table.insert("", "end", text=medlem, values=(medlem, f"{indbetalt:.2f} kr.", f"{mangler:.2f} kr."))

class WorstPayers(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Worst Payers")
        label.pack(pady=10, padx=10)

        # Create the table
        self.table = ttk.Treeview(self)
        self.table["columns"] = ("Medlem", "Mangler")
        self.table.heading("#0", text="Medlem")
        self.table.heading("Medlem", text="Medlem")
        self.table.heading("Mangler", text="Mangler")
        self.table.pack(fill="both", expand=True)

        # Populate the table
        self.update_table()

        button = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame("HomePage"))
        button.pack()

    def update_table(self):
        top_tre_manglende = sorted(betalinger, key=lambda x: 4500 - betalinger[x], reverse=True)[:3]
        for medlem in top_tre_manglende:
            mangler = max(0, 4500 - betalinger[medlem])
            self.table.insert("", "end", text=medlem, values=(medlem, f"{mangler:.2f} kr."))


class SinglePageApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FodboldTur")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)

        self.frames = {}
        self.create_frames()

        self.show_frame("HomePage")

    def create_frames(self):
        # Define all frames/pages here
        pages = [HomePage, RegisterPayment, ListPayments, WorstPayers]

        for F in pages:
            frame = F(self.container, self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    def show_frame(self, page_name):
        # Show a frame for the given page name
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = SinglePageApp()
    app.mainloop()
