import subprocess
import socket
import csv
from datetime import datetime
from pathlib import Path

#====================================================================
# Script : scanner_reseau.py
# projet : script d'automatisation reseau
# Auteur : Akpa Salomon Owess
# Objectif : 
# tester automatiquement la disponibilite des machines du lab,verifier
# certains ports importants et generer un rapport csv.
#======================================================================

# liste des machines a surveiller dans le lab

MACHINES = [
        {"nom": "serveur Ubuntu",
         "role": "serveur Interne",
         "ip": "10.132.153.237",
         "ports": [
             {"numero": 22,"service": "SSH"}
             ],
         },
        {
            "nom": "poste Windows 10",
            "role": "poste client Utilisateur",
            "ip": "10.132.153.182",
            "ports": [
                {"numero": 3389,"service": "RDP"}
                ],
            },
        {"nom": "Machine Kali",
         "role": "poste d'analyse reseau",
         "ip": "10.132.153.71",
         "ports": [],
         },
        ]

DOSSIER_RAPPORTS = Path("rapports")

def ping_machine(ip: str) -> bool:
     
     systeme = platform.system().lower()

     if systeme == "windows":
         commande = ["ping", "-n", "2", "-w", "1000", ip]
     else:
         commande = ["ping", "-c", "2", "-W", "1", ip]


         try:
             resultat = subprocess.run(
                     commande,
                     stdout=subprocess.DEVNULL,
                     stderr=subprocess.SEVNULL
                     )
             return resultat.runcode == 0
         except Exceptiom:
             return False

def verifier_port(ip: str, port: int, timeout: int = 2) -> bool:

     try:
         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connexion:
             connexion.settimeout(timeout)
             resultat = connexion.connect_ex((ip, port))
             return resultat == 0
     except Exception:
             return False


def generer_rapport_csv(resultat: list) -> Path:

    DOSSIER_RAPPORTS.mkdir(exist_ok=True)

    date_fichier = datetime.now().strftime("%y%m%d_%H%M%S")
    chemin_rapport = DOSSIER_RAPPORT /f"rapport_scan_{date_fichier}.csv"

    with open(chemin_rapport, "w", newline="", encoding="utf-8") as fichier :
        writer = csv.writer(fichier)

        writer.writerow([
            "date",
            "Machine",
            "role",
            "Adresse ip",
            "ping",
            "port",
            "service",
            "Etat du port",
            ])

        writer.writerow(resultats)

        return chemin_rapport


def afficher_entete(date_scan: str) -> None:

    print("=" * 75)
    print("SCANNER D'AUTOMATISATION RESEAU - LAB IT")
    print("=" * 75)
    print(f"date du scan : {date_scan}")
    print("-" * 75)



def main() ->None:

    resultat = []
    date_scan = datetime.now.strftime("%Y-%m-%d %H:%M:%S")

    total_machine = len(MACHINES)
    machines_accessibles = 0
    ports_testes = 0
    ports_ouverts = 0

    afficher_entete(date_scan)

    for machine in MACHINES:
        nom = machine["nom"]
        role =  machine["role"]
        ip = machine["ip"]
        ports = machine["ports"]

        ping_ok = ping_machine(ip)
        statut_ping = "ok" if ping_ok else "KO"

        if ping_ok:
            machine_accessible += 1

        print(f"\nMachine : {nom}")
        print(f"Role      : {role}")
        print(f"IP        : {ip}")
        print(f"Ping      : {statut_ping}")

        if ports:
            for port in ports:
                numero_port = port["numero"]
                service = port["service"]
                port_testes += 1

                port_ok = verifier_port(ip, numero_port)
                Tatut_port = "OUVERT" if port_ok else "FERMER"

                if port_ok:
                    ports_ouvert += 1

                print(f"Port {numero_port} ({service}) : {statut_port}")

                resultats.append([
                    date_scan,
                    nom,
                    role,
                    ip,
                    statut_ping,
                    numero_port,
                    service,statut_port
                    ])
            else:
                print("Port    : Aucun port specifique tester")

                resultats.append([
                    date_scan,
                    nom,
                    role,
                    ip,
                    statut_ping,
                    "Aucun",
                    "non defini"
                    "non tester"
                    ])

                chemin_rapport = generer_rapport_csv(resultats)

                print("\n" + "=" * 75)
                print(" RESUMER DU SCAN")
                print("=" * 75)
                print(f"machines testees       : {total_machines}")
                print(f"Machines accessibles   : {machines_accessibles}/{total_machines}")
                print(f"Ports tester           : {ports_testes}")
                print(f"ports ouverts detectes : {ports_ouverts}")
                print(f"Rapport generer        : {chemin_rapport}")
                print("=" * 75)


            if __name__ == "__main__":
                main()



