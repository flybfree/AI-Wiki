---
title: Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems
url: http://arxiv.org/abs/2610.23372v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_12-23-56Z_BeyondSuccessRate_InterventionalEvaluationofMemory.md
generated_at: 2026-10-18 21:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the Interventional Memory Evaluation Protocol (IMEP), a rigorous evaluation framework for vision-language-action (VLA) systems that goes beyond simple success-rate ablations to determine whether a robot's memory system genuinely contributes task-relevant information to decision-making. The authors demonstrate that aggregate success rates can mask offsetting gains and losses, and they propose controlled interventions—such as target-fact substitutions, fact-preserving replacements, and minimal numerical perturbations—to isolate whether memory effects are specific to task-relevant facts. Their experiments reveal that while a full memory configuration can dramatically improve task success (from 39.1% to 74.3%), establishing that a memory system truly leverages stored facts requires fact-specific causal evidence rather than aggregate performance comparisons.

## Key Takeaways
- Success-rate ablations are fundamentally insufficient for evaluating memory in VLA systems because they simultaneously alter information content and computational capacity, and aggregate metrics can conceal offsetting gains and losses across different task components. The IMEP framework addresses this by separating decision correctness from motor execution success and by comparing interventions that change task-relevant facts against control conditions like fact-preserving replacements and exact replicas.
- In cross-episode learned-bank experiments, a one-unit-in-the-last-place (ULP) intervention—including its installation procedure—altered 11.9% of seed-paired outcomes, yet changing key facts produced no clear additional effect beyond fact-preserving replacements. This finding suggests that the observed performance differences may stem from procedural or structural artifacts of the memory system rather than from the actual content of stored task-relevant facts, highlighting a critical gap in how memory contributions are currently assessed.
- The authors introduce ChainBench, a benchmark where correct decisions require historical information that is unavailable in current observations. The full memory configuration raises task success from 39.1% to 74.3%, matching an oracle-decision condition under shared recorded executions. This demonstrates that correct historical information can indeed support robot decisions, but the gap between this potential and what a deployed memory system actually achieves demands fact-specific causal evidence to verify.

## Context
Vision-language-action systems are increasingly deployed in robotics and embodied AI, where memory mechanisms—spanning within-episode, cross-episode, and agentic architectures—are marketed as enabling persistent, context-aware behavior. However, the field lacks standardized protocols to verify whether these memory components actually influence task outcomes through their stored content, as opposed to confounding factors like architectural changes or computational overhead. This paper fills that methodological gap by formalizing four evaluation questions and introducing controlled intervention designs, positioning itself within a broader movement toward causal and mechanistic evaluation in AI systems rather than relying on end-to-end performance metrics alone.

## Implications
For practitioners building and deploying VLA systems, this work signals that current evaluation practices may overstate the functional contribution of memory modules, potentially leading to overconfident claims about persistent robot capabilities. Industry stakeholders should adopt fact-specific interventional testing before certifying memory-augmented robots for safety-critical or long-horizon tasks. For the research community, the IMEP protocol and ChainBench benchmark provide reusable tools for auditing memory systems, encouraging a shift from aggregate success reporting toward causal, content-specific verification that can guide more honest and reproducible progress in embodied AI.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23372v1)
