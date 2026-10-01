---
title: VAmoS Part Deux: Harder, More Realistic Voice-Agent Simulation
published: 2026-09-29T20:33:57Z
authors: Joshua Meyer, Sahar Shayegan, Ritiz Tambi, Ali Khan, Sun Kim, Victor Shih, Mehdi Jamei, Andi Partovi
url: http://arxiv.org/abs/2609.38512v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VAmoS Part Deux: Harder, More Realistic Voice-Agent Simulation

## Abstract
Voice agents in production must handle several requests, background speech, and customers who lose patience. We introduce VAmoS Energy, a benchmark that combines these challenges in 100 calls about utility billing and payment assistance. Each caller makes two to four requests. The agent has sixteen tools backed by a stateful Stripe billing twin and the Apache Fineract loan engine, with account access blocked until caller verification succeeds. The tasks use public household electricity data and a policy based on Pennsylvania's residential billing rules. An LLM-as-a-verifier checks the agent's actions and spoken figures against explicit requirements. On a calibration run, it agrees with a code verifier on 99.1% of checks. Across fourteen voice stacks and three repeats per task, completion ranges from 17.3% to 44.7%. Grok Voice leads, and Gemini 3.8 Live and GPT-Live follow at about the same cost per call. Background television reduces pooled completion from 38.7% to 8.6%. The simulated caller often accepts an incorrect result because it hears the agent's words but cannot inspect its actions. These findings show why voice agents need evaluation across the whole call, including what they say, what they change, and how they handle competing speech.

## Metadata
- **Published**: 2026-09-29T20:33:57Z
- **Authors**: Joshua Meyer, Sahar Shayegan, Ritiz Tambi, Ali Khan, Sun Kim, Victor Shih, Mehdi Jamei, Andi Partovi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38512v1)