---
title: UDHRBench: Benchmarking Human Rights in Large Language Models
published: 2026-10-10T20:59:28Z
authors: Alak Raad, Noreldin Morssy, Zeerak Suhail, Serin Atiani, Mustafa Jarrar
url: http://arxiv.org/abs/2610.15179v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# UDHRBench: Benchmarking Human Rights in Large Language Models

## Abstract
Large language models are increasingly deployed in contexts requiring adherence to ethical and legal norms, yet their alignment with internationally recognized human rights standards remains underexplored. We introduce UDHRBench, a large-scale benchmark for operationalising the evaluation of large language model compliance with the Universal Declaration of Human Rights. The dataset comprises 1,124 human rights confronting questions covering all 30 articles and 4,496 responses from four large language models (ChatGPT, Grok, Gemini, and Fanar), manually annotated by experts for alignment, with high inter-annotator agreement ($κ= 0.801$). Our analysis reveals systematic and non-trivial misalignments, showing that violations typically arise through seemingly rational reasoning: appeals to efficiency, risk management, or scientific neutrality, rather than explicit rejection of rights. We further propose an LLM-as-a-Judge framework for automated evaluation using zero-shot and few-shot prompting, achieving 89.8\% weighted F1-score in detecting human-rights misalignment, alongside a novel Alignment Leniency Score that quantifies how judge models resolve ambiguous cases. The dataset, annotations, and code will be released as open-source resources (https://sina.birzeit.edu/UDHRBench).

## Metadata
- **Published**: 2026-10-10T20:59:28Z
- **Authors**: Alak Raad, Noreldin Morssy, Zeerak Suhail, Serin Atiani, Mustafa Jarrar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15179v1)