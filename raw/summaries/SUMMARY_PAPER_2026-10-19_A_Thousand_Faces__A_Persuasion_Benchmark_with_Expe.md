---
title: A Thousand Faces: A Persuasion Benchmark with Experience-Grounded Persuadees Informed by Psychology and Pragmatics
url: http://arxiv.org/abs/2610.25206v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-18_12-02-03Z_AThousandFaces_APersuasionBenchmarkwithExperience_.md
generated_at: 2026-10-19 23:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces A Thousand Faces (ATF-Persu), a persuasion benchmark comprising 1,000 personas across 200 topics and nine domains, designed to evaluate how well persuasive arguments address the personal, experience-grounded reasons behind a person's beliefs rather than merely matching stated positions. The authors demonstrate that existing benchmarks reward superficially matching arguments while overlooking whether those arguments engage the actual grounds for a person's views, and their evaluation shows lower persuasion success rates compared to three comparison benchmarks, indicating that experience-grounded persuasion is substantially harder than benchmark specifications suggest.

## Key Takeaways
- The paper argues that persuasion effectiveness depends on how a person's beliefs and desires arose from their experiences, which shape what they find credible, what matters to them, and what could prompt reconsideration. Existing benchmarks that specify beliefs and desires without these experiential connections can reward arguments that superficially match a description while failing to address the person's actual reasons for holding those views.
- ATF-Persu constructs five distinct personas per factual context by drawing on personality and attitude theories as well as conversational implicature, explicitly linking personal experiences to judgments, indirect expression of views, and grounds for revision. This design ensures that persuasion must engage with how views arose and how they are communicated, not just what the views are.
- Evaluation results show that complete background specifications yield broader use of supplied personal grounds and higher persona faithfulness compared to simplified specifications. Blinded reviewers rated ATF-Persu above the CToMPersu benchmark on identifiable personal reasons, their influence on responses, and contextual expression, validating the benchmark's design. The dataset is publicly available on HuggingFace.

## Context
This work sits at the intersection of NLP evaluation, computational persuasion, and cognitive psychology, addressing a recognized gap in how AI systems are benchmarked for their ability to persuade diverse human audiences. As large language models are increasingly deployed in contexts requiring tailored communication—healthcare, education, policy, and marketing—the field has lacked benchmarks that capture the nuanced, experience-dependent nature of human belief formation and the indirect ways people express their views through conversational context.

## Implications
For AI practitioners building persuasion systems, this benchmark signals that current evaluation methods may overestimate model performance by ignoring the personal and contextual dimensions of persuasion, meaning models that score well on existing benchmarks may fail in real-world applications where understanding a person's history and communication style is essential. For the broader field, the public availability of ATF-Persu provides a resource for developing and testing models that must reason about individual psychology and pragmatics, potentially driving progress toward more genuinely adaptive and empathetic AI communication systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25206v1)
