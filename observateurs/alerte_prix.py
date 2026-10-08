import tkinter as tk
from observateurs.observateur import Observateur

class AlertePrix(Observateur):

    def __init__(self, parent):
        frame = tk.LabelFrame(parent, text="Alertes", padx=10, pady=10)
        frame.pack(fill=tk.X, padx=10, pady=5)
        self._label = tk.Label(frame, text="Aucune alerte", fg="gray", justify=tk.LEFT, wraplength=380)
        self._label.pack(anchor="w")

    def actualiser(self, sujet):
        donnees = sujet.get_donnees()
        alertes = []
        for ticker in donnees:
            prix = donnees[ticker]["prix"]
            bas = donnees[ticker]["seuil_bas"]
            haut = donnees[ticker]["seuil_haut"]
            if prix is not None:
                if prix >= haut:
                    alertes.append(f"⚠️ {ticker} dépasse le seuil haut ({prix:.2f} $ ≥ {haut:.2f} $)")
                elif prix <= bas:
                    alertes.append(f"⚠️ {ticker} sous le seuil bas ({prix:.2f} $ ≤ {bas:.2f} $)")

        if alertes:
            self._label.config(text="\n".join(alertes), fg="red")
        else:
            self._label.config(text="Aucune alerte", fg="gray")