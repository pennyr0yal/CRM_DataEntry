# ===================== BIBLIOTECAS
import pyautogui
import time
import subprocess
import pyperclip
import messagebox
from limpar_dados import limpar_dados_cadastro

# ===================== SCRIPT
print('\nPreparando dados para registro...')
df = limpar_dados_cadastro()

print("\nAcessando a janela do CRM em 5 segundos...", end='', flush=True)

for i in range(5, 0, -1):
    print(f"\rAcessando a janela do CRM em {i} segundos... ", end='', flush=True)
    time.sleep(1)

rodar_crm = subprocess.Popen(['python', 'Script/mock_crm.py'])

time.sleep(1)

for i, row in df.iterrows():
    registros_restantes = len(df) - i
    print(f"\r{registros_restantes} registros restantes, por favor não mexa no seu mouse ou teclado até o programa encerrar...", end='', flush=True)
    def digitar(text):
        pyperclip.copy(text)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)

    def clicar_opcao(valor, mapa):
        if valor in mapa:
            pyautogui.click(*mapa[valor])
        else:
            print(f"[ERRO] Valor '{valor}' não encontrado.")

    # Preenche campos de texto
    campos_formulario = [
        ((930, 374), 'Nome completo'),
        ((930, 406), 'E-mail'),
        ((930, 434), 'Telefone'),
        ((930, 471), 'Empresa'),
    ]

    for (x, y), coluna in campos_formulario:
        pyautogui.click(x, y)
        time.sleep(0.2)
        digitar(str(row[coluna]))

    # Preenche "Origem do Lead"
    origem_coords = {
    'Site': (937, 521),
    'Indicação': (937, 534),
    'Anúncio': (937, 553),
    'Ligação fria': (937, 566)
    }

    pyautogui.click(x=961, y=499)    # Abre a lista suspensa
    time.sleep(0.2)
    clicar_opcao(row['Origem do Lead'],origem_coords)
    time.sleep(0.1)

    # Preenche "Status do Lead"
    status_coords = {
    'Novo': (861, 534),
    'Contato feito': (956, 534),
    'Qualificado': (1057, 534),
    }
    
    clicar_opcao(row['Status do Lead'],status_coords)

    # Preenche "Interesses"
    if 'Newsletter' in row['Interesses']:
        pyautogui.click(x=839, y=571)
    if 'Demonstração' in row['Interesses']:
        pyautogui.click(x=839, y=591)
    if 'Preços' in row['Interesses']:
        pyautogui.click(x=893, y=616)

    # Preenche "Observações"
    pyautogui.click(x=930, y=715)
    digitar(str(row['Observações']))

    # Clica em "Registrar"
    pyautogui.click(x=1147, y=764)

    # Wait a bit before next entry (adjust based on your CRM response time)
    time.sleep(0.2)

# Fecha a janela do CRM
pyautogui.click(x=1232, y=324)

messagebox.showinfo('Sucesso!','Dados registrados no CRM')