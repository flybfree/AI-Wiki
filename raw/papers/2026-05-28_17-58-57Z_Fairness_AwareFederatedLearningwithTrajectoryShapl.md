---

title: Fairness-Aware Federated Learning with Trajectory Shapley Value
published: "2026-05-28T17:58:57Z"
authors: Daniel Kuznetsov, Ziqi Wang
url: http://arxiv.org/abs/2605.30336v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Fairness-Aware Federated Learning with Trajectory Shapley Value



**Source**: [Original Paper](http://arxiv.org/abs/2605.30336v1)
## Abstract
Federated learning is an emerging distributed paradigm that addresses the challenges posed by heterogeneous, privacy-sensitive data. It enables multiple clients to train a model collaboratively by aggregating their local updates at a server. However, conventional aggregation schemes typically use fixed weights that fail to reflect unequal and time-varying client contributions, leading to biased and unstable learning. To improve fairness and stability, we propose the Trajectory Shapley Value (TSV), a contribution metric that evaluates how each client influences the optimization trajectory of the global model using a validation-based, temporally consistent utility. Building on TSV, we design FedTSV, an adaptive aggregation method that converts per-round evaluations into dynamic client weights, allowing the server to respond to heterogeneous and adversarial participation in real time. Experiments on benchmark datasets show that FedTSV accelerates convergence, improves robustness, and yields more equitable contribution assessments, thereby providing a principled foundation for fairness-aware federated optimization.

## Metadata
- **Published**: 2026-05-28T17:58:57Z
- **Authors**: Daniel Kuznetsov, Ziqi Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.30336v1)