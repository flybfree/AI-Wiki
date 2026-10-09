---
title: Reading the Room: Foundations, Design, and Challenges of Normative Competence in LLMs
published: 2026-10-07T21:02:52Z
authors: Andrea Wynn, Harsh Satija,  Seokhyun,  Baek, Anqi Liu, Eric Nalisnick, Gillian K. Hadfield
url: http://arxiv.org/abs/2610.10906v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reading the Room: Foundations, Design, and Challenges of Normative Competence in LLMs

## Abstract
Human communities are governed by normative systems: shared standards that produce \textit{norms} dictating acceptable behavior, enforced through community sanctioning. Aligning increasingly autonomous AI systems with these norms is a central alignment challenge, complicated by the fact that norms are vast in number, change quickly, and are often arbitrary (e.g., dress or language conventions). Thus, alignment requires \textit{normative competence}: the ability to discern from interaction alone what norms a community enforces without relying on static pretrained knowledge. We introduce a multi-agent community debate setting, where access to debate is governed by synthetic norms, to study normative competence in isolation from pretraining exposure. We show that baseline LLM agents fail to learn norms even when doing so would improve their accuracy. We then experiment with various \textit{normative modules} -- architectural components for norm inference -- finding that norm-following is highly sensitive to both the style of norm and the model powering the normative module, suggesting a lack of generalizability. Furthermore, when idiosyncratic, non-normative behaviors accompany the true norm, LLM agents exhibit an unselective attribution failure: they indiscriminately copy idiosyncratic noise alongside enforced rules, a pattern that persists even when imitating unnecessary behaviors is explicitly penalized. To the best of our knowledge, our work is the first to operationalize and evaluate normative competence in LLMs, demonstrating that current AI systems excel at behavioral mimicry but lack the capacity to discern socially enforced order.

## Metadata
- **Published**: 2026-10-07T21:02:52Z
- **Authors**: Andrea Wynn, Harsh Satija,  Seokhyun,  Baek, Anqi Liu, Eric Nalisnick, Gillian K. Hadfield
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.10906v1)