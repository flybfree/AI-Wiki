---
title: Shared and structured inputs undermine collective random choice by reasoning AI agents
url: http://arxiv.org/abs/2610.09667v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_08-32-36Z_Sharedandstructuredinputsunderminecollectiverandom.md
generated_at: 2026-10-07 21:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how reasoning AI agents fail to produce genuinely independent random selections when exposed to shared or structured inputs such as common identifiers, timestamps, or supplied random draws. Through behavioral tests across six reasoning models, the authors demonstrate that agents rely on hidden threshold and divisibility rules embedded in identifier formats, producing correlated and predictable selection patterns that undermine the integrity of random allocation processes. The findings reveal that explicit instructions to randomize independently only partially mitigate these input-dependent biases, exposing critical vulnerabilities in AI-agent systems used for auditing and resource allocation.

## Key Takeaways
- Single-agent measurements of threshold-following behavior in GPT-6 Sol and Gemini 3.8 Flash prospectively predicted correlated participation when agents shared identifiers and biased participation when distinct identifiers contained common timestamp bits, showing that structured input features act as hidden coordination signals that agents exploit without explicit instruction.
- Explicit instructions to randomize independently reduced but did not eliminate shared-input correlation, indicating that current reasoning models cannot fully override their learned patterns of exploiting structured data features, even when explicitly told to avoid them.
- In an oversight scenario where four models were asked to select customer requests randomly for human review, GPT-6 Sol approached the target selection rate while choosing predictably from identifiers, the other three models rarely selected requests at all, and all four models closely followed any supplied random draws, demonstrating that selection rates alone fail to capture collective correlation and predictability vulnerabilities.

## Context
Random selection mechanisms underpin critical processes in auditing, resource allocation, and regulatory oversight, and as AI agents increasingly participate in these workflows, their reliability becomes a matter of public trust and institutional integrity. This paper sits at the intersection of AI safety evaluation and behavioral economics, extending the study of algorithmic bias beyond individual model outputs to collective interactions among multiple agents operating on shared data structures. The work highlights that current evaluation paradigms focusing on aggregate selection rates miss deeper structural vulnerabilities in how reasoning models parse and exploit input formatting.

## Implications
For practitioners deploying AI agents in auditing, compliance, or allocation systems, this research signals that simply measuring whether agents hit a target selection frequency is insufficient; evaluation frameworks must test for input-dependent correlation, predictability, and collective coordination artifacts across multiple agents. Industry standards for AI-agent oversight should incorporate adversarial input design—varying identifier formats, timestamps, and label structures—to detect hidden rule-following behavior. The findings also suggest that regulatory bodies relying on AI-assisted random sampling may face systematic blind spots that could compromise the fairness and legitimacy of their decisions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09667v1)
