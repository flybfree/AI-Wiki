---
title: PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agents
url: http://arxiv.org/abs/2610.22124v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_16-01-38Z_PROBE_LearningtoAuditPolicyComplianceinTool_UsingL.md
generated_at: 2026-10-15 22:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces PROBE (Policy Rule Observation via Behavioral Exploration), a training framework for LLM-based auditors that interact with deployed agentic systems through multi-turn, tool-mediated dialogue to uncover policy compliance violations. The authors formalize agent auditing as a two-player Markov game with a composite reward function and demonstrate that trained auditors discover substantially broader and higher-yield policy violations than zero-shot adversaries, even when the auditor model is significantly smaller than the target agent being audited.

## Key Takeaways
- Existing evaluation methods create a critical gap: capability benchmarks measure what agents can accomplish, and content-safety red-teaming measures harmful generations, but neither tests whether agents comply with predefined policies (pricing, privacy, confirmation, safety) during otherwise valid tool use. Policy violations are especially difficult to audit because their effects may emerge only after several turns, span multiple tool calls, or surface in downstream systems.
- PROBE formalizes agent auditing as a two-player Markov game and proposes a composite reward that balances four objectives: violation discovery, behavioral plausibility, conversation progress, and policy diversity. The authors compare GRPO, DPO, and GFlowNet-based optimization strategies in a controlled setting to study which training objectives and reward designs best support effective auditing behavior.
- Trained auditors uncover substantially broader and higher-yield policy violations than same-architecture zero-shot adversaries, and this advantage holds even when the auditor is significantly smaller than the target agent. The results establish multi-turn behavioral auditing as a distinct and necessary axis of agent evaluation that complements existing capability and safety benchmarks.

## Context
As agentic systems increasingly deploy language models with external tools in consequential settings such as customer service, financial transactions, and healthcare interactions, policy compliance becomes a regulatory and operational necessity. Current AI evaluation infrastructure is bifurcated between capability benchmarks and content-safety red-teaming, leaving a structural blind spot for behavioral policy violations that only manifest through extended multi-turn tool use. PROBE addresses this gap by treating auditing as an interactive, adversarial exploration problem rather than a static classification task, aligning with the broader research trend toward agentic evaluation and adversarial testing in large language model systems.

## Implications
For practitioners deploying agentic systems in regulated industries, PROBE offers a scalable path toward automated policy auditing that can surface compliance failures invisible to single-turn safety checks, reducing the need for manual compliance review. The proposed co-evolutionary loop—where auditors expose failures and agents improve from auditor feedback—suggests a practical feedback mechanism for iterative agent hardening in production environments. For the research community, the finding that smaller trained auditors outperform larger zero-shot adversaries challenges assumptions about the scaling requirements for evaluation and points toward more efficient, targeted auditor training as a viable strategy for auditing increasingly complex agentic systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22124v1)
