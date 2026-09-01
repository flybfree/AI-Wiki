---
title: Evaluating the Semantic Specificity of Representation Steering in Language Models
published: 2026-08-29T20:31:32Z
authors: Zhangdie Yuan, Andreas Vlachos
url: http://arxiv.org/abs/2608.29431v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating the Semantic Specificity of Representation Steering in Language Models

## Abstract
Localized Representation Steering (LRS) is widely used to correct reasoning pathologies in large language models. However, standard benchmark evaluations can easily be fooled by superficial label overrides, creating a false impression of reasoning circuit repairs. In this work, we propose Cross-Rule Transfer (CRT), a diagnostic framework that audits representational interventions by evaluating them on rule families where the model is natively competent. Evaluating late-layer LRS for a widespread logical failure, contradiction blindness, reveals that the intervention merely injects a global label bias: applying the steering vector to rules the model already handles correctly (99.6% baseline) degrades performance to 40.4% by forcing false contradiction predictions. We support this diagnosis with four complementary controls (direct logit bias equivalence, control vector label-flipping, cross-model grafting, and early-layer steering checks), providing a rigorous methodology to distinguish genuine reasoning repairs from superficial label overrides.

## Metadata
- **Published**: 2026-08-29T20:31:32Z
- **Authors**: Zhangdie Yuan, Andreas Vlachos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29431v1)