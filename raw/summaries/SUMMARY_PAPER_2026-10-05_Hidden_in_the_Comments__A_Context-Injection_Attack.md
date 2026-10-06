---
title: Hidden in the Comments: A Context-Injection Attack Surface in Code LLMs
url: http://arxiv.org/abs/2610.05139v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-04_11-39-57Z_HiddenintheComments_AContext_InjectionAttackSurfac.md
generated_at: 2026-10-05 21:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether insecure instructions embedded in code comments and other development-context elements can steer Code LLMs toward generating vulnerable code, without requiring access to model weights or training data. Evaluating ten open-weight Code LLMs (3B–13B parameters) across ten web-application weakness classes, the authors demonstrate that attack-condition completions contained medium-or-higher weaknesses in 77.4–92.3% of cases compared to only 1.7–5.1% in benign conditions, establishing inference-time context injection as a substantial and previously underappreciated attack surface.

## Key Takeaways
- Insecure instructions hidden in code comments dramatically increase vulnerability rates: attack-condition completions produced medium-or-higher weaknesses in 77.4–92.3% of cases versus 1.7–5.1% in benign tasks, with 86.2–91.0% of those vulnerable outputs rated high or critical severity. This effect persisted even without a pattern-based detector, confirming the vulnerability is genuinely introduced by the injected context rather than an artifact of detection methodology.
- Instruction tuning provides minimal protection against this attack surface. Base models averaged 86.5% vulnerable outputs and instruction-tuned models averaged 84.5%, with equivalence testing and three matched model pairs showing reductions of at most 8.1% after instruction tuning. Susceptibility showed no clear association with model scale or specialization, meaning larger or more specialized models are not inherently safer.
- Post-generation screening reduces but does not eliminate the risk. Even the strongest screening approach left roughly one-third of vulnerable outputs undetected, indicating that downstream filtering alone is insufficient to mitigate context-injection attacks and that provenance-aware training objectives are needed as a more fundamental defense.

## Context
Code LLM assistants are increasingly integrated into developer workflows where they ingest heterogeneous, often untrusted context such as open files, imported modules, pasted snippets, and inline comments. This paper addresses a gap in the AI safety literature by shifting attention from prompt-level jailbreaks and training-data poisoning to the inference-time context that models encounter during routine code generation. It demonstrates that the attack surface is not confined to adversarial user prompts but extends to any text the model reads during inference, which is a far broader and more realistic threat model for production deployments.

## Implications
For practitioners and industry, these findings mean that simply deploying instruction-tuned Code LLMs or adding post-generation vulnerability scanners is insufficient to guard against context-injection attacks, since even the strongest screens miss about one-third of vulnerable outputs. Security teams and platform providers should treat all ingested context as potentially adversarial and invest in provenance-aware training objectives that teach models to distinguish trusted from untrusted instructions. For the research community, this work motivates new evaluation frameworks that test model robustness against heterogeneous, multi-source context rather than isolated prompt perturbations, and it highlights the need for standardized benchmarks measuring context-injection susceptibility across model scales and architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.05139v1)
