import json


ARQUIVO_CADASTROS = "cadastros.json"


def exibir_menu():
    print("\n---------- MENU DO SISTEMA ----------")
    print("1 - Cadastrar pessoa")
    print("2 - Ver cadastros")
    print("3 - Sair")
    print("----------------------------------------")


def salvar_cadastros(cadastros):
    with open (ARQUIVO_CADASTROS, "w", encoding="utf-8") as arquivos:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)


def carregar_cadastros():
    try:
        with open(ARQUIVO_CADASTROS, "w", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except (FileNotFoundError,json.JSONDecodeError):
        return []
    

    def cadastrar_pessoa(cadastros):
        nome = input("Nome: ")
        idade = input("Idade: ")
        turma = input("Turma: ")
        curso = input("Curso: ")

        cadastros.append("Nome": nome, "Idade")