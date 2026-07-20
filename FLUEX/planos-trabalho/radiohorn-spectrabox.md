# Plano de Trabalho — RadioHorn / SpectraBox

## 1. Identificação

| Campo | Informação |
|-------|-----------|
| **Título do Plano** | Desenvolvimento de Frontend Web para o SpectraBox |
| **Projeto Vinculado** | Via Láctea — Comunicação Educacional (Programa Hermathena) |
| **Discente** | [Nome do(a) bolsista] |
| **Orientador** | Prof. [Nome do(a) orientador(a)] |
| **Período** | 15 semanas (350 horas totais) |
| **Carga Horária Semanal** | 24h (aproximadamente 14,5 semanas efetivas) |
| **Local de Realização** | Laboratório do Projeto Hermathena / UFCG / Remoto |

---

## 2. Contextualização

O **SpectraBox** é uma unidade de visualização e controle para radiotelescópios amadores baseados em **Rádio Definido por Software (SDR)**. O sistema capta sinais de rádio na faixa de radioastronomia amadora e os converte em visualizações espectrais em tempo real.

O **RadioHorn** é o frontend web do SpectraBox — a interface gráfica que permite a alunos, professores e entusiastas interagir com o hardware, visualizar espectros, controlar aquisições e explorar conceitos de radioastronomia de forma intuitiva.

Este equipamento será utilizado em **atividades ATEM** (Ação Transversal de Educação Musical/Científica) nas escolas públicas da Paraíba, como parte das ações de educação científica do Núcleo Via Láctea.

### Público-Alvo da Interface

| Perfil | Nível de Expertise | Necessidades |
|--------|-------------------|--------------|
| Alunos Ensino Médio | Iniciante | Interface intuitiva, visualizações atrativas |
| Alunos Ensino Fundamental | Básico | Gamificação, experimentos guiados |
| Professores | Intermediário | Controles, dados exportáveis, planos de aula |
| Entusiastas / Amadores | Avançado | Configurações SDR, dados brutos, APIs |

---

## 3. Objetivos

### Objetivo Geral

Desenvolver um frontend web responsivo e intuitivo para o SpectraBox, permitindo visualização em tempo real de espectros de rádio e controle de receptores SDR para atividades educacionais de radioastronomia.

### Objetivos Específicos

1. Projetar e implementar interface de **visualização espectral em tempo real** (spectrograma + curva de potência);
2. Desenvolver **painel de controle** para configuração do receptor SDR (frequência, ganho, banda, modos);
3. Implementar **módulo de gravação e replay** de dados espectrais para uso em sala de aula;
4. Criar **dashboard educacional** com visualizações interativas e métricas em tempo real;
5. Desenvolver **sistema de presets** educacionais (experimentos pré-configurados);
6. Garantir **acessibilidade e usabilidade** para o público da educação básica;
7. Documentar o código e produzir **guia do usuário** para professores.

---

## 4. Metodologia

### 4.1 Ciclo de Desenvolvimento

O desenvolvimento seguirá o método **Scrum adaptado**, com **sprints semanais** de 24h cada:

1. **Planejamento (início da semana):** Definição das tarefas da sprint
2. **Desenvolvimento (segunda a quinta):** Implementação, testes, revisão
3. **Revisão (sexta):** Validação com orientador e ajustes
4. **Retrospectiva (final da semana):** Documentação e planejamento da próxima sprint

### 4.2 Stack Tecnológico

| Camada | Tecnologia | Justificativa |
|--------|-----------|---------------|
| **Framework** | React / Next.js | Componentização, SSR, ecossistema maduro |
| **Visualização** | D3.js / Chart.js | Gráficos espectrais interativos |
| **Tempo Real** | WebSocket / Socket.IO | Comunicação bidirecional com backend SDR |
| **Áudio/Web** | Web Audio API | Processamento de sinais no navegador |
| **Estilo** | Tailwind CSS | Prototipação rápida, responsividade |
| **Testes** | Jest + Cypress | Testes unitários e E2E |
| **Versionamento** | Git + GitHub | Controle de versão e colaboração |

