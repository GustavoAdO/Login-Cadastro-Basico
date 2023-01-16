import mysql.connector
import time
import re
import os 

def main():
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='157456El@',
        database='sistemadecadastro'
    )
    cursor = conexao.cursor(prepared=True)
    while True:
        os.system('cls')
        print("INTERFACE")
        print("Digite 1 para se cadastrar")
        print("Digite 2 para fazer login")
        print("Digite 0 para sair")
        interface = int(input())
        
        if interface == 0:
            break
        
        elif interface == 1:
            email = input("Digite o Email:\n")
            
            if not re.search('[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',email):
                print("Email com formato invalido")
                time.sleep(3)
                continue
            
            login = input("Digite o Login:\n")
            senha = input("Digite a Senha:\n")
            
            if email_existe(cursor,email) or login_existe(cursor,login):
                print("Email ou Login já existente")
                time.sleep(3)
            else:
                inserindo = 'INSERT INTO usuarios(email,login,senha) VALUES(%s,%s,%s) '
                cadastrando = (email, login, senha)
                cursor.execute(inserindo, cadastrando)
                conexao.commit()
                print("Cadastro Efetuado")
                time.sleep(3)
                
        elif interface == 2:
            login = input("Digite o Login:\n")
            senha = input("Digite a Senha:\n")
            
            if login_existe(cursor, login) and senha_existe(cursor, senha):
                print("Login efetuado")
                time.sleep(3)
            else:
                print("Algo errado, tente novamente")
                time.sleep(3)
    cursor.close()
    conexao.close()

def email_existe(cursor, email):
    ler_email = 'SELECT email FROM usuarios WHERE email = %s'
    cursor.execute(ler_email, (email,))
    return cursor.fetchone() is not None

def login_existe(cursor, login):
    ler_login = 'SELECT login FROM usuarios WHERE login = %s'
    cursor.execute(ler_login, (login,))
    return cursor.fetchone() is not None
   
def senha_existe(cursor, senha):
    ler_senha = 'SELECT senha FROM usuarios WHERE senha = %s'
    cursor.execute(ler_senha, (senha,))
    return cursor.fetchone() is not None

if __name__ == "__main__":
    main()
