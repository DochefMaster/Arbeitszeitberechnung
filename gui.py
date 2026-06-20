import customtkinter as ctk
from berechnung import berechnung_arbeitsstunden_tag

ABSTAND_THEMENWECHSEL = 20
ABSTAND_EINGABEFELD = 2

# Standard-Design festlegen
ctk.set_appearance_mode("System")  # Übernimmt den hellen/dunklen Modus des Betriebssystems
ctk.set_default_color_theme("blue")  # Setzt das Farbthema für Knöpfe und Felder

# Das Hauptfenster initialisieren
app = ctk.CTk()
app.title("Arbeitszeitberechnung")
app.geometry("450x750")

# Callback funktion. Logik was passiert, wenn der Button gedrückt wird
def button_klick():
    try:
        # Daten auslesen aus den feldern
        pensum = int(pensum_input.get())
        ferienwochen = int(ferien_input.get())
        arbeitstage = int(tage_input.get())
        ferienarbeit = int(ferienarbeit_input.get())
        bruecktag = int(bruecktag_input.get())
        ueberzeit = float(ueberzeit_input.get())

        # Daten an Funktion übergeben
        soll_stunden, soll_minuten = berechnung_arbeitsstunden_tag(
            arbeitstage,
            pensum,
            ferienarbeit,
            ferienwochen,
            ueberzeit,
            bruecktag
        )

        #Ausgabelabel mit der berechneten Zeit aktualisieren
        ergebnis_label.configure(text=f"Tages-Soll: {soll_stunden} Std. {soll_minuten} Min.",
                              text_color="#2b712b"
        )

    except ValueError:
        #Falls eine Eingabe nicht stimmt
        ergebnis_label.configure(text=f"Fehler: Bitte alle Felder korrekt ausfüllen",
                                 text_color="#a33b3b"
        )

def maus_betritt(event):
    info_pensum.configure(text="Test!")

def maus_verlassen(event):
    info_pensum.configure(text="")


# Titel erstellen
titel_label = ctk.CTkLabel(app, text="Arbeitszeit-Berechnung", font=("Arial",20, "bold"))
titel_label.pack(pady=(20,30))

# Eingabe: Pensum
pensum_label = ctk.CTkLabel(app, text="Arbeitspensum (%):")
pensum_label.pack(pady=(0, ABSTAND_EINGABEFELD))

pensum_input = ctk.CTkEntry(app, placeholder_text="10...100", width=100)
pensum_input.pack(pady=(0, ABSTAND_EINGABEFELD))

info_pensum = ctk.CTkLabel(app, text="", font=("Arial", 12, "italic"), text_color="gray")
info_pensum.pack(pady=(0, 0))



# Eingabe: Anzahl Wochen Ferien
ferien_label = ctk.CTkLabel(app, text="Anzahl Ferienwochen:")
ferien_label.pack(pady=(0, ABSTAND_EINGABEFELD))

ferien_input = ctk.CTkEntry(app, placeholder_text="z.B. 5", width=100)
ferien_input.pack(pady=(0, ABSTAND_EINGABEFELD))

ferien_info_label = ctk.CTkLabel(app, text="Bitte die Angabe aus Siaxma verwenden im Monatsraport vom Januar (FEKA).", font=("Arial",11))
ferien_info_label.pack(pady=(0,ABSTAND_THEMENWECHSEL))

# Eingabe: Arbeitstage pro Woche
tage_label = ctk.CTkLabel(app, text="Arbeitstage pro Woche:")
tage_label.pack(pady=(0,ABSTAND_EINGABEFELD))

tage_input = ctk.CTkEntry(app, placeholder_text="1...5", width=100)
tage_input.pack(pady=(0, ABSTAND_THEMENWECHSEL))

# Eingabe: Anzahl Arbeitstage in Ferien
ferienarbeit_label = ctk.CTkLabel(app, text="Arbeitstage während Schulferien:")
ferienarbeit_label.pack(pady=(0, ABSTAND_EINGABEFELD))

ferienarbeit_input = ctk.CTkEntry(app, placeholder_text="z.B. 12", width=100)
ferienarbeit_input.pack(pady=(0,ABSTAND_THEMENWECHSEL))

# Eingabe: Anzahl genommene Brückentage
bruecktag_label = ctk.CTkLabel(app, text="Wie viele Brückentage werden genommen:")
bruecktag_label.pack(pady=(0, ABSTAND_EINGABEFELD))

bruecktag_input = ctk.CTkEntry(app, placeholder_text="z.B. 2", width=100)
bruecktag_input.pack(pady=(0,ABSTAND_THEMENWECHSEL))

# Eingabe: Mitgenommen Überzeit
ueberzeit_label = ctk.CTkLabel(app, text="Mitgenommene Überstunden von Vorjahr:")
ueberzeit_label.pack(pady=(0, ABSTAND_EINGABEFELD))

ueberzeit_input = ctk.CTkEntry(app, placeholder_text="z.B. 24.5", width=100)
ueberzeit_input.pack(pady=(0,ABSTAND_THEMENWECHSEL))

#Ausgabe: Berechnete Zeit mit einer Trennlinie dazwischen
trenner = ctk.CTkFrame(app, height=2, width=400)
trenner.pack(pady=(0,ABSTAND_THEMENWECHSEL))

berechnen_button = ctk.CTkButton(app, text="Berechnen", width=200, height=40, font=("Arial", 14, "bold"), command=button_klick)
berechnen_button.pack(pady=(0, ABSTAND_THEMENWECHSEL))

ergebnis_label = ctk.CTkLabel(app, text="Tages-Soll: -- Std. -- Min.", font=("Arial", 18, "bold"), text_color="#1f6aa5")
ergebnis_label.pack(pady=(0, ABSTAND_THEMENWECHSEL))


#Events verknüpfen
pensum_label.bind("<Enter>", maus_betritt)
pensum_label.bind("<Leave>", maus_verlassen)


# Die endlose Ereignisschleife starten dd
if __name__ == "__main__":
    app.mainloop()