import sqlalchemy as sql
import database as db

class Pagamento(db.Base):
    __tablename__ = "pagamentos"
    id = sql.Column(sql.Integer, primary_key=True, index=True)
    email = sql.Column(sql.String)
    nome = sql.Column(sql.String)
    CPF = sql.Column(sql.String)
    valor = sql.Column(sql.Integer)
    forma_de_pagamento = sql.Column(sql.String)
    boleto = sql.Column(sql.String)
    nome_cartao = sql.Column(sql.String)
    numero_cartao = sql.Column(sql.String)
    bandeira_cartao = sql.Column(sql.String)
    validade = sql.Column(sql.String)
    codigo_CVV = sql.Column(sql.Integer)
    Pago = sql.Column(sql.String)