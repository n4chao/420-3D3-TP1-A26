import tkinter as tk
from views.action_titres import ActionsTitres

class GestionTitres:

    def __init__(self, parent, portfolio, affichage_prix):
        self._portfolio = portfolio
        self._frame = tk.LabelFrame(parent, text="Gérer les titres", padx=10, pady=10)
        self._frame.pack(fill=tk.X, padx=10, pady=5)

        # Ligne 1 : formulaire d'ajout
        ligne_ajout = tk.Frame(self._frame)
        ligne_ajout.pack(fill=tk.X)
        self.entry_ticker = self._champ(ligne_ajout, "Ticker", 8)
        self.entry_quantite = self._champ(ligne_ajout, "Qté", 5, "1")
        self.entry_seuil_bas_ajout = self._champ(ligne_ajout, "Alerte basse", 7)
        self.entry_seuil_haut_ajout = self._champ(ligne_ajout, "Alerte haute", 7)

        self._actions = ActionsTitres(self, portfolio, affichage_prix)
        tk.Button(ligne_ajout, text="Ajouter", command=self._actions.ajouter).pack(side=tk.LEFT)

        tk.Label(
            self._frame,
            text="(Alertes optionnelles : si vides, calculées à ±20% du prix actuel)",
            font=("Segoe UI", 8), fg="gray"
        ).pack(anchor="w", pady=(2, 5))

        # Ligne 2 : liste + retrait
        ligne_liste = tk.Frame(self._frame)
        ligne_liste.pack(fill=tk.X)
        self.listbox_titres = tk.Listbox(ligne_liste, height=4, exportselection=False)
        self.listbox_titres.pack(side=tk.LEFT, fill=tk.X, expand=True)
        tk.Button(ligne_liste, text="Retirer", command=self._actions.retirer).pack(
            side=tk.LEFT, padx=(5, 0), anchor="n"
        )

        # Ligne 3 : modification
        ligne_modif = tk.Frame(self._frame)
        ligne_modif.pack(fill=tk.X, pady=(8, 0))
        tk.Label(ligne_modif, text="Sélection →").pack(side=tk.LEFT)
        self.entry_nouvelle_quantite = self._champ(ligne_modif, "Qté", 5)
        self.entry_nouveau_seuil_bas = self._champ(ligne_modif, "Alerte basse", 7)
        self.entry_nouveau_seuil_haut = self._champ(ligne_modif, "Alerte haute", 7)
        tk.Button(ligne_modif, text="Modifier sélection", command=self._actions.modifier).pack(side=tk.LEFT)

        self.label_statut_titres = tk.Label(self._frame, text="", font=("Segoe UI", 9), fg="gray")
        self.label_statut_titres.pack(anchor="w", pady=(5, 0))

        self._remplir_liste()

    def _champ(self, parent, texte, width, valeur_defaut=""):
        tk.Label(parent, text=f"{texte}:").pack(side=tk.LEFT)
        entry = tk.Entry(parent, width=width)
        if valeur_defaut:
            entry.insert(0, valeur_defaut)
        entry.pack(side=tk.LEFT, padx=(2, 8))
        return entry

    def _remplir_liste(self):
        self.listbox_titres.delete(0, tk.END)
        for ticker in self._portfolio.obtenir_titres():
            self.listbox_titres.insert(tk.END, self._texte_listbox(ticker))

    def _texte_listbox(self, ticker):
        titre = self._portfolio.obtenir_titres()[ticker]
        return (
            f"{ticker} — {titre.quantite} action(s) "
            f"(alerte : {titre.seuil_bas:.2f} $ / {titre.seuil_haut:.2f} $)"
        )

    def rafraichir_liste(self):
        selection = self.listbox_titres.curselection()
        index = selection[0] if selection else None
        self._remplir_liste()
        if index is not None and index < self.listbox_titres.size():
            self.listbox_titres.selection_set(index)

    def ticker_selectionne(self):
        selection = self.listbox_titres.curselection()
        if not selection:
            return None
        index = selection[0]
        texte = self.listbox_titres.get(index)
        return index, texte.split(" — ")[0]

    def statut(self, texte, couleur):
        self.label_statut_titres.config(text=texte, fg=couleur)
