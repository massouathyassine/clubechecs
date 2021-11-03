# Application d'échecs

Cette application de tournois d'échecs est une application en console pour gérer les joueurs et les tournois basée sur le système Suisse.

## Installation

1. Installer [Python 3](https://www.python.org/downloads/).

2. Créer un enverenement virtual en utilisant la commande suivante

```bash
python3 -m venv venv
```
3. Activer l'enveirenement virtual en utilisant la commande suivante 

```bash
source venv/bin/activate
```

4. Télécharger le programme via GitHub avec la commande ci-dessous ou en téléchargeant [l'archive](https://github.com/massouathyassine/clubechecs.git).
```bash
git clone https://github.com/massouathyassine/clubechecs.git
```

5. installer les modules via la commande:
```cmd
pip install -r requirements.txt
```

## Utilisation

Utiliser la commande ci-dessous pour lancer l'application.

```cmd
py main.py
```
## Génération de rapport Flake8

Utiliser la commande ci-dessous pour générer un rapport Flake8.
```cmd
flake8 views models controllers --format=html --htmldir=flake-report

```


