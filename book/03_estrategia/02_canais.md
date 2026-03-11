
# Estratégia Multicanal

# Canais Digitais

## Estratégia Multicanal

O Projeto Hermathena adota uma estratégia de comunicação multicanal, onde cada plataforma tem uma função específica no ecossistema de comunicação:

```
┌─────────────────────────────────────────────────────────────────┐
│                 ECOSISTEMA DIGITAL HERMATHENA                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│                        ┌───────────┐                           │
│                        │  PORTAL   │                           │
│                        │   WEB     │ ← Central de conteúdo    │
│                        │  (Base)   │                           │
│                        └─────┬─────┘                           │
│                              │                                  │
│        ┌─────────────────────┼─────────────────────┐           │
│        │                     │                     │           │
│        ▼                     ▼                     ▼           │
│   ┌─────────┐          ┌─────────┐          ┌─────────┐       │
│   │ ENGAJAR │          │APROFUNDAR│          │ NOTIFICAR│       │
│   │         │          │         │          │         │       │
│   │Instagram│          │YouTube  │          │ Email   │       │
│   │ Facebook│          │Spotify  │          │ WhatsApp│       │
│   │ TikTok  │          │Blog     │          │         │       │
│   └─────────┘          └─────────┘          └─────────┘       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 1. Portal Web (bingotelescope.org)

### Função
Central de conteúdo e repositório oficial de todos os materiais do projeto.

### Estrutura Proposta

```
bingotelescope.org/
├── /
│   ├── Hero: O que é o BINGO
│   ├── Últimas notícias
│   ├── Próximos eventos
│   └── Chamada para ação (newsletter)
│
├── /sobre
│   ├── O projeto BINGO
│   ├── Colaboração internacional
│   ├── Equipe brasileira
│   └── Linha do tempo
│
├── /para-quem
│   ├── /estudantes (Fundamental, Médio)
│   ├── /educadores (Materiais didáticos)
│   ├── /pesquisadores (Publicações técnicas)
│   └── /publico-geral (Conteúdo acessível)
│
├── /noticias
│   ├── /tekoha (Notícias locais)
│   ├── /urania (Notícias gerais)
│   └── /guaraci (Institucional)
│
├── /eixos
│   ├── /tengre (Fundamental)
│   ├── /shiva-nataraja (Médio)
│   ├── /sun-wukong (Técnico)
│   └── /guaraci (Institucional)
│
├── /materiais
│   ├── Download de cartilhas
│   ├── Vídeos
│   ├── Podcasts
│   └── Infográficos
│
├── /visite
│   ├── Como chegar
│   ├── Agendamento de visitas
│   ├── Roteiros virtuais
│   └── FAQ
│
└── /contato
    ├── Formulário
    ├── Imprensa
    └── Parcerias
