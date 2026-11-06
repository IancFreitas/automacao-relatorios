---
name: gridcraft
description: Cria e analisa planilhas com o GridCraft (clone open-source do Excel em Rust) pela linha de comando ou MCP — preencher células e intervalos, 500+ funções (incluindo matrizes dinâmicas, LET, LAMBDA, PROCV/XLOOKUP), formatos de número, negrito e cores, tabelas, ordenação e filtros, gráficos (colunas, barras, linhas, pizza, dispersão…), formatação condicional e tabelas dinâmicas; lê e grava XLSX, CSV, TSV, JSON e HTML, abre XLS antigo e importa XLSB/ODS; avalia fórmulas e lê intervalos direto do terminal. Use quando o usuário pedir planilhas, tabelas com cálculo, relatórios de métricas, gráficos a partir de dados, converter XLSX/CSV, ler dados de um Excel, testar uma fórmula, ou mencionar GridCraft ou "excel".
---

# GridCraft

GridCraft (github.com/storytold/gridcraft) é uma planilha no estilo Excel, com o XLSX como formato
nativo. Todo botão da faixa e atalho é um **comando** com id (~340 comandos), e o motor de cálculo
tem 514 funções.

> Faz parte da família ArtCraft. Para escolher o app e encadear apps, veja a skill `artcraft`.
> Passagens comuns: dados e gráficos vão para o DeckCraft (`insert.chart` lá aceita `categories`/
> `series`) e para o WordCraft; o CSV/JSON alimenta a mala direta do WordCraft.

## 1. Garantir a CLI

```sh
bash .claude/skills/gridcraft/scripts/instalar.sh
```

## 2. Descobrir comandos e funções

```sh
gridcraft-cli commands --search sort          # (--json para máquina)
gridcraft-cli functions --search lookup       # funções de planilha
```

Catálogos gerados da CLI: `references/comandos.md` e `references/funcoes.md`.

## 3. CLI

| Subcomando | Uso |
|---|---|
| `run [--in ARQ \| --sample budget\|sales\|grades] [--cmd 'id={json}']… [--script ARQ.jsonl] [--out ARQ] [--print A1:D10]` | Roda comandos e salva (formato pela extensão). |
| `cat ARQ [--range A1:D20] [--sheet S] [--formulas] [--csv]` | Mostra um intervalo no terminal (valores ou fórmulas). |
| `eval FÓRMULA [--in ARQ] [--sheet S] [--cell A1]` | Calcula uma fórmula, opcionalmente sobre uma planilha. |
| `convert IN OUT [--sheet NOME]` / `info ARQ` | xlsx/csv/tsv/json/html / abas, intervalos usados, tabelas, gráficos. |
| `check ARQ…` | Recalcula e compara com os valores salvos (fidelidade do arquivo). |
| `mcp [--connect PORTA] [--in ARQ \| --sample NOME]` | Servidor MCP. |

## 4. Receitas (testadas)

`plan.jsonl`, uma tabela de audiência com fórmulas, formatação, ordenação e gráfico:

```jsonl
{"command":"range.setValues","params":{"range":"A1","values":[["Episódio","Views","Likes","Taxa"],["Iara",5100,420,"=C2/B2"],["Saci",3400,310,"=C3/B3"],["Curupira",1200,95,"=C4/B4"],["Total","=SUM(B2:B4)","=SUM(C2:C4)","=C5/B5"]]}}
{"command":"home.bold","params":{"range":"A1:D1","on":true}}
{"command":"home.numberFormat","params":{"range":"D2:D5","format":"Percentage"}}
{"command":"data.sort","params":{"range":"A1:D4","header":true,"keys":[{"column":"B","order":"desc"}]}}
{"command":"insert.chart","params":{"range":"A1:B4","type":"column","title":"Views por episódio","at":"F2"}}
```

```sh
gridcraft-cli run --script plan.jsonl --out audiencia.xlsx --print A1:D5
gridcraft-cli cat audiencia.xlsx --range A1:D5            # conferir valores calculados
gridcraft-cli cat audiencia.xlsx --range A1:D5 --formulas
gridcraft-cli convert audiencia.xlsx audiencia.csv
gridcraft-cli eval '=AVERAGE(B2:B4)' --in audiencia.xlsx
gridcraft-cli info audiencia.xlsx

# Editar um existente
gridcraft-cli run --in audiencia.xlsx --cmd 'cell.set={"cell":"B6","input":"=MAX(B2:B4)"}' --out audiencia.xlsx
# Ler um CSV e salvar como Excel
gridcraft-cli convert dados.csv dados.xlsx
```

Regras práticas:
- `range.setValues {range: "A1", values: [[…]]}` escreve um bloco a partir da célula; textos que
  começam com `=` viram fórmulas. Uma célula: `cell.set {cell, input}`.
- Formatação recebe `range`: `home.bold`, `home.fillColor {color}`, `home.numberFormat {format}`
  ("Currency", "Percentage", "Short Date" ou um código como "0.00").
- Tabela formatada: `insert.table {range, header: true, style}`; ordenação: `data.sort {range, header, keys}`.
- Gráficos: `insert.chart {range, type, title, at}`.
- Os nomes das funções são os do Excel em inglês (`SUM`, `AVERAGE`, `XLOOKUP`…), não os do Excel em português.

## 5. Via MCP

```sh
claude mcp add gridcraft -- gridcraft-cli mcp --in /abs/planilha.xlsx      # headless
claude mcp add gridcraft-app -- gridcraft-cli mcp --connect 7979           # app aberto (gridcraft --control 7979)
```

Ferramentas: `execute_command`, `list_commands`, `inspect_workbook`, `read_range`, `write_range`,
`set_cell`, `get_cell`, `evaluate_formula`, `select`, `format_range`, `insert_chart`, `create_table`,
`sort_range`, `filter`, entre outras. Este servidor não tem flags de confinamento de pasta.

## 6. Cuidados

- XLS antigo abre só com valores, fórmulas e formatos de número (sem formatação/objetos); XLSB e
  ODS entram com os valores salvos, sem fórmulas.
- App em alfa: confira os números com `cat` antes de entregar.
