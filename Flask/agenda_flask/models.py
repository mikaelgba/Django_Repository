from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Pessoas(Base):
    __tablename__ = 'pessoa'
    id = Column(Integer, primary_key = True)
    nome = Column(String(60), index=True)
    idade = Column(Integer)

    def __repr__ (self):
        return '<Pessoa {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key = True)
    nome = Column(String(120), index=True)
    pessoa_id = Column(Integer, ForeignKey('pessoa.id'))
    pessoa = relationship('Pessoas')

    def __repr__ (self):
        return '<Atividade {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

def start_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    start_db()