```

### Funcionalidades

| Funcionalidade | Descrição | Prioridade |
|----------------|-----------|------------|
| Sistema de busca | Encontrar conteúdo por tema, faixa etária, formato | Alta |
| Newsletter | Cadastro para boletim quinzenal | Alta |
| Downloads | Materiais em PDF, vídeos | Alta |
| Agendamento | Sistema de marcação de visitas | Média |
| Blog | Artigos e notícias | Alta |
| Multilíngue | Português e inglês | Média |
| Acessibilidade | Contraste, fontes, leitor de tela | Alta |

### Especificações Técnicas

- **Plataforma:** WordPress ou similar (CMS)
- **Hospedagem:** VPS ou cloud (AWS, DigitalOcean)
- **CDN:** CloudFlare para performance
- **Analytics:** Google Analytics + Hotjar
- **SEO:** Yoast ou RankMath

---

## 2. Instagram

### Estratégia de Conteúdo

#### Tipos de Post

| Formato | Frequência | Objetivo |
|---------|------------|----------|
| **Carrossel educativo** | Diário | Educação |
| **Reels** | 3x/semana | Viralização |
| **Stories** | Diário | Engajamento |
| **Live** | 2x/mês | Interação |

#### Linhas Editoriais

**#CosmoEm60Segundos**
- Explicações rápidas de conceitos
- Curiosidades astronômicas
- Duração: 15-30 segundos

**#BINGONoDetalhe**
- Bastidores
- Entrevistas curtas
- Mostra de equipamentos

**#ParaibaNoEspaco**
- Conexão com o Sertão
- Belezas do Vale do Piancó
- Histórias locais

**#DesafioSTEM**
- Quiz interativos
- Desafios práticos
- Gamificação

### Calendário Editorial (Exemplo Semanal)

| Dia | Manhã | Tarde | Noite |
|-----|-------|-------|-------|
| Seg | - | Carrossel: Curiosidade | Stories: Bastidor |
| Ter | Stories: Enquete | Carrossel: Conceito | Reels: Experimentos |
| Qua | - | Carrossel: História | Stories: Q&A |
| Qui | Stories: Quiz | Carrossel: Notícia | Reels: Time-lapse |
| Sex | - | Carrossel: Próximo evento | Stories: Fim de semana |
| Sáb | Stories: Comunidade | - | Reels: Destaque semana |
| Dom | - | Carrossel: Inspiração | Stories: Previsão semana |

### Métricas

- **Seguidores:** Meta 5.000 (ano 1)
- **Engajamento:** >5%
- **Alcance:** 100.000/mês
- **Saves:** Indicador de valor educacional

---

## 3. YouTube

### Estratégia de Conteúdo

#### Séries de Vídeos

| Série | Formato | Frequência | Duração |
|-------|---------|------------|---------|
| **Cosmologia para Todos** | Educativo | 2x/mês | 8-12 min |
| **Construindo o BINGO** | Documental | 1x/mês | 10-15 min |
| **Pergunte ao Cientista** | Q&A | Semanal | 5-10 min |
| **Bastidores da Ciência** | Vlog | Mensal | 15-20 min |

#### Estrutura de Vídeo

```
┌─────────────────────────────────────────────────────────────┐
│ 00:00 - VINHETA (5s)                                        │
│ 00:05 - HOOK/TEASER (10-15s)                                │
│     "Você sabia que...?"                                    │
│ 00:20 - INTRODUÇÃO (30s)                                    │
│     Apresentação do tema                                    │
│ 00:50 - DESENVOLVIMENTO (corpo do vídeo)                    │
│     Conteúdo principal                                      │
│ 08:00 - CONCLUSÃO (1 min)                                   │
│     Resumo e takeaways                                      │
│ 09:00 - CALL-TO-ACTION (30s)                                │
│     "Inscreva-se, comente, compartilhe"                     │
│ 09:30 - TELA FINAL (20s)                                    │
│     Links e recomendações                                   │
└─────────────────────────────────────────────────────────────┘
```

### Otimização para SEO

- **Título:** Palavra-chave + curiosidade (máx. 60 caracteres)
- **Thumbnail:** Texto grande, contraste alto, rosto humano
- **Descrição:** Primeiras 2 linhas com keywords
- **Tags:** 5-8 tags relevantes
- **Legendas:** Sempre ativadas (acessibilidade + SEO)

---

## 4. Spotify (Podcasts)

### Programas

#### "Cosmos em Foco" (Principal)

- **Formato:** Entrevista
- **Duração:** 30-45 minutos
- **Frequência:** Quinzenal
- **Estrutura:**
  1. Intro (3 min) - Notícias astronômicas
  2. Entrevista (25-35 min) - Tema aprofundado
  3. Encerramento (2 min) - Próximos episódios

#### "BINGO Minuto" (Micro-podcast)

- **Formato:** Notícias rápidas
- **Duração:** 5-8 minutos
- **Frequência:** Semanal
- **Conteúdo:** Atualizações do projeto, curiosidades

### Dicas de Produção

- **Áudio:** Microfone de qualidade, ambiente tratado
- **Edição:** Remover hesitações, normalizar volume
- **Música:** Intro/outro curto (5-10s)
- **Show notes:** Descrição completa com links

---

## 5. Email Marketing

### Estratégia

#### Tipos de Email

| Tipo | Frequência | Conteúdo |
|------|------------|----------|
| **Newsletter** | Quinzenal | Resumo de notícias, destaques |
| **Alerta de evento** | Eventual | Próximas atividades |
| **Boletim interno** | Mensal | Para educadores parceiros |
| **Relatório** | Trimestral | Para financiadores |

#### Estrutura da Newsletter

```
┌─────────────────────────────────────────┐
│ HEADER                                  │
│ Logo + Data                             │
├─────────────────────────────────────────┤
│ DESTAQUE PRINCIPAL                      │
│ Imagem + Título + Resumo + CTA          │
├─────────────────────────────────────────┤
│ NOTÍCIAS (3 itens)                      │
│ • Título + 2 linhas + link              │
├─────────────────────────────────────────┤
│ PRÓXIMOS EVENTOS                        │
│ Lista de atividades programadas         │
├─────────────────────────────────────────┤
│ DESTAQUE REDES SOCIAIS                  │
│ Melhor post da semana + CTA seguir      │
├─────────────────────────────────────────┤
│ FOOTER                                  │
│ Contato + Unsubscribe                   │
└─────────────────────────────────────────┘
```

### Ferramentas

- **Mailchimp** (gratuito até 500 contatos)
- **Sendinblue**
- **Google Groups** (para listas internas)

---

## 6. TikTok

### Estratégia

Diferente do Instagram, o TikTok demanda:
- **Tom mais descontraído**
- **Edição dinâmica** (cortes rápidos)
- **Músicas trending**
- **Participação em trends educativas**

#### Formatos

| Formato | Descrição | Exemplo |
|---------|-----------|---------|
| **Explicação rápida** | Conceito em 60s | "Por que o céu é azul?" |
| **React** | Reagindo a mitos astronômicos | "O que você aprendeu errado..." |
| **POV** | "POV: Você é um fotão" | Narrativa em primeira pessoa |
| **Duet** | Responder perguntas | Interação com seguidores |
| **Behind the scenes** | Bastidores divertidos | "Um dia no BINGO" |

---

## 7. Calendário Editorial Integrado

### Exemplo de Semana Tipo

| Dia | Canal | Conteúdo | Responsável |
|-----|-------|----------|-------------|
| **Seg** | Instagram | Carrossel: "O que são BAO?" | Andromeda |
| **Seg** | Portal | Publicação de artigo | Via Láctea |
| **Ter** | YouTube | Vídeo novo | Triangulum |
| **Ter** | Instagram | Reels: Experimento caseiro | Andromeda |
| **Qua** | Spotify | Episódio de podcast | Triangulum |
| **Qua** | Instagram | Stories: Enquete | Andromeda |
| **Qui** | TikTok | Vídeo viral educativo | Andromeda |
| **Qui** | Instagram | Carrossel: Notícia da semana | Via Láctea |
| **Sex** | Email | Newsletter quinzenal | Via Láctea |
| **Sex** | Instagram | Stories: Próxima semana | Andromeda |
| **Sáb** | YouTube | Shorts: Curiosidade rápida | Triangulum |
| **Dom** | Instagram | Reels: Melhores momentos | Andromeda |

---

## 8. Métricas por Canal

### Dashboard de Acompanhamento

| Canal | Métrica Principal | Meta Ano 1 |
|-------|-------------------|------------|
| Portal | Visitas/mês | 1.000 |
| Portal | Tempo médio | >3 min |
| Instagram | Seguidores | 5.000 |
| Instagram | Engajamento | >5% |
| YouTube | Inscritos | 2.000 |
| YouTube | Horas assistidas | 500/mês |
| Spotify | Downloads/mês | 500 |
| Spotify | Retenção | >50% |
| TikTok | Seguidores | 3.000 |
| Email | Taxa abertura | >25% |
| Email | Assinantes | 1.000 |

### Ferramentas de Análise

| Função | Ferramenta |
|--------|------------|
| Analytics portal | Google Analytics |
| Heatmaps | Hotjar |
| Social media | Metricool / Sprout Social |
| YouTube | YouTube Analytics |
| Spotify | Spotify for Podcasters |
| Email | Relatórios nativos |

---

## 9. Políticas e Diretrizes

### Tom de Voz

| Característica | Descrição |
|----------------|-----------|
| **Acessível** | Linguagem simples, evitar jargões |
| **Inspirador** | Celebrar conquistas, motivar curiosidade |
| **Preciso** | Informações cientificamente corretas |
| **Respeitoso** | Valorizar saberes locais |
| **Entusiasta** | Demonstrar paixão pela ciência |

### Não fazer

- ❌ Publicar sem revisão de conteúdo científico
- ❌ Ignorar comentários e mensagens
- ❌ Usar imagens sem direitos autorais
- ❌ Prometer o que não pode cumprir
- ❌ Publicar em horários irregulares
- ❌ Copiar conteúdo de outros sem crédito

---

## 10. Recursos Necessários

### Ferramentas (Assinaturas)

| Ferramenta | Custo Mensal | Função |
|------------|--------------|--------|
| Canva Pro | R$ 50 | Design de posts |
| Metricool | R$ 80 | Agendamento e analytics |
| Adobe CC | R$ 150 | Edição profissional |
| Mailchimp | R$ 0-100 | Email marketing |
| **Total** | **~R$ 380/mês** | |

### Equipe Dedicada

| Função | Dedicada a | Tempo |
|--------|-----------|-------|
| Social Media Manager | Todas as redes | 40h/semana |
| Designer | Visual | 20h/semana |
| Redator | Conteúdo escrito | 20h/semana |
| Editor de vídeo | YouTube, Reels | 30h/semana |

---

*Canais e estratégias sujeitos a evolução conforme métricas e novas plataformas.*
