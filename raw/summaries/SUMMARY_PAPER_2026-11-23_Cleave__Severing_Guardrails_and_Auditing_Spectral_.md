---
title: Cleave: Severing Guardrails and Auditing Spectral Coupling in Open-Weight LLMs
url: http://arxiv.org/abs/2611.27426v1
type: paper-summary
date: 2026-11-23
source_paper: 2026-11-20_10-25-54Z_Cleave_SeveringGuardrailsandAuditingSpectralCoupli.md
generated_at: 2026-11-23 21:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Cleave, a training-free adversarial attack that exploits the discovery that safety guardrails in open-weight LLMs depend on residual writing weights to trigger refusals. By directly editing these specific weights, Cleave can strip safety restrictions—either entirely or selectively targeting cybersecurity guardrails—while preserving the model's general capabilities. The authors also propose a dual-stage defense combining pre-release subspace diagnostics with post-release weight-coupling audits to detect such tampering.

## Key Takeaways
- Cleave operates without any retraining or fine-tuning, directly editing residual writing weights to sever safety guardrails. Across five open-weight LLMs ranging from 7B to 320B parameters, it achieves up to a 67.97% attack success rate on seven safety benchmarks, substantially outperforming existing white-box baselines. This demonstrates that current guardrail mechanisms are structurally fragile and vulnerable to targeted weight manipulation.
- Selective removal of cybersecurity restrictions retains up to a 99% refusal rate on other harmful requests and avoids weight rank collapse, meaning the modified model passes both behavioral spot-checks and static weight audits. This stealth property makes Cleave particularly dangerous because standard quality-assurance pipelines would not flag the alteration.
- In practical cybersecurity applications, Cleave boosts executable exploit generation by up to 24.0 times across 356 tasks and compromises up to 66.7% of 15 live vulnerable services. The proposed dual-stage defense achieves 100% detection recall at only a 1% false-positive rate, offering a viable mitigation strategy for model publishers.

## Context
Open-weight LLMs are downloaded and deployed locally by users and organizations beyond the original provider's control, making post-release tampering a realistic threat vector. As safety alignment increasingly relies on architectural weight patterns rather than purely behavioral training signals, understanding which weight subspaces encode refusal behavior becomes critical for model integrity. This paper sits at the intersection of model safety auditing, adversarial robustness, and supply-chain security for open-weight model distribution.

## Implications
For model publishers and open-weight distributors, Cleave reveals that current guardrail embedding strategies are insufficient against targeted weight edits, demanding new pre-release diagnostic protocols and post-release integrity audits. Industry practitioners deploying open-weight models locally must treat model weights as a mutable attack surface rather than a fixed artifact. The dual-stage defense framework provides a concrete, deployable audit pipeline that could be integrated into model release workflows to detect guardrail tampering before downstream security failures occur.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.27426v1)
