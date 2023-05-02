import sqlite3 
from sqlite3 import Error

###Criar conexao
def ConexaoBanco():
    caminho="D:\\Python\\Aulas\\Banco\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

#####Criar tabela
#vsql="""CREATE TABLE tb_contatos(
#            N_IDCONTATO INTEGER PRIMARY KEY AUTOIMCREMENT,
#            T_NOMECONTATO VARCHAR(30),
#            T_TELEFONECONTATO VARCHAR(14),
#            T_EMAILCONTATO VARCHAR(30)
#        );"""

#SELECT - CONSULTA(SET)  ####fetchall() - pegar todas as consultas do banco.
def consulta(conexao,sql):
        c=conexao.cursor()
        c.execute(sql)
        resultado=c.fetchall()
        return resultado
    
vsql="SELECT * FROM tb_contatos"
res=consulta(vcon,vsql)
for r in res:
    print(r)