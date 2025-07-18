# ===================== BIBLIOTECAS
import pandas as pd
import os
import re
from difflib import get_close_matches

# ===================== SCRIPT
def limpar_nomes(name):
    # Títulos mais comuns no português brasileiro. Essa lista pode ser alterada se outro título for identificado.
    titulos = [
        r'Dr\.?', r'Dra\.?', r'Sr\.?', r'Srta\.?', r'Senhor', r'Senhora',
        r'Prof\.?', r'Eng\.?', r'Mestre', r'Doutor', r'Doutora'
    ]

    # Padrão regex para identificar a ocorrência dos títulos
    padrao = r'^\s*(' + '|'.join(titulos) + r')\s+'

    # Identifica os títulos e remove do nome
    nome_limpo = re.sub(padrao, '', name, flags=re.IGNORECASE)
    return nome_limpo.strip()

def limpar_telefone(tel):
    if not isinstance(tel, str):
        tel = str(tel)

    # Remove tudo que não for dígito
    numeros = re.sub(r'\D', '', tel)

    # Remove zeros à esquerda
    numeros = re.sub(r'^0+', '', numeros)

    # Remove código do país '55' no início, se existir, e quaisquer zeros que seguirem
    numeros = re.sub(r'^(55)0*', '', numeros)

    return numeros

def limpar_interesses(texto):
    INTERESSES_PADRAO = ['Newsletter', 'Preços', 'Demonstração']

    if not isinstance(texto, str):
        return []

    # Separa palavras-chave "grudadas" (ex: NewsletterPrecos -> Newsletter Precos) a partir da primeira letra minúscula seguida de uma maiúscula
    texto = re.sub(r'([a-z])([A-Z])', r'\1 \2', texto)
    
    # Remove pontuações e substitui por espaço
    texto = re.sub(r'[,.;]', ' ', texto)

    # Remove espaços múltiplos
    texto = re.sub(r'\s+', ' ', texto).strip()

    # Separa as palavras em uma lista
    palavras = texto.split(' ')

    # Corrige palavras aproximadas usando close matches
    resultados = []
    for p in palavras:
        correspondentes = get_close_matches(p, INTERESSES_PADRAO, n=1, cutoff=0.6)
        if correspondentes:
            resultados.append(correspondentes[0])
        else:
           resultados.append(None)   # Se não encontra, retorna vazio

    # Remove duplicatas
    resultados_unicos = []
    for r in resultados:
        if r not in resultados_unicos:
            resultados_unicos.append(r)

    return ', '.join(resultados_unicos)   # Retorna todos os itens da lista separados por vírgula

def parse_date(date):
    if pd.api.types.is_datetime64_any_dtype(type(date)) or isinstance(date, pd.Timestamp):
        # Se já for data, não faz nada
        return date
    # Converte datas
    for kwargs in [{'yearfirst': True}, {'dayfirst': True}]:
        try:
            return pd.to_datetime(date, **kwargs)
        except (ValueError, TypeError):
            continue
    return pd.NaT

def limpar_dados_cadastro():
    df = pd.read_excel(os.path.join(os.getcwd(),'clientes_a_cadastrar.xlsx'))

    # Realiza a limpeza dos dados
    df['Nome completo'] = df['Nome completo'].apply(limpar_nomes)
    df['Telefone'] = df['Telefone'].apply(limpar_telefone)
    df['Interesses'] = df['Interesses'].apply(limpar_interesses)
    df['Data do Cadastro'] = df['Data do Cadastro'].apply(parse_date).dt.strftime('%d/%m/%Y')
    df['Código do Cliente'] = df['Código do Cliente'].apply(lambda x: f'CLI-{x}')
    df = df.fillna('-')

    return df


df = limpar_dados_cadastro()
df.to_clipboard()