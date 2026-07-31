---
title: Same Facts, Different Diagnosis: Measuring and Mitigating Narrative Anchoring in Clinical Language Models
url: http://arxiv.org/abs/2607.27384v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-29_18-43-47Z_SameFacts_DifferentDiagnosis_MeasuringandMitigatin.md
generated_at: 2026-07-30 20:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates narrative anchoring in clinical language models, where identical medical facts expressed in different sociolinguistic registers produce divergent diagnostic outputs. It demonstrates a statistically significant gap across seven models and proposes NarrativeShield to reduce it near zero, achieving the lowest rate of severely unstable decisions.

## Key Takeaways
- The narrative anchoring gap ranges from 0.064 to 0.151, indicating a measurable divergence in diagnostic confidence despite identical facts.
- Chain-of-thought reasoning and debiasing instructions only partially mitigate the bias but often cause accuracy collapse.
- NarrativeShield reduces the gap to near zero with minimal accuracy loss and yields the lowest severely unstable decisions rate.

## Context
This work highlights that bias can arise from linguistic style rather than demographic cues, challenging the assumption that prompt content alone drives model behavior. It underscores the need for robust fact verification in diagnostic AI and suggests that sociolinguistic variation is a critical factor in clinical reasoning models.

## Implications
For clinicians and developers, this suggests that standard debiasing prompts are insufficient without underlying instruction-following capability. The findings push toward more systematic, pipeline-level solutions to prevent false diagnoses and improve trustworthiness of AI-assisted medical decision support.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27384v1)
