---
title: Proof-Carrying Contracts: Commitments AI Agents Cannot Break
url: http://arxiv.org/abs/2610.28484v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_16-30-34Z_Proof_CarryingContracts_CommitmentsAIAgentsCannotB.md
generated_at: 2026-10-20 21:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Proof-Carrying Contracts (PC2), a framework designed to make agreed-upon constraints enforceable during AI agent interactions without requiring mutual trust or inspection between parties. The core mechanism requires an agent to supply a machine-checkable proof demonstrating that a requested operation preserves all contractual constraints across every case permitted by its model, with an execution system called the Airlock verifying the proof before granting access. The authors prove that these constraints hold at every instant during execution, even against adversarial agents, and establish conditions under which formal guarantees translate into real-world safety.

## Key Takeaways
- PC2 shifts the burden of safety from designing a separate permission policy and proving every permitted decision is safe, to requiring the agent itself to supply reasoning that justifies its decisions while remaining free to adapt its strategy. This means parties specify the conditions to preserve, and the agent supplies the proof, creating a separation of concerns that avoids brittle policy engineering.
- The Airlock execution system acts as a gatekeeper: before any operation runs, the agent must present a machine-checkable proof that the operation preserves agreed constraints in every case allowed by its model. This provides a formal, verifiable enforcement mechanism rather than relying on textual instructions, policies, or agreements that an agent may ignore, misinterpret, or be redirected by.
- The framework provides formal guarantees that constraints hold at every instant during execution even for adversarial agents, and the authors identify precise conditions under which these formal guarantees imply safety in the real world. Reusable capability modules supply tools and guarantees from which contracts can be composed, enabling modular construction of enforceable agreements.

## Context
As AI agents increasingly act autonomously on behalf of humans and other agents—purchasing services, exchanging information, and delegating work—the question of how to make agreements binding without inspecting or trusting the other party's agent becomes central to building a functioning agent economy. Existing approaches rely on textual instructions, policies, or agreements that agents may violate due to mistakes, redirection by context, or divergent interests. PC2 addresses a fundamental gap in multi-agent systems research by providing a formal, proof-based enforcement layer that operates independently of the agent's internal reasoning or alignment, making it applicable regardless of the underlying model architecture.

## Implications
For practitioners building agent-to-agent marketplaces, delegation systems, or autonomous service exchanges, PC2 offers a concrete foundation for constructing enforceable agreements that protect both delegating parties and those carrying out work, reducing the need for costly oversight or trust assumptions. For the broader field, the separation between specifying constraints and supplying proofs suggests a modular approach to safety engineering where capability modules can be composed into contracts, potentially enabling standardized, reusable guarantee components across different agent systems and domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28484v1)
