import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# строка подключения к базе данных берется из переменной окружения DATABASE_URL,
# чтобы не хранить учетные данные в коде
SQLALCHEMY_DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://user:password@localhost:5432/startml",
)

# создаем engine (прослойку sqlalchemy, которая уничтожает различия между базами данных)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# создаем сессию для подключения, забора данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# объявляем костяк, по которому сможем создавать классы создания таблиц
Base = declarative_base()
