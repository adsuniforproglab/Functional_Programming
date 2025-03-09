# CRUD de Usuários com Programação Funcional

Este projeto demonstra a aplicação de conceitos de programação funcional em uma aplicação CRUD (Create, Read, Update, Delete) web usando Flask e SQLAlchemy para gerenciamento de usuários.

## Sobre o Projeto

Esta aplicação foi desenvolvida como um exemplo prático de como os princípios da programação funcional podem ser aplicados em uma aplicação web Python para criar código mais limpo, testável e manutenível.

## Conceitos de Programação Funcional Implementados

### 1. Funções Puras
Funções que não possuem efeitos colaterais e sempre retornam o mesmo resultado para os mesmos argumentos.

- `para_maiusculo(texto)`: Converte texto para maiúsculo
  ```python
  # Exemplo: para_maiusculo("nome") -> "NOME"
  ```
- `para_minusculo(texto)`: Converte texto para minúsculo
  ```python
  # Exemplo: para_minusculo("NOME") -> "nome"
  ```
- `capitalizar(texto)`: Capitaliza o texto
  ```python
  # Exemplo: capitalizar("nome") -> "Nome"
  ```
- `contar_caracteres(texto)`: Conta caracteres em uma string
  ```python
  # Exemplo: contar_caracteres("nome") -> 4
  ```

### 2. Funções de Alta Ordem
Funções que recebem outras funções como parâmetros ou retornam funções.

- `compor(f, g)`: Combina duas funções em uma
  ```python
  # Exemplo: compor(para_maiusculo, capitalizar)("nome") -> "NOME"
  ```
- `aplicar_a_todos(funcao, lista)`: Aplica uma função a cada elemento da lista
  ```python
  # Exemplo: aplicar_a_todos(para_maiusculo, ["a", "b"]) -> ["A", "B"]
  ```

### 3. Operações Funcionais em Coleções
- **Map**: Transformações de dados através de `map()`
  ```python
  # Exemplo: list(map(para_maiusculo, ["a", "b"])) -> ["A", "B"]
  ```
- **Filter**: Filtragem de dados através de `filter()`
  ```python
  # Exemplo: list(filter(lambda x: len(x) > 3, ["a", "abc", "abcd"])) -> ["abcd"]
  ```
- **Reduce**: Agregação de dados através de `reduce()`
  ```python
  # Exemplo: reduce(lambda x, y: x + y, [1, 2, 3]) -> 6
  ```

### 4. Outras Técnicas Funcionais
- **List Comprehension**: Criação concisa de listas
  ```python
  # Exemplo: [x.upper() for x in ["a", "b"]] -> ["A", "B"]
  ```
- **Funções Lambda**: Funções anônimas para operações curtas
  ```python
  # Exemplo: lambda x: x * 2
  ```
- **Composição de Funções**: Combinação de funções pequenas para criar operações complexas
  ```python
  # Exemplo: f(g(h(x)))
  ```

## Por que usar Programação Funcional?

1. **Código mais legível**: Funções pequenas com propósito único são mais fáceis de entender e manter.
2. **Menos bugs**: Funções puras são previsíveis, testáveis e não possuem efeitos colaterais.
3. **Paralelismo**: Operações sem efeitos colaterais podem ser executadas em paralelo com segurança.
4. **Manutenibilidade**: Código funcional tende a ser mais modular, organizado e fácil de refatorar.
5. **Testabilidade**: Funções puras são mais fáceis de testar já que não dependem de estado externo.

## Requisitos

- Python 3.7+
- Flask
- SQLAlchemy
- Outras dependências listadas em `requirements.txt`

## Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/adsuniforproglab/Functional_Programming.git
cd Functional_Programming
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
python main.py
```

4. Acesse o navegador em `http://localhost:5000`

## Estrutura do Projeto

```
GRUD-UNIFOR/
├── main.py              # Ponto de entrada da aplicação
├── templates/           # Templates HTML
│   ├── index.html
│   └── ...
├── static/              # Arquivos estáticos (CSS, JS)
├── utils/               # Utilitários de programação funcional
├── models.py            # Modelos de dados
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo
```

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir um issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a licença MIT