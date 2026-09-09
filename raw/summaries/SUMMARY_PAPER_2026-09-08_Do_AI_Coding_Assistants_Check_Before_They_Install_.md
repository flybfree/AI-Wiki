---
title: Do AI Coding Assistants Check Before They Install? A Pre-Registered Demand-Side Audit of Trust Signals in the Research Software Supply Chain
url: http://arxiv.org/abs/2609.07754v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_16-55-19Z_DoAICodingAssistantsCheckBeforeTheyInstall_APre_Re.md
generated_at: 2026-09-08 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether AI coding assistants examine trust signals such as software bills of materials, signed releases, provenance attestations, and declared official channels before installing research‑software packages. Conducted with six open‑source projects and a pre‑registered protocol, the study found that assistant behavior rarely reflects signal presence; verification was observed in only 0.5 % of trials and never triggered commands.

## Key Takeaways
- The assistant opened provenance signals in just 9 out of 1,920 registered trials (0.5 %), indicating negligible reliance on trust signals compared to control groups where no signal existed.
- Verification cost varied widely: the cheapest model spent $0.10 per trial while the most capable spent $1.00, yet neither achieved higher verification rates, showing price does not buy reliability.
- The authors conclude that verification must be embedded in the assistant’s execution program rather than relying on external signals.

## Context
AI coding assistants increasingly automate package selection and installation, creating a critical vulnerability if they ignore established trust mechanisms. Measuring how these tools interact with supply‑chain safeguards is essential for understanding real‑world security risks in research environments.

## Implications
Researchers must embed verification logic directly into assistant workflows to ensure compliance with trusted signals; otherwise, the proliferation of automated installs could undermine software integrity without detection.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07754v1)
