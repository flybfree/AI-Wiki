---

title: 'Forward-Learned Discrete Diffusion: Learning how to noise to denoise faster'
published: "2026-05-18T10:43:36Z"
authors: Grigory Bartosh, Teodora Pandeva, Sushrut Karmalkar, Javier Zazo
url: http://arxiv.org/abs/2605.18204v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Forward-Learned Discrete Diffusion: Learning how to noise to denoise faster



**Source**: [Original Paper](http://arxiv.org/abs/2605.18204v1)
## Abstract
Discrete diffusion models are a powerful class of generative models with strong performance across many domains. For efficiency, however, discrete diffusion typically parameterizes the generative (reverse) process with factorized distributions, which makes it difficult for the model to learn the target process in a small number of steps and necessitates a long, computationally expensive sampling procedure. To reduce the gap between the target and model distributions and enable few-step generation, we propose Forward-Learned Discrete Diffusion (FLDD), which introduces discrete diffusion with a learnable forward (noising) process. Rather than fixing a Markovian forward chain, we adopt a non-Markovian formulation with learnable marginal and posterior distributions. This allows the generative process to remain factorized while matching the target defined by the noising process. We train all parameters end-to-end under the standard variational objective. Experiments on various benchmarks show that, for a given number of sampling steps, our approach produces a higher quality samples than conventional discrete diffusion models using the same reverse parameterization.

## Metadata
- **Published**: 2026-05-18T10:43:36Z
- **Authors**: Grigory Bartosh, Teodora Pandeva, Sushrut Karmalkar, Javier Zazo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.18204v1)