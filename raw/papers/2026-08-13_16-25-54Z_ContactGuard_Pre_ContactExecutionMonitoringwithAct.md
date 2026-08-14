---
title: ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models
published: 2026-08-13T16:25:54Z
authors: Gehan Zheng, Matthew Johnson-Roberson, Weiming Zhi
url: http://arxiv.org/abs/2608.13438v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ContactGuard: Pre-Contact Execution Monitoring with Action-Conditioned Latent World Models

## Abstract
Contact-rich manipulation failures are often detected only after the robot has committed to contact. This is especially limiting in wrist-camera setups: close gripper--object views help observe contact, but a poor approach may already push, miss, slip, or disturb the object before conventional detectors react. We introduce \emph{ContactGuard}, a pre-contact execution monitor for chunked visuomotor policies. Given the policy's planned action chunk, ContactGuard predicts its short-horizon consequence in latent visual space and aborts if the predicted future latent indicates likely failure. Its latent world model is trained from unlabelled robot trajectories to predict compact multi-view visual embeddings under planned actions, avoiding pixel-level video prediction. A lightweight failure probe is then trained from a small labelled set of pre-contact clips. At deployment, ContactGuard anchors prediction before an imminent contact event, rolls the model forward under the policy's own actions, and verifies the predicted post-contact latent. Across real-world contact-rich manipulation tasks, ContactGuard predicts failure more accurately than direct and corrupted-action ablations, and transfers to live robot as a pre-contact abort signal without modifying the underlying policy.

## Metadata
- **Published**: 2026-08-13T16:25:54Z
- **Authors**: Gehan Zheng, Matthew Johnson-Roberson, Weiming Zhi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13438v1)