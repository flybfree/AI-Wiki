---
title: FedSkillGit: Federated Skill Evolution via Version Control
url: http://arxiv.org/abs/2610.21348v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_06-29-57Z_FedSkillGit_FederatedSkillEvolutionviaVersionContr.md
generated_at: 2026-10-15 22:20
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
FedSkillGit introduces a federated skill evolution framework for large language model agents that replaces full-document skill updates with bounded patch-based commits, enabling multiple data owners to collaboratively improve reusable natural-language skills without pooling their raw private data. The framework incorporates a two-stage privacy filter, server-side deduplication, and client-side validation gating before any skill version is published, and experiments across three datasets and three language model families demonstrate up to 22% improvement over state-of-the-art baselines while approaching the performance of centralized evolution.

## Key Takeaways
- The naive federated approach of having each client evolve and upload its entire skill document suffers from three critical flaws: evolved documents can leak client-specific content distilled from private traces, repeatedly transmitting a nearly unchanged document wastes bandwidth on knowledge the population already shares, and a single client's contribution becomes unattributable within a merged document. FedSkillGit addresses all three by shifting to a commit-and-patch model where each client submits only a bounded set of patches over named rules alongside a local experience summary, both of which must pass a two-stage privacy filter before leaving the client.
- The server-side aggregation pipeline in FedSkillGit deduplicates submitted patches and local experience summaries across all participants, maintains a global experience document that is accessible only to the optimizer components, and merges surviving patches into a candidate skill version. This candidate is then distributed back to clients, who independently score it on their own validation sets and report results, and the new version is published only when aggregate reported scores demonstrate improvement over the current published version, creating a quality-gated version control mechanism.
- Empirical results on three distinct datasets and three language model families show that FedSkillGit outperforms existing federated skill evolution baselines by up to 22% and approaches the performance ceiling of centralized skill evolution, all without any client ever sharing its raw execution traces or private data with the server or other participants.

## Context
This work sits at the intersection of federated learning, LLM agent self-improvement, and version control systems, addressing a practical deployment constraint: organizations that deploy LLM agents across multiple data owners cannot share raw interaction traces due to privacy, regulatory, or competitive reasons, yet they benefit from collectively evolving the agents' reusable skill libraries. Prior federated approaches to skill evolution treated the skill document as an opaque blob to be averaged or merged, ignoring the structured, rule-based nature of skill documents and the privacy risks embedded in distilled experience. FedSkillGit reframes skill evolution as a software-engineering problem with commits, patches, and merge gates, borrowing directly from Git-style version control to make contributions attributable, auditable, and privacy-preserving.

## Implications
For practitioners deploying LLM agents in multi-tenant or cross-organizational settings, FedSkillGit provides a concrete protocol for collaborative agent improvement that satisfies data governance requirements without sacrificing performance, making it viable for healthcare, finance, and legal domains where raw traces cannot leave their originating institution. For the broader AI research community, the commit-and-patch paradigm suggests that structured, rule-level updates are a more natural unit of federated collaboration than whole-document averaging, potentially influencing future work on federated prompt optimization, federated tool-use learning, and privacy-preserving agent training pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21348v1)
