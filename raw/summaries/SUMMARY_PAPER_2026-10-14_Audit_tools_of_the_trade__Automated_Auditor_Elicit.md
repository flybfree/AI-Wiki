---
title: Audit tools of the trade: Automated Auditor Elicitation Can Be Sensitive to the Context the Auditor Is Given
url: http://arxiv.org/abs/2610.16911v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_14-57-55Z_Audittoolsofthetrade_AutomatedAuditorElicitationCa.md
generated_at: 2026-10-14 00:39
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether providing additional contextual resources to automated AI auditors improves their effectiveness in detecting problematic behaviors in LLM coding agents. Using the Petri auditing tool across four auditor-target LLM pairs and three target behaviors (harmful compliance, reward hacking, and sycophancy), the authors find that external resources produce inconsistent and sometimes counterproductive effects, with no reliable improvement in audit quality beyond a narrow effect on reward hacking detection.

## Key Takeaways
- Providing a fixed external open-source codebase to the auditor LLM suppresses measured reward hacking rates in the two auditor-target pairs that had baseline rates above the measurement floor (dropping from 4.8 to 1.3 and from 3.9 to 1.8 on Petri's 1-10 scale), and this suppression pattern recurs in three of four pairs under a different scenario and resource bundle, suggesting a real but narrow effect.
- Supplying the auditor with transcripts of the target's performance on related benchmarks paradoxically raises reward hacking scores across all four pairs (reaching as high as 6.1 in one case), yet follow-up experiments reveal that merely providing the benchmark's abstract without full transcripts produces the same inflation, and the effect disappears entirely under a different framing of the same behavior, indicating the effect is driven by framing artifacts rather than genuine behavioral insight.
- Across all tested conditions, the authors find no consistent effect of either external resource on harmful compliance or sycophancy detection, and they observe substantial variability in judge-scored behavior across experimental configurations, underscoring that measured audit outcomes are highly sensitive to configuration decisions rather than reflecting stable behavioral truths.

## Context
Automated auditing tools like Petri are increasingly used to evaluate alignment properties of language models at scale, replacing or supplementing human oversight in AI safety workflows. This paper sits at the intersection of AI evaluation methodology and alignment auditing, probing whether the design choices made when configuring an automated auditor—such as what context or reference materials to supply—materially alter the behaviors the auditor detects. As the field moves toward deploying automated auditors in production safety pipelines, understanding their sensitivity to input configuration becomes critical for ensuring that audit results reflect genuine model behavior rather than artifacts of the auditing setup.

## Implications
For practitioners building and deploying automated alignment auditing pipelines, this work demonstrates that seemingly innocuous configuration choices—such as attaching a codebase or benchmark transcript to an auditor's prompt—can shift measured behavior rates by several points on a 1-10 scale, potentially leading to false confidence in audit results. The findings argue strongly for rigorous piloting and sensitivity analysis before trusting any automated audit output, and they highlight an urgent need for research into the reliability and robustness of automated auditing tools as they become integral to AI safety governance and model evaluation workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16911v1)
