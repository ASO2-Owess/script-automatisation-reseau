import csv
import socket
import subprocess
from datetime import datetime
from pathlib import Path

MACHINES = [
    {"nom": "Serveur Ubuntu", "role": "Serveur interne", "ip": "10.132.153.237", "ports": [{"numero": 22, "service": "SSH"}]},
    {"nom": "Poste Windows 10", "role": "Poste client", "ip": "10.132.153.182", "ports": [{"numero": 3389, "service": "RDP"}]},
    {"nom": "Machine Kali", "role": "Poste analyse", "ip": "10.132.153.71", "ports": []},
]

def ping_machine(ip):
    resultat = subprocess.run(
        ["ping", "-c", "2", "-W", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return resultat.returncode == 0

def verifier_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connexion:
            connexion.settimeout(2)
            return connexion.connect_ex((ip, port)) == 0
    except Exception:
        return False

def generer_rapport(resultats):
    dossier = Path("../rapports")
    dossier.mkdir(exist_ok=True)

    fichier = dossier / f"rapport_scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

    with open(fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "Machine", "Role", "IP", "Ping", "Port", "Service", "Etat"])
        writer.writerows(resultats)

    return fichier

def main():
    resultats = []
    date_scan = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    machines_accessibles = 0
    ports_testes = 0
    ports_ouverts = 0

    print("=" * 70)
    print("SCANNER D'AUTOMATISATION RESEAU — LAB IT")
    print("=" * 70)

    for machine in MACHINES:
        nom = machine["nom"]
        role = machine["role"]
        ip = machine["ip"]
        ports = machine["ports"]

        ping_ok = ping_machine(ip)
        statut_ping = "OK" if ping_ok else "KO"

        if ping_ok:
            machines_accessibles += 1

        print(f"\nMachine : {nom}")
        print(f"Role    : {role}")
        print(f"IP      : {ip}")
        print(f"Ping    : {statut_ping}")

        if ports:
            for port in ports:
                numero = port["numero"]
                service = port["service"]
                ports_testes += 1

                port_ok = verifier_port(ip, numero)
                statut_port = "OUVERT" if port_ok else "FERME"

                if port_ok:
                    ports_ouverts += 1

                print(f"Port {numero} ({service}) : {statut_port}")
                resultats.append([date_scan, nom, role, ip, statut_ping, numero, service, statut_port])
        else:
            print("Port    : Aucun port specifique teste")
            resultats.append([date_scan, nom, role, ip, statut_ping, "Aucun", "Non defini", "Non teste"])

    rapport = generer_rapport(resultats)

    print("\n" + "=" * 70)
    print("RESUME DU SCAN")
    print("=" * 70)
    print(f"Machines testees       : {len(MACHINES)}")
    print(f"Machines accessibles   : {machines_accessibles}/{len(MACHINES)}")
    print(f"Ports testes           : {ports_testes}")
    print(f"Ports ouverts detectes : {ports_ouverts}")
    print(f"Rapport genere         : {rapport}")
    print("=" * 70)

if __name__ == "__main__":
    main()
