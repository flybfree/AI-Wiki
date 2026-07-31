---
title: VAmoS Bench: Voice Agent Simulation Bench
published: 2026-07-29T20:42:38Z
authors: Joshua Meyer, Sahar Shayegan, Ritiz Tambi, Ali Khan, Sun Kim, Victor Shih, Mehdi Jamei, Andi Partovi
url: http://arxiv.org/abs/2607.27453v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VAmoS Bench: Voice Agent Simulation Bench

## Abstract
Production voice agents span cascaded, speech-to-speech, and hybrid architectures. Voice-agent benchmarks typically measure component quality and conversational properties such as word error rate, latency, naturalness, and turn-taking. Fewer measure whether the agent handled a phone call correctly on its own. Contact centers refer to this as ``containment'': the share of phone calls the automated system resolves without handing off to a human. On some phone calls the right outcome is refusal or a redirect. To address this gap, we introduce VAmoS Bench, the Voice Agent Simulation Bench. It measures complete voice-agent systems end to end in a stateful customer-support task. The agent is Riley, a credit-card support representative for a fictional bank who can freeze, cancel, replace, or activate a card. Each of 100 scenarios supplies a simulated caller with a private goal and a seeded PostgreSQL backend. The platform uses each scenario to populate and activate an isolated simulation in which the caller reaches Riley over audio; roughly one-third apply adversarial pressure. The agent can use five tools that execute real SQL against the backend. Each scenario also defines binary assertions. A grader evaluates them against the complete trace of what the caller and agent said and what the agent did, including tool invocations, arguments, and returned rows. This catches an agent that claims to have changed a card without updating the database, as well as one that makes the right database change while disclosing protected information. This first benchmark version focuses on financial services. Its evaluation protocol supports an evolving leaderboard: additional voice agents can be evaluated on the same version, while later versions can expand the tasks and scenarios.

## Metadata
- **Published**: 2026-07-29T20:42:38Z
- **Authors**: Joshua Meyer, Sahar Shayegan, Ritiz Tambi, Ali Khan, Sun Kim, Victor Shih, Mehdi Jamei, Andi Partovi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27453v1)