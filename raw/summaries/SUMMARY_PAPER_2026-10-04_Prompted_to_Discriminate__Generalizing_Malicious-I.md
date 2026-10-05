---
title: Prompted to Discriminate: Generalizing Malicious-Input Probes in the Wild
url: http://arxiv.org/abs/2610.02413v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_19-36-57Z_PromptedtoDiscriminate_GeneralizingMalicious_Input.md
generated_at: 2026-10-04 21:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether appending a short classification instruction after a user's turn can sharpen activation probes used as runtime safety monitors in LLM agents. Through controlled experiments across 13 safety benchmarks and three open-weight model families, the authors demonstrate that a classification-format suffix consistently improves out-of-distribution detection by up to approximately 4 AUC points, and that the benefit stems from the classification format itself rather than the specific labels used.

## Key Takeaways
- A classification suffix appended after the user's input reliably improves out-of-distribution detection on a single-position probe, gaining up to ~4 AUC points over no suffix. Crucially, prompting the model to classify the input—even into content-free, meaningless labels—outperforms off-topic or merely-attentive suffixes, indicating the structural act of classification is what concentrates the signal the probe must separate.
- The gain is format-driven, not criterion-driven: a content-free suffix matches the performance of a real malicious/benign classification suffix, with the named criterion adding precision only at strict operating thresholds. This means practitioners do not need to craft domain-specific label sets to benefit from the technique.
- The benefit generalizes beyond single-position probes to multi-position pooling probes used in production deployments (attention-based, multi-max, and MLP readouts), though the optimal suffix choice becomes readout-dependent in those settings. Served through a KV-cache fork, the technique is a cheap drop-in for any activation-probe monitor, but it is not universally beneficial—its effectiveness varies by model family and probe architecture.

## Context
Activation probes have emerged as a lightweight, low-latency mechanism for runtime safety monitoring in LLM agents, detecting prompt injections, jailbreaks, and unsafe requests by reading the model's hidden state before the agent acts. As LLM-as-judge prompting has popularized the idea of steering model representations through classification instructions, this paper bridges that prompting technique with internal-state monitoring, asking whether the same prompting tricks transfer to probe sharpening. The work addresses a practical deployment question: whether a probe trained on known attack types generalizes to unseen ones in production, and whether a trivial suffix can close that generalization gap.

## Implications
For practitioners deploying safety monitors in production LLM systems, this work offers a near-zero-cost intervention—appending a classification instruction via a KV-cache fork—that can meaningfully improve detection of novel attack types without retraining the probe or the model. However, the findings also caution against treating the technique as a universal fix: the optimal suffix and its magnitude of benefit depend on the specific model family and probe readout architecture, meaning teams must validate the approach within their own stack rather than assuming a one-size-fits-all gain. The discovery that content-free labels perform comparably to real labels also simplifies engineering workflows, removing the need for carefully curated classification taxonomies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02413v1)
