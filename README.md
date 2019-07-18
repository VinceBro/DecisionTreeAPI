# DecisionTreeAPI

## Installation

### Cloner le repo
Git clone https://github.com/VinceBro/DecisionTreeAPI.git

### Installer les librairies
pip install flask flask-restful sklearn joblib pandas

### Trouver votre adresse ip locale pour la communication de l'api flask et Excel

ouvrir un terminal (ligne de commande)

lancer la commande "ipconfig"
trouver l'adresse IPv4 ressemblant à 192.168.x.xxx

écrire cette adresse dans le code python api.py à la ligne 26

écrire cette adresse dans le code VBA, module 1 à la ligne 38 (URL = "http://192.168.x.xxx:5000/send")

### Ajouter les références dans VBA

Outils -> Références ->

  Cocher "Microsoft Scripting Runtime"
  
  Cocher "Microsoft WinHTTP Services, version 5.1"
  
  Cocher "Microsoft Internet Controls"

### Lancer l'application
ouvrir une ligne de commande dans le dossier du projet et lancer l'API flask avec la ligne "python api.py"
