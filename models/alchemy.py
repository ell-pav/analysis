from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy import DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
# Définir les classes ORM pour chaque


class Region(Base):
    __tablename__ = 'region'

    id_region = Column(Integer, primary_key=True)
    region_name = Column(String(50), nullable=False)

    # Relation avec la table Patient
    patients = relationship('Patient', back_populates='region')


class Sex(Base):
    __tablename__ = 'sex'

    id_sex = Column(Integer, primary_key=True)
    sex_label = Column(String(50), nullable=False)

    # Relation avec la table Patient
    patients = relationship('Patient', back_populates='sex')


class Smoker(Base):
    __tablename__ = 'smoker'

    id_smoker = Column(Integer, primary_key=True)
    is_smoker = Column(String(3), nullable=False)

    # Relation avec la table Patient
    patients = relationship('Patient', back_populates='smoker')


class UserRole(Base):
    __tablename__ = 'user_role'

    id_role = Column(Integer, primary_key=True)
    role_name = Column(String(50), nullable=False, unique=True)

    # Relation avec la table AppUser
    app_users = relationship('AppUser', back_populates='role')


class Patient(Base):
    __tablename__ = 'patient'

    id_patient = Column(Integer, primary_key=True)
    last_name = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    bmi = Column(DECIMAL(6, 3), nullable=False)
    patient_email = Column(String(50), nullable=False, unique=True)
    children = Column(Integer, nullable=False)
    charges = Column(DECIMAL(15, 5), nullable=False)

    id_smoker = Column(Integer, ForeignKey('smoker.id_smoker'), nullable=False)
    id_sex = Column(Integer, ForeignKey('sex.id_sex'), nullable=False)
    id_region = Column(Integer, ForeignKey('region.id_region'), nullable=False)

    # Relations avec les tables associées
    smoker = relationship('Smoker', back_populates='patients')
    sex = relationship('Sex', back_populates='patients')
    region = relationship('Region', back_populates='patients')


class AppUser(Base):
    __tablename__ = 'app_user'

    id_user = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    user_email = Column(String(50), nullable=False, unique=True)

    id_role = Column(Integer, ForeignKey('user_role.id_role'), nullable=False)

    # Relation avec la table UserRole
    role = relationship('UserRole', back_populates='app_users')


# Création de la base de données (SQLite pour cet exemple)
engine = create_engine('sqlite:///insurance.db', echo=True)

# Création des tables dans la base de données
Base.metadata.create_all(engine)

# Session pour interagir avec la base de données
Session = sessionmaker(bind=engine)
session = Session()

# Exemple d'ajout de données (optionnel)
# region = Region(region_name='Île-de-France')
# session.add(region)
# session.commit()

# Fermer la session
session.close()

print("Les tables ont été créées avec succès.")
