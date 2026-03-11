:::{mermaid}flowchart TB

L[Laniakea<br>Stakeholders]

V[Virgo<br>Steering Committee]

M[Magellan<br>Infraestrutura Digital]

VL[Via Láctea<br>Comunicação Educacional]

A[Andromeda<br>Engajamento Digital]

T[Triangulum<br>Comunicação de Profundidade]

L --> V
V --> M

M --> VL
M --> A
M --> T
:::

:::{mermaid}
flowchart LR

VL[Via Láctea<br>conteúdo educacional]

T[Triangulum<br>conteúdo profundo]

A[Andromeda<br>engajamento]

M[Magellan<br>plataformas]

P[Portal Web]

RS[Redes Sociais]

YT[YouTube / Podcast]

VL --> M
T --> M
A --> M

M --> P
M --> RS
M --> YT
:::

:::{mermaid}
flowchart LR

A[Demanda institucional]

B[Virgo<br>priorização]

C[Projeto ou campanha]

D[Distribuição para núcleos]

E[Produção de conteúdo]

F[Publicação]

G[Métricas e avaliação]

A --> B
B --> C
C --> D
D --> E
E --> F
F --> G
G --> B
:::

:::{mermaid}
flowchart LR

R[Pesquisa científica]

S[Roteiro]

P[Produção]

V[Validação científica]

E[Edição]

D[Distribuição]

M[Métricas]

R --> S
S --> P
P --> V
V --> E
E --> D
D --> M
:::

:::{sphinx}
flowchart TB

C[Conteúdo]

CMS[CMS / Portal]

API[APIs redes sociais]

SCH[Agendamento]

ANA[Analytics]

C --> CMS
CMS --> API
API --> SCH
SCH --> ANA
:::