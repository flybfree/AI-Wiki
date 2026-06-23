---
title: Can LLMs Reliably Self-Report Adversarial Prefills, and How?
published: 2026-06-22T17:56:30Z
authors: Quang Minh Nguyen, Uzair Ahmed, Taegyoon Kim
url: http://arxiv.org/abs/2606.23671v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can LLMs Reliably Self-Report Adversarial Prefills, and How?

## Abstract
Prior work shows that large language models (LLMs) exhibit introspective capability on benign tasks. We extend the question to safety contexts and examine how reliably a model can recognize that its own prior response was elicited by an adversarial prefill attack. Across ten open-weight instruction-tuned LLMs (3B to 70B) and four safety benchmarks, no model reliably recognizes its own compromised outputs, with models claiming intent on prefilled responses at an average rate of $27.3\%$. Introspective signal stems largely from safety- and refusal-related reasoning. Orthogonalizing models' weights against the refusal direction collapses the gap between claiming rates on prefilled and natural outputs to near zero, though the direction is not its unique mediator. The signal is also probe-dependent: framing the question as internal intention versus external tampering elicits qualitatively different responses on the same models. We test three LoRA finetuning methods (SFT, GRPO, DPO) on eight models from 3B to 27B; all three widen the intention-probe gap on every model from 8B to 27B, with method ranking varying by model. The intervention does not transfer to the tampering probe and counterintuitively raises attack success rate under adversarial prefill on most models, amounting to a partial mitigation. These findings outline mechanisms underpinning the observed introspective signals in safety contexts and highlight risks in the reliability of LLM self-reports.

## Metadata
- **Published**: 2026-06-22T17:56:30Z
- **Authors**: Quang Minh Nguyen, Uzair Ahmed, Taegyoon Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.23671v1)