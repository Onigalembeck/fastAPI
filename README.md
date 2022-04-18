# fastAPI
Projeto de pagamentos utilizando FastAPI e SQLAlchemy

## REQUERIMENTOS
`pip install typing fastapi sqlalchemy pydantic random datetime uvicorn`

EM SEGUIDA, PARA DAR INÍCIO AO API, ABRA O TERMINAL MUDE PARA O DIRETÓRIO ONDE O ARQUIVO pagamentos.py ESTÁ LOCALIZADO E RODE: 

`uvicorn pagamentos:app`

UM LINK SERÁ GERADO NO TERMINAL, CLIQUE NELE COM A TECLA "Ctrl" PRESSIONADA OU COPIE PARA A BARRA DE ENDERÇO. COM O SITE ABERTO, VÁ NA BARRA DE ENDEREÇO E ADICIONE "/docs" PARA ABRIR O SWAGGER.


AGORA DAREMOS INÍCIO AOS PROCEDIMENTOS:

* 1 - GET /pagamentos/ Todos Pagamentos: Aqui você pode ver os pagamentos realizados, clique na barra, no canto direito pressione "Try it out". Agora coloque o limite de intervalo de pagamentos que você deseja ver. Clique em execute e logo abaixo em Response body todos os pagamentos realizados serão apresentados.

* 2 - POST /pagamentos/ Adicionar Pagamento: Nesta área você adicionará os pagamentos e suas informações. Clique na barra, no canto direito pressione "Try it out". Um "Request body" será apresentado, é nele que você preencherá as informações.

 * "email": "string", aqui você deverá preencher entre as aspas com o seu email 
 * "nome": "string", aqui você deverá preencher entre as aspas com o seu nome
 * "CPF": "string", aqui você deverá preencher entre as aspas com o seu CPF
 * "valor": 0, aqui você deverá colocar o valor a ser pago entre os ":" e a ","
 * "forma_de_pagamento": "string", aqui você deverá escrever "boleto" ou cartao, qualquer coisa além disso não será considerado
 * "nome_cartao": "string", aqui você deverá preencher entre as aspas com o nome no cartão
 * "numero_cartao": "string", aqui você deverá preencher entre as aspas com o número do seu cartão, para identificar a bandeira criamos 3 tipos possível, Cartão1 que começa com 01, Cartão2 com 03 e Cartão3 com 09. Qualquer cartão além destes não realizará o pagamento
 * "validade": "string", aqui você deverá preencher entre as aspas da seguinte forma "01/01", com o mês e o ano. Caso o seu cartão esteja vencido, com ano abaixo de 22 ou mês abaixo de 4 no ano de 22, ele não efeturará o pagamento.
 * "codigo_CVV": 0 aqui você deverá preencher com o código do cartão depois dos ":" , para este caso coloquei que todo cartão com código 123 será validado e realizará a o pagamento, qualquer código além desse não considerará o pagamento efetuado 	

Ao finalizar o preenchimento é só clicar em exercute, logo abaixo.

* 3 - GET /pagamentos/{pagamento_id} Identificar Um Pagamento: Aqui você pode ver um pagamento individual. Clique na barra, no canto direito pressione "Try it out". Coloque o ID do seu pagamento e clique em execute, abaixo no response body será apresentado o seu pagamento. 

* 4 - GET /pagamentos/{pagamento_id} Identificar Um Pagamento: Aqui você pode ver se um pagamento foi realizado. Clique na barra, no canto direito pressione "Try it out". Coloque o ID do seu pagamento e clique em execute, abaixo no response body será apresentado o status do pagamento desejado. Caso leia "Efetuado", seu pagamento foi validado e caso apresente "Não efetuado", ele não foi.

Para resolver este desafio utilizei como base o modelo MVC no qual dividi as funcionalidades do projeto. Porém como utilizei um swagger não foi necessário o view.
