---
title: Text Dominance in Paralinguistic Conflict: Tracing Suppression Through Audio LLM Circuits
url: http://arxiv.org/abs/2610.25599v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_00-05-24Z_TextDominanceinParalinguisticConflict_TracingSuppr.md
generated_at: 2026-10-19 21:32
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether audio large language models (LLMs) deployed in real-world settings like crisis hotlines and customer support rely more on transcript content than on paralinguistic acoustic cues such as emotion, speaker identity, and sarcasm. Across six audio LLMs tested under LISTEN-style conflict conditions, the authors find a mean text-dominance rate of 0.78 (0.86 excluding sarcasm), demonstrating that these models systematically suppress audio-grounded information in favor of textual content. Through mechanistic interpretability techniques including probing, back-patching, and attention knockout, the authors trace how text-dominant claims propagate through intermediate relay tokens rather than through a single direct connection, and show that the effect manifests only in free-form generation, not in closed-set multiple-choice formats.

## Key Takeaways
- Across six audio LLMs evaluated under conflict conditions where text and audio signals disagree, the mean text-dominance rate reaches 0.78 overall and 0.86 when sarcasm is excluded, indicating a strong and consistent bias toward transcript content over paralinguistic cues such as emotion, speaker identity, and sarcasm. This suggests that current audio LLMs are not meaningfully leveraging acoustic information beyond what a standard speech-to-text pipeline would already provide.
- Probing in the most text-dominant model reveals that speaker identity remains linearly decodable at ceiling accuracy at the language model's input, meaning the failure to use paralinguistic information is not a perceptual encoding problem but rather a downstream suppression mechanism. Back-patching, a technique previously reported to repair lexical text dominance, shows no measurable effect here, though the authors note their own replication of its source task also failed (n=300), so they treat the null result as uninformative rather than conclusive evidence of non-transfer.
- Attention knockout experiments demonstrate that blocking the claim from propagating through intermediate tokens during open-ended generation partially restores audio-grounded output, while blocking the answer position's direct connection to the conflicting claim has no effect. This reveals that text-dominant influence travels through an intermediate relay circuit rather than a single severable edge. Critically, the effect appears only in free-form generation and not in closed-set multiple-choice evaluation, implying that benchmarks using multiple-choice formats may be systematically blind to this class of failure.

## Context
This work sits at the intersection of mechanistic interpretability and multimodal AI evaluation, addressing a critical gap in how audio LLMs are assessed for real-world deployment. As audio LLMs are increasingly proposed for sensitive applications like crisis hotlines and customer support—settings where emotional tone, speaker identity, and sarcasm carry essential meaning—understanding whether these models actually process acoustic information or merely default to transcript-based reasoning becomes a foundational question for the field. The paper contributes to a growing body of mechanistic interpretability research that seeks to trace specific failure modes through model circuits rather than relying solely on behavioral benchmarks.

## Implications
For practitioners deploying audio LLMs in emotionally sensitive or safety-critical settings, this research signals that current models may not be meaningfully more capable than a speech-to-text pipeline followed by a text-only LLM, undermining the value proposition of audio-native architectures. For the evaluation community, the finding that text dominance is invisible in closed-set multiple-choice benchmarks but visible in free-form generation calls for a rethinking of benchmark design to include open-ended generation tasks that can surface suppression effects. For interpretability researchers, the identification of an intermediate relay mechanism rather than a single direct edge suggests that targeted circuit interventions must account for distributed propagation pathways, complicating straightforward repair strategies like back-patching.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25599v1)
