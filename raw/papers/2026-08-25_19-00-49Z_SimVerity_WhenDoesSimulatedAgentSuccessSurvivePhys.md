---
title: SimVerity: When Does Simulated Agent Success Survive Physical Deployment?
published: 2026-08-25T19:00:49Z
authors: Zhonghao Zhan, Yefan Zhang, Krinos Li, Hamed Haddadi
url: http://arxiv.org/abs/2608.25067v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SimVerity: When Does Simulated Agent Success Survive Physical Deployment?

## Abstract
Simulated evaluation is widely used to benchmark AI agents, yet how much evidence a simulated pass provides about physical deployment has not been systematically quantified. We present SimVerity, a verdict-transfer assurance framework: it replays matched scenarios on target smart home deployments and cross-validates agent execution against independently qualified physical witnesses. Our evaluation highlights that deployment success is a real-world process, not a static property in simulation: completion, reported state, observable effect, and settled outcome diverged within the same execution. Although an advanced simulator cleared all 240 light trials, a camera caught 42 sub-second failures invisible to settled-state checks. False clearance was predictable: a risk profile learned from measured trials and locked before evaluation predicted failures on a path it never physically measured, beating a property-blind baseline in all eleven held-out sessions across two cohorts. Agent auditability was also measurable: switching one agent loop's model-client/serving configuration raised its scenario-matching share from 52-88% to 100%. Finally, a second qualified simulator added no independent cross-check: it never disagreed on any overlapping case, and only physical measurement exposed their shared blind spots. SimVerity turns verdict transfer into an explicit decision: clear, abstain, or escalate before deployment.

## Metadata
- **Published**: 2026-08-25T19:00:49Z
- **Authors**: Zhonghao Zhan, Yefan Zhang, Krinos Li, Hamed Haddadi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25067v1)