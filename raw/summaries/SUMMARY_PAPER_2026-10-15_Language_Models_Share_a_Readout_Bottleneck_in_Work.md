---
title: Language Models Share a Readout Bottleneck in Working Memory
url: http://arxiv.org/abs/2610.21176v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_03-32-37Z_LanguageModelsShareaReadoutBottleneckinWorkingMemo.md
generated_at: 2026-10-15 22:23
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether the working-memory limitations observed in large language models on the N-back task share a common mechanism with human working-memory failures. By testing 15 pretrained LLMs across three model families and minimal transformers trained from scratch, the author dissociates two competing explanations—attention precision failure versus interference during readout—and finds strong evidence that the bottleneck lies in reading items out under interference rather than in locating them via attention.

## Key Takeaways
- Attention heads in all three model families consistently attend to the correct target item on most missed matches, and linear probes can decode near-perfectly whether a matching letter occurred at the target or lure position even on trials where the model false-alarms. This directly contradicts the precision account, which posits that softmax attention fails to concentrate weight on the item N positions back, instead retrieving adjacent items.
- Sharpening attention yields negligible performance gains, whereas suppressing the letter identity of non-target items improves sensitivity (d') in nearly all model-by-load conditions tested. This demonstrates that the critical failure point is not locating the correct item but rather the readout stage where competing item contents corrupt the decision, aligning with interference accounts of human working memory.
- In larger models the task distributes across more attention heads, and removing interference provides greater benefit, suggesting that scale does not eliminate the bottleneck but rather redistributes it. In minimal transformers, a single attention layer is genuinely limited by precision constraints, but adding a second layer removes this constraint, revealing that architectural depth can partially compensate for readout interference.

## Context
This work sits at the intersection of cognitive science and mechanistic interpretability, probing whether behavioral parallels between LLMs and human working memory reflect shared underlying mechanisms or merely superficial similarity. The N-back task is a well-established paradigm in cognitive psychology for measuring working-memory capacity, and its reproduction by LLMs has raised questions about whether these models genuinely simulate cognitive processes or simply mimic behavioral patterns. By providing a mechanistic dissociation between attention precision and interference-based readout failure, the paper contributes to the growing effort to understand internal representations and decision pathways in transformer architectures.

## Implications
For practitioners building retrieval-augmented or memory-augmented language systems, this finding suggests that improving attention mechanisms alone will not resolve working-memory failures; instead, architectures should incorporate strategies to suppress or gate the content of non-target items during readout, such as attention masking or interference-filtering layers. For cognitive scientists, the results strengthen the parallel between LLM working-memory limits and human interference-based working-memory accounts, offering a computational testbed for theories of cognitive capacity. For model developers, the observation that deeper architectures can partially overcome single-layer precision limits highlights a concrete architectural lever for improving sequential reasoning tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21176v1)
