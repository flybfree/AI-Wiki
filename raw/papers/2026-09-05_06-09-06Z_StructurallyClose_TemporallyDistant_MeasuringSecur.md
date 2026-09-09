---
title: Structurally Close, Temporally Distant: Measuring Security Exposure in Long-Horizon LLM Agents
published: 2026-09-05T06:09:06Z
authors: Md Jafrin Hossain, Nur Al Hasan Haldar
url: http://arxiv.org/abs/2609.05911v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Structurally Close, Temporally Distant: Measuring Security Exposure in Long-Horizon LLM Agents

## Abstract
Long-horizon LLM agents interact with untrusted content, persistent memory, external state, and sensitive tools. Existing analyses often characterize attacks by the number of execution steps between malicious input and a downstream action. We show that temporal remoteness can overstate security separation in stateful agents. We introduce a provenance-aware execution graph linking agent events through deterministic state, identifier, and tool provenance, and define \emph{influence distance} $\DI$ as the shortest structural path from an untrusted source to a sensitive action. We compare it with \emph{sequence distance} $\DT$, the shortest injection--sink path in the ordered trajectory. Since the influence graph contains every sequence edge, $\DI \leq \DT$; $\Gap=\DT-\DI$ measures the separation hidden by step count. Across 454 injection--sink pairs from 360 long-horizon AgentDojo trajectories over OpenAI's \texttt{gpt-4o-mini} and \texttt{gpt-4o} and Claude's Haiku 4.5 and Sonnet 4.6, $\Gap>0$ for 96.9% of pairs, with a median gap of 9 hops; 91.0% remain decoupled after removing the largest provenance-only edge class. On AgentDojo's banking suite, 33.8% of 231 pairs from 377 trajectories decouple through different provenance mechanisms. Among 274 OpenAI pairs, $\Gap$ does not independently predict attack success after controlling for $\DT$, attack family, and backend ($β_{\Gap}=0.066$, $p=.088$). At matched thresholds $k=2,3$, a deterministic $\DI$-based pre-execution gate blocks five attack sinks missed by a sequence-only gate with no additional benign blocking, although the paired gain is not significant ($p=.0625$). Execution structure therefore reveals proximity hidden by step count and can support targeted runtime intervention. We measure candidate influence pathways rather than causal attribution.

## Metadata
- **Published**: 2026-09-05T06:09:06Z
- **Authors**: Md Jafrin Hossain, Nur Al Hasan Haldar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05911v1)