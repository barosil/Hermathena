# Plano de Trabalho — Magellan: Infraestrutura Tecnológica

## 1. Identificação

| Campo | Informação |
|-------|-----------|
| **Título do Plano** | Desenvolvimento do Portal Web e Sistemas de Automação |
| **Projeto Vinculado** | Magellan — Tecnologia da Informação (Programa Hermathena) |
| **Discente** | [Nome do(a) bolsista] |
| **Orientador** | Prof. [Nome do(a) orientador(a)] |
| **Período** | 12 meses (24h/semana ≈ 1.248h totais) |
| **Carga Horária Semanal** | 24h |
| **Local de Realização** | Laboratório de Informática UFCG / Remoto |

---

## 2. Contextualização

O Núcleo Magellan é responsável por toda a infraestrutura tecnológica do Programa Hermathena. O bolsista atuará no desenvolvimento e manutenção do **Portal Web do BINGO**, sistemas de **automação de publicações**, **dashboard de indicadores** e **chatbot** para atendimento ao público. Este conjunto de ferramentas é a espinha dorsal digital do programa, sem a qual os demais núcleos não podem operar de forma eficiente.

O bolsista aplicará conhecimentos de **desenvolvimento web (React/Next.js, Python/Django)**, **banco de dados (PostgreSQL)** e **DevOps (Docker, CI/CD)** em um projeto real de comunicação científica, integrando teoria e prática de engenharia de software.

---

## 3. Objetivos

### Objetivo Geral

Desenvolver e manter a infraestrutura tecnológica do Programa Hermathena, incluindo portal web, sistemas de automação e ferramentas de suporte à comunicação científica.

### Objetivos Específicos

1. Projetar e implementar o **Portal Web do BINGO** com CMS customizado
2. Desenvolver **sistema de automação** para agendamento e publicação em redes sociais
3. Criar **dashboard de indicadores** para acompanhamento de métricas do programa
4. Implementar **chatbot** para atendimento ao público e FAQ
5. Garantir **infraestrutura de servidores**, backup e segurança

---

## 4. Metodologia

### 4.1 Ciclo de Desenvolvimento

**Scrum adaptado** com sprints quinzenais:

| Dia | Atividade |
|-----|-----------|
| Seg-Qua | Desenvolvimento (código, testes) |
| Qui | Code review, documentação |
| Sex | Validação com orientador, planejamento próxima sprint |

### 4.2 Stack Tecnológico

| Camada | Tecnologia |
|--------|-----------|
| **Frontend** | React / Next.js, Tailwind CSS |
| **Backend** | Python (Django / FastAPI) ou Node.js |
| **Banco** | PostgreSQL, Redis (cache) |
| **DevOps** | Docker, GitHub Actions |
| **Cloud** | AWS / Google Cloud |
| **Testes** | Jest, Playwright |

### 4.3 Arquitetura do Portal

```
bingo-portal/
├── frontend/              # Next.js App
│   ├── components/        # Componentes reutilizáveis
│   ├── pages/             # Rotas e páginas
│   ├── styles/            # Estilos globais
│   └── lib/               # Utilitários e hooks
├── backend/               # API Django/FastAPI
│   ├── api/               # Endpoints REST
│   ├── models/            # Modelos de dados
│   ├── services/          # Lógica de negócio
│   └── admin/             # CMS customizado
├── infrastructure/        # Docker, CI/CD
└── docs/                  # Documentação
```

---

## 5. Estrutura das Atividades (24h/semana — 12 meses)

### Fase 1 — Setup e Fundamentação (M1-M2 ≈ 192h)

| Atividade | Horas | Período | Descrição |
|-----------|:-----:|:-------:|-----------|
| Ambientação no projeto e stack | 24 | S1-S2 | Estudo da arquitetura, repositórios |
| Configuração de ambiente dev | 16 | S1-S2 | Docker, variáveis, dependências |
| Setup do repositório Git e CI/CD | 16 | S2-S3 | GitHub, Actions, lint, testes |
| Definição de arquitetura do portal | 24 | S3-S4 | Design de componentes, fluxos |
| Prototipação de UI/UX | 32 | S4-S5 | Wireframes, mockups |
| Configuração de servidores cloud | 16 | S5-S6 | VPS, domínios, SSL, backups |
| Configuração inicial do CMS | 32 | S5-S6 | Modelos de conteúdo, mídia |
| Reuniões e documentação | 32 | Contínuo | Alinhamento semanal |

