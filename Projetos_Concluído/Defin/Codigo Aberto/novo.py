from tkinter import *
import pandas as pd
from tkinter import ttk, messagebox, Menu, IntVar, Checkbutton
import tkinter as tk


#controle de linha
#print(con_pl)

def data_ant (S_publicador):

    planilha = pd.read_csv("Base_dados.csv")

    data = planilha[:]
    con_pl = len(planilha)

    data['DATA'] = pd.to_datetime(data['DATA'], format='%d/%m/%Y')
    data_planilha = data.sort_values(by='DATA', ascending=True)
    troca = []

    for p in range(con_pl):            
        if data_planilha.iloc[p, 6] == S_publicador :
            data_formatada = data_planilha.iloc[p, 1].strftime("%d/%m/%Y")
            resultado = f"{data_planilha.iloc[p,0]:<18} {data_formatada:<15} {data_planilha.iloc[p,2]:<30} {data_planilha.iloc[p,3]:<20} {data_planilha.iloc[p,4]:<7} {data_planilha.iloc[p,5]:<15}{planilha.iloc[p,7]:<5}"
            troca.append(resultado)
    return troca       

def Atualizar():
    arquivo_base = 'Base_dados.csv'
    arquivo_novo = 'Novo_mês.csv'

    # Carregar ambos os arquivos CSV para DataFrames do Pandas
    df_base = pd.read_csv(arquivo_base)
    df_novo = pd.read_csv(arquivo_novo)

    # Definir o nome como índice para facilitar a atualização
    df_base.set_index('NOME', inplace=True)
    df_novo.set_index('NOME', inplace=True)

    for nome,row in df_novo.iterrows():
        if nome not in df_base.index:
            df_base = df_base._append(row)

    # Atualizar as colunas do arquivo base com base no arquivo novo
    df_base.update(df_novo)

    # Resetar o índice para obter a estrutura original
    df_base.reset_index(inplace=True)

    # Salvar o DataFrame atualizado de volta para um arquivo CSV
    df_base.to_csv('Base_dados.csv', index=False)

    messagebox.showinfo('Atualizado', 'Arquivo Base_dados atualizado com sucesso')

#Adição de um novo publicador
def nova_jan():
    nova = tk.Toplevel()
    nova.title("Adicionar")

    n_nome = Label(nova, text='Nome:')
    n_nome.grid(row=0, column=0 )
    no_me_ent = Entry(nova, font="Arial 12", width=20)
    no_me_ent.grid(row=0, column=1)


    se_xo = Label(nova, text="[M/F]")
    se_xo.grid(row=1 , column=0)
    se_xo_ent = Entry(nova, font="Arial 12", width=5)
    se_xo_ent.grid(row=1, column=1)

    def p_g():
        no_me = no_me_ent.get()
        sex_o = se_xo_ent.get().upper()

        if no_me.strip() == '' or sex_o.strip() == '':
            messagebox.showerror('Erro', 'Por favor, preencha todos os campos.')
            return
#               NOME,DATA,Num.Parte,Ajudante,Lição,Sala,Sexo,Lição_con
        novo_dado = [no_me,'01/01/2020','none','-','0','None',sex_o,'none']

        arquivo_base = 'Base_dados.csv'

        df_base = pd.read_csv(arquivo_base)
        df_base = df_base._append(pd.Series(novo_dado, index=df_base.columns), ignore_index=True)
        df_base.to_csv(arquivo_base, index=False)

        messagebox.showinfo('Sucesso', f'{no_me} foi adicionado com sucesso!')
        nova.lift()

    envi_ar = Button(nova, text="Enviar",font="Arial 12", command=p_g)
    envi_ar.grid(row=2 ,column=0, columnspan=2)

#Função nova Janela para status
def in_ativ():
    planilha = pd.read_csv("Base_dados.csv")
    con_pl = len(planilha)
    
    nova_inat = tk.Toplevel()
    nova_inat.title("Inativar")
    sta_tus = IntVar()


    no_me = Label(nova_inat, text='Nome:')
    no_me.grid(row=0, column=0 )
    no_me_ina = Entry(nova_inat, font="Arial 12", width=20)
    no_me_ina.grid(row=0, column=1)

#Função procura o publicado 

    def procurar():
        pe_gar_pesquisa = no_me_ina.get()

        erro1 = False
        for p in range(con_pl):
            if pe_gar_pesquisa == planilha.iloc[p, 0]  :
                pes_soa = planilha.iloc[p, 0]
                erro1 = True
                if planilha.iloc[p, 6] == "*M" or planilha.iloc[p, 6] == "*F" :
                    sta_tus.set(1)
                    
                else:
                    sta_tus.set(0)

                messagebox.showinfo('Encontrado', f'Publicador encontrado {pes_soa} !')
                nova_inat.lift()
                break
        if not erro1:
            messagebox.showinfo('Erro1', f'Nome digitado errado ou não exite!')
            nova_inat.lift()

    no_me_procurar = Button(nova_inat, text="Procurar",font="Arial 12", command=procurar)
    no_me_procurar.grid(row=1 ,column=1, pady=5)

    nova_inat.update_idletasks()
    ina_rea_ent = Checkbutton(nova_inat,text='Inativo', font="Arial 12", width=5, onvalue=1, offvalue=0, variable=sta_tus)
    ina_rea_ent.grid(row=3, column=1)

#Função para Salvar as informações

    def salvar():
        fim = no_me_ina.get()
        atual_status = sta_tus.get()
        deletar()
        if not deletar():
            for p in range(con_pl):
                if fim == planilha.iloc[p, 0] :
                    if atual_status == 1:
                        if not planilha.iloc[p, 6].startswith('*'):
                            planilha.iloc[p, 6]= '*'+ planilha.iloc[p, 6]
                    else:
                        if planilha.iloc[p, 6].startswith('*'):
                            planilha.iloc[p,6]= planilha.iloc[p,6][1:]

                    planilha.to_csv("Base_dados.csv", index=False)
                    messagebox.showinfo('Atualizado', f'{fim} foi atualizado com sucesso!')
                    nova_inat.lift()        
                    break
    
    dele_ta = Label(nova_inat, text="Escreva [DEL] para Deletar:")
    dele_ta.grid(row=4 , column=0)
    dele_ta_ent = Entry(nova_inat, font="Arial 12", width=10)
    dele_ta_ent.grid(row=4, column=1)

#Função para deletar um publicador

    def deletar():
        fim = no_me_ina.get()
        info = dele_ta_ent.get().upper()
        if info == 'DEL':
            treee = True
            for p in list(planilha.index):
                if fim == planilha.iloc[p,0]:
                    planilha.drop(p, inplace=True)
                    planilha.to_csv("Base_dados.csv", index=False)
                    messagebox.showinfo('Deletado', f'{fim} foi apagado com sucesso!')
                    nova_inat.lift()
                    break
        else:
            treee = False
        return treee

    no_me_att = Button(nova_inat, text="Atualizar",font="Arial 12", command=salvar)
    no_me_att.grid(row=5 ,column=1, pady=5)
    
  