import csv
import pandas as pd


planilha = pd.read_csv("Planilha teste.csv")

con_pl = len(planilha)

#controle de linha
print(con_pl)

#função de escolha

def ta_b (escolha):

#indicação para a sala

    if(escolha == 1):
        escolha = str(input("Digite uma opção, Sala(Principal/B): "))
        for e in range(0, con_pl):
            if planilha.iloc[e,5] == escolha:
                print(f"Nome: {planilha.iloc[e,0]} {planilha.iloc[e,1]} |Num.Parte: {planilha.iloc[e,2]} |Titular/Ajudante: {planilha.iloc[e,3]} |Concluiu: {planilha.iloc[e,4]} |Sala: {planilha.iloc[e,5]}")

#indicação para a Concluiu
    if(escolha == 2):
        escolha = str(input("Digite uma opção, Concluiu(S/N): ")).upper()
        for e in range(0, con_pl):
            if planilha.iloc[e,4] == escolha:
                print(f"Nome: {planilha.iloc[e,0]} {planilha.iloc[e,1]} |Num.Parte: {planilha.iloc[e,2]} |Titular/Ajudante: {planilha.iloc[e,3]} |Concluiu: {planilha.iloc[e,4]} |Sala: {planilha.iloc[e,5]}")

#indicação para a titular
    if(escolha == 3):
        escolha = str(input("Digite uma opção, Titular/Ajudante(T/A): ")).upper()
        for e in range(0, con_pl):
            if planilha.iloc[e,3] == escolha:
                print(f"Nome: {planilha.iloc[e,0]} {planilha.iloc[e,1]} |Num.Parte: {planilha.iloc[e,2]} |Titular/Ajudante: {planilha.iloc[e,3]} |Concluiu: {planilha.iloc[e,4]} |Sala: {planilha.iloc[e,5]}")

#função de Pesquisa de nome
def n_ome(publicador):
    for p in range(0, con_pl):
        if planilha.iloc[p,0] == publicador:
            print(f"\nNome: {planilha.iloc[p,0]} {planilha.iloc[p,1]} |Num.Parte: {planilha.iloc[p,2]} |Titular/Ajudante: {planilha.iloc[p,3]} |Concluiu: {planilha.iloc[p,4]} |Sala: {planilha.iloc[p,5]}\n")
            print("Gotaria de alterar alguma informação?")
            p_al = input("[S/N]").upper()

            if(p_al == 'S'):
                print("Nome [ 1 ]")
                print("Data [ 2 ]")
                print("Num.Parte [ 3 ]")
                print("Titular/Ajudante: [ 4 ]")
                print("Concluiu: [ 5 ]")
                print("Sala: [ 6 ]")
                p_al_Digito = int(input("Informe a opção:")) - 1
                p_al_Novo = input("Digite a alteração:")


                planilha.iloc[p,p_al_Digito]= p_al_Novo
#Troca as informações
                planilha.to_csv("Planilha teste.csv", index=False)

                print(f"\nNome: {planilha.iloc[p,0]} {planilha.iloc[p,1]} |Num.Parte: {planilha.iloc[p,2]} |Titular/Ajudante: {planilha.iloc[p,3]} |Concluiu: {planilha.iloc[p,4]} |Sala: {planilha.iloc[p,5]}\n")




def add_p():


# Solicitar ao usuário para inserir os dados
    new_nome = input("Digite o nome:")
    new_data = input("Digite o data:")
    new_num_parte = input("Digite o Numero da Parte:")
    new_tit_aju = input("Digite o Ajudante [A] ou Titular [T]:").upper()
    new_con = input("Digite o Concluiu a parte [S/N]:").upper()
    new_sala = input("Digite o Sala [Principal/B]:")
    new = [new_nome, new_data, new_num_parte, new_tit_aju, new_con, new_sala]

    with open('Planilha/Planilha teste.csv', 'a', newline='') as new_linha:
        writer = csv.writer(new_linha)
        writer.writerow(new)




#Programa
while True:
    print("Deseja Pesquisar, a ultima designação de um publicador?")
    p_var = input("[S/N]:").upper()
    if(p_var == 'S'):
        print("Informe o nome do publicador")
        publicador = input("Nome:")

#Chama a função de pesquisa
        n_ome(publicador)




    print("\nEscolha uma Opção:")
    print("sala [1]")
    print("Concluiu [2]")
    print("Tit/Aju [3]")
    #print("Adicionar Publicador [4]")
    print("Sair [0]")

    escolha_str = input("Digite um número: ")

    if not escolha_str:
        print("Você não digitou nada!")
    else:
        escolha = int(escolha_str)

        if escolha == 0:
            # Aqui você pode querer interromper o programa ou sair de um loop
            break

        ta_b(escolha)