### Fase 2 — Desenvolvimento do Portal (M3-M6 ≈ 416h)

| Atividade | Horas | Período | Descrição |
|-----------|:-----:|:-------:|-----------|
| API REST (CRUD de conteúdo) | 40 | S7-S8 | Endpoints, autenticação, permissões |
| Páginas públicas do portal | 48 | S8-S10 | Home, sobre, notícias, blog |
| Página de conteúdo científico | 32 | S10-S11 | Artigos, publicações, mídia |
| CMS administrativo | 48 | S11-S13 | Dashboard admin, editor de conteúdo |
| Sistema de busca | 24 | S13-S14 | Busca textual, filtros |
| Integração com redes sociais | 32 | S14-S15 | Embed, compartilhamento |
| Newsletter e formulários | 24 | S15-S16 | Cadastro, disparo |
| SEO e performance | 24 | S16-S17 | Meta tags, Lighthouse, CDN |
| Testes de integração e QA | 48 | S15-S17 | Testes E2E, correções |
| Deploy do MVP do portal | 24 | S17-S18 | Lançamento da versão 1.0 |
| Reuniões e documentação | 72 | Contínuo | Alinhamento semanal |

### Fase 3 — Automação e Dashboard (M7-M9 ≈ 312h)

| Atividade | Horas | Período | Descrição |
|-----------|:-----:|:-------:|-----------|
| Sistema de agendamento de posts | 40 | S19-S21 | Calendário editorial, fila |
| Automação de publicação multicanal | 48 | S21-S23 | API Instagram, TikTok, Facebook |
| Dashboard de indicadores | 48 | S23-S25 | Gráficos, KPIs, exportação |
| Sistema de métricas de redes sociais | 32 | S24-S25 | Coleta automatizada de analytics |
| Relatórios automáticos | 24 | S25-S26 | Geração PDF, email automático |
| Chatbot BINGO (MVP) | 40 | S26-S28 | FAQ, atendimento básico |
| Testes de automação | 32 | S27-S28 | Validação de fluxos |
| Reuniões e documentação | 48 | Contínuo | Alinhamento semanal |

### Fase 4 — Otimização e Documentação (M10-M12 ≈ 328h)

| Atividade | Horas | Período | Descrição |
|-----------|:-----:|:-------:|-----------|
| Manutenção evolutiva | 48 | S29-S32 | Correções, melhorias contínuas |
| Otimização de performance | 32 | S30-S32 | Cache, lazy loading, compressão |
| Documentação técnica | 48 | S31-S34 | README, JSDoc, guias de deploy |
| Testes de segurança | 24 | S32-S33 | Auditoria básica, CORS, SQLi |
| Treinamento da equipe | 24 | S33-S34 | Workshop de uso do CMS |
| Relatório final | 32 | S34-S35 | Resultados, métricas, lições |
| Planejamento de evolução | 16 | S35-S36 | Roadmap, próximas features |
| Reuniões e documentação | 56 | Contínuo | Alinhamento semanal |

---

## 6. Distribuição Horária Sumarizada

| Fase | Meses | Horas | Entregável Principal |
|------|:-----:|:-----:|---------------------|
| F1: Setup | M1-M2 | 192h | Ambiente configurado, protótipos |
| F2: Portal | M3-M6 | 416h | Portal Web v1.0 no ar |
| F3: Automação | M7-M9 | 312h | Sistema de automação + dashboard |
| F4: Otimização | M10-M12 | 328h | Documentação, treinamento |
| **Total** | **12 meses** | **~1.248h** | |

---

## 7. Produtos Esperados

| Produto | Prazo | Descrição |
|---------|-------|-----------|
| Portal Web v1.0 | M6 | Site institucional com CMS |
| Sistema de automação | M8 | Agendamento + publicação multicanal |
| Dashboard de KPIs | M9 | Indicadores do programa |
| Chatbot BINGO | M10 | Atendimento automatizado |
| API pública | M11 | Dados abertos do projeto |
| Documentação técnica | M12 | Guias, README, manual do CMS |
| Relatório final | M12 | Resultados e métricas |

---

## 8. Avaliação e Acompanhamento

| Instrumento | Frequência | Responsável |
|------------|-----------|-------------|
| Reunião semanal de alinhamento | Semanal | Orientador |
| Review de sprint | Quinzenal | Orientador |
| Code review | Contínuo | Orientador / pares |
| Relatório mensal de atividades | Mensal | Discente |
| Relatório final | M12 | Discente |
