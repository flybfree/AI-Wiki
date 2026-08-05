---
title: Reachability Is Not Realization: Tracing the Sources of LLM Benchmark Gains
published: 2026-08-04T06:52:27Z
authors: Yanchao Li, Wanhao Liu, Jiaqing Xie, Ben Gao, Yanbo Wang, Tianfan Fu, Yuqiang Li
url: http://arxiv.org/abs/2608.03219v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reachability Is Not Realization: Tracing the Sources of LLM Benchmark Gains

## Abstract
Benchmark gains are often treated as evidence of greater LLM capability. Yet the same gain can reflect different changes in model behavior. A model may reach new answers, or produce answers that were already within reach. Aggregate scores do not distinguish these changes question by question. We establish a question-level audit under fixed budgets, temperatures, and answer formats. A question is realized when the default deployment procedure produces the correct answer. A question is reachable when a specified probe finds that answer within a fixed budget. We first test whether inference-time layer routing can expand reachability. Under a matched budget, random routes match or exceed structured search in all 43 model and task settings. Answer-blind procedures retain almost none of this gain, which instead requires access to the correct answer. We then ask why reachable answers sometimes fail to appear. Across six cases spanning 0.5B to 31B, silencing one identified MLP block repairs 68 to 92 percent of a predefined failure set. We next test whether training closes the gap by expanding reachability. In five of six matched evaluations, deployed performance rises while the reachable ceiling remains flat or falls. For DAPO, the deployed score rises by 14.7 points while the reachable ceiling falls by 13.3 points. Across the settings we audit, realization and reachability therefore do not always change together. Claims of capability expansion should report both realized performance and reachability under matched evaluation conditions. Code is available at https://github.com/LiZaiyuan0619/reachability-not-realization

## Metadata
- **Published**: 2026-08-04T06:52:27Z
- **Authors**: Yanchao Li, Wanhao Liu, Jiaqing Xie, Ben Gao, Yanbo Wang, Tianfan Fu, Yuqiang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03219v1)