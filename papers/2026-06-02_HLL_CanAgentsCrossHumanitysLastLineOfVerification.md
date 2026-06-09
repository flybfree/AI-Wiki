---
title: "HLL: Can Agents Cross Humanity's Last Line of Verification?"
arxiv: 2606.02449
date: 2026-06-01
authors: Song, Xinhao; Su, Su; Song, Sirui; Wu, Hongliang; Shen, Wen; Wei, Zhihua; Liu, Gongshen; Zhang, Linfeng; Liu, Dongrui
subjects: [cs.AI, cs.CL, cs.CV, cs.LG, cs.MM]
pages: 27
figures: 14
code: https://github.com/XinhaoS0101/HLL
tags: [CAPTCHA, agent-evaluation, multimodal-agents, human-substitution, GUI-agents, benchmark]
---

# HLL: Can Agents Cross Humanity's Last Line of Verification?

## Summary

This paper introduces **Humanity's Last Line of Verification (HLL)**, a controlled benchmark that uses interactive CAPTCHA verification to evaluate whether multimodal agents can truly substitute for humans in workflows that services deliberately protect against automation.

## Key Points

- **CAPTCHA as a human-verification boundary**: CAPTCHAs are not merely visual puzzles — they represent a deliberate barrier placed before account creation, content access, form submission, and other protected actions.
- **HLL benchmark**: Uses interactive CAPTCHA verification to test whether agents can cross this boundary through grounded, human-like interaction rather than recognition alone.
- **Controlled realism stressors**: HLL exposes agents to cluttered webpages, harder task variants, and trace-conditioned validation of the solving process.
- **Evaluation**: Tests eight frontier multimodal agents in a closed-loop GUI environment.
- **Findings**: Current agents remain brittle at this human-substitution boundary — performance varies sharply across verification types, degrades under realistic interface conditions, and drops further when correct answers must be supported by valid action traces.
- **Gaps exposed**: Localization, action calibration, state tracking, and process consistency.

## Why It Matters

HLL provides a concrete testbed for measuring how close multimodal agents are to acting as human substitutes in protected real-world workflows. If agents can consistently cross CAPTCHA verification with valid action traces, it signals a significant step toward fully autonomous agent deployment.

## Links

- **arXiv**: https://arxiv.org/abs/2606.02449
- **Code**: https://github.com/XinhaoS0101/HLL
