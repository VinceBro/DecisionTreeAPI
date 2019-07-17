import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from joblib import dump, load
import pandas as pd


class AnimalDecisionTree(object):

    def __init__(self, trained=False):
        dataset = pd.read_csv("zoo.csv")
        self.dataset = dataset.drop("nom animal", axis=1)
        

        self.class_to_species = {
            1: "Mamifère",
            2: "Oiseau",
            3: "Reptile",
            4: "Poisson",
            5: "Amphibiens",
            6: "Insectes",
            7: "Crustacés"
        }


        self.features = self.dataset.drop("classe", axis=1)
        self.targets = self.dataset["classe"]

        self.train_features, self.test_features, self.train_targets, self.test_targets = train_test_split(
            self.features, self.targets, train_size=0.75)

        if trained:
            self.tree = load("tree.joblib")
        else:
            self.tree = DecisionTreeClassifier(
                criterion="entropy", max_depth=5)
            self.tree = self.tree.fit(self.train_features, self.train_targets)
            dump(self.tree, "tree.joblib")

            self.prediction = self.tree.predict(self.test_features)

            score = self.tree.score(self.test_features, self.test_targets)
            print(f"Prediction accuracy : {score * 100}")

    def predict(self, features):
        features = {key: (1 if value == "oui" else 0 if value=="non" else value)
                    for (key, value) in features.items()}
        features = pd.DataFrame(
            [features], columns=self.train_features.columns)
        prediction = self.tree.predict(features)[0]
        print(f"La prédiction est: {self.class_to_species[prediction]}")
        return self.class_to_species[prediction]


if __name__ == "__main__":
    test = AnimalDecisionTree(True)
    test.predict({
        "poil": "non",
        "plumes": "non",
        "oeufs": "oui",
        "lait": "non",
        "vole": "non",
        "aquatique": "non",
        "predateur": "non",
        "dents": "oui",
        "colonne": "oui",
        "respire": "non",
        "venimeux": "non",
        "nageoires": "oui",
        "jambes": "non",
        "queue": "oui",
        "domestique": "non",
        "gros": "oui"
    })
