from datetime import datetime, timedelta

def calculeaza_ora_trimite():
    # Cere ora la care dorești să ajungă trupele
    ora_sosire = input("Introdu ora la care dorești să ajungă trupele (format hh:mm:ss): ")

    # Cere timpul pe care îl parcurg trupele până la destinație
    timp_parcurs = input("Introdu timpul pe care îl parcurg trupele până la destinație (format hh:mm:ss): ")

    # Converteste string-urile la obiecte datetime
    ora_sosire = datetime.strptime(ora_sosire, '%H:%M:%S')
    timp_parcurs = datetime.strptime(timp_parcurs, '%H:%M:%S')

    # Calculează ora la care trebuie să trimiți trupele
    ora_trimite = ora_sosire - timedelta(hours=timp_parcurs.hour, minutes=timp_parcurs.minute, seconds=timp_parcurs.second)

    # Afișează rezultatul
    print(f"Trebuie să trimiți trupele la ora {ora_trimite.strftime('%H:%M:%S')}.")

# Rulează funcția
calculeaza_ora_trimite()

# Așteaptă o apăsare de tastă înainte de a se închide
input("Apasă orice tastă pentru a închide.")
