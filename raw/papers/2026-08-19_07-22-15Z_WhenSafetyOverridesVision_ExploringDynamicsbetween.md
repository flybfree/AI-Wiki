---
title: When Safety Overrides Vision: Exploring Dynamics between Vision Influence and Safety Alignment in Vision-Language Models
published: 2026-08-19T07:22:15Z
authors: Mehak Gupta, Tanmoy Chakraborty
url: http://arxiv.org/abs/2608.18628v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Safety Overrides Vision: Exploring Dynamics between Vision Influence and Safety Alignment in Vision-Language Models

## Abstract
Aligned vision-language models (VLMs) are designed to balance grounded visual reasoning with safe generation behavior. However, we observe a striking phenomenon: under safety-constrained instruction, models frequently abstain from answering questions that remain correctly answerable under default instruction despite receiving identical image-question inputs. This raises a fundamental question: does safety alignment suppress perceptual grounding itself, or does visual evidence remain internally available while generation is redirected toward abstention? In this work, we investigate the internal decoding dynamics underlying safety-induced abstention in aligned VLMs. Across multiple architectures and multimodal benchmarks, we show that abstained generations remain consistently influenced by visual evidence throughout decoding, indicating that perceptual grounding is largely preserved despite refusal behavior. We further demonstrate that, although the representational organization of refusal differs substantially across architectures, safety-constrained instruction consistently alters late-stage hidden-state dynamics toward refusal-oriented decoding. Finally, through targeted activation-level interventions, we show that suppressing refusal-related representations reliably restores grounded answering behavior across models without retraining or modifying visual inputs. Together, these findings reveal a previously underexplored failure mode in aligned VLMs: safety alignment can override grounded visual expression even when perceptual evidence remains internally preserved.

## Metadata
- **Published**: 2026-08-19T07:22:15Z
- **Authors**: Mehak Gupta, Tanmoy Chakraborty
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18628v1)