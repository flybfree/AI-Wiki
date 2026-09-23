---
title: On the Lexical Superstition of Large Language Models for Code Comprehension: Re-evaluation on Code of Low Lexical Quality
published: 2026-09-22T13:27:57Z
authors: Xin Shen, San-Zhuo Xi, Yali Du, Ming Li
url: http://arxiv.org/abs/2609.26388v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Lexical Superstition of Large Language Models for Code Comprehension: Re-evaluation on Code of Low Lexical Quality

## Abstract
Recent advances in large language models (LLMs) have made them widely used for code-related tasks. Identifier names are statistically informative in naturally occurring code, but their information is not always reliable. We investigate whether current LLMs assign disproportionate weight to lexical cues when renaming preserves program structure. We introduce Face/Off, a semantics-preserving identifier-renaming framework, and evaluate progressive naming conditions across multiple models and code-comprehension tasks. Within this framework, lexical overemphasis is pervasive across the evaluated models and primary tasks: performance generally decreases as identifier information is removed or made misleading, and outputs are often directed toward the meanings suggested by misleading names. The pattern persists under representative prompt- and fine-tuning-based interventions, suggesting that lexical overemphasis is an entrenched problem. A type-inference control confirms a boundary: naming effects are smaller when the answer is locally recoverable without the target name. These results do not imply that identifiers are unhelpful; rather, they reveal a systematic vulnerability in how current LLMs balance lexical cues against program structure. Our findings motivate evaluations and modeling methods that preserve the benefits of natural code regularities while keeping conclusions grounded in accurate, formalized code semantics.

## Metadata
- **Published**: 2026-09-22T13:27:57Z
- **Authors**: Xin Shen, San-Zhuo Xi, Yali Du, Ming Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.26388v1)