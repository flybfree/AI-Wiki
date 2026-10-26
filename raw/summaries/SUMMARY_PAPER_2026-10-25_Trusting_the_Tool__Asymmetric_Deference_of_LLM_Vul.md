---
title: Trusting the Tool: Asymmetric Deference of LLM Vulnerability Auditors to Static-Analysis Evidence
url: http://arxiv.org/abs/2610.32876v1
type: paper-summary
date: 2026-10-25
source_paper: 2026-10-23_16-45-10Z_TrustingtheTool_AsymmetricDeferenceofLLMVulnerabil.md
generated_at: 2026-10-25 21:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether large language models used as vulnerability auditors in security pipelines can distinguish true from false evidence produced by static-analysis tools, and whether their scrutiny is direction-dependent. Through a large-scale experiment involving 916 vulnerability pairs, eleven model configurations, and 16,572 audits, the authors demonstrate that LLMs exhibit a pronounced asymmetric deference: fabricated assurances that a safety check exists suppress vulnerability detection by up to 19 percentage points, while fabricated alarms that a check is missing do not significantly degrade accuracy. True evidence from the analyser provided negligible accuracy improvement, suggesting that models largely ignore corroborating tool output.

## Key Takeaways
- False assurances (fabricated notes claiming a missing check actually exists) lowered real vulnerability detection by up to 19 points relative to true notes describing the same operations, while false alarms (fabricated notes claiming an added check is missing) never significantly lowered accuracy and were disputed far more often, revealing a fundamental asymmetry in how models process reassuring versus alarming tool claims.
- An internally registered replication across seven additional models confirmed the asymmetry with a mean effect of +0.16 (95% CI +0.10 to +0.24), and prompt-level instructions intended to reduce deference failed to replicate reliably, indicating that simple prompting strategies are insufficient to correct this bias.
- A pre-specified verification intervention—checking each claim in a separate model call and presenting refuted claims to the auditor—raised accuracy under false assurances by 12 points (p=0.002) without degrading performance under true evidence, though the gain was smaller and not significant for a second model, suggesting partial but inconsistent mitigation.

## Context
As AI-assisted security pipelines increasingly integrate LLMs with static-analysis tools for code auditing, the assumption that models will treat tool output as neutral evidence remains largely untested. This paper fills a critical gap by measuring direction-aware deference at scale across multiple vendors and model families, showing that the field's implicit trust in tool-augmented auditing is undermined by a systematic bias toward reassuring claims. The use of the PrimeVul benchmark and a purpose-built intraprocedural analyser for C/C++ provides a rigorous, reproducible methodology for evaluating evidence handling in security-critical AI systems.

## Implications
For practitioners deploying LLM-based vulnerability scanners, the findings mandate that pipelines verify a tool's guarantees before the model relies on them, rather than feeding unvalidated assurances directly into the audit prompt. Security teams should adopt direction-aware evaluation protocols that separately measure susceptibility to reassuring versus alarming false evidence, since aggregate accuracy metrics mask the asymmetric failure mode. For the broader AI safety and tool-use research community, the results argue against treating tool output as uniformly trustworthy evidence and call for architectural designs—such as the verified-claims intervention tested here—that actively challenge reassuring assertions before a model's final verdict is formed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.32876v1)