### 4.3 Arquitetura do Frontend

```
spectrabox-frontend/
├── src/
│   ├── components/          # Componentes reutilizáveis
│   │   ├── spectrogram/     # Visualização espectral
│   │   ├── controls/        # Painéis de controle SDR
│   │   ├── dashboard/       # Dashboard educacional
│   │   └── common/          # Componentes compartilhados
│   ├── hooks/               # Custom React hooks
│   ├── services/            # Conexão WebSocket / API
│   ├── utils/               # Processamento de sinais
│   ├── pages/               # Rotas da aplicação
│   └── styles/              # Estilos globais
├── public/                  # Assets estáticos
├── docs/                    # Documentação
└── tests/                   # Testes automatizados
```

---

## 5. Estrutura das Atividades (350 horas)

### Fase 1 — Fundamentação e Setup (40h)

| Atividade | Horas | Sprint | Descrição |
|-----------|:-----:|:------:|-----------|
| Estudo de fundamentos de SDR e radioastronomia | 12 | S1 | Conceitos de espectro, frequência, banda, modulação |
| Estudo da stack tecnológica | 10 | S1 | React, D3.js, WebSocket, Tailwind |
| Configuração do ambiente de desenvolvimento | 6 | S1 | Repositório, CI/CD, dependências |
| Definição de arquitetura e protótipos | 8 | S2 | Wireframes, fluxos de usuário |
| Pesquisa de referências de UI/UX científica | 4 | S2 | Análise de interfaces similares |

### Fase 2 — MVP do Espectrograma (80h)

| Atividade | Horas | Sprint | Descrição |
|-----------|:-----:|:------:|-----------|
| Setup do projeto React/Next.js | 6 | S3 | Estrutura inicial, roteamento |
| Comunicação WebSocket com backend SDR | 12 | S3 | Conexão em tempo real, heartbeat |
| Componente de spectrograma (D3.js) básico | 16 | S3-S4 | Canvas heatmap com waterfall |
| Componente de curva de potência (frequência × intensidade) | 12 | S4 | Gráfico dinâmico em tempo real |
| Indicadores de nível de sinal | 8 | S4 | Medidores visuais (VU meter espectral) |
| Testes unitários do módulo de visualização | 10 | S5 | Jest para componentes críticos |
| Integração contínua com GitHub Actions | 6 | S5 | Pipeline de build e testes |
| Revisão e correção de bugs | 10 | S5 | Validação com orientador |

### Fase 3 — Painel de Controle SDR (80h)

| Atividade | Horas | Sprint | Descrição |
|-----------|:-----:|:------:|-----------|
| Componente de controle de frequência | 10 | S6 | Slider + input numérico, range 980-1260 MHz |
| Controles de ganho e banda | 10 | S6 | Ajuste de ganho LNA, largura de banda |
| Seletor de modo de operação | 8 | S6 | Modos: espectro contínuo, burst, waterfal |
| Barra de ferramentas (zoom, pan, reset) | 10 | S7 | Navegação no espectro |
| Painel de configurações avançadas | 8 | S7 | FFT size, windowing, integração |
| Salvamento e carregamento de configurações | 10 | S7 | LocalStorage + export JSON |
| Testes E2E do painel de controle | 8 | S8 | Cypress para fluxos críticos |
| Testes de usabilidade com usuários simulados | 8 | S8 | Feedback de professores parceiros |
| Correções e refinamentos | 8 | S8 | Ajustes pós-feedback |

### Fase 4 — Módulo de Gravação e Replay (60h)

| Atividade | Horas | Sprint | Descrição |
|-----------|:-----:|:------:|-----------|
| Implementação de gravação de espectro | 10 | S9 | Captura de dados em tempo real |
| Sistema de arquivos de sessão | 8 | S9 | Organização e metadados |
| Player de replay (play/pause/seek) | 12 | S9-S10 | Reprodução de sessões gravadas |
| Controles de velocidade de replay | 8 | S10 | Acelerar/desacelerar reprodução |
| Exportação de dados (CSV, PNG) | 10 | S10 | Dados para análise em sala de aula |
| Anotações e marcações em sessões | 8 | S10 | Bookmarking de eventos no espectro |
| Testes de integração do módulo | 4 | S11 | Validação do fluxo completo |

