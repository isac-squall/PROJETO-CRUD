# Todo Streamlit App

Este projeto é uma aplicação simples de gerenciamento de tarefas (CRUD) construída com Streamlit. A aplicação permite que os usuários adicionem, editem e removam tarefas de uma lista.

## Estrutura do Projeto

```
todo-streamlit-app
├── src
│   ├── app.py          # Ponto de entrada da aplicação Streamlit
│   ├── models
│   │   └── task.py     # Definição da classe Task
│   ├── services
│   │   └── crud.py     # Funções para operações CRUD
│   └── utils
│       └── __init__.py # Inicializador do pacote utils
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação do projeto
```

## Instalação

Para instalar as dependências do projeto, execute o seguinte comando:

```
pip install -r requirements.txt
```

## Execução

Para executar a aplicação, utilize o seguinte comando:

```
streamlit run src/app.py
```

## Funcionalidades

- Adicionar novas tarefas
- Editar tarefas existentes
- Remover tarefas
- Marcar tarefas como concluídas

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.