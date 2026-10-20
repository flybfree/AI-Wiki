---
title: Who Speaks, Who Authorizes, Who Acts? Understanding Trust Boundaries in Multi-Agent LLMs
url: http://arxiv.org/abs/2610.24298v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-16_22-49-41Z_WhoSpeaks_WhoAuthorizes_WhoActs_UnderstandingTrust.md
generated_at: 2026-10-19 20:55
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the distinct trust boundaries in multi-agent LLM systems by separating message delivery (communication), signing authority (authorization), and tool-side enforcement (execution) into independent structures. Through controlled paired hidden-state studies across multiple models, the authors demonstrate that these boundaries do not align in practice: a false claim can pass a deterministic tool gate if it carries a policy-valid proof from a compromised-signer coalition, revealing a critical gap between proof validity and factual truth. The findings argue that delivered information, qualified authorization, model proposals, and committed actions must be evaluated as separate safety layers rather than conflated into a single trust pipeline.

## Key Takeaways
- No fixed-message routing contrast across four models met the prespecified large-effect criterion, but when relay agents rewrite messages, executed false-state action rates vary significantly by model and route configuration. This means the act of message rewriting by intermediary agents introduces model-dependent and configuration-dependent risk that static routing studies would miss entirely.
- Presenting source-identity cues to models did not uniformly increase protected-action selection across three tested models, undermining the assumption that transparency about message origin automatically improves safety behavior. On invalid-proof cases, Nemotron and Llama requested protected actions in 52.1% and 54.2% of trials respectively, yet a deterministic tool gate committed none of them, exposing a divergence between request-level and commitment-level safety readouts.
- A separate single-model authorization check confirmed that a false claim accompanied by a policy-valid compromised-signer proof can pass the tool gate, because the gate validates proof structure rather than factual truth. The "authority cut" concept identifies the smallest independently compromised signer coalition capable of constructing such a proof, providing a formal tool for auditing authorization vulnerabilities.

## Context
Multi-agent LLM architectures are increasingly deployed in enterprise workflows, autonomous planning systems, and tool-augmented agents where multiple model instances coordinate through message passing before invoking external tools. Prior safety research has largely treated agent pipelines as monolithic, assuming that if a message is delivered and a tool is gated, the system is safe. This paper challenges that assumption by formalizing communication, authorization, and execution as structurally independent trust boundaries, drawing on concepts from distributed systems security and formal verification. The work sits at the intersection of LLM safety evaluation, multi-agent coordination theory, and tool-use auditing, addressing a gap where existing benchmarks conflate model-level reasoning with system-level commitment.

## Implications
For practitioners deploying multi-agent LLM pipelines, the findings demand that safety evaluation be decomposed into at least four independent layers: what information is delivered, who is qualified to authorize it, what the model proposes, and what the tool actually commits. Industry teams relying on deterministic tool gates as a final safety net should recognize that such gates validate proof structure, not factual accuracy, meaning a compromised-signer coalition can produce structurally valid but factually false authorizations. Future benchmark design and compliance auditing frameworks should adopt the authority-cut methodology to identify minimal vulnerable signer sets, enabling targeted hardening of authorization boundaries rather than blanket trust in message routing or source attribution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24298v1)