### Fase 5 — Dashboard Educacional (50h)

| Atividade | Horas | Sprint | Descrição |
|-----------|:-----:|:------:|-----------|
| Tela inicial com visão geral do sistema | 6 | S11 | Status, conexão, modo atual |
| Sistema de presets de experimentos | 10 | S11 | Experimentos pré-configurados (ex: "Linha de 21cm", "Ruído Solar") |
| Cartões informativos contextuais | 8 | S11 | Tooltips e explicações científicas |
| Indicadores de descoberta (gamificação) | 8 | S12 | Badges ao identificar fenômenos |
| Guia interativo para alunos | 8 | S12 | Tutorial passo-a-passo na interface |
| Modo演示 (demonstração sem hardware) | 6 | S12 | Simulação de dados para testes em sala |
| Testes de aceitação com usuários reais | 4 | S12 | Validação em escola piloto |

### Fase 6 — Finalização e Documentação (40h)

| Atividade | Horas | Sprint | Descrição |
|-----------|:-----:|:------:|-----------|
| Responsividade e ajustes mobile | 8 | S13 | Adaptação para tablets e celulares |
| Acessibilidade (WCAG 2.1) | 6 | S13 | Contraste, navegação por teclado, leitores de tela |
| Documentação técnica do código | 8 | S13 | README, JSDoc, storybook |
| Guia do usuário (professores e alunos) | 8 | S14 | Manual ilustrado em português |
| Correções finais de bugs | 6 | S14 | QA completo |
| Preparação do repositório open-source | 4 | S14 | Licença, contributing guidelines |
| **Total** | **350h** | **14 semanas** | |

---

## 6. Cronograma Sumarizado

| Fase | Semanas | Horas | Entregável Principal |
|------|:-------:|:-----:|---------------------|
| F1: Fundamentação | S1-S2 | 40h | Stack configurada, wireframes aprovados |
| F2: MVP Espectrograma | S3-S5 | 80h | Componente de espectro funcional |
| F3: Painel de Controle | S6-S8 | 80h | Controles SDR operacionais |
| F4: Gravação/Replay | S9-S11 | 60h | Módulo de sessões completo |
| F5: Dashboard Educacional | S11-S12 | 50h | Interface educacional integrada |
| F6: Finalização | S13-S14 | 40h | Documentação e repositório |

---

## 7. Produtos Esperados

| Produto | Descrição | Prazo |
|---------|-----------|-------|
| **Frontend SpectraBox v1.0** | Aplicação web funcional com espectrograma em tempo real | S14 |
| **Repositório GitHub** | Código-fonte aberto com README, licença e CI/CD | S14 |
| **Guia do Usuário** | Manual ilustrado para professores e alunos | S14 |
| **Documentação Técnica** | JSDoc, arquitetura, guia de contribuição | S14 |
| **Relatório Técnico Final** | Descrição do desenvolvimento, decisões e resultados | S14 |
| **Presets Educacionais** | Conjunto de experimentos pré-configurados | S12 |

## 8. Avaliação e Acompanhamento

| Instrumento | Frequência | Responsável |
|------------|-----------|-------------|
| Reunião semanal de alinhamento | Semanal | Orientador + Discente |
| Review de sprint | Quinzenal | Orientador |
| Validação de protótipo | Mensal | Equipe Via Láctea |
| Teste com usuários reais | Fim F5 | Professores parceiros |
| Relatório parcial | Mês 2 | Discente |
| Relatório final | Mês 4 | Discente |

## 9. Referências

- Radioastronomia amadora e SDR: [SARAO, SDR Tutorials]
- React + D3.js: [React-D3 Library, ObservableHQ]
- WebSocket para tempo real: [MDN WebSocket API]
- Espectrogramas em Canvas: [MDN Canvas API, Spectrogram examples]
- Acessibilidade web: [WCAG 2.1, WAI-ARIA]
