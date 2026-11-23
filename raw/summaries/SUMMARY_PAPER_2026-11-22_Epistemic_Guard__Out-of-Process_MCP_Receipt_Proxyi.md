---
title: Epistemic Guard: Out-of-Process MCP Receipt Proxying, Post-Turn Prose Supervision, and Provenance-Gated Memory for Tool-Using Autonomous Agents
url: http://arxiv.org/abs/2611.27095v1
type: paper-summary
date: 2026-11-22
source_paper: 2026-11-20_04-10-02Z_EpistemicGuard_Out_of_ProcessMCPReceiptProxying_Po.md
generated_at: 2026-11-22 21:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces epistemic-guard (v0.5.2), an open-source Python library and out-of-process stdio MCP receipt proxy designed to close three runtime verification gaps in language-model agents that use the Model Context Protocol: action fabrication, provenance collapse, and syndicated echo amplification. The system achieves 93.2% accuracy on frozen-benchmark traces at 17.9 ms warm median CPU latency, outperforming 12B-14B GPU-based LLM judges by 6.4-6.8 accuracy points while requiring zero GPU VRAM and only 279.48 MB of CPU-resident model weights.

## Key Takeaways
- The system addresses three distinct failure modes in MCP-using agents: post-tool prose narrating side effects that never executed (action fabrication), unverified model or web text contaminating durable memory alongside genuine tool outputs (provenance collapse), and mirrored web pages falsely satisfying multi-source corroboration requirements from a single origin (syndicated echo amplification). Existing MCP firewalls only inspect wire calls before execution, and LLM-judge guardrails demand multi-gigabyte VRAM without binding prose to cryptographic receipts.
- epistemic-guard employs a layered architecture: Ed25519 signing keys isolated out-of-process, RFC 6962 Merkle logs with AER-1 receipt translation for tamper detection, post-turn prose supervision on CPU using SHA-256-verified OpenVINO INT8 encoders (4 models totaling 279.48 MB, with only 82.67 MB on the supervision path), SQLite write gating across 7 provenance domains, and collapsing of verbatim or lightly edited wire-syndicated RAG mirrors.
- Conformance results demonstrate 100% rejection of tampered receipts across 200 Merkle leaves, 58/58 official AER-1 ingestion vectors passed, 50/50 reference-verified AER-1 exports, 100% verification of 40 fault-injected wire calls and 100 concurrent appends with zero key leaks, and 100% blocking of 100 unauthorized memory writes. On live mcp-proxy traces (N=60), the system catches 96.15% of hazards at 76.67% accuracy with a 38.24% false-positive rate, gaining 18.34 accuracy points over Stage-1-only detection (p=0.001) in 9.16 ms p50 latency.

## Context
As autonomous agents increasingly rely on tool-use protocols like MCP to interact with external systems, the trust boundary between executed tool outputs and model-generated narrative prose has become a critical security and reliability concern. Current defenses either operate at the wire-call level before execution or depend on large GPU-resident judge models that cannot cryptographically bind generated text to verified receipts. This paper positions itself at the intersection of cryptographic provenance verification, lightweight CPU-based inference supervision, and memory integrity for agentic systems, addressing a gap that existing MCP firewalls and LLM-judge guardrails leave open.

## Implications
For practitioners deploying tool-using agents in production, epistemic-guard offers a zero-VRAM, CPU-only verification layer that can be integrated as an out-of-process proxy without modifying agent architecture, making it feasible for edge deployments, cost-constrained environments, and compliance-sensitive applications where GPU judge models are impractical. The provenance-gated memory architecture and syndicated-mirror collapsing directly mitigate hallucination contamination in agent memory stores, which is increasingly relevant as agents accumulate long-lived context across sessions. The statistical significance of accuracy gains over GPU judges (p=0.0259, p=0.0095) at 4.26-4.5x lower latency suggests that structured cryptographic verification combined with small quantized encoders can outperform brute-force large-model judging for the specific task of prose-to-receipt binding.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.27095v1)
