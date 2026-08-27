---
title: The Imperfective Paradox Is Not Necessarily in Large Language Models: A Benchmark Failure Before a Model Failure
published: 2026-08-25T18:00:18Z
authors: Kaiqiao Han, Yizhou Sun
url: http://arxiv.org/abs/2608.25005v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Imperfective Paradox Is Not Necessarily in Large Language Models: A Benchmark Failure Before a Model Failure

## Abstract
The imperfective paradox provides a useful test of compositional semantic analysis. Recent work constructs an NLI benchmark and reports that models frequently infer completed telic events from progressive descriptions, attributing this behavior to a Teleological Bias. It further argues that prompting interventions cause a Calibration Crisis. We reexamine the benchmark and conclusions and show that it is substantially affected by conceptual and evaluation mis-specifications. We identify three conceptual mis-specifications. In particular, Aspectual Reduction affects the benchmark construction, analysis, experiments, and conclusions. Under a strict NLI standard, 76% of Group A instances do not explicitly rule out culmination. In our native-speaker annotation, 38% of Group A examples and 29% of the Group C examples were judged to permit an alternative interpretation. To control these issues and lexical variation, we construct Lexically Matched Minimal Pairs. At the evaluation level, we formulate event-semantic NLI as a Multi-step Reasoning Problem and assess both intermediate semantic decisions and final predictions. Our results show that models often do not affirm culmination but nevertheless accept the corresponding simple-past hypothesis, a pattern we characterize as Sufficiency Bias. We further show that prompting interventions produce a Decision Shift among labels without reliably improving the underlying semantic understanding and reasoning. Intermediate and oracle-guided analyses identify two additional failure modes: errors in compositional aspectual classification and Surface-form Attraction toward surface-associated answers. Our experiments on Qwen-7B with suitable prompts, GPT-5.4, and Qwen-72B provide initial evidence for the context sensitivity of aspectual classification and suggest that these models can achieve performance comparable to that of human annotators.

## Metadata
- **Published**: 2026-08-25T18:00:18Z
- **Authors**: Kaiqiao Han, Yizhou Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25005v1)