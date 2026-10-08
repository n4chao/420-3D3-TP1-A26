from modeles.titre import Titre

class ActionsTitres:

    def __init__(self, vue, portfolio, affichage_prix):
        self._vue = vue
        self._portfolio = portfolio
        self._affichage_prix = affichage_prix

    def ajouter(self):
        ticker = self._vue.entry_ticker.get().strip().upper()
        if not ticker:
            return

        try:
            quantite = int(self._vue.entry_quantite.get().strip())
            if quantite <= 0:
                raise ValueError
        except ValueError:
            self._vue.statut("La quantité doit être un nombre entier positif.", "red")
            return

        texte_bas = self._vue.entry_seuil_bas_ajout.get().strip()
        texte_haut = self._vue.entry_seuil_haut_ajout.get().strip()
        try:
            seuil_bas = float(texte_bas) if texte_bas else None
            seuil_haut = float(texte_haut) if texte_haut else None
            if seuil_bas is not None and seuil_bas <= 0:
                raise ValueError
            if seuil_haut is not None and seuil_haut <= 0:
                raise ValueError
            if seuil_bas is not None and seuil_haut is not None and seuil_bas >= seuil_haut:
                self._vue.statut("L'alerte basse doit être inférieure à l'alerte haute.", "red")
                return
        except ValueError:
            self._vue.statut("Les alertes doivent être des nombres positifs.", "red")
            return

        try:
            prix = self._portfolio._strategie.recuperer_prix(ticker)
        except Exception:
            self._vue.statut(f"Le titre '{ticker}' n'existe pas.", "red")
            return

        if seuil_bas is None:
            seuil_bas = prix["prix"] * 0.8
        if seuil_haut is None:
            seuil_haut = prix["prix"] * 1.2

        try:
            self._portfolio.ajouter(Titre(
                ticker, quantite, round(seuil_bas, 2), round(seuil_haut, 2)
            ))
        except ValueError as e:
            self._vue.statut(str(e), "orange")
            return

        self._vue.rafraichir_liste()
        self._vider_ajout()
        self._affichage_prix.ajouter_ligne(ticker, prix["prix"], prix["ouverture"])
        self._vue.statut(f"{ticker} ajouté au portfolio ({quantite} action(s)).", "green")

    def retirer(self):
        selection = self._vue.ticker_selectionne()
        if selection is None:
            self._vue.statut("Sélectionnez un titre à retirer.", "orange")
            return

        index, ticker = selection
        self._portfolio.retirer(ticker)
        self._vue.rafraichir_liste()
        self._affichage_prix.retirer_ligne(ticker)
        self._vue.statut(f"{ticker} retiré du portfolio.", "gray")

    def modifier(self):
        selection = self._vue.ticker_selectionne()
        if selection is None:
            self._vue.statut("Sélectionnez un titre à modifier.", "orange")
            return

        index, ticker = selection
        qte = self._vue.entry_nouvelle_quantite.get().strip()
        bas = self._vue.entry_nouveau_seuil_bas.get().strip()
        haut = self._vue.entry_nouveau_seuil_haut.get().strip()

        if not qte and not bas and not haut:
            self._vue.statut("Entrez une nouvelle quantité et/ou de nouvelles alertes.", "orange")
            return

        try:
            quantite = int(qte) if qte else None
            if quantite is not None and quantite <= 0:
                raise ValueError
            seuil_bas = float(bas) if bas else None
            seuil_haut = float(haut) if haut else None
            if seuil_bas is not None and seuil_bas <= 0:
                raise ValueError
            if seuil_haut is not None and seuil_haut <= 0:
                raise ValueError
            if (seuil_bas is None) != (seuil_haut is None):
                self._vue.statut("Les deux alertes doivent être fournies ensemble.", "red")
                return
            if seuil_bas is not None and seuil_bas >= seuil_haut:
                self._vue.statut("L'alerte basse doit être inférieure à l'alerte haute.", "red")
                return
        except ValueError:
            self._vue.statut("La quantité et les alertes doivent être des nombres positifs.", "red")
            return

        self._portfolio.modifier(ticker, quantite, seuil_bas, seuil_haut)
        self._vue.rafraichir_liste()
        self._vider_modification()
        self._vue.statut(f"{ticker} mis à jour.", "green")

    def _vider_ajout(self):
        self._vue.entry_ticker.delete(0, 'end')
        self._vue.entry_quantite.delete(0, 'end')
        self._vue.entry_quantite.insert(0, '1')
        self._vue.entry_seuil_bas_ajout.delete(0, 'end')
        self._vue.entry_seuil_haut_ajout.delete(0, 'end')

    def _vider_modification(self):
        self._vue.entry_nouvelle_quantite.delete(0, 'end')
        self._vue.entry_nouveau_seuil_bas.delete(0, 'end')
        self._vue.entry_nouveau_seuil_haut.delete(0, 'end')
