# DecisionTreeAPI

## Cloner le repo
Git clone https://github.com/VinceBro/DecisionTreeAPI.git

## installer les librairies
pip install flask flask-restful sklearn joblib pandas

## trouver votre adresse ip locale pour l'api flask

ouvrir un terminal (ligne de commande)

lancer la commande "ipconfig"
trouver l'adresse IPv4 ressemblant à 192.168.x.xxx

écrire cette adresse dans le code python api.py à la ligne 26

écrire cette adresse dans le code VBA, module 1 à la ligne 38 (URL = "http://192.168.x.xxx:5000/send")

## Lancer l'application
ouvrir une ligne de commande dans le dossier du projet et lancer l'API flask avec la ligne "python api.py"
