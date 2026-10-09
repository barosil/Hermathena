# Visual Lab

Ferramenta restrita para explorar combinações cromáticas do Projeto Hermathena e
exportar um CSS simples. Implementa as decisões registradas em
`../../.github/prompts/id.md` e no guia editorial `../../book/06_material/02_guia-editorial.md`.

## Uso

Abra `visual-lab.html` diretamente no navegador (arquivo único, sem dependências
locais; requer conexão para as fontes Outfit/Inter via Google Fonts).

## Parâmetros disponíveis

- **Fundo** — claro (Branco quente `#F7F1E8`) ou escuro (Grafite `#2B3147`).
- **Número de cores** — 2 (primária + secundária), 3 (+1 acento) ou 4 (+2 acentos).
- **Papéis** — seleção de cor primária, secundária e acentos a partir das 9 cores da
  paleta BR01.
- **Eixo temático** — opção de partir de um preset por eixo (ver abaixo).
- **Exportação** — gera um CSS com variáveis e estilos de exemplo.

## Regras aplicadas

- Ciano (`#22D3EE`), roxo (`#5A3FB2`) e ouro (`#C9A34A`) **não** podem ser cores
  primárias (ficam bloqueados no seletor).
- Cada **acento** deve manter contraste ≥ 4,5:1 com a primária e a secundária; o
  diagnóstico indica as combinações que não atendem.
- O contraste fundo × texto é verificado automaticamente.
- A cor nunca é o único portador de informação (a prévia usa rótulos e filetes).

## Mapeamento provisório dos eixos — PROPOSTA

A atribuição de cor por eixo temático está registrada como **A DECIDIR** nos
documentos BR01. O laboratório traz o mapeamento abaixo como **proposta**, a ser
homologada pela equipe. Edite o bloco `EIXOS` em `visual-lab.html` para consolidar
a decisão.

| Eixo | Primária | Secundária | Acento |
| --- | --- | --- | --- |
| Tengre | Azul céu profundo `#08268F` | Grafite `#2B3147` | Laranja Uirapuru `#F28A34` |
| Shiva Nataraja | Grafite `#2B3147` | Azul céu profundo `#08268F` | BINGO ouro `#C9A34A` |
| Sun Wukong | Azul céu profundo `#08268F` | Grafite `#2B3147` | Electric cyan `#22D3EE` |
| Tekoha | Grafite `#2B3147` | Azul céu profundo `#08268F` | Laranja Uirapuru `#F28A34` |
| Urania | Azul céu profundo `#08268F` | Grafite `#2B3147` | BINGO ouro `#C9A34A` |
| Guaraci | Grafite `#2B3147` | Azul céu profundo `#08268F` | Electric cyan `#22D3EE` |

> **Nota técnica.** A restrição de contraste para o acento (≥ 4,5:1 simultaneamente
> com primária e secundária) limita as combinações válidas a pares escuros (grafite,
> azul céu profundo) com acentos claros (laranja, ouro, cyan). Essa é a razão pela
> qual a proposta repete pares de fundo entre eixos, variando o acento.
