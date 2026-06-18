# Daten für das Jahr 2026
ARBEITSTAGE_JAHR_5T = 250  # Mit 100% Anstellung und 5 Wochen Ferien
ARBEITSSTUNDEN_JAHR_VOLLZEIT = 2100  # Mit 100% Anstellung und 5 Wochen Ferien
SCHULFERIEN_WOCHEN = 14
ARBEITSFERIEN_WOCHEN = 5


def berechnung_arbeitsstunden_tag(anzahl_arbeitstage_pro_woche, arbeits_pensum, arbeitstage_ferien):
    # Jahressoll auf auf Pensum skalieren
    arbeitsstunden_jahr_teilzeit = ARBEITSSTUNDEN_JAHR_VOLLZEIT * arbeits_pensum / 100
    # Das komplette Jahr (Arbeitstage) auf Pensum skalieren
    arbeitstage_jahr_teilzeit = ARBEITSTAGE_JAHR_5T * (anzahl_arbeitstage_pro_woche / 5)
    # Zwischenrechnung wie viele Tage man zusätzlich noch weg ist, über die bezahlten ferien hinaus
    schulferien_unbezahlt_tage_teilzeit = (SCHULFERIEN_WOCHEN - ARBEITSFERIEN_WOCHEN) * anzahl_arbeitstage_pro_woche
    abwesenheit_schulferien_tage = schulferien_unbezahlt_tage_teilzeit - arbeitstage_ferien
    # Tagessoll berechnen mit allen Abhängigkeiten
    return (arbeitsstunden_jahr_teilzeit / (arbeitstage_jahr_teilzeit - abwesenheit_schulferien_tage))


# --- Test-Bereich für das Terminal ---
if __name__ == "__main__":

    berechneter_wert = berechnung_arbeitsstunden_tag(4, 70, 13)
    print("Der Testdurchlauf ergab: ", berechneter_wert)
