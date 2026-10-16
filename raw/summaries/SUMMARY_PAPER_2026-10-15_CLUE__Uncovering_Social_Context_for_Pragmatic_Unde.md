---
title: CLUE: Uncovering Social Context for Pragmatic Understanding
url: http://arxiv.org/abs/2610.22167v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_16-28-19Z_CLUE_UncoveringSocialContextforPragmaticUnderstand.md
generated_at: 2026-10-15 23:10
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
CLUE is a two-stage training pipeline designed to teach language models how to discover and leverage social-contextual cues embedded within conversations to support pragmatic interpretation. By combining supervised evidence reasoning with a reinforcement learning reward called Grounded Information Utilization (IU_G), the method trains models to identify relevant social inferences while penalizing unnecessary reasoning effort. The approach yields substantial performance gains over a base Qwen model across multiple tasks, languages, and genres, while simultaneously reducing reasoning token usage by more than 80%.

## Key Takeaways
- CLUE introduces a two-stage pipeline that first trains a model through supervised evidence reasoning to identify socially relevant cues in dialogue, then fine-tunes it using GRPO (Group Relative Policy Optimization) guided by the IU_G reward signal. This reward specifically credits novel, evidence-supported social inferences while penalizing verbose or unsupported reasoning chains, effectively teaching the model to be both accurate and efficient in its interpretive process.
- The method demonstrates strong generalization: trained on a small set of conversational examples, CLUE achieves relative gains of 17.3% in-domain and 9.3% out-of-domain in average weighted F1 compared to base Qwen, with higher F1 on four of five out-of-domain evaluations spanning different tasks, languages, and genres. At inference time, the model operates in a fully self-contained manner, reasoning only over the supplied interaction without requiring external context injection.
- Human evaluation confirms that CLUE more reliably grounds its explanations in specific conversational content, showing closer alignment between its quoted evidence and context selected by human annotators. This suggests the model learns to distinguish genuinely relevant social cues from spurious associations, a critical capability for trustworthy pragmatic understanding.

## Context
Pragmatic understanding in NLP has long been hindered by the assumption that social context must be externally supplied to models. Prior work demonstrated that injecting relevant context improves social judgments, but this paper challenges that paradigm by showing that much of the needed information is already latent in the conversation itself. CLUE shifts the research direction from context injection to context discovery, aligning with broader efforts in the field to build models that perform grounded, evidence-based reasoning rather than relying on retrieval or prompt engineering tricks.

## Implications
For practitioners building conversational AI systems, CLUE offers a path toward models that can autonomously extract social cues from dialogue without requiring curated context pipelines, reducing engineering overhead and improving interpretability. The dramatic reduction in reasoning tokens (over 80%) also has practical cost and latency implications for deployment at scale. For the research community, the IU_G reward framework provides a template for training models to balance inferential accuracy against reasoning efficiency, a principle that could extend to other domains requiring grounded, evidence-based interpretation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22167v1)
