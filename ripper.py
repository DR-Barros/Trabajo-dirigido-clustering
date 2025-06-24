import wittgenstein as lw
import pandas as pd
import numpy as np

class MultiClassRipperClassifier:
    def __init__(self, random_state=42):
        self.random_state = random_state
        self.models = {}
        self.classes_ = []

    def fit(self, X, Y):
        """
        Entrena un modelo RIPPER por clase usando estrategia one-vs-rest.
        """
        self.classes_ = np.unique(Y)
        for cls in self.classes_:
            # Crear etiqueta binaria para esta clase vs el resto
            df_copy = X.copy()
            df_copy['class'] = (Y == cls).astype(int)
            model = lw.RIPPER(random_state=self.random_state)
            model.fit(df_copy, class_feat='class')
            self.models[cls] = model

    def predict(self, X):
        """
        Predice la clase con mayor confianza para cada muestra.
        """
        scores = {}
        for cls, model in self.models.items():
            probas = model.predict_proba(X)
            scores[cls] = [p[1] for p in probas] 

        df_scores = pd.DataFrame(scores)
        return df_scores.idxmax(axis=1).values  

    def predict_with_reasons(self, X):
        """
        Devuelve la clase predicha y la regla que se activó (si hay) por muestra.
        """
        reasons_all = {}
        scores = {}
        for cls, model in self.models.items():
            pred, reasons = model.predict(X, give_reasons=True)
            scores[cls] = [1 if p else 0 for p in pred]
            reasons_all[cls] = reasons

        df_scores = pd.DataFrame(scores)
        best_classes = df_scores.idxmax(axis=1).values

        selected_reasons = []
        for i, cls in enumerate(best_classes):
            rule = reasons_all[cls][i] if reasons_all[cls][i] else None
            selected_reasons.append(rule)

        return best_classes, selected_reasons

    def get_rules(self):
        """
        Devuelve las reglas de cada clase como diccionario.
        """
        rules_by_class = {}
        for cls, model in self.models.items():
            rules_by_class[cls] = model.ruleset_
        return rules_by_class

    def print_rules(self):
        """
        Imprime las reglas por clase.
        """
        for cls, model in self.models.items():
            print(f"\nReglas para clase: {cls}")
            print(model.ruleset_)
