# ===================== BIBLIOTECAS
import tkinter as tk
from tkinter import ttk

# ===================== SCRIPT
def centralizar_janela():
    root.update_idletasks()
    w = root.winfo_width()
    h = root.winfo_height()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (w // 2)
    y = (screen_height // 2) - (h // 2)
    root.geometry(f'+{x}+{y}')

root = tk.Tk()
root.title('Sistema CRM - Cadastro de Clientes')
root.configure(padx=20, pady=20)
root.geometry('580x470')
root.resizable(False, False)
root.attributes('-topmost', True)
root.deiconify()
root.lift()
root.focus_force() 

root.after(10, centralizar_janela)

FONTE = ('Arial', 10, 'bold')
LARGURA_PADRAO = 50

campos = []
# Adiciona os campos de texto
def add_input_label(row, texto, var_dict):
    tk.Label(root, text=texto + ':', font=FONTE).grid(row=row, column=0, sticky='e', padx=5, pady=5)
    entrada = tk.Entry(root, width=LARGURA_PADRAO)
    entrada.grid(row=row, column=1, sticky='w', padx=5, pady=5)
    var_dict[texto] = entrada
    campos.append(entrada)

entradas = {}
linha = 0

for campo in ['Nome completo', 'E-mail', 'Telefone', 'Empresa']:
    add_input_label(linha, campo, entradas)
    linha += 1

# Adiciona dropdown menu de Origem do Lead
tk.Label(root, text='Origem do Lead:', font=FONTE).grid(row=linha, column=0, sticky='e', padx=5, pady=5)
origem_input = ttk.Combobox(root, values=['Site', 'Indicação', 'Anúncio', 'Ligação fria'], state='readonly', width=LARGURA_PADRAO-3)
origem_input.grid(row=linha, column=1, sticky='w', padx=5, pady=5)
entradas['Origem do Lead'] = origem_input
linha += 1

# Adiciona botões para selecionar Status do Lead
tk.Label(root, text='Status do Lead:', font=FONTE).grid(row=linha, column=0, sticky='ne', padx=5, pady=5)
status_var = tk.StringVar()
frame_status = tk.Frame(root)
frame_status.grid(row=linha, column=1, sticky='w', padx=5, pady=5)
for status in ['Novo', 'Contato feito', 'Qualificado']:
    tk.Radiobutton(frame_status, text=status, variable=status_var, value=status).pack(side='left', padx=5)
entradas['Status do Lead'] = status_var

linha += 1

# Adiciona botões de multiseleção de Interesses do cliente
tk.Label(root, text='Interesses:', font=FONTE).grid(row=linha, column=0, sticky='ne', padx=5, pady=5)
frame_check = tk.Frame(root)
frame_check.grid(row=linha, column=1, sticky='w', padx=5, pady=5)
interesses_vars = {}
for interesse in ['Newsletter', 'Demonstração', 'Preços']:
    var = tk.BooleanVar()
    tk.Checkbutton(frame_check, text=interesse, variable=var).pack(anchor='w')
    interesses_vars[interesse] = var
entradas['Interesses'] = interesses_vars
linha += 1

# Adiciona campo de observações
tk.Label(root, text='Observações:', font=FONTE).grid(row=linha, column=0, sticky='ne', padx=5, pady=5)
obs_txt = tk.Text(root, width=LARGURA_PADRAO, height=5)
obs_txt.grid(row=linha, column=1, sticky='w', padx=5, pady=5)
entradas['Observações'] = obs_txt
campos.append(obs_txt)
linha += 1

def limpar_tudo():
    # Limpa os campos de texto para receber novos dados
    for campo in campos:
        if isinstance(campo, tk.Entry):
            campo.delete(0, tk.END)
        elif isinstance(campo, tk.Text):
            campo.delete('1.0', tk.END)
    # Limpa as checkboxes de Interesses
    for var in interesses_vars.values():
        var.set(False)

# Adiciona botão "Registrar"
botao = tk.Button(root, text='Enviar', command=limpar_tudo, width=20, bg='#4CAF50', fg='white', font=('Arial', 10, 'bold'))
botao.grid(row=linha, column=1, pady=20, sticky='e')

root.mainloop()