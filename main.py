from modeles.portfolio import Portfolio
from modeles.titre import Titre
from strategies.prix_titre import PrixTitre
from views.dashboard import Dashboard
from views.action_titres import ActionsTitres

portfolio = Portfolio(PrixTitre())
portfolio.ajouter(Titre("AAPL", 10, 150.0, 200.0))
portfolio.ajouter(Titre("GOOGL", 5, 120.0, 160.0))
portfolio.ajouter(Titre("MSFT", 8, 380.0, 430.0))

app = Dashboard(portfolio)
app.mainloop()
