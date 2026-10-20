---
title: Formal Raising: Embedding Verifiable Ethical Properties into the Development of AI
url: http://arxiv.org/abs/2610.25501v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-18_19-41-46Z_FormalRaising_EmbeddingVerifiableEthicalProperties.md
generated_at: 2026-10-20 00:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes Formal Raising (FR), a framework that embeds selected moral values as explicit, machine-checkable properties directly into the development, evaluation, and action-selection processes of AI systems, rather than treating ethics as a post-hoc alignment step. The authors present a C-based reasoning framework in which candidate actions are evaluated against prioritized ethical properties, with conflicts resolved through a defined priority order and strict rules treated as non-defeasible constraints. The work draws on Alan Turing's "child machine" concept and recent "model raising" literature to argue that moral values should accompany capability acquisition from the beginning of an AI system's development.

## Key Takeaways
- Formal Raising treats moral values as explicit, machine-checkable properties that participate in the full lifecycle of AI development, evaluation, and action selection, rather than being bolted on after a model is already trained. This shifts the paradigm from post-hoc alignment to developmental embedding, meaning ethical constraints shape the system as it grows in capability, not after the fact.
- The C-based reasoning framework evaluates candidate actions against prioritized ethical properties, resolving conflicts according to a given order. Strict rules are explicitly non-defeasible, meaning they cannot be overridden by competing considerations, and underdetermination—cases where no clear ethical resolution exists—is reported explicitly rather than silently resolved. Exceptions are not hard-coded as special cases but emerge organically from the comparison of alternatives, reducing the risk of brittle rule-based systems.
- The authors outline a property layer inspired by Property Specification Language (PSL), a formal specification language used in hardware verification, adapted here for state and temporal ethical requirements. This suggests a path toward formally verifiable ethical behavior in AI systems, with concrete examples covering conflicts involving life, truthfulness, harm, privacy, autonomy, and strict rules.

## Context
The broader AI landscape has increasingly grappled with alignment as a reactive, post-training correction process, where models are first trained for capability and then nudged toward desirable behavior through techniques like RLHF or constitutional AI. Formal Raising challenges this sequencing by reviving Turing's developmental vision and the recent "model raising" literature, which argues that values and capabilities should co-develop. This positions the paper within a growing movement that seeks to make AI ethics not an afterthought but a structural component of system architecture, bridging formal methods from software verification with the practical demands of LLM safety and governance.

## Implications
For AI practitioners and safety researchers, Formal Raising offers a concrete, implementable path toward verifiable ethical behavior by leveraging formal specification techniques already proven in hardware and software verification, potentially enabling auditable and testable ethical guarantees rather than relying on opaque behavioral evaluations. For industry and regulatory contexts, the emphasis on explicit priority orders, non-defeasible strict rules, and explicit reporting of underdetermination provides a structured mechanism for encoding institutional or legal ethical constraints into AI decision-making pipelines, which could support compliance frameworks and reduce the ambiguity that currently complicates AI governance. The approach also signals a shift in how AI development teams should think about the integration of ethics: not as a separate alignment phase but as a co-developing property layer woven into the system's reasoning architecture from the earliest stages of training and deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25501v1)
