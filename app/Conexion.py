import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

# Asegúrate de configurar esta variable de entorno en el entorno de Render o donde estés desplegando tu aplicación
DATABASE_URL = os.getenv("DATABASE_URL", "mysql://u90tcvps80ln32im:IE6lHiP3qACiQ0buKfNg@bbdqxdh6h22vemwb2whz-mysql.services.clever-cloud.com:3306/bbdqxdh6h22vemwb2whz")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
