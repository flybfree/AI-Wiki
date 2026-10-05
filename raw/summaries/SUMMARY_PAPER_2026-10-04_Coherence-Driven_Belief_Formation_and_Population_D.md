---
title: Coherence-Driven Belief Formation and Population Dynamics of Contagion in LLM Agents
url: http://arxiv.org/abs/2610.02654v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_01-20-52Z_Coherence_DrivenBeliefFormationandPopulationDynami.md
generated_at: 2026-10-04 21:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper empirically measures how language model agents adopt beliefs from peers, revealing that belief adoption follows a sigmoid kernel characteristic of complex contagion rather than simple contagion. The authors demonstrate that the threshold for belief adoption is governed by three factors—claim plausibility, source reliability, and agent disposition—which collapse into a single effective dimension interpretable as the coherence of an incoming belief with the agent's prior beliefs. They further show that collective belief dynamics among AI agents exhibit hallmark features of complex contagion, including preferential spread on clustered networks, bifurcating cascade windows, and hysteretic consensus that is far harder to remove than to establish.

## Key Takeaways
- The belief adoption kernel in LLM agents is sigmoid, meaning agents require a critical mass of peer endorsements before adopting a claim, a signature of complex contagion rather than simple contagion. This threshold is sensitive to three distinct sources: the intrinsic plausibility of the claim, the perceived reliability of the source endorsing it, and the agent's own disposition or prior beliefs. Critically, these three dimensions are well approximated by a single effective dimension, which the authors frame as the coherence of the incoming belief with the agent's existing belief structure.
- At the population level, belief spread among AI agents is significantly more effective on clustered networks than on random networks, mirroring findings in human social contagion research. This clustering effect suggests that community structure and echo chambers play a decisive role in how beliefs propagate through multi-agent LLM systems.
- The system exhibits a bifurcating cascade window and self-sustaining hysteretic consensus, meaning that once a consensus is established among agents, it becomes far more resistant to removal than it was to establish. This hysteresis implies that belief states in multi-agent LLM systems can become locked in, creating path-dependent outcomes that are difficult to reverse.

## Context
Social contagion models have traditionally assumed individual-level belief adoption rules and then derived emergent population behavior from those assumptions. This paper inverts that approach by directly measuring belief adoption in LLM agents, providing empirical grounding for how multi-agent AI systems process and propagate information. As LLM-based agents are increasingly deployed in simulated social environments, policy modeling, and collaborative reasoning tasks, understanding their contagion dynamics becomes essential for predicting emergent group behavior and preventing unintended consensus lock-in.

## Implications
For practitioners building multi-agent LLM systems, the finding that consensus is hysteretic and far harder to remove than to establish raises serious concerns about echo chambers, misinformation lock-in, and the difficulty of correcting group-level errors in AI agent swarms. Industry applications involving agent-based simulations of markets, public opinion, or organizational decision-making must account for clustered network structures that amplify belief spread and for the coherence-driven threshold that determines whether agents will adopt or reject incoming claims. This work also suggests that designing interventions to shift agent beliefs requires targeting the coherence dimension directly rather than simply increasing the number of endorsing peers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02654v1)
