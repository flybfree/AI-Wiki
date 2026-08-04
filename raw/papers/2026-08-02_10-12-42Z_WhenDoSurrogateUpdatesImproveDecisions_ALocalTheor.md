---
title: When Do Surrogate Updates Improve Decisions? A Local Theory of Trajectory-Wise Transfer
published: 2026-08-02T10:12:42Z
authors: Yuyang Shen
url: http://arxiv.org/abs/2608.01130v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Do Surrogate Updates Improve Decisions? A Local Theory of Trajectory-Wise Transfer

## Abstract
A broad range of models face the mismatch where they are updated through trajectory losses but are evaluated by downstream task reward. Here, a trajectory is a training instance that induces a surrogate loss whose reduction might not track the model's decision utility update. Theoretically, we ask when one step of trajectory training reduces both population surrogate loss and decision risk, and how transfer accumulates along repeated updates. To formalize this, we first fix a checkpoint and a restricted update space, and define the reductions in population surrogate risk and decision risk induced by a trajectory as its learnability and decision utility, respectively. On this basis, our theory yields four main results. First, a one-step transfer bound separates their discrepancy into first-order gradient misalignment after nonnegative calibration and second-order curvature; and a pathwise extension accumulates the same terms over repeated updates. Second, when the accessible surrogate gradient is nonzero, universal first-order transfer over every accessible direction holds exactly when the accessible surrogate and decision gradients are positively collinear. Third, the calibration gap bounds the decision regret of learnability-based trajectory selection, while a candidate-difference refinement tightens this guarantee by retaining only directions that affect pairwise rankings. Finally, we establish an approximation--calibration trade-off across nested update spaces. Controlled gridworld and LLM post-training experiments yield results consistent with our predictions.

## Metadata
- **Published**: 2026-08-02T10:12:42Z
- **Authors**: Yuyang Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01130v1)