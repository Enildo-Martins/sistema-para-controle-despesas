
# Sistema de Controle de Despesas Pessoais 💰

## 📋 Descrição do Sistema

Este sistema tem como objetivo auxiliar o usuário no registro e controle de seus gastos diários.

Principais funcionalidades:
- Cadastro de categorias de despesa (ex: alimentação, transporte, lazer);
- Registro de novas despesas com valor, data (DD-MM-YYYY), categoria, descrição e status (Paga ou Pendente);
- Consulta de despesas por período (mês ou semana);
- Exibição do total de despesas por categoria;
- Geração de relatório simples das despesas do mês atual;
- Relatório adicional exclusivo para visualização das despesas pendentes;
- Interface no terminal aprimorada com a biblioteca `colorama`, proporcionando uma melhor visualização para o usuário.

O sistema utiliza um arquivo `.json` como armazenamento de dados, garantindo simplicidade e facilidade de uso.

---

## 🏗️ Arquitetura do Sistema

**Estilo arquitetural:** MVC (Model-View-Controller)

**Organização do código:**
- **Model (`model.py`)**: Manipulação dos dados e persistência no arquivo JSON.
- **View (`view.py`)**: Interface do usuário via terminal, menus e relatórios coloridos com `colorama`.
- **Controller (`controller.py`)**: Regras de negócio, validações e integração entre Model e View. Inclui validação de datas no formato brasileiro DD-MM-YYYY.
- **Main (`main.py`)**: Ponto de entrada da aplicação.

---

## 🧩 Diagrama do Sistema

```
[Usuário]
    ↓
[View (Terminal, colorama)]
    ↓
[Controller (Regras de Negócio)]
    ↓
[Model (Manipulação de Dados)]
    ↔
[data.json (Armazenamento de Dados)]
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Bibliotecas:**
  - `json`: Armazenamento simples e eficiente.
  - `datetime`: Manipulação e filtragem de datas.
  - `colorama`: Interface colorida no terminal para melhor usabilidade.

**Justificativas:**
- Python: Simples, fácil de aprender e rápido para desenvolvimento.
- JSON: Banco de dados leve e sem dependências externas.
- Colorama: Interface de terminal mais amigável e organizada.

---

## 💻 Requisitos Mínimos

- **Processador:** Dual-Core 1.0 GHz ou superior
- **Memória RAM:** 512 MB
- **Armazenamento:** 100 MB livres
- **Sistema Operacional:** Compatível com Python 3.x (Windows, Linux ou MacOS)

**Observação:**  
O sistema é leve e roda em praticamente qualquer ambiente que suporte Python 3.x.

---

## ✅ Conclusão

Este projeto foi desenvolvido seguindo as melhores práticas de arquitetura de software para atender à atividade acadêmica proposta.

Diferenciais implementados:
- Campo de descrição da despesa;
- Controle de status da despesa (Paga/Pendente);
- Relatório exclusivo de despesas pendentes;
- Interface aprimorada com cores para melhor experiência do usuário;
- Datas no formato brasileiro (DD-MM-YYYY).

---

### 🚀 Como executar o projeto:

1. Clone este repositório:
   ```bash
   git clone <URL-do-repositório>
   cd <nome-da-pasta>
   ```

2. Instale as dependências:
   ```bash
   pip install colorama
   ```

3. Execute o sistema:
   ```bash
   python main.py
   ```

---

**Autor:** Enildo  
**Disciplina:** Arquitetura de Software  
**Data:** 06/04/2025