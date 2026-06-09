---
title: A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders
published: 2026-05-18T11:09:22Z
authors: Zegu Zhang, Jianhua Peng, Jian Zhang
url: http://arxiv.org/abs/2605.18224v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Simplex Witness Certificate for Constant Collapse in Variational Autoencoders

## Abstract
This note studies exact constant collapse in variational autoencoders, where the encoder mean becomes independent of the input. The goal is to make this specific failure mode pre-designable, monitorable during training, and certifiable after training. The prior is kept as the standard Gaussian. Given a fixed teacher posterior, we attach to the latent mean a fixed simplex witness head. The resulting teacher-student alignment loss has an exact constant-predictor baseline equal to the teacher information. If the alignment loss is below this baseline, the latent mean cannot be input-independent constant collapsed.   The simplex witness also has a closed-form inverse. Any full-support teacher posterior can be represented by embedding its centered log-odds into the latent space. This gives an explicit latent energy cost and explains when the alignment loss can be made small. A computable view gap handles the case where teacher targets are computed from a different view. Thus exact constant collapse is converted from an after-the-fact training pathology into a design-and-certificate problem.

## Metadata
- **Published**: 2026-05-18T11:09:22Z
- **Authors**: Zegu Zhang, Jianhua Peng, Jian Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.18224v1)