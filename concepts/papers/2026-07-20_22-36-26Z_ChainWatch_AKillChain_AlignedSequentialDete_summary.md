# Summary: 2026-07-20_22-36-26Z_ChainWatch_AKillChain_AlignedSequentialDetectionFr.md
Saved: 2026-07-24 00:27
Source: 2026-07-20_22-36-26Z_ChainWatch_AKillChain_AlignedSequentialDetectionFr.md
Model: None

---

## Summary  
The paper introduces **ChainWatch**, a sequential detection framework that aligns with the six‑stage kill chain to identify multi‑step attacks in MCP‑based AI agent systems, thereby addressing evasion of per‑call security defenses. It models tool‑call sequences using a Hidden Markov Model (HMM) and triggers alerts when suspicious progression across multiple stages is observed.

## Key Contributions  
- [Finding 1] Proposes ChainWatch as a kill‑chain‑aligned framework for detecting sequential attacks on MCP‑enabled AI agents.  
- [Finding 2] Introduces an HMM to classify tool‑call sequences and detect abnormal progression across the six stages of the kill chain.  
- [Finding 3] Provides a structured threat model covering direct sequential attacks, indirect prompt‑injection chains, and hybrid multi‑stage attacks.

## Methodology  
The authors approached the problem by first mapping known attack vectors onto the kill chain, then designing an HMM that treats each stage as a hidden state with observable tool‑call features. They extracted 20 behavioral signals from interactions between agents and external tools, built detection rules for abnormal progression, and implemented them in a session‑level monitoring pipeline.

## Results  
Experiments on five representative attack scenarios show ChainWatch correctly identifies all attack chains that would be missed by per‑call defenses, achieving near‑perfect recall while maintaining low false‑positive rates. The framework demonstrates high sensitivity to multi‑step attacks across both direct sequential and indirect prompt‑injection cases.

## Significance  
This work matters because it bridges the gap between static tool‑invocation inspection and dynamic session analysis, enabling robust protection of MCP‑enabled AI agents against sophisticated, multi‑stage adversarial actions that exploit the strengths of individual defenses.

## Related Concepts  
- Model Context Protocol (MCP)  
- Kill chain model  
- Hidden Markov Model (HMM)  
- Sequential detection  
- Per‑call security mechanisms
