from app.db.session import SessionLocal
from sqlalchemy import text
from sqlalchemy.orm import Session
from app.models.usuario import Usuario

# Inicializar base de datos (crear tablas)
def run_seed():
    db: Session = SessionLocal()
    
    try:
        if db.query(Usuario).first():
            return
        
        with open("inserts_prueba.sql", "r", encoding="utf-8") as f:
            sql_statements = f.read().split(";")
            
            for statement in sql_statements:
                stmt = statement.strip()
                if stmt:
                    db.execute(text(stmt))
        
        db.commit()
    
    except Exception as e:
        db.rollback()
        print("Error en seed:", e)
    
    finally:
        db.close()
