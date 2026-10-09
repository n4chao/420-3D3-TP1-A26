import tkinter as tk
from observateurs.observateur import Observateur


class AlertePrix(Observateur):

    def __init__(self, parent):
        frame = tk.LabelFrame(
            parent,
            text="Alertes",
            padx=10,
            pady=10
        )
        frame.pack(fill=tk.X, padx=10, pady=5)

        self._label = tk.Label(
            frame,
            text="Aucune alerte",
            fg="gray",
            justify=tk.LEFT,
            wraplength=380
        )
        self._label.pack(anchor="w")

    def actualiser(self, sujet):
        donnees = sujet.get_donnees()
        alertes = []

        for ticker in donnees:
            titre = donnees[ticker]

            prix = titre["prix"]
            bas = titre["seuil_bas"]
            haut = titre["seuil_haut"]

            if prix is not None:
                if prix >= haut:
                    alertes.append(
                        f"{ticker} dépasse le seuil haut "
                        f"({prix:.2f} $ >= {haut:.2f} $)"
                    )
                elif prix <= bas:
                    alertes.append(
                        f"{ticker} est sous le seuil bas "
                        f"({prix:.2f} $ <= {bas:.2f} $)"
                    )

        if alertes:
            self._label.config(
                text="\n".join(alertes),
                fg="red"
            )
        else:
            self._label.config(
                text="Aucune alerte",
                fg="gray"
            )

