Voici le contenu simple, sans commentaires inutiles :

````md
# Script d'automatisation réseau

## Présentation

Ce projet est un script Python permettant d'automatiser l'analyse d'un réseau local.

Il permet de détecter les machines actives, d'analyser les ports ouverts et de générer un rapport au format CSV.

## Objectifs

- Scanner un réseau local
- Détecter les hôtes actifs
- Identifier les ports ouverts
- Générer un rapport CSV
- Organiser les résultats et les captures
- Documenter le projet sur GitHub

## Outils utilisés

- Kali Linux
- Python 3
- Nmap
- Git
- GitHub
- Ubuntu Server
- Windows 10 Client

## Structure du projet

```bash
script-automatisation-reseau/
├── captures/
│   ├── github/
│   ├── kali/
│   │   ├── environnement/
│   │   ├── execution-script/
│   │   └── resultats/
│   ├── ubuntu-server/
│   │   ├── ports/
│   │   └── ssh/
│   └── windows10-client/
│       ├── ports/
│       └── reseau/
├── rapports/
├── scripts/
│   └── scanner_reseau.py
├── scanner_reseau.py
└── README.md
````

## Fonctionnalités

* Scan du réseau local
* Détection des machines connectées
* Scan des ports ouverts
* Affichage des résultats dans le terminal
* Génération automatique d'un rapport CSV
* Sauvegarde des résultats dans le dossier `rapports`

## Installation

Cloner le dépôt :

```bash
git clone https://github.com/ASO2-Owess/script-automatisation-reseau.git
```

Entrer dans le dossier :

```bash
cd script-automatisation-reseau
```

Vérifier Python :

```bash
python3 --version
```

Vérifier Nmap :

```bash
nmap --version
```

Installer Nmap si nécessaire :

```bash
sudo apt update
sudo apt install nmap -y
```

## Utilisation

Lancer le script principal :

```bash
python3 scanner_reseau.py
```

Ou lancer le script depuis le dossier `scripts` :

```bash
python3 scripts/scanner_reseau.py
```

## Commandes utiles

Afficher l'adresse IP :

```bash
ip addr
```

Afficher la route réseau :

```bash
ip route
```

Scanner le réseau local :

```bash
sudo nmap -sn 10.132.153.0/24
```

Scanner les ports d'une machine :

```bash
nmap -sV adresse_ip
```

Exemple :

```bash
nmap -sV 10.132.153.104
```

## Rapports

Les rapports générés sont enregistrés dans le dossier :

```bash
rapports/
```

Afficher un rapport :

```bash
cat rapports/nom_du_rapport.csv
```

## Captures

Les captures sont organisées dans le dossier :

```bash
captures/
```

Organisation :

```bash
captures/github/
captures/kali/environnement/
captures/kali/execution-script/
captures/kali/resultats/
captures/ubuntu-server/ssh/
captures/ubuntu-server/ports/
captures/windows10-client/reseau/
captures/windows10-client/ports/
```

## Mise à jour GitHub

Ajouter les fichiers modifiés :

```bash
git add .
```

Créer un commit :

```bash
git commit -m "Mise à jour du projet"
```

Envoyer sur GitHub :

```bash
git push origin main
```

## Résultat attendu

À la fin du projet, on obtient :

* un script Python fonctionnel
* des rapports CSV générés automatiquement
* des captures d'écran organisées
* un dépôt GitHub propre
* une documentation claire du projet

## Auteur

Projet réalisé par : AKPA Salomon Owess

GitHub : ASO2-Owess

## Remarque

Ce projet est réalisé dans un cadre d'apprentissage et de test.

Il ne doit être utilisé que sur un réseau autorisé.

# script-automatisation-reseau
Script Python de vérification automatique des machines réseau
