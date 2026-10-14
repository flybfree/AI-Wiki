---
title: PrivacyGuard: Source-Linked Sanitization and Locally Resolvable PII References for Cloud GUI Agents
url: http://arxiv.org/abs/2610.16778v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_13-34-52Z_PrivacyGuard_Source_LinkedSanitizationandLocallyRe.md
generated_at: 2026-10-14 01:15
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
PrivacyGuard introduces a two-component framework—Source-Linked Sanitization (SAN) and a Structured Reference Lifecycle (REF)—designed to prevent personally identifiable information from leaking when cloud GUI agents transmit instructions and screenshots to remote planners. The system reconstructs fragmented or overlapping PII evidence, rewrites complete source extents, and links changed appearances to session entities so that references remain locally resolvable without returning raw values to the upload path. Across multiple benchmarks and four reader-language combinations, PrivacyGuard reduces audited source-value leakage by 33.55% to 82.60% relative to the closest prior full-pipeline system while simultaneously improving task completion rates.

## Key Takeaways
- Source-Linked Sanitization (SAN) addresses a critical gap in existing placeholder defenses: prior systems mask detected spans and reuse exact strings, but fragmented or altered forms of PII can still leak through or break entity continuity across conversational turns. SAN reconstructs fragmented or overlapping evidence and rewrites the complete source extent, ensuring that partial or rephrased PII is caught and sanitized at the source level rather than relying on exact string matching.
- The Structured Reference Lifecycle (REF) raises strict cross-form continuity from 0.04 under exact-value reuse to 0.81, meaning that when a user's name or identifier appears in a different form across turns, the system correctly links it to the same session entity. This enables locally resolvable references so that downstream task execution can proceed without transmitting raw PII values back to the remote planner, preserving both privacy and functional continuity.
- On practical Android task benchmarks, PrivacyGuard increases verified completion in reference-required tasks from 8/30 and 7/30 to 17/30 and 20/30, and achieves the highest or tied-highest task-success point estimate among all protection pipelines on AndroidLab for all four planners. On the PrivScreen benchmark, it reduces fixed-reader field exposure by 62.72% to 62.84%, demonstrating that privacy protection and task performance are not mutually exclusive.

## Context
Cloud GUI agents—systems that interpret screenshots and user instructions to automate tasks on remote devices—have become a prominent area of AI research, with benchmarks like AndroidLab driving evaluation of planner capabilities. However, the very mechanism that makes these agents useful, namely sending rich visual and textual context to remote planners, creates a persistent privacy vulnerability. Existing defenses rely on simple placeholder masking and exact-string reuse, which fail when PII appears in fragmented, overlapping, or rephrased forms across multi-turn interactions. PrivacyGuard represents a shift from naive masking toward a structured, source-aware sanitization pipeline that treats PII as a lifecycle problem rather than a one-time detection problem.

## Implications
For practitioners deploying cloud-based GUI automation in enterprise or consumer settings, PrivacyGuard demonstrates that strong privacy guarantees can be achieved without sacrificing task success, which is essential for compliance with regulations such as GDPR and for building user trust in AI agents that handle sensitive data. The structured reference lifecycle model offers a reusable architectural pattern for any system that must maintain entity continuity across turns while preventing raw PII from traversing network boundaries, making it relevant beyond GUI agents to chatbots, document-processing pipelines, and multi-modal assistants. The benchmark results across four reader-language combinations and multiple planners suggest the approach generalizes across linguistic and model configurations, providing a practical template for privacy-aware agent design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16778v1)
