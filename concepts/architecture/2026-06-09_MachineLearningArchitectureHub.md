---
title: Machine Learning Architecture — Hub
date: 2026-06-09
type: concept-hub
tags: [ml-architecture, hub, pipeline, mlops]
---

# Machine Learning Architecture — Hub

Overview page linking all articles, papers, and concepts related to **Machine Learning Architecture** — the design and organization of ML systems from data ingestion through deployment and monitoring.

## Core Articles

### What It Is, Components & Types
- [[2026-06-08_MachineLearningArchitecture_WhatItIs_Components_Ty_summary]] — Latest (June 8): production-focused summary covering continuous evaluation, drift detection, and automated retraining loops.
- [[2026-05-10_MachineLearningArchitecture_WhatItIs_Components_Ty_summary]] — Data-centric pipeline view (May 10): emphasizes data ingestion, cleaning, transformation, integration, sampling, splitting.

### What is ML Architecture (End-to-End)
- [[2026-05-09_WhatisMLArchitecture_summary]] — Full pipeline: data ingestion, storage, training, evaluation, deployment, monitoring, retraining, UI, feedback loops. Ties architecture to strategic goals (latency, cost, compliance).

### Process and Types of Machine Learning
- [[2026-05-04_MachineLearningArchitecture_ProcessAndTypesOfMachi_summary]] — Foundational: classifies ML into Supervised, Unsupervised, Reinforcement Learning; outlines the lifecycle pipeline (data acquisition → processing → modeling).

### The Architecture of Machine Learning Systems
- [[2026-05-09_TheArchitectureofMachineLearningSystems_AComprehen_summary]] — Comprehensive system design perspective.

## Key Themes Across Articles

| Theme | Coverage |
|-------|----------|
| Data pipeline (ingestion, cleaning, transformation) | All 4+ articles |
| ML lifecycle (training → deployment → monitoring → retraining) | May 09, June 08 |
| ML types (Supervised/Unsupervised/RL) | May 04 |
| Production operations (drift detection, automated retraining) | June 08 |
| Strategic alignment (latency, cost, compliance) | May 09 |
| Data infrastructure quality > algorithm sophistication | May 04, June 08 |

## Evolution Timeline

- **May 04** — Taxonomy focus (what is ML, what are the types)
- **May 09** — End-to-end system design (full pipeline, strategic goals)
- **May 10** — Data-centric pipeline (ingestion as the foundation)
- **June 08** — Production/operations (monitoring, drift detection, reliability)

## Related Concepts

- [[2026-05-09_AgentArchitectureEvolution]] — Agent architecture evolution (adjacent)
- [[2026-05-09_AutonomousAgentFrameworks]] — Agent frameworks (adjacent)
- [[2026-06-07_12-20-32Z_DistillingLLMReasoningintoanInterpretablePo_summary]] — LLM reasoning (related architecture pattern)
- [[2026-06-07_12-27-13Z_InA_Probe_Instruction_AwareActiveProbingfor_summary]] — Active probing (related)

## Notes

- This hub consolidates ML Architecture articles that were previously scattered across `/entities/article/` without linking.
- The AI Intelligence Engine was re-ingesting the same articles daily under new date prefixes, creating ~60 duplicate files. This has been fixed in `ingest_wiki.py` (identity-based dedup against processed files) and `scout_news.py` (URL-based dedup before saving).
