import csv
import pandas as pd


planilha = pd.read_csv("Planilha teste.csv")

data = planilha[:]

con_pl = len(planilha)

#controle de linha
print(con_pl)

#função de escolha

def ta_b (escolha):

#indicação para a sala

    if(escolha == 1):
        escolha = str(input("Digite uma opção, Sala(Principal/B): ")).capitalize()
        print('-'*130)
        print(f"\033[31m{'Nome':<20}{'Data':<15}{'Num.Parte':<30}{'Ajudante':<20}{'Lição':<10}{'Sala':<12}{'Concluiu':>0}\033[m")
        print('-'*130)
        for e in range(0, con_pl):
            if planilha.iloc[e,5] == escolha:
                print(f"{planilha.iloc[e,0]:<18} {planilha.iloc[e,1]:<15} {planilha.iloc[e,2]:<35} {planilha.iloc[e,3]:<17} {planilha.iloc[e,4]:<6} {planilha.iloc[e,5]:<5}{planilha.iloc[e,7]:>10}")
            

#indicação para a Concluiu
    if(escolha == 2):
        escolha = str(input("Digite uma opção, Concluiu(S/N): ")).upper()
        print('-'*130)
        print(f"\033[31m{'Nome':<20}{'Data':<15}{'Num.Parte':<30}{'Ajudante':<20}{'Lição':<10}{'Sala':<12}{'Concluiu':>0}\033[m")
        print('-'*130)
        for e in range(0, con_pl):
            if planilha.iloc[e,7] == escolha:
                print(f"{planilha.iloc[e,0]:<18} {planilha.iloc[e,1]:<15} {planilha.iloc[e,2]:<35} {planilha.iloc[e,3]:<17} {planilha.iloc[e,4]:<6} {planilha.iloc[e,5]:<5}{planilha.iloc[e,7]:>10}")

#função de Pesquisa de nome
def n_ome(publicador):
    for p in range(0, con_pl):
        if planilha.iloc[p,0] == publicador:
            print('-'*130)
            print(f"\033[31m{'Nome':<20}{'Data':<15}{'Num.Parte':<30}{'Ajudante':<20}{'Lição':<10}{'Sala':<12}{'Concluiu':>0}\033[m")
            print('-'*130)
            print(f"{planilha.iloc[p,0]:<18} {planilha.iloc[p,1]:<15} {planilha.iloc[p,2]:<35} {planilha.iloc[p,3]:<17} {planilha.iloc[p,4]:<6} {planilha.iloc[p,5]:<5}{planilha.iloc[p,7]:>10}\n")
            print("Gotaria de alterar alguma informação?")
            p_al = input("[S/N]").upper()

            if(p_al == 'S'):
                print("Nome [ 1 ]")
                print("Data [ 2 ]")
                print("Num.Parte [ 3 ]")
                print("Ajudante: [ 4 ]")
                print("Lição: [ 5 ]")
                print("Sala: [ 6 ]")
                print("Concluiu: [ 8 ]")
                p_al_Digito = int(input("Informe a opção:")) - 1
                p_al_Novo = input("Digite a alteração:").upper()
                planilha.iloc[p,p_al_Digito]= p_al_Novo
                #Troca as informações
                planilha.to_csv("Planilha teste.csv", index=False)
                print('-'*150)
                print(f"\033[31m{'Nome':<20}{'Data':<15}{'Num.Parte':<30}{'Ajudante':<20}{'Lição':<10}{'Sala':<12}{'Concluiu':>0}\033[m")
                print('-'*150)
                print(f"{planilha.iloc[p,0]:<18} {planilha.iloc[p,1]:<15} {planilha.iloc[p,2]:<30} {planilha.iloc[p,3]:<20} {planilha.iloc[p,4]:<7} {planilha.iloc[p,5]:<5}{planilha.iloc[p,7]:>10}\n")

def data_ant ():

    data['DATA'] = pd.to_datetime(data['DATA'], format='%d/%m/%Y')
    data_planilha = data.sort_values(by='DATA', ascending=True)
    S_publicador = input("Lista Irmãs [F]\nLista Varões [M]").upper() 

    print('-'*150)
    print(f"\033[31m{'Nome':<20}{'Data':<15}{'Num.Parte':<30}{'Ajudante':<20}{'Lição':<10}{'Sala':<12}{'Concluiu':>0}\033[m")
    print('-'*150)
    #ordena por data
    for p in range(con_pl):
        if data_planilha.iloc[p, 6].upper() == S_publicador:
            data_formatada = data_planilha.iloc[p, 1].strftime("%d/%m/%Y")
            print(f"{data_planilha.iloc[p,0]:<18} \033[32m{data_formatada:<15}\033[0m {data_planilha.iloc[p,2]:<30} {data_planilha.iloc[p,3]:<20} {data_planilha.iloc[p,4]:<7} {data_planilha.iloc[p,5]:<15}{planilha.iloc[p,7]:>0}")
        

#Adicionar novo publicador
'''def add_p():
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
        writer.writerow(new)'''




#Programa
while True:
    print("Deseja Pesquisar, a ultima designação de um publicador?")
    p_var = input("[S/N]:").upper()
    if(p_var == 'S'):
        print("Informe o nome do publicador")
        publicador = input("Nome:")

#Chama a função de pesquisa
        n_ome(publicador)

#Chama a Função para data
    print('Lista os publicadores por data?')
    data_in = input('[S/N]:').upper()
    if(data_in == 'S'):
        data_ant()

    print("\nEscolha uma Opção:")
    print("sala [1]")
    print("Concluiu [2]")
    #print("Adicionar Publicador [3]")
    print("Sair [0]")
    escolha_str = input("Digite um número: ")

    if not escolha_str:
        print("Você não digitou nada!")
    else:
        escolha = int(escolha_str)
        if escolha == 0:
            break
        ta_b(escolha)



