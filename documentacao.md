# **Documentação do Projeto: Miliviaflix (nome não definitivo)**
## **1. Visão Geral**
**Tecnologia Utilizada:**

* Python
* FastAPI
* Uvicorn
* Pydantic
* OpenAI API
* SQLite
* TMDB API

**Descrição:** Implementação de uma aplicação web de recomendação de filmes personalizada com uso de inteligência artificial. </br>
**Objetivo:** Desenvolver uma plataforma onde usuários possam registrar, avaliar filmes e receber sugestões personalizadas com base em suas preferências, utilizando integração com APIs externas para enriquecimento de dados e geração de recomendações..

</br>
</br>
</br>

## **2. Descrição Detalhada do Projeto**
### **O que é projeto?**
O projeto consiste em um sistema no qual o usuário registrado poderá buscar por sugestões de filmes com base no seu gosto pessoal. Para isso, o programa contará com a funcionalidade de registro dos filmes já assistidos pelo usuário e a avaliação dele. Também contará com opções de filtros na página de recomendações para selecionar de forma mais precisa as obras. As recomendações serão propostas por uma Inteligência Artificial que será consultada através da API disponibilizada pela OpenAI, enquanto sua exibição contará com a API  do TMDB para trazer uma ficha mais detalhada dos filmes propostos. Cada usuário precisará se registrar no sistema e suas credenciais ficarão salvas em um banco de dados, assim como os dados que fornecer (como seus filmes assistidos e suas respectivas avaliações).

</br>

### **2.1 Funcionalidades Principais**
* **Funcionalidade 01:** / </br>
    método: GET </br>
    descrição: Exibe a página inicial
* **Funcionalidade 02:** /cadastro </br>
    método: GET </br>
    descrição: Exibe a página de cadastro
* **Funcionalidade 03:** /cadastro </br>
    métodos: POST </br>
    descrição: Envia os dados para cadastrar um usuário
* **Funcionalidade 04:** /login </br>
    método: GET </br>
    descrição: Exibe a página de login
* **Funcionalidade 05:** /login </br>
    método: POST </br>
    descrição: Envia os dados para logar um usuário
* **Funcionalidade 06:** /logout </br>
    método: POST </br>
    descrição: Encerra a sessão do usuário
* **Funcionalidade 07:** /{user} </br>
    método: GET </br>
    descrição: Exibe a página home
* **Funcionalidade 08:**  /{user}/meus-filmes </br>
    método: GET </br>
    descrição: Exibe uma página com os filmes assistidos e avaliados pelo usuário
* **Funcionalidade 09:**  /{user}/meus-filmes </br>
    método: POST </br>
    descrição: Permite que o usuário adicione novos filmes à sua lista
* **Funcionalidade 10:**  /{user}/meus-filmes/{movie_id} </br>
    método: GET </br>
    descrição: Exibe uma página contendo as informações de um dos filmes da lista do usuário
* **Funcionalidade 11:**  /{user}/meus-filmes/{movie_id} </br>
    método: PUT </br>
    descrição: Permite que o usuário atualize as informações que forneceu a respeito de determinado filme
* **Funcionalidade 12:**  /{user}/meus-filmes/{movie_id} </br>
    método: DELETE </br>
    descrição: Permite que o usuário delete um filme da sua lista
* **Funcionalidade 13:**  /{user}/sugerir-filmes </br>
    método: GET </br>
    descrição: Exibe uma página onde será possível especificar as característas desejadas nos filmes
* **Funcionalidade 14:**  /{user}/sugerir-filmes </br>
    método: POST </br>
    descrição: Envia uma requisição à API da OpenAI com as informações especiicadas e retorna essas sugestões na forma de cards, que possuirão informações mais detalhadas graças à API do TMDB.

</br>

### **2.2 Arquitetura do Código**

```
projeto_pos/
├── main.py            # Código principal da API
├── api.py             # Requisições à API da OpenAI
├── models.py          # Modelos com Pydantic
├── requirements.txt   # Dependências do projeto
├── database.sql       # Banco de dados da aplicação
```

</br>
</br>
</br>

## **3. Etapas de Entrega (Cronograma Detalhado)**

### Etapa 1:
**Data limite:** 15/06 </br>
**Tarefa:** Criar o design das telas </br>
**Descrição:** Definição da interface visual da aplicação, incluindo as principais páginas como login, cadastro, perfil, lista de filmes e recomendações.

### Etapa 2:
**Data limite:** 22/06 </br>
**Tarefa:** Implementar o HTML das telas </br>
**Descrição:** Codificação das telas criadas na etapa anterior em HTML, estruturando a interface para posterior integração com o backend.

### Etapa 3:
**Data limite:** 29/06 </br>
**Tarefa:** Criar o banco de dados e rotas de autenticação </br>
**Descrição:** Estruturação do banco de dados e desenvolvimento das rotas de cadastro, login, logout e, se possível, edição de perfil e exclusão de conta.

### Etapa 4:
**Data limite:** 06/07 </br>
**Tarefa:** Criar rotas da lista de filmes e integrar com TMDB </br>
**Descrição:** Implementação das rotas para gerenciar a lista de filmes do usuário (CRUD) e integração com a API do TMDB para exibição dos dados dos filmes.

### Etapa 5:
**Data limite:** 13/07 </br>
**Tarefa:** Criar rota de recomendação e tela de filtros </br>
**Descrição:** Desenvolvimento da funcionalidade de recomendação com integração à API da OpenAI, criação da interface com filtros e exibição dos resultados enriquecidos com a API do TMDB.
