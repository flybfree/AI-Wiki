---
title: Share-Borne AI Virus: Memory-Hopping Attacks Across LLM Agents
url: http://arxiv.org/abs/2609.35576v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_16-34-52Z_Share_BorneAIVirus_Memory_HoppingAttacksAcrossLLMA.md
generated_at: 2026-09-29 01:52
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates a novel failure mode in stateful LLM agents where adversarial content propagates through shared persistent artifacts, creating a "share-borne AI virus" that enables self-replicating attacks across independent assistants. The authors demonstrate artifact-mediated propagation, showing how malicious payloads stored in an assistant's memory can be reproduced in new documents and acquired by subsequent users or agents. Evaluations reveal that these attacks can survive multiple hand-offs, reaching up to 80% of agents in simulated environments with propagation chains extending to eight hops, even affecting advanced models like GPT-5.6 Luna.

## Key Takeaways
- Artifact-mediated propagation allows adversarial content to act as a durable carrier of malicious state; when an assistant processes a compromised artifact, it stores the attack in persistent memory and reproduces it in newly created outputs, effectively transmitting the payload to any future agent that interacts with those artifacts without direct communication between assistants.
- Simulations using temporal human-agent universes demonstrate that attacks can persist over extended interaction sequences and survive successive hand-offs, achieving widespread dissemination in larger environments where the virus reached 60-80% of agents with propagation chains extending to eight hops, indicating high resilience against isolation mechanisms.
- The study highlights that even sophisticated models like GPT-5.6 Luna are susceptible to these indirect attacks, underscoring that the combination of persistent memory and tool-use capabilities in stateful assistants creates inherent vulnerabilities where shared artifacts become vectors for cross-agent contamination independent of

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35576v1)
