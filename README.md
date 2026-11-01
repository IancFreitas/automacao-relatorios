# Automação de Relatórios de Vendas

![CI](https://github.com/IancFreitas/automacao-relatorios/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.11%2B-3776AB)
![pandas](https://img.shields.io/badge/pandas-2.x-150458)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green)

Automação em Python que substitui o trabalho manual de juntar planilhas de vendas todo mês:
ela **lê vários arquivos CSV/Excel, limpa os dados, calcula os indicadores, gera um relatório
formatado em Excel e envia um resumo por e-mail** com a planilha em anexo.

## O problema

Em muitas empresas, alguém passa horas todo mês fazendo o mesmo processo:

1. baixar as planilhas de vendas de cada sistema ou filial (cada uma num formato um pouco diferente);
2. copiar e colar tudo numa planilha só e corrigir linhas com erro;
3. montar tabelas dinâmicas por vendedor, produto e região;
4. mandar o resultado por e-mail para a gestão.

Este projeto faz tudo isso com um comando, e pode ser agendado para rodar sozinho.

## Funcionalidades

- **Leitura de múltiplos arquivos** `.csv` e `.xlsx` de uma pasta
- **Tolerante a formatos diferentes**:
  - separador `,` ou `;` detectado automaticamente;
  - datas ISO (`2026-10-05`) ou brasileiras (`05/10/2026`);
  - valores como `1234.56` ou `R$ 1.234,56`;
  - cabeçalhos com ou sem acento e em maiúsculas ou minúsculas.
- **Limpeza de dados**: descarta linhas com campos vazios, datas inválidas, quantidade ≤ 0
  e registros duplicados, informando quantas linhas foram removidas de cada arquivo
- **Indicadores**: faturamento total, número de vendas, itens vendidos, ticket médio, evolução mês a mês,
  rankings por vendedor, produto e região com participação percentual
- **Relatório Excel** com 6 abas formatadas (moeda, porcentagem, datas, cabeçalho fixo) e gráfico de faturamento mensal
- **Resumo em HTML** pronto para o corpo do e-mail
- **Envio por e-mail** via SMTP com TLS, com credenciais em variáveis de ambiente ou num arquivo `.env`
- **Filtro por mês** (`--mes 2026-10`) para o fechamento mensal

## Instalação

```bash
git clone https://github.com/IancFreitas/automacao-relatorios.git
cd automacao-relatorios
pip install .
```

## Uso

O repositório já inclui dados fictícios em [`dados/exemplo`](dados/exemplo), gerados por
[`scripts/gerar_dados_exemplo.py`](scripts/gerar_dados_exemplo.py), incluindo linhas com erro de propósito.

```bash
# Relatório com todos os dados da pasta
relatorios --entrada dados/exemplo --saida saida

# Fechamento de um mês específico
relatorios --entrada dados/exemplo --mes 2026-10

# Gerar e enviar por e-mail
relatorios --entrada dados/exemplo --mes 2026-10 --enviar-email
```

Saída:

```
WARNING vendas_2026-10.csv: 3 linha(s) inválida(s) ignorada(s).
INFO    3 arquivo(s) lidos: 629 linhas válidas, 3 rejeitadas, 2 duplicadas.
INFO    Faturamento: R$ 1.671.091,36 em 629 vendas. Relatório salvo em saida/relatorio_vendas_2026-11-01.xlsx
```

### Formato dos arquivos de entrada

| Coluna           | Exemplo                       |
|------------------|-------------------------------|
| `Data`           | `2026-10-05` ou `05/10/2026`  |
| `Vendedor`       | `Ana Lima`                    |
| `Produto`        | `Notebook Pro 14`             |
| `Região`         | `Sudeste`                     |
| `Quantidade`     | `2`                           |
| `Valor Unitário` | `5899.00` ou `5.899,00`       |

Colunas extras são ignoradas. Se faltar alguma obrigatória, o programa avisa qual e em qual arquivo.

### Configurando o envio de e-mail

Copie [`.env.exemplo`](.env.exemplo) para `.env` e preencha:

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORTA=587
SMTP_USUARIO=seu.email@gmail.com
SMTP_SENHA=sua-senha-de-app
RELATORIO_DESTINATARIOS=gestor@empresa.com,financeiro@empresa.com
```

O `.env` está no `.gitignore`, para que senhas nunca sejam versionadas. No Gmail, use uma
[senha de app](https://myaccount.google.com/apppasswords).

### Agendando a execução

**Windows (Agendador de Tarefas)**: todo dia 1º às 8h:

```powershell
schtasks /create /tn "Relatorio de Vendas" /sc monthly /d 1 /st 08:00 /tr "relatorios --entrada C:\vendas --saida C:\relatorios --enviar-email"
```

**Linux (cron)**:

```cron
0 8 1 * * cd /opt/relatorios && relatorios --entrada /dados/vendas --enviar-email
```

## Arquitetura

```
src/relatorios
├── loader.py        Leitura dos arquivos, normalização de colunas, conversão e limpeza
├── analysis.py      Indicadores e rankings (pandas groupby)
├── excel_report.py  Planilha formatada + gráfico (openpyxl)
├── email_report.py  Resumo HTML, montagem da mensagem e envio SMTP
├── formatting.py    Moeda e porcentagem no padrão brasileiro
└── cli.py           Orquestra o fluxo: carregar → resumir → gerar → enviar
```

Cada etapa é uma função independente e testável. A CLI só faz a orquestração.

## Desenvolvimento

```bash
pip install -e ".[dev]"
pytest        # testes (o envio SMTP é testado com mock, sem mandar e-mail de verdade)
ruff check .  # lint
```

O GitHub Actions roda lint e testes em Python 3.11, 3.12 e 3.13, gera o relatório com os
dados de exemplo e disponibiliza o Excel como artefato da execução.
