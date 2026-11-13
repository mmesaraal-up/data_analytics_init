

"""Module d'analyse statistique des ventes."""

import math


def analyser_ventes(transactions):
    """Analyse une liste de montants de ventes (en euros).

    - Ignore les valeurs négatives ou nulles (erreurs de saisie).
    - Calcule nombre, somme, moyenne, médiane, écart-type, min et max.
    - Détecte les anomalies : transactions > 2 fois la moyenne.

    Retourne un dictionnaire d'indicateurs.
    """
    
    valides = [t for t in transactions if t > 0]

    if not valides:
        return {
            "nombre_transactions": 0,
            "somme_totale": 0,
            "moyenne": None,
            "mediane": None,
            "ecart_type": None,
            "minimum": None,
            "maximum": None,
            "seuil_anomalie": None,
            "anomalies": [],
        }

    
    n = len(valides)
    somme = sum(valides)
    moyenne = somme / n

    triees = sorted(valides)
    milieu = n // 2
    if n % 2 == 1:
        mediane = triees[milieu]
    else:
        mediane = (triees[milieu - 1] + triees[milieu]) / 2

    variance = sum((x - moyenne) ** 2 for x in valides) / n
    ecart_type = math.sqrt(variance)

    
    seuil = 2 * moyenne
    anomalies = [t for t in valides if t > seuil]

   
    return {
        "nombre_transactions": n,
        "somme_totale": somme,
        "moyenne": moyenne,
        "mediane": mediane,
        "ecart_type": ecart_type,
        "minimum": min(valides),
        "maximum": max(valides),
        "seuil_anomalie": seuil,
        "anomalies": anomalies,
    }


if __name__ == "__main__":
    
    ventes_test = [150, 200, 175, -50, 0, 220, 180, 195, 210, 2500, 165]

    resultats = analyser_ventes(ventes_test)

    print("=" * 40)
    print("     RAPPORT STATISTIQUE DES VENTES")
    print("=" * 40)
    print(f"Transactions valides : {resultats['nombre_transactions']}")
    print(f"Somme totale         : {resultats['somme_totale']:.2f} €")
    print(f"Moyenne              : {resultats['moyenne']:.2f} €")
    print(f"Médiane              : {resultats['mediane']:.2f} €")
    print(f"Écart-type           : {resultats['ecart_type']:.2f} €")
    print(f"Minimum              : {resultats['minimum']:.2f} €")
    print(f"Maximum              : {resultats['maximum']:.2f} €")
    print(f"Seuil d'anomalie     : {resultats['seuil_anomalie']:.2f} €")
    print(f"Anomalies détectées  : {resultats['anomalies']}")
    print("=" * 40)