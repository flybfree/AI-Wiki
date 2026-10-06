---
title: Hidden in the Comments: A Context-Injection Attack Surface in Code LLMs
published: 2026-10-04T11:39:57Z
authors: Noor Munir, Francesco Quinzan, Stephen Roberts
url: http://arxiv.org/abs/2610.05139v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hidden in the Comments: A Context-Injection Attack Surface in Code LLMs

## Abstract
Code large language model (Code LLM) assistants generate code from heterogeneous development contexts, including open files, imported modules, pasted snippets, and comments, much of which may originate from untrusted sources. We investigate whether insecure instructions embedded in such contexts can steer Code LLMs toward vulnerable code without access to model weights or training data. We evaluate ten open-weight Code LLMs spanning 3B--13B parameters, including four base and six instruction-tuned models, across ten web-application weakness classes. We compare completion tasks containing insecure instructions embedded as code comments with benign tasks without malicious instructions. Attack-condition completions contained a medium-or-higher weakness in {\bf 77.4--92.3}\% of cases, compared with {\bf 1.7--5.1}\% in the benign condition. Base and instruction-tuned models averaged 86.5\% and 84.5\% vulnerable outputs, respectively; equivalence testing and three matched model pairs indicated reductions of at most 8.1\% after instruction tuning. Susceptibility showed no clear association with model scale or specialization. Among vulnerable attack outputs, 86.2--91.0\% were rated high or critical, and the effect persisted without the pattern-based detector. Post-generation screening reduced but did not eliminate the risk, the strongest screen leaving roughly one-third undetected. These findings identify inference-time context injection as a substantial attack surface and motivate provenance-aware training objectives.

## Metadata
- **Published**: 2026-10-04T11:39:57Z
- **Authors**: Noor Munir, Francesco Quinzan, Stephen Roberts
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05139v1)