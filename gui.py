import customtkinter as ctk
from dataclasses import dataclass
from typing import Dict
from berechnung import berechnung_arbeitsstunden_tag

ABSTAND_THEMENWECHSEL = 20
ABSTAND_EINGABEFELD = 2



# ---Bauplan für Kantonsstruktur erstellen.---
# Erster Schritt: Klasse für die verschiedenen Anstellungsmodelle
@dataclass
class ModellDaten:
    arbeitsstunden: float

# Zweiter schritt:Klasse für die Jahresdaten erstellen
@dataclass
class JahresDaten:
    modelle: Dict[int, ModellDaten]

# Dritter Schritt: Klasse für Kanton, mit Klasse Jahresdaten, erstellen
@dataclass
class Kanton:
    name: str
    jahre: Dict[int, JahresDaten]

# --- Neue Klasse der Kantone mit Daten füllen ---
kantons_daten = {
    "Zug": Kanton(
        name="Zug",
        jahre={
            2026: JahresDaten(
                modelle={
                    42: ModellDaten(arbeitsstunden=2100),
                    43: ModellDaten(arbeitsstunden=2150)
                }
            ),
            2027: JahresDaten(
                modelle={
                    42: ModellDaten(arbeitsstunden=2108.4,),
                    43: ModellDaten(arbeitsstunden=2158.6,)
                }
            ),
            2028: JahresDaten(
                modelle={
                    42: ModellDaten(arbeitsstunden=2091.6,),
                    43: ModellDaten(arbeitsstunden=2141.4,)
                }
            ),
            2029: JahresDaten(
                modelle={
                    42: ModellDaten(arbeitsstunden=2074.8,),
                    43: ModellDaten(arbeitsstunden=2124.2,)
                }
            ),
            2030: JahresDaten(
                modelle={
                    42: ModellDaten(arbeitsstunden=2074.8,),
                    43: ModellDaten(arbeitsstunden=2124.2,)
                }
            )
        }
    ),
    "Bern": Kanton(
        name="Bern",
        jahre={
            2026: JahresDaten(
                modelle={
                    42: ModellDaten(arbeitsstunden=2122.2),
                    43: ModellDaten(arbeitsstunden=0)
                }
            ),
            2027: JahresDaten(
                modelle={
                    42: ModellDaten(arbeitsstunden=2140),
                    43: ModellDaten(arbeitsstunden=0)

                }
            ),
            2028: JahresDaten(
                modelle={
                    42: ModellDaten(arbeitsstunden=0),
                    43: ModellDaten(arbeitsstunden=0)

                }
            ),
            2029: JahresDaten(
                modelle={
                    42: ModellDaten(arbeitsstunden=0),
                    43: ModellDaten(arbeitsstunden=0)

                }
            ),
            2030: JahresDaten(
                modelle={
                    42: ModellDaten(arbeitsstunden=0),
                    43: ModellDaten(arbeitsstunden=0)

                }
            )
        }

    )
}


# Standard-Design festlegen
ctk.set_appearance_mode("System")  # Übernimmt den hellen/dunklen Modus des Betriebssystems
ctk.set_default_color_theme("blue")  # Setzt das Farbthema für Knöpfe und Felder

# Das Hauptfenster initialisieren
app = ctk.CTk()
app.title("Arbeitszeitberechnung")
app.geometry("500x750")

# Daten für Dropdown menu definieren
jahreszahlen_optionen = ["2026", "2027", "2028", "2029", "2030"]
kantone_optionen = ["Zug", "Bern", "t.b.d."]
anstellung_optionen = ["42", "43"]
bezahlte_ferien_optionen = ["4 Wochen (20 Tage)", "5 Wochen (25 Tage)", "6 Wochen (30 Tage)"]

