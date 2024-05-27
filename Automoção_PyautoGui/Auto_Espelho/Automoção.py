import pyautogui
import time
import pandas

pyautogui.PAUSE = 1 

pyautogui.hotkey('win','r')
pyautogui.write("C:\\Users\\deand\\Documents\\Projetos prontos\\NOVO ESPELHO COM LIMPAR\\main.exe")
pyautogui.press('enter')

tabela = pandas.read_csv('Teste de Designações Planilha1.csv')


for linha in tabela.index:
    time.sleep(2)
# Titular
    Nome = tabela.loc[linha,"Nome"]
    pyautogui.write(Nome)
    pyautogui.press('tab')

# Ajudante
    aju = tabela.loc[linha,"Ajudante"]
    if not pandas.isna(aju):  
        pyautogui.write(aju)
        pyautogui.press('tab')
    else:
        pyautogui.press('tab')

# Data
    
    pyautogui.write(tabela.loc[linha,"Semana"])
    pyautogui.press('tab')

# numero
    
    pyautogui.write(tabela.loc[linha, "Designacao "])
    pyautogui.press('tab')

    Sala = tabela.loc[linha,"Sala"]
    if "A" in Sala:
        pyautogui.press('space')
        pyautogui.press('tab')
        pyautogui.press('tab')
 
    elif "B" in Sala:
        pyautogui.press('tab')
        pyautogui.press('space')
        pyautogui.press('tab')
        
    pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(2)
    pyautogui.press('tab')
    pyautogui.press('space')
    time.sleep(2)
    pyautogui.press('tab')





   





