---
title: Governing Enterprise AI Traffic at Scale: Design and Operation of a Policy-Driven, Multi-Vendor LLM Gateway on Envoy
url: http://arxiv.org/abs/2610.35509v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-26_14-33-48Z_GoverningEnterpriseAITrafficatScale_DesignandOpera.md
generated_at: 2026-10-26 23:11
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper describes the design and production operation of the Cosmos LLM Gateway at PayPal, a governed entry point for enterprise LLM traffic built on the Envoy proxy. The gateway addresses the operational challenges of consuming multiple LLM vendors simultaneously—credential sprawl, format lock-in, unbounded spend, and inconsistent governance—by splitting control-plane decisions into an out-of-process external-processing service and data-plane operations into a Rust WebAssembly filter running in-proxy. As of September 2026, the system serves over 12,000 developers, handles approximately 200 billion tokens per day across more than 100 models, and achieves 99.999% availability with a median overhead of only 4 ms on the core request path.

## Key Takeaways
- The architecture deliberately splits work by latency profile: I/O-bound control decisions such as authentication, credential brokering, policy evaluation, and budget checks run in an out-of-process external-processing service, while wire-format translation, token metering, and prompt-cache shaping run in-proxy as a Rust WebAssembly filter. This design ensures that streamed response body chunks never wait on an out-of-process call by default, preserving low-latency streaming for end users.
- Governance is implemented as declarative policy evaluated by Open Policy Agent (OPA), managed through a control plane that supports role-scoped authoring, approvals, pilots, shadow-mode rollout, usage notifications, and versioned policy bundles. Models, providers, and prices are treated as validated data rather than code, reducing the blast radius of configuration errors and enabling safe, auditable changes.
- Spend scopes are implemented as views over per-model usage counters, meaning a newly defined budget automatically applies to spend already recorded within its time window without requiring data migration. Additionally, an optional data-loss-prevention layer can block, redact, or pseudonymize detected sensitive content before it reaches any provider, adding a compliance safeguard for regulated workloads.

## Context
As enterprises increasingly adopt multi-vendor LLM strategies to avoid lock-in and optimize cost and capability, the operational complexity of managing heterogeneous APIs, credentials, streaming protocols, and pricing models has become a critical infrastructure challenge. This paper contributes a production-grade reference architecture showing how a policy-driven gateway can unify governance across dozens of providers while maintaining near-native latency, filling a gap in the literature where most LLM infrastructure discussions remain at the level of single-vendor SDKs or academic benchmarks rather than large-scale operational systems.

## Implications
For practitioners and platform teams, the paper demonstrates that enterprise-scale LLM governance does not require sacrificing performance: a well-architected proxy can add only single-digit milliseconds of overhead while enforcing budgets, policies, and data-loss-prevention rules across hundreds of models. The use of declarative policy bundles, shadow-mode rollouts, and data-as-configuration patterns offers a replicable template for organizations seeking to centralize LLM access control without building bespoke integrations for each vendor, potentially accelerating the adoption of governed AI infrastructure across regulated industries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35509v1)
