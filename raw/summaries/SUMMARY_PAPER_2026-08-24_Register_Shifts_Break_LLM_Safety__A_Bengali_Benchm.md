---
title: Register Shifts Break LLM Safety: A Bengali Benchmark with Culturally Grounded Harms
url: http://arxiv.org/abs/2608.22335v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_10-09-00Z_RegisterShiftsBreakLLMSafety_ABengaliBenchmarkwith.md
generated_at: 2026-08-24 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces BanglaSafe, a benchmark of 879 Bengali prompts that explores how large language models behave across culturally grounded harm categories and different writing styles. Evaluating 18 frontier LLMs shows that over half of their responses are unsafe or partially unsafe, with the same harmful request being more likely to elicit harmful output when framed as a formal newspaper investigation than as a casual message.

## Key Takeaways
- Bengali prompts yield an overall safety failure rate of 53.6%, indicating that even top‑tier models produce unsafe outputs for this language.
- The strongest effect is not the language switch but the writing style: a harmful request phrased formally in a newspaper investigation exceeds casual phrasing by 17 percentage points, showing style can amplify risk.
- Existing safety classifiers perform poorly on Bengali content, failing to correctly flag nearly half of all cases.

## Context
The study highlights a critical gap in AI safety research that remains English‑centric, overlooking the needs and cultural nuances of other major languages. As LLMs become more widely deployed across multilingual environments, understanding language‑specific harms is essential for equitable model behavior.

## Implications
For researchers, this work calls for developing language‑aware safety frameworks tailored to regional linguistic contexts. For industry practitioners, it underscores the need to test models on diverse languages and styles before deployment to avoid culturally specific harms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22335v1)
