# Instruções para o repositório Hermathena

Estas diretrizes orientam toda contribuição — humana ou assistida por IA — à
documentação, aos materiais e às ferramentas do **Projeto Hermathena**
(comunicação, educação e engajamento público do Radiotelescópio BINGO).

## Tom e voz

Toda comunicação deve ser **sóbria e formal, porém moderna e agradável, com tom
científico e tecnológico**. Em termos práticos:

- **Sóbrio e formal** — precisão, respeito institucional, ausência de
  sensacionalismo e de juízos não fundamentados.
- **Moderno e agradável** — frases claras e bem construídas, ritmo legível,
  terminologia atual, sem arcaísmo nem jargão gratuito.
- **Científico/tecnológico** — rigor conceitual, dados verificáveis, unidades e
  referências corretas.

Atributos da voz **Hermathena**: *Acessível · Inspirador · Preciso · Respeitoso ·
Entusiasta*. O entusiasmo nunca deve comprometer a precisão.

### Escreva assim

- Prefira a voz ativa e o presente do indicativo.
- Uma ideia por período; evite cadeias longas de orações subordinadas.
- Defina siglas na primeira ocorrência: "Oscilações Acústicas de Bárions (BAO)".
- Use unidades e grandezas conforme o SI, com espaço antes da unidade (`21 cm`,
  `1,4 GHz`, `R$ 132.160,00`).
- Referencie fontes, dados e créditos sempre que houver afirmação factual.

### Evite

- Emojis, exclamações e superlativos em texto institucional ou técnico.
- Gírias, regionalismos coloquiais e abreviações informais (`vc`, `pq`, `blz`).
- Mistura de idiomas sem critério; o padrão do projeto é **português (pt-BR)**.
- Afirmações não verificadas, promessas vagas e "encher linguiça".
- Uso de cor como único portador de informação (acessibilidade).

## Idioma

Documentação, guias e materiais oficiais em **pt-BR**. Termos técnicos
consagrados podem permanecer em inglês quando forem a forma canônica de uso
(ex.: *intensity mapping*, *pipeline*, *backend*), sem tradução forçada.

## Identidade visual

Qualquer artefato visual (site, CSS, apresentações, impressos) deve respeitar as
diretrizes de marca. Resumo operacional:

- **Tipografia** — *Outfit* para títulos, chamadas e métricas; *Inter* para corpo,
  tabelas, legendas e interface.
- **Paleta** — 9 cores cadastradas (ver guia editorial). Contraste é diagnóstico.
- **Hierarquia** — cores **primárias** dominam áreas e textos; **secundárias**
  para contraste; **acento** (até 4) em alto contraste com primária/secundária.
- **Restrição** — ciano, roxo e ouro **não** devem ser usados como cores primárias.
- **Logotipo** — tamanho fixo por aplicação (cabeçalho, thumbnail, favicon);
  variações em grafite, laranja Uirapuru, ciano e versões preto/branco.
- **Editorias** — os esquemas de cor do portal derivam dos eixos temáticos do
  projeto, preservando em larga escala o layout de `bingotelescope.org`.

## Referências do repositório

- Guia editorial e de identidade: `book/06_material/02_guia-editorial.md`.
- Diretrizes de marca (BR01): `src/BINGO_visual_lab/Estudo_Id_Visual_01/`.
- Diretriz de identidade/visual lab: `.github/prompts/id.md`.

## Ao editar este repositório

- Respeite o padrão MyST Markdown e a estrutura em `book/`.
- Mantenha coerência com o conteúdo existente antes de introduzir novos termos.
- Ao alterar tom ou terminologia, prefira edições incrementais e verificáveis.
