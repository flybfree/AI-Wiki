---
title: RESKILL: Explicit Failure Attribution and Structured Repair for Interactive Language Agents
published: 2026-09-14T14:55:13Z
authors: Mengyi Deng, Xin Li, Duyi Pan, Zilin Wang, Zhiwei Li, Zhijiang Guo, Wei Wang
url: http://arxiv.org/abs/2609.15684v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RESKILL: Explicit Failure Attribution and Structured Repair for Interactive Language Agents

## Abstract
Language agents increasingly rely on reusable skills, but post-failure repair is often handled by opaque one-shot reflection: a model generates a skill patch without explicitly maintaining how failure explanations relate to candidate repairs or how unsuccessful retests should influence later edits. We introduce RESKILL, a structured repair framework that maintains an explicit repair state across repair rounds. Given a failed rollout, the framework links failure hypotheses to candidate skill patches, selects local repairs through coverage-based attribution, retests the edited skill set in the environment, and uses retest outcomes to guide subsequent repair updates. The language model supplies structured repair factors, while the repair procedure records them, compares local skill patches by how well they address active failure explanations, and carries unsuccessful retest outcomes into later repair rounds. We evaluate RESKILL on ALFWorld and TextCraft across three model sizes under fixed repair budgets. RESKILL obtains the strongest final success in all six benchmark-model settings, improving average final success by 3.7 percentage points over direct repair and 3.3 points over hypothesis-conditioned repair. These results suggest that explicit attribution alone is insufficient; durable improvement emerges when attribution is integrated with repair selection and persistent retest-conditioned update.

## Metadata
- **Published**: 2026-09-14T14:55:13Z
- **Authors**: Mengyi Deng, Xin Li, Duyi Pan, Zilin Wang, Zhiwei Li, Zhijiang Guo, Wei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15684v1)