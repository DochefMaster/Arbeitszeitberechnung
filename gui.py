import customtkinter as ctk

# Standard-Design festlegen
ctk.set_appearance_mode("System")  # Übernimmt den hellen/dunklen Modus des Betriebssystems
ctk.set_default_color_theme("blue")  # Setzt das Farbthema für Knöpfe und Felder

# Das Hauptfenster initialisieren
app = ctk.CTk()
app.title("Arbeitszeitberechnung")
app.geometry("450x600")

# Titel erstellen
titel_label = ctk.CTkLabel(app,text="Arbeitszeit-Berechnung",font=("Arial",20, "bold"))
titel_label.pack(pady=20)

# Eingabe: Pensum
pensum_label = ctk.CTkLabel(app,text="Arbeitspensum (%):")
pensum_label.pack(pady=(10,20))

# Die endlose Ereignisschleife starten
if __name__ == "__main__":
    app.mainloop()