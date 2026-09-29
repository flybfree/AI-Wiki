---
title: Steering Language Model Goals with Value Transplant
published: 2026-09-28T00:26:19Z
authors: Pengcheng Jiang, Fabien Roger
url: http://arxiv.org/abs/2609.34056v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Steering Language Model Goals with Value Transplant

## Abstract
Reasoning models often act as if they pursue goals, but their efforts are not always directed toward what users intend, sometimes leading them to pursue unintended outcomes. Previous work has examined how models may internally track their progress toward their goals through a "value axis." We study whether changing such a signal can retarget the model's search toward a different goal. We test value transplant: at each token, we shift the host model's activation along a candidate value axis by the donor-host difference in value coordinates (multiplied by a large scalar), aiming to redirect the host toward the donor's goal. We study this intervention in Qwen3-8B and GPT-OSS-20B models fine-tuned into honest and cheating variants. We test several candidate value axes, including a self-rating axis constructed from activations preceding high versus low elicited self-ratings of progress. The intervention works in both directions, with an honest donor reducing test-gaming in a cheating host and a cheating donor increasing test-gaming in an honest host, showing that this signal can influence which strategy the model follows. On solvable coding tasks, transplant from an honest donor also improves the cheating host's hidden-test performance. Value transplant also works across model families, providing preliminary evidence for the intervention in a setting relevant to model control.

## Metadata
- **Published**: 2026-09-28T00:26:19Z
- **Authors**: Pengcheng Jiang, Fabien Roger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34056v1)