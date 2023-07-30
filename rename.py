import os
import re
from datetime import datetime

# Verzeichnispfad, in dem die Bilder liegen
verzeichnis_pfad = input('Geben Sie den Verzeichnispfad ein, in dem die Bilder liegen: ')
#verzeichnis_pfad = '/home/win/src/PCAP-31/PE2_Test/test//home/win/src/PCAP-31/PE2_Test/test/'

# Funktion, um das Datum aus dem Dateinamen zu extrahieren
def extrahiere_datum(dateiname):
    datum_muster = r'\d{4}-\d{2}-\d{2} \d{2}-\d{2}-\d{2}'
    datum_str = re.search(datum_muster, dateiname).group()
    return datetime.strptime(datum_str, "%Y-%m-%d %H-%M-%S")

# Bilder im Verzeichnis auflisten und nach Datum sortieren
bilder = [datei for datei in os.listdir(verzeichnis_pfad) if datei.endswith('.png')]

# Umbenennen der Bilder
for idx, datei in enumerate(bilder):
    try:
        bilder.sort(key=lambda datei: extrahiere_datum(datei))
        for idx, datei in enumerate(bilder):
            neues_pfad = os.path.join(verzeichnis_pfad, f'Q_{idx + 1}.png')
            os.rename(os.path.join(verzeichnis_pfad, datei), neues_pfad)
    except IndexError:
        print(f"Fehler beim Verarbeiten der Datei: {datei}")

print("Bilder wurden erfolgreich umbenannt.")