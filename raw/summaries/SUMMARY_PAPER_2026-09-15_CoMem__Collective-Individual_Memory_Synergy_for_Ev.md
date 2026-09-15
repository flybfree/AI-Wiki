---
title: CoMem: Collective-Individual Memory Synergy for Evolutionary Multi-Agent Systems
url: http://arxiv.org/abs/2609.15009v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-14_04-15-55Z_CoMem_Collective_IndividualMemorySynergyforEvoluti.md
generated_at: 2026-09-15 03:29
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces CoMem, a novel memory architecture designed to enhance LLM-driven Multi-Agent Systems by synergizing collective knowledge with individual experience. By addressing the limitations of flat, unstructured memory systems that accumulate noise and homogenize agent capabilities, CoMem enables agents to learn collaboratively while preserving unique expertise. Experimental evaluations on ALFWorld and PDDL benchmarks demonstrate that this approach significantly improves overall task performance while effectively preventing memory pollution.

## Key Takeaways
- Private Experience Sedimentation allows each agent to continuously retain and refine its own successful strategies over time, ensuring that individual expertise is preserved rather than overwritten by shared data.
- Collective Wisdom Curation implements a rigorous filtering mechanism that only disseminates widely validated insights across the agent network, preventing unverified or noisy information from degrading group performance.
- Parallel Dual-Stream Retrieval enables agents to simultaneously access their personal memory archives and the curated collective repository, utilizing clustering techniques to maintain diverse perspectives during decision-making processes.

## Context
As large language models increasingly power multi-agent frameworks for complex task solving, scalable memory architectures have become a critical bottleneck in system design. Traditional flat storage methods struggle with information overload and agent homogenization, hindering long-term collaborative learning in dynamic environments. This research addresses these challenges by introducing structured, dual-tier memory systems that balance individual autonomy with collective intelligence, aligning with the broader AI push toward sustainable, evolving agent ecosystems.

## Implications
The proposed CoMem architecture offers a practical blueprint for developing more resilient and adaptive multi-agent platforms in industries reliant on autonomous coordination, such as supply chain logistics, customer service automation, and distributed robotics. By mitigating memory pollution and preserving agent diversity, practitioners can deploy larger, more specialized agent networks that continuously improve without suffering from catastrophic forgetting or information degradation. This approach paves the way for next-generation evolutionary AI systems capable of sustained, collaborative problem-solving in real-world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.15009v1)
