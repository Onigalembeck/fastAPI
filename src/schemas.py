import pydantic as pydantic

class PagamentoBase(pydantic.BaseModel):
    email: str
    nome: str
    CPF: str
    valor : int
    forma_de_pagamento : str
    nome_cartao : str
    validade : str
    numero_cartao : str
    codigo_CVV: int
    class Config:
        orm_mode = True

class PagamentoSituação(pydantic.BaseModel):
    Pago : str
    class Config:
        orm_mode = True

class Pagamentos(PagamentoBase):
    Pago: str
    id: int
    boleto : str
    bandeira_cartao : str
    class Config:
        orm_mode = True