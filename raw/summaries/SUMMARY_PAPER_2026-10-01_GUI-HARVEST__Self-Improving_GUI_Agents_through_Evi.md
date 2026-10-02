---
title: GUI-HARVEST: Self-Improving GUI Agents through Evidence-Driven Harness Evolution
url: http://arxiv.org/abs/2610.00948v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-10-01_02-31-20Z_GUI_HARVEST_Self_ImprovingGUIAgentsthroughEvidence.md
generated_at: 2026-10-01 21:13
model: qwen3.6-35b-a3b
---

## Summary
GUI-HARVEST introduces an automatic harness optimizer that enables self-improving graphical user interface agents using frozen backbone models, addressing challenges in aligning model intent with visual outcomes, diagnosing execution variability, and identifying recurrent failure patterns. The method grounds diagnosis by linking outputs to before-and-after screenshots, treats repeated task runs as joint evidence units, and consolidates findings into reusable source-code edits validated through prediction checks. Experiments demonstrate consistent performance gains across diverse open and proprietary backbones on OSWorld-Verified, with significant improvements transferring to WindowsAgentArena without further optimization, outperforming existing harness optimization baselines.

## Key Takeaways
- GUI-HARVEST aligns model outputs and executed actions with before-and-after screenshots to ground diagnosis in observed action effects, ensuring findings are tied directly to specific interface transitions rather than relying solely on textual descriptions.
- To manage execution variability, the optimizer treats repeated runs of the same task as a joint evidence unit, utilizing within-task comparisons to isolate outcome-relevant behavioral differences that might otherwise be obscured by stochastic agent behavior.
- The system consolidates verified findings across multiple tasks into recurring failure patterns and maps them to bounded source-code edits, employing a rigorous validation loop where predicted behavioral effects are checked alongside task performance through repeated execution before finalizing harness updates.

## Context
As autonomous agents increasingly interact with complex software environments, the executable harness that mediates between the language model and the interface becomes a critical bottleneck for performance and reliability. Current approaches often focus on optimizing the model itself or lack robust mechanisms to adapt the runtime behavior of GUI agents without retraining, limiting their ability to generalize across diverse tasks and platforms.

## Imp

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.00948v1)
