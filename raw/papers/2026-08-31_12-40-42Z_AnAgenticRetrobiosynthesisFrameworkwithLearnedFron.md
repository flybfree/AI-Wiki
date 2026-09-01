---
title: An Agentic Retrobiosynthesis Framework with Learned Frontier Selection
published: 2026-08-31T12:40:42Z
authors: Philippe Meyer, Guillaume Gricourt, Thomas Duigou, Joan Hérisson, Jean-Loup Faulon
url: http://arxiv.org/abs/2608.30702v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Agentic Retrobiosynthesis Framework with Learned Frontier Selection

## Abstract
Large language models are increasingly used as agents for multistep retrosynthesis, raising the question of how much their search policy contributes independently of the underlying reaction model. We investigate this question in a biological setting through rule-based retrobiosynthesis: a deterministic biochemical engine generates the same validated transitions for every method, searching for routes that terminate in metabolites available to an \emph{Escherichia coli} chassis, while the policy only selects which frontier molecule to expand next. Prompted and LoRA-tuned Qwen2.5-7B policies use a strict choice-only interface. The fine-tuned policy reaches $65\pm1$\% solve rate at 10 expansions on LASER versus 59\% for MCTS, and at 200 expansions reaches $78\pm1$\% versus 75\% on LASER, $88\pm3$\% versus 80\% on the RetroPath RL Golden benchmark, and $63\pm2$\% versus 45\% on the BioNavi-NP benchmark. Fine-tuning also consistently outperforms direct prompting. These results show that route-supervised frontier selection can improve budgeted search without altering biochemical generation, although performance remains dependent on frontier construction and reaction ranking.

## Metadata
- **Published**: 2026-08-31T12:40:42Z
- **Authors**: Philippe Meyer, Guillaume Gricourt, Thomas Duigou, Joan Hérisson, Jean-Loup Faulon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30702v1)