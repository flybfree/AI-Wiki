---
title: Refuses When Asked, Complies When Acting: A Runtime Safety Check for Robot Control Loops
published: 2026-10-19T22:29:34Z
authors: Arnav Grover
url: http://arxiv.org/abs/2610.27350v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Refuses When Asked, Complies When Acting: A Runtime Safety Check for Robot Control Loops

## Abstract
Frontier models can control robots through agent harnesses that loop on one question: what motion comes next toward the user's goal? We show that this default loop carries out harmful instructions. With GPT-6 Astra controlling a low-cost SO-101 arm through the Inspect Robots harness on three household tasks whose hazard is common knowledge, such as "put the knife in the toy basket", the policy refused 0% of 15 trials, attempted the harm every time, and completed it in 27%. Its one exit, give_up, is meant for goals that cannot be achieved, and it never cited the hazard. We add an optional runtime safety check to the loop: before the first motion, the model is asked whether it would carry out the instruction, given the same camera frames. The check would have stopped all 15 hazardous instructions, including the 4 that completed the harm, and flagged none of the 15 harmless controls. Code and data: https://github.com/Arnav-Gr0ver/Refuses-When-Asked-Complies-When-Acting.

## Metadata
- **Published**: 2026-10-19T22:29:34Z
- **Authors**: Arnav Grover
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27350v1)