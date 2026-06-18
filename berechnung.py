# Daten für das Jahr 2026
ARBEITSTAGE_JAHR_5T = 250  # Mit 100% Anstellung und 5 Wochen Ferien
ARBEITSSTUNDEN_JAHR_VOLLZEIT = 2100  # Mit 100% Anstellung und 5 Wochen Ferien
SCHULFERIEN_WOCHEN = 14  # Aus Jahresplan


def umrechnung_zeit(zeit_dezimal):
    return int(zeit_dezimal), int(round((zeit_dezimal - int(zeit_dezimal)) * 60, 0))



"""
anzahl_arbeitstage_pro_woche: Wird vom User eingegeben
arbeits_pensum: Wird vom User eingegeben
arbeitstage_ferien: Wird aus mehreren Eingaben im GUI berechnet
arbeitsferien_woche: Wird vom User eingegeben
vorhandene_ueberzeit: Wird vom User eingegeben
brueckentage_frei: Wird vom User eingegeben
"""


def berechnung_arbeitsstunden_tag(anzahl_arbeitstage_pro_woche, arbeits_pensum, arbeitstage_ferien, arbeitsferien_woche, vorhandene_ueberzeit=0, brueckentage_frei=0,):
    # Jahressoll auf auf Pensum skalieren
    arbeitsstunden_jahr_teilzeit = ARBEITSSTUNDEN_JAHR_VOLLZEIT * arbeits_pensum / 100 - vorhandene_ueberzeit
    # Das komplette Jahr (Arbeitstage) auf x Tagewoche skalieren
    arbeitstage_jahr_teilzeit = ARBEITSTAGE_JAHR_5T * (anzahl_arbeitstage_pro_woche / 5)
    # Effekte Zeit die aufgeholt werden muss berechnen
    schulferien_unbezahlt_tage_teilzeit = (SCHULFERIEN_WOCHEN - arbeitsferien_woche) * anzahl_arbeitstage_pro_woche
    abwesenheit_schulferien_tage = schulferien_unbezahlt_tage_teilzeit - arbeitstage_ferien + brueckentage_frei
    # Tagessoll berechnen mit allen Abhängigkeiten
    tagessoll_dezimal = (arbeitsstunden_jahr_teilzeit / (arbeitstage_jahr_teilzeit - abwesenheit_schulferien_tage))
    return umrechnung_zeit(tagessoll_dezimal)


# --- Test-Bereich für das Terminal ---
if __name__ == "__main__":

    stunden, minuten = berechnung_arbeitsstunden_tag(4, 70, 15, 5, 0, 0)
    print("Der Testdurchlauf ergab: ", stunden, "h ", minuten, "min")
