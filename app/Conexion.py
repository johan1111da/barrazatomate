import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Asegúrate de configurar esta variable de entorno en el entorno de Render o donde estés desplegando tu aplicación
DATABASE_URL = os.getenv("DATABASE_URL", "mysql://uzononyj9ilm10zt:KsNqXc83TPaI4QHIQkLl@b87dlp04louefhdei4wx-mysql.services.clever-cloud.com:3306/b87dlp04louefhdei4wx")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
