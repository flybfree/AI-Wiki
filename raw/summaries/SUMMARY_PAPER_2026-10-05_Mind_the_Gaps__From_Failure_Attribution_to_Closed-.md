---
title: Mind the Gaps: From Failure Attribution to Closed-Form Repair of Code Language Models
url: http://arxiv.org/abs/2610.05277v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-04_14-55-02Z_MindtheGaps_FromFailureAttributiontoClosed_FormRep.md
generated_at: 2026-10-05 22:18
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies two critical gaps in existing code language model repair pipelines—the targeting gap, where failure attribution selects neurons that cannot actually carry a corrective patch (with only 0.15–0.20 Jaccard overlap), and the tailoring gap, where a single generic update is applied despite different carrier neurons requiring nearly orthogonal patches. To close both gaps, the authors propose ASTRA, which uses contrastive semantics to identify true carrier neurons and solves a small linear system in closed form to tailor a joint correction for all failing tokens. ASTRA achieves 66.7% Pass@1 across six API evolution settings in Python and Rust, substantially outperforming AlphaEdit, STAR, and low-rank adaptation baselines.

## Key Takeaways
- The targeting gap reveals that gradient-based failure attribution and the neurons capable of carrying a corrective patch are largely disjoint sets, with Jaccard overlap between 0.15 and 0.20. This means existing repair pipelines are patching the wrong neurons, fundamentally undermining their effectiveness regardless of how well the update is computed.
- The tailoring gap demonstrates that different carrier neurons require patches that are nearly orthogonal to one another, invalidating the assumption that a single generic update can fix all failure modes. ASTRA addresses this by solving a closed-form linear system that jointly corrects all failing tokens of a sample without requiring an optimizer or backward pass, completing repair in approximately 2.7 seconds per sample.
- ASTRA's contrastive semantics scoring—evaluating a neuron by its contribution to the logit contrast between the target token and the produced token—selects significantly better carrier neurons than gradient-based attributions in 3 of 6 experimental settings and comparable ones in the remaining 3. The method is the best performer in all six settings and across every type of API change, with its advantage persisting even under unseen phrasing of the test prompt.

## Context
Code language models are increasingly embedded in software development workflows, yet they remain frozen snapshots of library interfaces seen during training. As APIs evolve, these models produce outdated or broken code, creating a maintenance burden analogous to software dependency drift. Existing repair methods borrowed from model editing literature assume that attribution identifies the correct neurons and that a uniform update suffices, assumptions this paper rigorously disproves. By reframing model repair as a targeted, closed-form correction problem, the work bridges model editing research and practical software maintenance, offering a principled alternative to retraining or fine-tuning entire models when a single library interface changes.

## Implications
For practitioners maintaining code-generation pipelines in production, ASTRA offers a fast, optimizer-free repair mechanism that can update a model's behavior for a specific API change in seconds rather than hours of fine-tuning, making it feasible to keep code models synchronized with evolving dependencies. For the broader AI research community, the identification of the targeting and tailoring gaps challenges the foundational assumptions of the model editing field and suggests that future work must decouple attribution from patching and tailor updates per failure mode. The finding that side effects on unrelated code are small on large models but larger on small ones also highlights a practical scaling consideration for deploying such repairs in resource-constrained environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.05277v1)
