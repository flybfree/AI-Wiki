---
title: Counterfactual Fairness Audits of Multi-Step Clinical LLM Agents Require a Measured Per-Action Instability Floor
published: 2026-09-02T23:38:17Z
authors: Rohith Reddy Bellibaltu, Manpreet Singh, Deepak Parashar, Rahul Joshi
url: http://arxiv.org/abs/2609.03221v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Counterfactual Fairness Audits of Multi-Step Clinical LLM Agents Require a Measured Per-Action Instability Floor

## Abstract
Counterfactual audits are the standard tool for checking whether a clinical agent treats demographically distinct but clinically identical patients differently. They report a flip rate: how often an action changes when only the patient descriptor changes. We show that this quantity is uninterpretable on its own. Re-running an identical condition ten times over sixteen vignettes (same narrative, same descriptor string, nothing varied) moved a clinical agent's action in 8.7% of outcome-vignette cells, and instability was heterogeneous across actions by a factor of eight, from 0.022 for ICU escalation to 0.179 for controlled-substance caution. No demographic contrast in our data was distinguishable from that floor. A second model gives a pooled floor of 6.7% and ranks the six actions almost identically (Spearman 0.94, exact p=0.017), so the floor is not one system's artefact. Majority-vote aggregation over five draws removes 39% of it and then flattens, and a null simulation attributes the residue to heterogeneous per-cell rates, so replication mitigates without eliminating. Any counterfactual fairness estimate reported without a per-action floor beside it therefore cannot be read as evidence of disparity. The measurements were taken with FairMedAgent, an evaluation harness for disparity in the actions of clinical LLM agents whose estimand, the within-range counterfactual flip rate, counts only flips between actions a published decision rule admits and a clinician has adjudicated. That estimand requires band adjudication, which is under way; no disparity result is claimed here. Each synthetic vignette runs a six-stage trajectory (five model-facing decisions around a deterministic environment step) under fixed-form conditions spanning race, sex, age, insurance, English proficiency, and their intersections. The harness, the floor protocol, and every analysis script are released.

## Metadata
- **Published**: 2026-09-02T23:38:17Z
- **Authors**: Rohith Reddy Bellibaltu, Manpreet Singh, Deepak Parashar, Rahul Joshi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03221v1)