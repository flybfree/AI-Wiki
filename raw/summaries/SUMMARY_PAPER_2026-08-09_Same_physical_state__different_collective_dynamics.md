---
title: Same physical state, different collective dynamics: state encodings select synchronization outcomes in language-model agents
url: http://arxiv.org/abs/2608.06968v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_08-44-20Z_Samephysicalstate_differentcollectivedynamics_stat.md
generated_at: 2026-08-09 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how different ways of encoding the same physical state influence collective behavior in language-model agents. By comparing low-order circular moment encodings with histogram encodings while keeping the underlying system unchanged, the authors show that the choice of encoding determines whether synchronization occurs and even its direction.

## Key Takeaways
- In GPT, using circular moments led to full population synchronization across all six seeds, whereas histogram encodings produced no synchronization.  
- The same experiment with Claude reversed the effect: moment encoding caused desynchronization while histogram encoding fostered alignment.  
- Replaying identical fields amplified differences in advance/stay/retard probabilities beyond typical within‑encoding variation, indicating that encodings shape model‑dependent interaction laws.

## Context
Language models are increasingly used as agents to interact with physical systems, but the way their internal state representations map to external observations remains opaque. This study reveals that such mappings are not neutral interfaces; they actively steer dynamics, highlighting a gap between abstract encoding choices and real‑world outcomes.

## Implications
For developers, selecting an appropriate state encoding can be crucial for achieving desired collective behavior in agent‑based simulations. Practitioners should treat encodings as part of the interaction law rather than interchangeable tools, guiding design decisions that align with intended system performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06968v1)
