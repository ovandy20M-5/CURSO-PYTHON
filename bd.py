from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import column, String, Integer, create_engine, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property


Base = declarative_base()

class Alumno(Base):
    __tablename__ = 'alumnos'

    id = column(Integer, primary_key=True)
    nombres = column(String, nullabe=False)
    apellidos = column(String, nullabe=False)
    carnet = column(Integer)
    notas = relationship('nota', back_populates='alumno')

    @hybrid_property
    def nombre_completo(self):
        return f'{self.nombres} {self.apellidos}

class Nota(Base):
    __tablename__ = 'notas'
    id = column(Integer, primary_key=True)
    curso = column(String)
    nota = column(Integer)
    alumno_id = column(Integer, ForeignKey('alumnos.Id'))
    alumno = relationship('Alumno',back_populares='notas')


engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(engine)

session = sessionmaker(bind=engine)
session = session()

lucia = Alumno(
    nombres = 'Lucia',
    apellidos = 'Gomez',
    carnet = 5432
)

print(lucia.id)
session.add(lucia)
session.commit()
session.refresh(lucia)
print(lucia.id)

lucia_from_db =session.query(Alumno).where(Alumno.nombres=='Lucia').first()
print(lucia_from_db)
print(lucia_from_db.apellidos)

lucia_from_db.carnet = 5432
session.add(lucia_from_db)
session.commit()

luis = Alumno(
    nombres = 'Luis',
    apellidos = 'perez',
    carnet = 5555
)

session.add(luis)
session.commit()

alumnos = session.query(Alumno).all()

print(alumnos[0].nombres)
print(alumnos[1].nombres)

print(luis.nombre_completo)

nota = Nota(
    curso = 'matematicas',
    nota = 90,
    alumno_id = luis.id
)

session.add(nota)
session.commit()

session.refresh(nota)
print(nota.alumno.nombres)
session.refresh(luis)
print(luis.notas[0].curso)
print(nota.alumno.notas[0].alumno.nombre_completo)

session.refresh(nota)
print(nota.alumno.nombres)
session.refresh(luis)
print(luis.notas[0].nota)
print(nota.alumno.notas[0].alumno.nombre_completo)
