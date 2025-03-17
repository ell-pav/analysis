import sqlite3
import csv

# Nom de la base de données SQLite
db_name = 'insurance_sql.db'

# Nom du fichier CSV
csv_file = 'data/insurance_fake.csv'

# Créer une connexion à la base de données SQLite
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Lecture du fichier CSV
with open(csv_file, newline='', encoding='utf-8') as f:
    reader = csv.reader(f)

    # Lire la première ligne pour récupérer les en-têtes (les noms de colonnes)
    headers = next(reader)

    # Créer une table avec les noms de colonnes extraits du CSV
    create_table_query = (
                        f"CREATE TABLE IF NOT EXISTS ma_table ("
                        f"{','.join([header + ' TEXT' for header in headers])}"
                        f");"
                        )
    cursor.execute(create_table_query)

    # Insérer les lignes du CSV dans la base de données
    for row in reader:
        insert_query = (
            f"INSERT INTO ma_table ({', '.join(headers)}) "
            f"VALUES ({', '.join(['?' for _ in headers])});"
        )
    cursor.execute(insert_query, row)

# Sauvegarder les changements
conn.commit()

# Fermer la connexion à la base de données
conn.close()

print("Les données ont été insérées dans la base de données SQLite")
