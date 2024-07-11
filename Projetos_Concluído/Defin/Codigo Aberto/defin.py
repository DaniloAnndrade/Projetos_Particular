from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, Menu
import pyperclip
from novo import  data_ant,Atualizar,nova_jan,in_ativ
import csv


"""

"""
#  Caminho para o arquivo CSV
caminho_arquivo = "Base_dados.csv"

# Cria uma Janela
janela = Tk()

# Título do programa
janela.title("Defin")
janela.geometry("1300x420")

#Modificação*
def mostrar(S_publicador):
    troca = data_ant(S_publicador)
    
    # Limpar itens existentes na Listbox
    for item in lista.get_children():
        lista.delete(item)
    
    # Adicionar novos itens à Listbox -. strip() retira espaços em volta dos nomes
    for item in troca:
        nome = item[:18].strip()
        data = item[19:33].strip()
        num_parte = item[33:63].strip()
        ajudante = item[66:83].strip()
        licao = item[83:90].strip()
        sala = item[90:105].strip()
        concluiu = item[105:].strip()
        lista.insert('', 'end', values=(nome, data, num_parte, ajudante, licao, sala, concluiu))


#Função que copia e adiciona os valores na Treeview
def copi_a2():
    dados_copy = entrada_colar.get()
    if dados_copy:
        dados = dados_copy.split('\t')# .Split() e a tabulação
        if len(dados) == len(colunas):
            dados_processados = [processar_dado(dado) for dado in dados]
            camp.insert('', 'end', values=dados_processados)# o .insert() define onde sera enviado os valores,no caso no "end" 
        else:
            messagebox.showerror('Erro', 'Dados copiados não correspondem ao formato esperado.')
    else:
        messagebox.showwarning('Aviso', 'Nada foi copiado.')#MassageBox mostra um pequena janela com erro

#Composição da variavel "copi_a2()"
def processar_dado(dado):
    return dado.strip()


#Cria um novo arquivo ou substitui um existente exportando os arquivos do segundo treeview
def exportar_csv():
    colunas = ('NOME','DATA','NumParte','Ajudante','Lição','Sala','Lição_con')
    with open('Novo_mês.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(colunas)  # Escreve os cabeçalhos das colunas
        for item in camp.get_children():
            row = camp.item(item)['values']
            writer.writerow(row)
    for item in camp.get_children():
        camp.delete(item)
    messagebox.showinfo('Exportação', 'Dados do Treeview camp exportados para Novo_mês.csv com sucesso.')

#Funsão para copiar
def copia():
    selec_itens = lista.selection()
    varios = []

    for coleta in selec_itens:
        item = lista.item(coleta)
        dados = item['values']
        linha = '\t'.join(map(str, dados))
        varios.append(linha)
    
    if varios:
        linhas_varios = '\n'.join(varios)
        pyperclip.copy(linhas_varios)

#Area do Layout ------------------------------------------------------------------------Inicio
texto = Label(text='Designações', font="Arial 12")
ir_mM = Button(text='Masculino', font="Arial 12", command=lambda: mostrar('M'))
ir_mF = Button(text='Feminino', font="Arial 12", command=lambda: mostrar('F'))

texto.grid(row=2, column=0, columnspan=2, pady=5)
ir_mM.grid(row=3, column=0, pady=5)
ir_mF.grid(row=3, column=1, pady=5)

# Campo de entrada para colar os dados
texto3 = Label(text='Insira os dados do publicador, e atualize sua designação')
texto3.grid(row=0, column=5)
entrada_colar = tk.Entry(janela, font="Arial 10", width=90)
entrada_colar.grid(row=1, column=5, columnspan=9, pady=5)

#Botão colar
btn_colar = tk.Button(janela, text="Colar", font="Arial 12", command=copi_a2)
btn_colar.grid(row=2, column=5, columnspan=4, pady=5)

menu = Menu(tearoff=0)
menu.add_command(label='Copiar', command=copia)

#Exportar 
export = tk.Button(janela, text='Exportar', font='Arial 12',command=exportar_csv)
export.grid(row=10, column=5, pady=5)

#Mesclar listas
mesclar = tk.Button(janela, text='Mesclar Lista final', font='Arial 12',command=Atualizar)
mesclar.grid(row=10, column=6, pady=5)

#Adição
texto2 = Label(text='Adiciona um Novo Publicador:',font='Arial 9')
add_ps = tk.Button(janela, text="ADD", font='Arial 9', command=nova_jan)
add_ps.grid(row=0, column=1)
texto2.grid(row=0, column=0)

#Inativar 
texto5 = Label(janela,text='Inativar,Ativar e Deletar :',font='Arial 9')
ina_tivar = tk.Button(janela, text='INA',font='Arial 9', command=in_ativ)
ina_tivar.grid(row=1, column=1)
texto5.grid(row=1, column=0)

#Area do Layout ------------------------------------------------------------------------ Final


#Nome das colunas ---------------------------------------------------------------------- Inicio
colunas = ('Nome', 'Data', 'Num.Parte', 'Ajudante', 'Lição', 'Sala', 'Concluiu')


#Primeira Tabela --- Lista ---
lista = ttk.Treeview(columns=colunas, show='headings')
lar = [120, 75, 130, 120, 40, 65, 65]
for col, largura in zip(colunas, lar):
    lista.heading(col, text=col)
    lista.column(col, width=largura)    
lista.grid(row=4, column=0, rowspan=6, columnspan=4, padx=5, pady=5)

#Area onde o click vai acontecer
lista.bind("<Button-3>", lambda event: menu.post(event.x_root, event.y_root))

#Seguinda Tabela --- Lista ---
camp = ttk.Treeview(columns=colunas, show='headings')
for col, largura in zip(colunas, lar):
    camp.heading(col, text=col)
    camp.column(col, width=largura)
camp.grid(row=4, column=5, rowspan=6, columnspan=9, padx=5, pady=5)
#Nome das colunas ---------------------------------------------------------------------- Fim

# Janela continua aberta por conta do mainloop
janela.mainloop()