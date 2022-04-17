import sqlalchemy.orm as orm
import boleto
import cartao_valido
import models as models, schemas as sch, database as database

def create_database():
    return database.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_boleto(db: orm.Session, pagamento: sch.PagamentoBase):
    db_pagamento = models.Pagamento(email=pagamento.email, nome=pagamento.nome, CPF=pagamento.CPF, valor= pagamento.valor, 
    forma_de_pagamento=pagamento.forma_de_pagamento, boleto= boleto.gera_boleto(), nome_cartao= pagamento.nome_cartao, numero_cartao= pagamento.numero_cartao, bandeira_cartao = cartao_valido.check_bandeira_cartao(pagamento.numero_cartao),
    validade=pagamento.validade, codigo_CVV=pagamento.codigo_CVV, Pago = "Não efetuado")
    db.add(db_pagamento)
    db.commit()
    db.refresh(db_pagamento)
    return db_pagamento

def validation_cartao_pago(db: orm.Session, pagamento: sch.PagamentoBase):
    db_pagamento = models.Pagamento(email=pagamento.email, nome=pagamento.nome, CPF=pagamento.CPF, valor= pagamento.valor, 
    forma_de_pagamento=pagamento.forma_de_pagamento, boleto= "nenhum", nome_cartao= pagamento.nome_cartao, numero_cartao= pagamento.numero_cartao, bandeira_cartao = cartao_valido.check_bandeira_cartao(pagamento.numero_cartao),
    validade=pagamento.validade, codigo_CVV=pagamento.codigo_CVV, Pago = "Efetuado")
    db.add(db_pagamento)
    db.commit()
    db.refresh(db_pagamento)
    return db_pagamento

def validation_cartao_nao_pago(db: orm.Session, pagamento: sch.PagamentoBase):
    db_pagamento = models.Pagamento(email=pagamento.email, nome=pagamento.nome, CPF=pagamento.CPF, valor= pagamento.valor, 
    forma_de_pagamento=pagamento.forma_de_pagamento, boleto= "nenhum", nome_cartao= pagamento.nome_cartao, numero_cartao= pagamento.numero_cartao, bandeira_cartao = cartao_valido.check_bandeira_cartao(pagamento.numero_cartao),
    validade=pagamento.validade, codigo_CVV=pagamento.codigo_CVV, Pago = "Não efetuado")
    db.add(db_pagamento)
    db.commit()
    db.refresh(db_pagamento)
    return db_pagamento

def get_pagamento(db: orm.Session, pagamento_id:int):
    return db.query(models.Pagamento).filter(models.Pagamento.id == pagamento_id).first()

def get_pagamentos(db: orm.Session, skip: int = 0, limit: int = 10000):
    return db.query(models.Pagamento).offset(skip).limit(limit).all()
