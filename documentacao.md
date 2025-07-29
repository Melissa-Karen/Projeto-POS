# Documentação do Projeto: Viagem+ (nome provisório)

## 1. Visão Geral

### Tecnologias Utilizadas

- Python  
- FastAPI  
- SQLModel  
- SQLite  
- Uvicorn  
- Pydantic  

### Descrição

Aplicação web de controle financeiro de viagens, permitindo cadastro de usuários, criação de viagens, registro de despesas e geração de resumos financeiros com alertas sobre orçamento.

### Objetivo

Oferecer uma plataforma simples e funcional para que usuários acompanhem os gastos em suas viagens e controlem o orçamento de forma prática.

---

## 2. Descrição Detalhada do Projeto

### O que é o projeto?

Viagem+ é um sistema que permite aos usuários registrar suas viagens, controlar despesas associadas e monitorar o orçamento definido para cada viagem. Cada usuário pode criar suas viagens, adicionar despesas com datas e valores, e obter um resumo financeiro para evitar ultrapassar o orçamento planejado.

---

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

### 2.2 Arquitetura do Código

```plaintext
projeto-pos/
├── main.py           # Código principal da API com as rotas
├── models.py         # Modelos SQLModel (Usuario, Viagem, Despesa)
├── auth.py           # Funções para hash e verificação de senha
├── requirements.txt  # Dependências do projeto
└── banco.db          # Banco de dados SQLite local
```

---

## 3. Etapas de Entrega (Cronograma Detalhado)

| Etapa       | Data         | Tarefa Principal             | Descrição                                                                                   |
| ----------- | ------------ | ---------------------------- | ------------------------------------------------------------------------------------------- |
| **Etapa 1** | 27/07        | Finalização do backend       | Concluir implementação das rotas, modelos, autenticação, lógica de viagens e despesas.      |
| **Etapa 2** | 02/08        | Desenvolvimento da interface | Criar o frontend com HTML/JS simples para testes. Integrar com as rotas da API via fetch.   |
| **Etapa 3** | 03/08        | Ajustes finais e refinamento | Melhorar usabilidade, corrigir erros, revisar fluxo, documentação e preparar entrega final. |
