# Daten für das Jahr 2026
#ARBEITSTAGE_JAHR_5T = 250  # Mit 100% Anstellung und 5 Wochen Ferien
#ARBEITSSTUNDEN_JAHR_VOLLZEIT = 2100  # Mit 100% Anstellung und 5 Wochen Ferien
SCHULFERIEN_WOCHEN = 14  # Aus Jahresplan


def umrechnung_zeit(zeit_dezimal):
    return int(zeit_dezimal), int(round((zeit_dezimal - int(zeit_dezimal)) * 60, 0))



"""
anzahl_arbeitstage_pro_woche: Wird vom User eingegeben
arbeits_pensum: Wird vom User eingegeben
arbeitstage_ferien: Wird aus mehreren Eingaben im GUI berechnet, wie viele Tage in den Ferien gearbeitet wird.
arbeitsferien_woche: Wird vom User eingegeben, wie viel wochen bezahlte ferien der User hat
vorhandene_ueberzeit: Wird vom User eingegeben
brueckentage_frei: Wird vom User eingegeben, Brückentage die Frei genommen werden
jahresarbeit_tage: Wird von der Datenbank genommen
jahresarbeit_stunden: Wird von der Datenbank genommen
"""


def berechnung_arbeitsstunden_tag(anzahl_arbeitstage_pro_woche, arbeits_pensum, arbeitstage_ferien, arbeitsferien_woche, vorhandene_ueberzeit=0, brueckentage_frei=0, jahresarbeit_stunden=0, arbeismodell = 42):
    # Anzahl Arbeitstage aus Jahresstunden berechnen
    standard_tages_stunden_vollzeit = arbeismodell / 5 #Tagessoll bei 100% anstellung berechnen
    jahresarbeit_tage = jahresarbeit_stunden / standard_tages_stunden_vollzeit #Anzahl Tage bei 100% anstellung

    # Jahressoll auf auf Pensum skalieren
    arbeitsstunden_jahr_teilzeit = jahresarbeit_stunden * arbeits_pensum / 100 - vorhandene_ueberzeit

    # Das komplette Jahr (Arbeitstage) auf x Tagewoche skalieren
    arbeitstage_jahr_teilzeit = jahresarbeit_tage * (anzahl_arbeitstage_pro_woche / 5)

    # Effekte Zeit die aufgeholt werden muss berechnen
    schulferien_unbezahlt_tage_teilzeit = (SCHULFERIEN_WOCHEN - arbeitsferien_woche) * anzahl_arbeitstage_pro_woche
    abwesenheit_schulferien_tage = schulferien_unbezahlt_tage_teilzeit - arbeitstage_ferien + brueckentage_frei

    # Tagessoll berechnen mit allen Abhängigkeiten
    tagessoll_dezimal = (arbeitsstunden_jahr_teilzeit / (arbeitstage_jahr_teilzeit - abwesenheit_schulferien_tage))

    return umrechnung_zeit(tagessoll_dezimal)


# --- Test-Bereich für das Terminal ---
if __name__ == "__main__":

    stunden, minuten = berechnung_arbeitsstunden_tag(4, 70, 15, 5, 0, 0, 250, 2100)
    print("Der Testdurchlauf ergab: ", stunden, "h ", minuten, "min")
