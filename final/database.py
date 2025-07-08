from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

# объявляем строку для подлючения к базе данных, по сути создали переменную
SQLALCHEMY_DATABASE_URL = "postgresql://robot-startml-ro:pheiph0hahj1Vaif@postgres.lab.karpov.courses:6432/startml"

# создаем engine (прослойку sqlalchemy, которая уничтожает различия между базами данных)
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# создаем сессию для подключения, забора данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# объявляем костяк, по которому сможем создавать классы создания таблиц
Base = declarative_base()
