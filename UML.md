# Diagramme UML — Portfolio Tracker

```mermaid
classDiagram

    class Sujet {
        <<interface>>
        - _observateurs : list
        + abonner(obs)
        + desabonner(obs)
        + notifier()
        + get_donnees() dict
    }

    class Portfolio {
        - _titres : dict
        - _prix_actuels : dict
        + ajouter_titre()
        + retirer_titre()
        + modifier_titre()
        + mettre_a_jour_prix()
        + calculer_valeur_totale()
        + get_donnees() dict
    }

    Sujet <|.. Portfolio : implémente


    class Observateur {
        <<interface>>
        + actualiser(sujet)
    }


    Portfolio ..> Observateur : notifie


    class AffichagePrix {
        + actualiser(sujet)
    }

    class AffichagePortfolio {
        + actualiser(sujet)
    }

    class AlertePrix {
        + actualiser(sujet)
    }

    class LoggerCSV {
        + actualiser(sujet)
    }


    Observateur <|.. AffichagePrix : implémente
    Observateur <|.. AffichagePortfolio : implémente
    Observateur <|.. AlertePrix : implémente
    Observateur <|.. LoggerCSV : implémente

