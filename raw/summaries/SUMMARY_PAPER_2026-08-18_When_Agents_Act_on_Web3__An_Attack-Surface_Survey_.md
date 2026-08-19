---
title: When Agents Act on Web3: An Attack-Surface Survey of MCP, Skills, and Tool Calling
url: http://arxiv.org/abs/2608.17275v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_02-04-58Z_WhenAgentsActonWeb3_AnAttack_SurfaceSurveyofMCP_Sk.md
generated_at: 2026-08-18 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper surveys how AI agents that modify external state via MCP, skills, and tool calling interact with blockchain execution layers, showing that attacks become irreversible losses rather than recoverable failures. It introduces an attack-surface taxonomy and a risk-mapping matrix linking attack classes to amplified impacts, amplifiers, mitigations, and gaps.

## Key Takeaways
- The surge in state-modifying tools has increased the share of tool use from 27% to 65%, raising the exposure surface for attacks on public blockchains.  
- Four blockchain properties—irreversibility, signing authority, continuous autonomy, and sequence-level composition—transform generic agent security assumptions into irreversible loss scenarios.  
- Measured protections stop fewer than 30% of attacks, and model-level safety refuses fewer than 3%, indicating current defenses are insufficient.

## Context
AI agents moving from passive reading to active state modification challenge traditional software security models. Blockchain execution layers provide a unique environment where failures cannot be recovered, making the security landscape distinct and high‑risk.

## Implications
For practitioners, this paper highlights that existing AI safety tools must be rethought for immutable blockchain contexts. The identified gaps suggest a need for research into blockchain‑aware defenses that address irreversible loss risks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17275v1)
