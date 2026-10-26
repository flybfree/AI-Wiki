---
title: Agentic AI Defense: Decode-Time Provenance Binding for MCP
published: 2026-10-22T22:27:13Z
authors: Eric Yocam, Varghese Vaidyan, Paris Kalathas, Patrick Tague, Bruce DeBruhl, Yong Wang
url: http://arxiv.org/abs/2610.31974v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic AI Defense: Decode-Time Provenance Binding for MCP

## Abstract
Agentic AI systems using the Model Context Protocol (MCP) are vulnerable to indirect prompt injection through untrusted tool outputs. We demonstrate cross-modal trust laundering, in which instructions concealed in an email-signature image using least-significant-bit (LSB), discrete cosine transform (DCT), or metadata steganography bypass text scanners and enter a multi-agent workflow when decoded by a tool. To counter this threat, we propose decode-time provenance binding, which combines HMAC-authenticated trust labels with an MCP-maintained provenance ledger and context-taint tracking. The mechanism labels decoded content as untrusted and blocks critical tool calls influenced by that content, even when a compromised agent substitutes a valid trusted label. We evaluate the approach using a real MCP testbed with three steganographic carriers and 24 adaptive payloads. The undefended pipeline exhibits 100% attack success, while keyword and regex defenses each permit 62.5% of attacks. Our mechanism blocks all attacks (0% success), including adversarial label substitution across mediated agent boundaries. A four-component ablation validates the roles of decode marking, cryptographic authentication, lineage tracking, and sink enforcement. An audited trusted-promotion mechanism increases legitimate-task completion from 67% to 100% without compromising protection. The approach provides carrier-independent containment within fully mediated MCP execution environments. Code and data are publicly available.

## Metadata
- **Published**: 2026-10-22T22:27:13Z
- **Authors**: Eric Yocam, Varghese Vaidyan, Paris Kalathas, Patrick Tague, Bruce DeBruhl, Yong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31974v1)