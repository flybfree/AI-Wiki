---
title: Recall Is Not Protection: Evaluating Safety Monitors Against Model Compliance
published: 2026-09-05T01:19:35Z
authors: Sripad Karne
url: http://arxiv.org/abs/2609.05797v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Recall Is Not Protection: Evaluating Safety Monitors Against Model Compliance

## Abstract
Safety monitors screen prompts sent to deployed language models, flagging harmful requests so they are never answered. They are evaluated by recall against harmfulness labels, but a catch only prevents harm if the model would otherwise have complied. We measure the difference directly: we sample repeated responses from the target model, call a harmful prompt \emph{elicitable} if the model complies at least once, and report monitor recall separately on elicitable and non-elicitable prompts. Across six monitor configurations and three model families, spanning activation probes, fine-tuned text guards, and a 120B policy-conditioned reasoning classifier, recall on elicitable prompts falls 0.22 to 0.38 below recall on non-elicitable prompts at a fixed false positive rate. The prompts a monitor misses are 2.8 to 5.6 times more likely to be complied with than the prompts it catches. The gap replicates across three model families and appears also in text-only monitors entirely independent of the target model. This suggests that standard recall may overstate the protection monitors provide in practice, and that monitors should be evaluated against what their models will actually answer.

## Metadata
- **Published**: 2026-09-05T01:19:35Z
- **Authors**: Sripad Karne
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05797v1)