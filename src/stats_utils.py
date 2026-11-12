import numpy as np

def analyser_ventes(transactions):
    ventes= np.array(transactions, dtype=float)
    ventes = ventes[ventes > 0]

    if len(ventes) ==0:
        return None
    nombre = len(ventes)
    somme = np.sum(ventes)
    moyenne = np.mean(ventes)
    mediane = np.median(ventes)
    ecart_type = np.std(ventes)
    maximum = np.max(ventes)
    minimum = np.min(ventes)

    outliers = ventes[ventes > 2 * moyenne]

    return {
        "nombre_transactions": nombre,
        "somme_totale": round(float(somme), 2),
        "moyenne": round(float(moyenne), 2),
        "mediane": round(float(mediane), 2),
        "ecart_type": round(float(ecart_type), 2),
        "maximum": float(maximum),
        "minimum": float(minimum),
        "outliers": outliers.tolist(),
    }

ventes_test = [150, 200, -50, 0, 320, 180, 95, 2500, 210, 175]
resultats = analyser_ventes(ventes_test)
print("===RAPPORT STATISTIQUE DE SVENTES ===")
for indicateur, valeur in resultats.items():
    print(f"{indicateur} : {valeur}")