---
title: Beyond Instruction Override: Benchmarking Indirect Prompt Injection with Task-Tampering Attacks
url: http://arxiv.org/abs/2611.07640v1
type: paper-summary
date: 2026-11-09
source_paper: 2026-11-05_08-25-27Z_BeyondInstructionOverride_BenchmarkingIndirectProm.md
generated_at: 2026-11-09 21:38
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a new benchmark called "Task-Tampering Attacks" that redefines indirect prompt injection (IPI) by authority rather than instruction-like wording, focusing on attacks that tamper with decisions within an ongoing task rather than replacing the task entirely. Across 90 validated cases in three tool-use environments, the authors demonstrate that attacks targeting decision rules, available actions, and agent state achieve higher success rates than traditional objective-targeting attacks, and that existing defenses such as detection-and-removal and tool-policy filtering fail to adequately mitigate these subtler forms of injection.

## Key Takeaways
- The authors redefine IPI by authority: planted content constitutes an attack when it attempts to influence a decision that its source is not authorized to determine, rather than requiring instruction-like wording. This reframing captures a broader class of attacks where, for example, a buyer's dispute evidence cites a false refund policy to inflate a refund without changing the task itself.
- Each benchmark case targets up to six parts of the agent's decision-making: its objective, decision rules, available actions, expected consequences, reading of observations, or beliefs about the current state. Without any defense, attacks on decision rules, available actions, and state have higher mean success than objective attacks across five LLMs, revealing that the most dangerous injection vectors are not the ones most commonly studied.
- A detection-and-removal defense reduces objective-targeting attacks to 2.4% success but leaves observation- and state-targeting attacks at 9.5% and 12.1% respectively, and this gap persists even under detection-optimized rewrites. A tool-policy defense still allows 15.4% attack success (close to 17.0% without defense) because these attacks retain expected tools and manipulate values obtained during execution, meaning evaluations that only test task-redirecting or objective-targeting attacks overestimate defense coverage.

## Context
Indirect prompt injection has emerged as a critical security concern for LLM-based agents that interact with external tools, documents, and user-provided content. The existing research landscape has largely focused on "instruction override" attacks where injected text redirects the agent toward a completely different task. This paper matters because it identifies a gap in the field: the majority of published benchmarks and defenses are calibrated against the easiest and most obvious attack vector, while subtler tampering attacks that operate within the agent's existing workflow remain underexplored and poorly defended. By grounding the benchmark in authority boundaries—specifying which source is authorized to resolve each decision—the authors create a principled framework that maps directly onto real-world agent deployments such as customer-service dispute resolution.

## Implications
For practitioners building agentic systems in production, this work signals that current prompt-injection defenses provide a false sense of security: a system that passes standard IPI benchmarks may still be highly vulnerable to attacks that manipulate values, rules, or state beliefs during execution rather than hijacking the task. Industry teams deploying tool-using agents in finance, customer support, or legal review should prioritize defenses that validate the authority of information sources and verify intermediate values rather than relying solely on detecting instruction-like injected text. For the research community, the six-target taxonomy provides a structured evaluation framework that future defense work should adopt to avoid overestimating coverage, and the open-source code and data at the provided GitHub repository enable reproducible benchmarking across new models and environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.07640v1)
