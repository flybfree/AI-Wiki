---
title: MemForm: Benchmarking Memory Formation Poisoning in LLM Agents
url: http://arxiv.org/abs/2610.14431v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_00-52-32Z_MemForm_BenchmarkingMemoryFormationPoisoninginLLMA.md
generated_at: 2026-10-13 21:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MemForm, a controlled diagnostic benchmark for evaluating Memory Formation Poisoning in LLM agents, defined as adversarial manipulation of the interfaces through which persistent agent memory is produced and committed. The benchmark covers five distinct interfaces—Content, Evidence, Scope, Selection, and Path Poisoning—and reveals that all six evaluated LLMs are broadly susceptible to poisoning at every interface, with consolidation order alone capable of altering agent behavior even when identical experiences are retained.

## Key Takeaways
- The authors formalize Memory Formation Poisoning as adversarial manipulation at the formation interfaces rather than at attack channels or corruption patterns, and introduce two novel controlled intervention categories—Selection Poisoning (isolating retention effects) and Path Poisoning (isolating consolidation order effects)—that had not been characterized in prior work. Each category pairs clean and poisoned conditions with interface-specific controls to enable precise diagnosis.
- Evaluations across six LLMs and two response formats demonstrate that authentic experiences with successful outcomes do not guarantee reliable downstream behavior after memory formation. Changes to contextual support, retention decisions, or consolidation order can induce undesirable behavior, and consolidation order can alter agent behavior even with identical retained experiences, depending on the memory formation procedure used.
- Interface applicability is architecture-dependent, and Path Poisoning susceptibility varies by the specific updater mechanism employed. The evaluated defenses provide only incomplete mitigation that differs across interfaces, indicating that no single defense strategy is sufficient across all memory formation pathways.

## Context
As LLM agents increasingly rely on long-term memory to learn from past interactions, the integrity of the memory formation pipeline becomes a critical security and reliability concern. Prior research on memory poisoning has largely organized threats by attack channels, corruption patterns, or lifecycle stages, leaving the formation interfaces themselves underexplored. MemForm fills this gap by providing a systematic, controlled benchmark that isolates each interface where adversarial influence can corrupt the commitment of experiences into persistent memory, enabling researchers to diagnose vulnerabilities at a granularity that existing taxonomies do not support.

## Implications
For practitioners building agentic systems with persistent memory, these findings underscore that securing what is stored is insufficient; the process by which memories are formed—including retention decisions and consolidation ordering—must also be hardened against adversarial manipulation. The architecture-dependent and updater-dependent nature of susceptibility means that defense strategies must be tailored to specific memory implementations rather than applied uniformly. The benchmark and its open-source code and data provide a reusable diagnostic tool for developers and researchers to stress-test their agent memory pipelines before deployment, motivating the design of formation-aware safeguards in production LLM agent systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.14431v1)
