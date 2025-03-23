# Impacta : Trabalho final
# Disciplina: Python for Data Engineer

## Descrição

Este projeto tem como objetivo realizar a limpeza e transformação de um conjunto de dados de voos, utilizando a linguagem Python e a biblioteca Pandas. Os dados são extraídos de um arquivo CSV, tratados e armazenados em um banco de dados SQLite.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos:

main.py - Script principal que executa o pipeline de processamento dos dados.

data_clean.py - Módulo responsável pela limpeza e padronização dos dados.

transform.py - Módulo de transformação dos dados, incluindo cálculo do tempo de voo em horas e determinação do período do dia da decolagem.

utils.py - Contém funções auxiliares para a criação do banco de dados.

## Dependências

Para executar este projeto, certifique-se de ter instalado:

Python 3.x

Pandas

Numpy

SQLAlchemy

SQLite3

## Para instalar as dependências necessárias, utilize:

pip install pandas numpy sqlalchemy

## Execução

Baixe ou clone este repositório.

Execute o script main.py:

python main.py

## Fluxo de Processamento

Carregamento do dataset a partir de um arquivo CSV.

Validação e limpeza de colunas.

Remoção de duplicatas e registros nulos.

Padronização dos campos de texto.

Cálculo do tempo de voo em horas.

Identificação do período do dia com base no horário de partida.

Armazenamento dos dados tratados em um banco de dados SQLite.

## Exemplo de Saída

Após a execução, os primeiros 10 registros são exibidos no terminal a partir do banco SQLite.
