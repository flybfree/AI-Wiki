---
title: PRISM: Transfer and Limits of Activation Interventions in Tool-Calling Language Models
published: 2026-10-14T18:55:23Z
authors: Giovana Kerche Bonás, Thales Sales Almeida, Marcelo da Silva Reis, Rodrigo Nogueira, Marcos Meideiros Raimundo
url: http://arxiv.org/abs/2610.20808v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PRISM: Transfer and Limits of Activation Interventions in Tool-Calling Language Models

## Abstract
Recent literature shows that unsafe tool calls can often accompany textual refusals in language models. To investigate this hidden vulnerability, we introduce PRISM, a framework for evaluating the transfer of activation interventions across precision, languages, and scales. Our findings demonstrate that leveraging lower-resource settings (specifically quantized NF4 labels and cross-lingual transfer) offers a robust pathway to expose and improve model alignment. Notably, using behavioral labels from an NF4 copy enables stable intervention estimation even with very few scenarios. Furthermore, these alignment improvements transfer effectively across languages: five-language NF4-supervised directions successfully transfer to held-out Arabic, reducing unsafe violations in Llama-3.1-8B by 21.95 percentage points without target-language tuning. By mapping paired benign activations, we also successfully transfer these safety interventions to much larger models (up to 70B parameters). Ultimately, PRISM highlights how auxiliary supervision from compressed models and multilingual data can uncover and mitigate hazardous tool-calling behaviors across different model families. We release all experimental code and supporting artifacts at https://github.com/GiKerche/prism, alongside an interactive explorer of recorded model responses and experimental results at https://gikerche.github.io/prism/.

## Metadata
- **Published**: 2026-10-14T18:55:23Z
- **Authors**: Giovana Kerche Bonás, Thales Sales Almeida, Marcelo da Silva Reis, Rodrigo Nogueira, Marcos Meideiros Raimundo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.20808v1)