# Callback funktion. Logik was passiert, wenn der Button gedrückt wird
def button_klick():
    try:
        # Daten auslesen aus den feldern
        pensum = int(pensum_input.get())
        wort_liste = dropdown_ferien_input.get().split()
        #print(wort_liste[0])
        ferienwochen = int(wort_liste[0])
        arbeitstage = int(tage_input.get())
        ferienarbeit = int(ferienarbeit_input.get())
        bruecktag = int(bruecktag_input.get())
        ueberzeit = float(ueberzeit_input.get())
        mein_kanton = kantons_daten[dropdown_kanton.get()]
        arbeitstunden_jahr = mein_kanton.jahre[int(dropdown_jahr.get())].modelle[
            int(dropdown_anstellung.get())].arbeitsstunden
        arbeits_modell = int(dropdown_anstellung.get())


        # Daten an Funktion übergeben
        soll_stunden, soll_minuten = berechnung_arbeitsstunden_tag(
            arbeitstage,
            pensum,
            ferienarbeit,
            ferienwochen,
            ueberzeit,
            bruecktag,
            arbeitstunden_jahr,
            arbeits_modell
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


# Titel erstellen
titel_label = ctk.CTkLabel(app, text="Arbeitszeit-Berechnung", font=("Arial",20, "bold"))
titel_label.pack(pady=(20,10))

# Allgemeine Infos einblenden
grid_infos = ctk.CTkFrame(app)
grid_infos.pack(pady=(0, ABSTAND_THEMENWECHSEL))

info_jahr_label = ctk.CTkLabel(grid_infos, text="Jahr: ")
info_jahr_label.grid(row=0, column=0, padx=(10, ABSTAND_EINGABEFELD), pady=5)
dropdown_jahr = ctk.CTkOptionMenu(grid_infos, values=jahreszahlen_optionen, width=80)
dropdown_jahr.set("2026")
dropdown_jahr.grid(row=0, column=1, padx=(0,ABSTAND_THEMENWECHSEL))

info_anstellung_label = ctk.CTkLabel(grid_infos, text="Std./Woche: ")
info_anstellung_label.grid(row=0, column=2, padx=(0, ABSTAND_EINGABEFELD), pady=5)
dropdown_anstellung = ctk.CTkOptionMenu(grid_infos, values=anstellung_optionen, width=80)
dropdown_anstellung.set("42")
dropdown_anstellung.grid(row=0, column=3, padx=(ABSTAND_EINGABEFELD, ABSTAND_THEMENWECHSEL), pady=5)

info_kanton_label = ctk.CTkLabel(grid_infos, text="Kanton: ")
info_kanton_label.grid(row=0, column=4, padx=(0, ABSTAND_EINGABEFELD), pady=5)
dropdown_kanton = ctk.CTkOptionMenu(grid_infos, values=kantone_optionen, width=80)
dropdown_kanton.set("Zug")
dropdown_kanton.grid(row=0, column=5, padx=(ABSTAND_EINGABEFELD, 10), pady=5)

# Eingabe: Pensum
pensum_label = ctk.CTkLabel(app, text="Arbeitspensum (%):")
pensum_label.pack(pady=(0, ABSTAND_EINGABEFELD))

pensum_input = ctk.CTkEntry(app, placeholder_text="10...100", width=100)
pensum_input.insert(0, "70")
pensum_input.pack(pady=(0, ABSTAND_THEMENWECHSEL))

# Eingabe: Anzahl Wochen Ferien
ferien_label = ctk.CTkLabel(app, text="Anzahl bezahlte Ferienwochen:")
ferien_label.pack(pady=(0, ABSTAND_EINGABEFELD))

"""
ferien_input = ctk.CTkEntry(app, placeholder_text="z.B. 5", width=100)
ferien_input.pack(pady=(0, ABSTAND_EINGABEFELD))
"""

dropdown_ferien_input = ctk.CTkOptionMenu(app, values=bezahlte_ferien_optionen)
dropdown_ferien_input.pack(pady=(0, ABSTAND_EINGABEFELD))

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


# Die endlose Ereignisschleife starten dd
if __name__ == "__main__":
    app.mainloop()