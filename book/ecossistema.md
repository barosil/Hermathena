# Ecossistema Hermathena

O Projeto Hermathena organiza as ações de comunicação científica do radiotelescópio **BINGO** como um ecossistema integrado de núcleos especializados.

Cada núcleo atua em uma dimensão específica da comunicação científica, permitindo transformar a presença do radiotelescópio no sertão paraibano em uma plataforma de **educação, inovação e desenvolvimento regional**.

```mermaid
flowchart TB

    BINGO["🔭 Radiotelescópio BINGO"]

    HER["Hermathena<br>Ecossistema de Comunicação Científica"]

    BINGO --> HER

    subgraph Nucleos["Núcleos Operacionais"]
        MAG["🛰 Magellan<br>Tecnologia"]
        VIA["🌌 Via Láctea<br>Educação"]
        AND["🌠 Andromeda<br>Engajamento"]
        TRI["🔭 Triangulum<br>Conteúdo Profundo"]
    end

    HER --> MAG
    HER --> VIA
    HER --> AND
    HER --> TRI

    MAG --> PORTAL["Portal Web"]
    MAG --> DATA["Infraestrutura digital"]

    VIA --> SCHOOL["Escolas"]
    VIA --> MATERIAL["Materiais educacionais"]

    AND --> SOCIAL["Redes sociais"]
    AND --> COMMUNITY["Comunidade"]

    TRI --> VIDEO["Documentários"]
    TRI --> POD["Podcasts"]
    TRI --> YT["YouTube"]

    PORTAL --> SOC["Sociedade"]
    SCHOOL --> SOC
    SOCIAL --> SOC
    VIDEO --> SOC
```