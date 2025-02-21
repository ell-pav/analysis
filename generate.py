import pandas as pd
from faker import Faker

# Charger la data
df = pd.read_csv('data/insurance.csv')

# Créer une instance de Faker
fake = Faker()

# Fonction pour générer un nom, un prénom et un email
def generate_fake_data():
    nom = fake.last_name()      # Nom de famille
    prenom = fake.first_name()  # Prénom
    email = fake.email()        # Email
    return pd.Series([nom, prenom, email])

# Appliquer la fonction pour générer les colonnes
df[['Nom', 'Prénom', 'Email']] = df.apply(lambda row: generate_fake_data(), axis=1)

# Sauvegarder le nouveau dataset avec les colonnes ajoutées
df.to_csv('data/insurance_fake.csv', index=False)

# Afficher un aperçu du résultat
print(df.head())