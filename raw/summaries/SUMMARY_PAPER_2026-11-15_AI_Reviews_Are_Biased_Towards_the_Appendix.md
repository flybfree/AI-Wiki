---
title: AI Reviews Are Biased Towards the Appendix
url: http://arxiv.org/abs/2611.17811v1
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-13_06-47-34Z_AIReviewsAreBiasedTowardstheAppendix.md
generated_at: 2026-11-15 21:21
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates where large language models direct their criticisms when generating peer review feedback for academic papers. Analyzing 2,000 papers from major conferences including ACL, EMNLP, COLM, and ICLR, the authors demonstrate that GPT and Claude models draw approximately 50% or more of their identified weaknesses from paper appendices, whereas human reviewers draw only 8.4% of their criticisms from appendices. The finding holds consistently across different LLM access methods, including API calls, coding-agent workflows, and web-access-based interactions.

## Key Takeaways
- LLMs disproportionately target appendices for criticism: across all tested access methods (API, coding-agent, and web access), GPT and Claude models consistently source about 50% or more of their review weaknesses from the appendix section of papers. This suggests a systematic bias in how these models parse and evaluate paper content, potentially over-weighting supplementary material relative to core contributions.
- Human reviewers behave fundamentally differently: humans draw only 8.4% of their weaknesses from appendices, and those criticisms primarily concern presentation quality and content directly related to the paper's core idea. This stark contrast highlights that LLM-generated reviews do not mirror human evaluative priorities and may misdirect reviewer attention toward peripheral sections.
- LLM criticisms target fine-grained technical details buried deep in appendices: rather than focusing on central contributions, methodology, or claim validity, LLMs identify weaknesses in granular technical details that are not central to a paper's contributions. This means AI-generated review feedback may generate noise that distracts from substantive evaluation of a paper's actual scientific merit.

## Context
As LLMs become increasingly embedded in the peer review pipeline at major AI and NLP conferences, understanding their behavior is critical for maintaining review quality and fairness. Prior research has examined how LLM-generated reviews align with human reviews in aggregate, but this paper fills a critical gap by dissecting the spatial distribution of criticisms across paper sections. The finding that LLMs systematically over-index on appendices reveals a structural blind spot in current AI-assisted reviewing workflows, raising questions about whether these tools genuinely evaluate scientific contribution or merely surface peripheral inconsistencies.

## Implications
For conference organizers and program committees integrating AI review tools, this bias means that AI-generated feedback may systematically underweight core methodological and conceptual weaknesses while overemphasizing minor technical details in supplementary material. Practitioners relying on LLM-assisted reviews should treat appendix-focused criticisms with caution and ensure human oversight prioritizes evaluation of central claims and contributions. The authors' publicly available code and dataset provide a foundation for developing mitigation strategies, such as section-aware prompting or weighting schemes, to make AI review tools more aligned with human evaluative standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.17811v1)
