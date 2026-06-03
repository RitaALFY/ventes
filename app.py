import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

print('ventes-par-région.html généré avec succès !')

# Graphique 2 - Ventes par produit 
ventes_produit = données.groupby('produit')['qte'].sum().reset_index()
figure2 = px.pie(ventes_produit, values='qte', names='produit', title='Ventes par produit')
figure2.write_html('ventes-par-produit.html')

# Graphique 3 - Chiffre d'affaires par produit 
données['chiffre_affaires'] = données['prix'] * données['qte']
ca_produit = données.groupby('produit')['chiffre_affaires'].sum().reset_index()
figure3 = px.pie(ca_produit, values='chiffre_affaires', names='produit', title="Chiffre d'affaires par produit")
figure3.write_html('chiffre-affaires-par-produit.html')

print('Tous les fichiers ont été générés avec succès !')