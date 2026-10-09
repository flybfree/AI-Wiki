---
title: Clinician use of language models diverges from how the models are evaluated
url: http://arxiv.org/abs/2610.11069v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_01-29-04Z_Clinicianuseoflanguagemodelsdivergesfromhowthemode.md
generated_at: 2026-10-08 21:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper examines whether public benchmarks used to evaluate large language models for clinical deployment actually reflect the real-world queries clinicians submit to AI assistants. By analyzing 127,833 queries from 6,342 clinicians across 35 specialties and comparing them against 58 public benchmarks, the authors demonstrate a severe mismatch: real clinical use is dominated by documentation and knowledge retrieval tasks, while benchmarks focus almost entirely on diagnostic reasoning. The findings suggest that current evaluation practices substantially misrepresent how clinical AI systems are actually used in practice.

## Key Takeaways
- Real clinical AI usage is overwhelmingly administrative and informational rather than diagnostic: documentation and administration tasks accounted for 36.2% of queries, knowledge retrieval for 28.9%, while diagnosis represented only 3.7%. This means nearly two-thirds of clinical AI interactions involve tasks that most evaluation benchmarks do not test, and more than a third of queries could not be adequately answered as posed, highlighting gaps in both model capability and evaluation coverage.
- The authors constructed the Clinical AI Benchmark Atlas by applying their clinician-validated RCQ-Map framework to 58 public benchmarks from major evaluation suites and frontier model reports. The median benchmark contained zero documentation requests and shared only 31% of the task distribution found in real clinical use—less than what a uniform random spread across task categories would produce. This reveals that even benchmarks explicitly designed to resemble clinical practice were no closer to real use than those used in frontier model evaluations.
- The RCQ-Map framework itself represents a methodological contribution, providing a structured taxonomy grounded in clinical question taxonomies and LLM evaluation taxonomies that records task type, intent, answerability, missing information, and potential harm for each query, enabling systematic comparison between benchmark items and real-world clinical interactions.

## Context
The evaluation of clinical AI systems has relied heavily on benchmark scores derived from examination questions, curated case vignettes, and diagnostic reasoning tasks, creating an ecosystem where model developers optimize for these narrow tasks while health systems deploy assistants for broad operational workflows. This paper addresses a critical blind spot in the AI evaluation literature: the assumption that benchmark performance predicts deployment performance has never been empirically validated against actual clinical query distributions. By bridging clinical informatics, LLM evaluation methodology, and real-world deployment data, the work challenges a foundational assumption in how healthcare AI readiness is assessed.

## Implications
For health systems and clinicians deploying AI assistants, this research signals that high benchmark scores should not be taken as evidence of readiness for the documentation, administrative, and knowledge-retrieval tasks that constitute the bulk of clinical AI use. For AI developers and evaluation researchers, the findings call for a fundamental redesign of clinical AI benchmarks to incorporate the task distributions actually encountered in practice, including multi-turn interactions, incomplete queries, and administrative workflows. For regulators and procurement decision-makers, the paper underscores that current evaluation suites may systematically overestimate diagnostic capability while underestimating the frequency of unanswerable or poorly posed queries, potentially leading to unsafe deployment decisions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11069v1)
