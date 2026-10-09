---
title: Distillation for Incrimination and Distillation for Capabilities
published: 2026-10-07T23:51:11Z
authors: Sebastian Prasanna, Jacqueline Tay, Alek Westover
url: http://arxiv.org/abs/2610.11012v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distillation for Incrimination and Distillation for Capabilities

## Abstract
Powerful misaligned AI models might recognize alignment evaluations and strategically behave well on them, rendering direct audits uninformative. However, distilling such a model into a weaker benign student places the teacher in a Distillation Double Bind: if misalignment transfers, the student may conceal it less effectively, revealing evidence about the teacher; if it does not, the student may learn useful capabilities while remaining benign. We introduce two distinct distillation approaches, one targeting each outcome. Distillation for Incrimination (DFI) aims to transfer misalignment but not the ability to conceal it. Distilling AuditBench's secret-keeping models into their underlying instruction-tuned model produces students that are significantly more likely than their teachers to admit their hidden behavior when asked, suggesting that knowledge of the behavior transferred more readily than the propensity to conceal it. Confession gains largely disappear when the student does not share the teacher's pretrained base, so DFI should target the teacher's own pre-RL checkpoint, which is weaker than the teacher but shares its base model. Distillation for Capabilities (DFC) aims to transfer capabilities but not misalignment. Among several techniques we evaluate, two are effective: inoculation prompting and training for more epochs on fewer unique examples. Both preserve the capability gains of standard distillation while substantially reducing the subliminal transfer of an animal preference, our proxy for misalignment. Together, these findings demonstrate two ways distillation can be used for AI safety: incriminating misaligned models, and extracting their capabilities without their misalignment.

## Metadata
- **Published**: 2026-10-07T23:51:11Z
- **Authors**: Sebastian Prasanna, Jacqueline Tay, Alek Westover
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11012v1)