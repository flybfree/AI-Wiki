---
title: FBFM: A Training-Free Asynchronous Feedback Mechanism for Flow-Matching in World-Action Models Execution
published: 2026-07-31T10:11:09Z
authors: Peize Li, Ruimeng Zhang, Ru Zhang, Cong Huang, Kai Chen, Shanghang Zhang
url: http://arxiv.org/abs/2607.29235v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FBFM: A Training-Free Asynchronous Feedback Mechanism for Flow-Matching in World-Action Models Execution

## Abstract
Although world-action models (WAMs) enhance long-horizon robot control by predicting visual evolution before acting, long-horizon reliability demands repeated re-grounding in real observations--not recursive rollout. Existing WAMs address this by refreshing history or KV cache with ground-truth data between chunks. However, such chunk-wise feedback operates at a coarse temporal granularity and thus fails to correct prediction errors at the individual time-step level. To address this, we propose Feedback Flow Matching (FBFM), a training-free inference mechanism that pushes re-grounding inside the actively generated chunk. During flow matching, FBFM applies a masked pseudoinverse correction to the conditional velocity field: it leverages the preceding action chunk to guide generation of the next action chunk, and uses the image observed after executing that preceding chunk to guide the next frame prediction. This cross-chunk pairing--where feedback from one chunk arrives in time to shape the next--creates an asynchronous loop that corrects errors without waiting for chunk boundaries. Being training-free, the mechanism improves responsiveness to unexpected events and suppresses drift in long-horizon tasks. We evaluate FBFM on both a joint-generation WAM (DreamZero) and a stage-wise WAM (LingBot-VA). On selected LIBERO and RoboTwin2.0 tasks, it improves success rates by over 5% in favorable settings, and real-world robot observation-prediction diagnostics show notably better tracking. We argue that FBFM offers a new paradigm for fine-grained online correction, bridging open-loop flow generation with closed-loop real-world dynamics.

## Metadata
- **Published**: 2026-07-31T10:11:09Z
- **Authors**: Peize Li, Ruimeng Zhang, Ru Zhang, Cong Huang, Kai Chen, Shanghang Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29235v1)