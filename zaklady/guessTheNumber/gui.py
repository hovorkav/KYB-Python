import tkinter as tk
import random

class GuessGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Hádej číslo")
        self.geometry("350x300")
        
        # Herní proměnné
        self.cislo = random.randint(1, 20)
        self.pokusy = 0
        self.max_pokusu = 10
        self.skore = 0
        
        # GUI prvky
        self.label_info = tk.Label(self, text="Hádej číslo od 1 do 20", font=("Arial", 14))
        self.label_info.pack(pady=10)
        
        self.entry = tk.Entry(self, font=("Arial", 14), width=10)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", lambda e: self.guess())  # Enter = hádej
        
        self.btn_guess = tk.Button(self, text="Hádej!", command=self.guess, font=("Arial", 12))
        self.btn_guess.pack(pady=10)
        
        self.label_status = tk.Label(self, text="", font=("Arial", 12), fg="blue")
        self.label_status.pack(pady=5)
        
        self.label_pokusy = tk.Label(self, text=f"Zbývá pokusů: {self.max_pokusu}", font=("Arial", 10))
        self.label_pokusy.pack(pady=5)
        
        self.label_skore = tk.Label(self, text=f"Skóre: {self.skore}", font=("Arial", 10))
        self.label_skore.pack(pady=5)
        
        self.btn_nova_hra = tk.Button(self, text="Nová hra", command=self.nova_hra, font=("Arial", 10))
        self.btn_nova_hra.pack(pady=10)
    
    def guess(self):
        try:
            pokus = int(self.entry.get())
        except ValueError:
            self.label_status.config(text="Zadej číslo!", fg="red")
            return
        
        self.entry.delete(0, tk.END)  # Vymaž vstup
        self.pokusy += 1
        zbyva = self.max_pokusu - self.pokusy
        
        if pokus == self.cislo:
            self.skore += 1
            self.label_status.config(text=f"Uhodl jsi! Číslo bylo {self.cislo}", fg="green")
            self.label_skore.config(text=f"Skóre: {self.skore}")
            self.nova_kolo()
        elif pokus < self.cislo:
            self.label_status.config(text="Číslo je VĚTŠÍ", fg="orange")
            self.label_pokusy.config(text=f"Zbývá pokusů: {zbyva}")
        else:
            self.label_status.config(text="Číslo je MENŠÍ", fg="orange")
            self.label_pokusy.config(text=f"Zbývá pokusů: {zbyva}")
        
        if zbyva <= 0 and pokus != self.cislo:
            self.label_status.config(text=f"Prohrál jsi! Číslo bylo {self.cislo}", fg="red")
            self.btn_guess.config(state="disabled")
    
    def nova_kolo(self):
        """Nové kolo po uhodnutí"""
        self.cislo = random.randint(1, 20)
        self.pokusy = 0
        self.label_pokusy.config(text=f"Zbývá pokusů: {self.max_pokusu}")
    
    def nova_hra(self):
        """Kompletní reset hry"""
        self.cislo = random.randint(1, 20)
        self.pokusy = 0
        self.skore = 0
        self.label_status.config(text="", fg="blue")
        self.label_pokusy.config(text=f"Zbývá pokusů: {self.max_pokusu}")
        self.label_skore.config(text=f"Skóre: {self.skore}")
        self.btn_guess.config(state="normal")

if __name__ == "__main__":
    app = GuessGUI()
    app.mainloop()



