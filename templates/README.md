# Templates — Projeto Hermathena

Coleção de modelos oficiais para produção de material impresso, digital e
apresentações, alinhados ao [Guia Editorial e de Identidade](../book/06_material/02_guia-editorial.md)
e às diretrizes de marca BR01.

## Estrutura

```
templates/
├── latex/                 # Overleaf / LaTeX (LuaLaTeX ou XeLaTeX)
│   ├── hermathena.sty     # Identidade visual compartilhada (cores + fontes)
│   ├── carta-formal.tex   # Carta formal institucional
│   └── comunicado-oficial.tex
├── beamer/
│   └── hermathena-beamer.tex   # Apresentação (Beamer)
├── revealjs/
│   └── hermathena-reveal.html  # Apresentação (Reveal.js)
└── docx/
    └── comunicado-oficial.md   # Fonte Markdown para Pandoc
```

## Identidade aplicada

- **Tipografia** — *Outfit* (títulos) e *Inter* (corpo). O estilo LaTeX recorre a
  *Latin Modern* como reserva quando as fontes não estão instaladas.
- **Paleta** — as 9 cores BR01 estão definidas em `hermathena.sty` e em variáveis
  CSS no template Reveal.js.
- **Restrições** — ciano, roxo e ouro não são usados como cores primárias; a cor
  nunca é o único portador de informação.

## LaTeX / Overleaf

1. Envie `hermathena.sty` (e, se houver, `bingo_logo.png`) para o projeto no
   Overleaf, no mesmo diretório do `.tex`.
2. Em **Menu → Compiler**, selecione **LuaLaTeX** ou **XeLaTeX** (o estilo usa
   `fontspec`).
3. Edite o bloco de comandos `\newcommand{...}` no topo do arquivo para ajustar
   remetente, destinatário, assunto e signatário.
4. Compile. As fontes Outfit/Inter são usadas quando disponíveis no sistema.

## Apresentações

- **Beamer** — `templates/beamer/hermathena-beamer.tex` (LuaLaTeX/XeLaTeX).
- **Reveal.js** — abra `templates/revealjs/hermathena-reveal.html` no navegador.
  Requer conexão para os CDNs de Reveal.js e Google Fonts.

## DOCX / ODT (Pandoc)

O estilo do Word/LibreOffice é aplicado por um documento de referência. Gere-o uma
vez, estilizando-o com Outfit/Inter e a paleta da marca:

```bash
pandoc -o referencia.docx --print-default-data-file reference.docx
# editar referencia.docx no Word/LibreOffice (estilos Título, Corpo, etc.)
```

Depois, gere os documentos a partir da fonte Markdown:

```bash
cd templates/docx
pandoc comunicado-oficial.md -o comunicado-oficial.docx --reference-doc=referencia.docx
pandoc comunicado-oficial.md -o comunicado-oficial.odt  --reference-doc=referencia.docx
```

## Convenções de conteúdo

Todo documento deve seguir o tom definido para o projeto: sóbrio e formal, porém
moderno e agradável, com rigor científico e tecnológico. Consulte também
`../.github/copilot-instructions.md`.
