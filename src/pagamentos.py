from typing import List
import fastapi as fastapi
import sqlalchemy.orm as orm
import services as serv, schemas as sch
import cartao_valido

app = fastapi.FastAPI(title="Pagamentos")  

serv.create_database()

@app.get("/")
def read_root():
    return {"Bem vindo": "Para acessar o site principal, vá na barra de endereço e adicione '/docs' e aperte enter"}

@app.post("/pagamentos/", response_model=sch.Pagamentos)
def Adicionar_pagamento(pagamento: sch.PagamentoBase, db: orm.Session = fastapi.Depends(serv.get_db)):
    if pagamento.forma_de_pagamento == "boleto":
        return serv.create_boleto(db=db, pagamento= pagamento)
    elif pagamento.forma_de_pagamento =="cartao":
        if cartao_valido.check_bandeira_cartao(pagamento.numero_cartao) == "NAO VALIDO":
            return serv.validation_cartao_nao_pago(db=db, pagamento= pagamento)
        else:
            if cartao_valido.check_validade_cartao(pagamento.validade) == "fora da validade":
                return serv.validation_cartao_nao_pago(db=db, pagamento= pagamento)
            else:
                if pagamento.codigo_CVV == 123:
                    return serv.validation_cartao_pago(db=db, pagamento= pagamento)
                else:
                    return serv.validation_cartao_nao_pago(db=db, pagamento= pagamento)
    else:
        raise fastapi.HTTPException(status_code=404, detail="Desculpe, mas este método de pagamento não existe!")

@app.get("/pagamentos/", response_model=List[sch.Pagamentos])
def Todos_pagamentos(
    skip: int = 0,
    limit: int = 10,
    db: orm.Session = fastapi.Depends(serv.get_db),
):
    pagamentos = serv.get_pagamentos(db=db, skip=skip, limit=limit)
    return pagamentos

@app.get("/pagamentos/{pagamento_id}", response_model=sch.Pagamentos)
def Identificar_um_pagamento(pagamento_id: int, db: orm.Session = fastapi.Depends(serv.get_db)):
    db_pagamento = serv.get_pagamento(db=db, pagamento_id=pagamento_id)
    if db_pagamento is None:
        raise fastapi.HTTPException(
            status_code=404, detail="Desculpe, este pagamento não existe!"
        )
    return db_pagamento

@app.get("/pagamentos/{pagamento_id}/status_do_pagamento", response_model=sch.PagamentoSituação)
def Situação_do_pagamento(pagamento_id: int, db: orm.Session = fastapi.Depends(serv.get_db)):
    db_pagamento = serv.get_pagamento(db=db, pagamento_id=pagamento_id)
    if db_pagamento is None:
        raise fastapi.HTTPException(
            status_code=404, detail="Desculpe, este pagamento não existe!"
        )
    return db_pagamento