---
title: MIRROR: Multipath Quorum Integrity for LLM Multi-Agent Communication
url: http://arxiv.org/abs/2610.02349v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_18-22-22Z_MIRROR_MultipathQuorumIntegrityforLLMMulti_AgentCo.md
generated_at: 2026-10-04 22:07
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MIRROR, a communication-layer integrity primitive designed to defend Large Language Model Multi-Agent Systems against Agent-in-the-Middle (AiTM) attacks, where an intermediary manipulates messages in transit without compromising the agents themselves. MIRROR works by replicating a canonicalized payload across k logical routes and accepting a message only when a strict majority of routes report the same digest, reducing Attack Success Rates to 0% at just 1x LLM token cost across multiple benchmarks and deployment scenarios.

## Key Takeaways
- MIRROR's security guarantee rests entirely on the assumption that honest routes form a strict majority (alpha < 0.5). It uses unkeyed hashing, meaning it authenticates nothing on its own; an active on-path adversary can always recompute a digest over a modified payload. The digest's role is limited to making witness routes constant-size and binding the recovered payload to the quorum-agreed value under second-preimage resistance. This is a fundamentally different trust model from cryptographic authentication.
- The paper extends the integrity guarantee to correlated routes, where the critical quantity is the size of the largest shared-failure group rather than the total route count. This is a significant practical contribution because real-world network paths often share infrastructure, making naive route-counting assumptions insufficient for security guarantees.
- MIRROR demonstrates that availability and integrity degrade at the same threshold (alpha = 0.5): below this bound, quorum-denial and message-dropping adversaries cannot block honest traffic. Empirically, across MMLU, HumanEval, and MBPP on two frameworks and four communication topologies, MIRROR achieves 0% ASR at 1x LLM token cost, whereas LLM-as-a-Judge defenses cost 35x and block up to 44.2% of benign outputs.

## Context
LLM Multi-Agent Systems are increasingly deployed in production settings where agents communicate over networks, creating a new attack surface distinct from prompt injection or model poisoning. Prior defenses either rely on semantic validation through additional LLM inference—which is expensive and prone to false positives—or transport-layer encryption, which fails when an intermediary legitimately terminates TLS. MIRROR addresses this gap by operating at the communication layer with a quorum-based integrity check, positioning itself as a lightweight, protocol-level primitive rather than a semantic filter.

## Implications
For practitioners building multi-agent pipelines, MIRROR offers a defense that is orders of magnitude cheaper than LLM-as-a-Judge approaches while avoiding the false-positive blocking rates that plague semantic validation methods. The correlated-route analysis is particularly relevant for cloud and enterprise deployments where network paths share infrastructure, providing a more realistic threat model than assuming fully independent routes. The paper also highlights that availability and integrity share a common failure threshold, suggesting that system designers should treat these as a unified design constraint rather than optimizing them independently.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02349v1)
