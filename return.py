import mysql.connector

try:
    con = mysql.connector.connect (host="localhost", user="root", passwd="123456", db="teste")
    consulta_sql = "SELECT * FROM dados"
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print("Numero de registos encontrados: ", cursor.rowcount)


    print("Mostrando as pessoas cadastradas")
    for linha in linhas:
        print("Id:", linha[0])
        print("Nome:", linha[1])
        print("Idade:", linha[2])
        print("Nome da Mãe:", linha[2], "\n")

except Error as e:
    print("Erro ao acessa a tabela MSQL", e)
finally:
    if(con.is_connected()):
        con.close()
        cursor.close()
        print("Conexão com o banco fechada")