# Preenchimento Automático de CRM
Este projeto simula uma **automação de data entry** em um sistema CRM desktop usando `PyAutoGUI`. A interface do CRM foi construída com `tkinter` para fins de teste, mas o programa pode ser adaptado para qualquer outro sistema.

---

## Funcionalidades

- Lê uma base de dados contendo nomes, e-mails, telefones, datas, entre outros dados de cadastro.
- Realiza tratamento e padronização dos dados:
  - Remoção de títulos (Sr., Dr., etc.) dos nomes
  - Normalização de números de telefones
  - Correção de erros e variações nos interesses utilizando correspondência aproximada.
  - Padronização de datas
- Cria uma interface gráfica com campos realistas de um CRM.
- Utiliza `PyAutoGUI` para simular a digitação e seleção dos campos.
- Mostra feedback no terminal com contagem de registros restantes.

## Como Usar

1. Execute o arquivo .bat na pasta principal. O programa instalará o venv e as bibliotecas necessárias.
2. Uma contagem regressiva será exibida no terminal antes do início da automação.
3. O programa abrirá a janela do CRM e começará a preencher os campos com os dados da planilha.
4. O terminal exibirá o número de registros restantes durante o processo.
5. Ao final, a automação é encerrada automaticamente e a janela do CRM é fechada.

## Observações

- O programa pode ser customizado para diferentes tipos de sistemas.
- A base de dados inclui valores propositalmente "sujos" para simular um cenário de RPA realista, com necessidade de tratamento antes da entrada dos dados.
- Possíveis melhorias incluem explorar outros possíveis erros humanos a serem tratados na base de dados, e desenvolver uma automação que consegue usar vários sistemas ao mesmo tempo, como acontece em empresas maiores.
  
# Autora
Desenvolvido por Natalia Junghans

📧 natbjunghans@gmail.com
