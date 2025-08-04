# Documentação do Projeto: Viagem+

## 1. Visão Geral

### Tecnologias Utilizadas

- Python  
- FastAPI  
- SQLModel  
- SQLite  
- Uvicorn  
- Pydantic  
- Requests
- Tabulate

### Descrição

Aplicação de controle financeiro de viagens, permitindo cadastro de usuários, criação de viagens, registro de despesas e geração de resumos financeiros com alertas sobre orçamento. Possui interface CLI para interação com o usuário.

### Objetivo

Oferecer uma plataforma simples e funcional para que usuários acompanhem os gastos em suas viagens e controlem o orçamento de forma prática através de uma interface amigável.

---

## 2. Descrição Detalhada do Projeto

### Arquitetura do Sistema

O sistema é composto por:
1. Backend: API RESTful construída com FastAPI
2. Frontend: Interface CLI que consome a API
3. Banco de Dados: SQLite para persistência de dados

### 2.1 Funcionalidades Principais

| Funcionalidade                   | Rota                               | Método | Descrição                                             |
|---------------------------------|----------------------------------|--------|-------------------------------------------------------|
| Criar usuário                   | `/usuarios`                      | POST   | Cadastro de um novo usuário com nome, email e senha. |
| Login                          | `/login`                        | POST   | Autenticação de usuário por email e senha.            |
| Criar viagem                   | `/usuarios/{usuario_id}/viagens`| POST   | Criação de nova viagem associada ao usuário.          |
| Listar viagens do usuário      | `/usuarios/{usuario_id}/viagens`| GET    | Listar todas as viagens de um usuário.                 |
| Atualizar viagem               | `/viagens/{id}`                 | PUT    | Atualizar dados de uma viagem.                         |
| Deletar viagem                | `/viagens/{id}`                 | DELETE | Remover viagem do sistema.                             |
| Adicionar despesa              | `/viagens/{viagem_id}/despesas`| POST   | Adicionar despesa à viagem.                            |
| Listar despesas da viagem      | `/viagens/{viagem_id}/despesas`| GET    | Listar despesas registradas em uma viagem.             |
| Atualizar despesa             | `/despesas/{id}`                | PUT    | Atualizar informações de uma despesa.                  |
| Deletar despesa              | `/despesas/{id}`                | DELETE | Excluir despesa do sistema.                            |
| Resumo financeiro da viagem    | `/viagens/{viagem_id}/resumo`   | GET    | Calcular total gasto, saldo restante e alerta de orçamento. |

---

### 2.2 Estrutura do Projeto

```plaintext
projeto-pos/
├── backend/
│   ├── main.py           # Código principal da API com as rotas
│   ├── models.py         # Modelos SQLModel 
│   ├── auth.py           # Funções para hash e verificação de senha
│   ├── interface.py      # Ponto de entrada da interface CLI
│   └── requirements.txt  # Dependências do frontend CLI
├── frontend/
│   ├── cli/
│   │   ├── config.py     # Configurações da API e cabeçalhos
│   │   ├── despesa.py    # Funções para gerenciamento de despesas
│   │   ├── menus.py      # Menus de navegação do sistema
│   │   ├── terminal.py   # Funções auxiliares para o terminal
│   │   ├── usuario.py    # Funções para gerenciamento de usuários
│   │   └── viagem.py     # Funções para gerenciamento de viagens
└── banco.db              # Banco de dados SQLite local

```

---

## 3. Etapas de Entrega (Cronograma Detalhado)

| Etapa       | Data         | Tarefa Principal             | Descrição                                                                                   |
| ----------- | ------------ | ---------------------------- | ------------------------------------------------------------------------------------------- |
| **Etapa 1** | 27/07        | Finalização do backend       | Concluir implementação das rotas, modelos, autenticação, lógica de viagens e despesas.      |
| **Etapa 2** | 02/08        | Desenvolvimento da interface | Criar o frontend CLI com menus navegáveis. Integrar com as rotas da API via requests.   |
| **Etapa 3** | 03/08        | Ajustes finais e refinamento | Concluir a interface, melhorar usabilidade, corrigir erros, revisar fluxo, documentação e preparar entrega final. |
