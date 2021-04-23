import PySimpleGUI as sg 
import mysql.connector

# Gera a string de conexao ex.: seu host, seu usuario, sua senha e seu db
banco = mysql.connector.connect (
            host="localhost", 
            user="root", 
            passwd="123456", 
            db="teste"
)
class TelaPython:
    def __init__(self):
        #layout
        #Anotaçõs: size(tamanho de texto)
        layout = [
            [sg.Text('Nome: ', size=(5,0)), sg.Input(size=(50,0), key='nome')],
            [sg.Text('Idade: ', size=(5,0)), sg.Input(size=(15,0), key='idade')],
            [sg.Text('Nome da Mãe: ', size=(5,0)), sg.Input(size=(50,0), key='nome_mae')],
            [sg.Button('Enviar Dados')]

        ]
        #Janela
        janela = sg.Window('Dados do Usuário').layout(layout)
        #Extrair dados
        self.button, self.values = janela.Read()
    
    def Iniciar(self):
        nome = self.values['nome']
        idade = self.values['idade']
        nome_mae = self.values['nome_mae']

        print({nome})
        print({idade})
        print({nome_mae})
        
        #Inserindo no Banco de dados
       
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO dados (nome, idade,nome_mae) VALUES (%s, %s, %s)"
        dados = (nome,idade, nome_mae)
        cursor.execute(comando_SQL, dados)
        banco.commit()
        banco.close()
        cursor.close()

tela = TelaPython()
tela.Iniciar()




