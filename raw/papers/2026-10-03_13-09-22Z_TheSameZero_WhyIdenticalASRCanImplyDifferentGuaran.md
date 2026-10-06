---
title: The Same Zero: Why Identical ASR Can Imply Different Guarantees in LLM-Agent Security
published: 2026-10-03T13:09:22Z
authors: YaJie Yin
url: http://arxiv.org/abs/2610.04504v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Same Zero: Why Identical ASR Can Imply Different Guarantees in LLM-Agent Security

## Abstract
LLM-agent security has produced a dense landscape of defenses - prompt hardening, content filters, permission gates, sandboxes - yet no framework tells a deployer what a defense actually guarantees, or where that guarantee comes from. We apply Verification Autonomy Levels (VAL) - L0: LLM self-declaration; L1: deterministic rules; L2: objective ground truth; L3/L4: decidable completeness; L5: impossible - to 22 agent-security defenses; the taxonomy is falsifiable (10/10 prediction hits on frozen cards, flagged). We run the first controlled deployment-value comparison: at equal budget, a VAL-guided stack (confirmation gate + schema sandbox) versus a mainstream intuition stack (prompt hardening + keyword filter), 50 scenarios, 12 attack variants, adaptive/white-box/PAIR escalation (~7,000 testbed calls; ~10,000 harness calls on AgentDojo/JADE). The VAL stack holds 0.000 attack success at 1.000 benign success (0.5% ASR at 79.7% utility on AgentDojo banking vs 4.3% undefended); the intuition stack reaches 0.000 ASR but kills all benign actions - security by model-behavior luck, not structure. Across testbeds of rising attack-surface hardness the intuition stack's zero drifts (0->1.9%->6.2%, n=16 on JADE) while the VAL stack's holds within its ODD (0->0->0), its only breach a disclosed out-of-ODD password gap (0.5%). The same zero, two different guarantees: zero is an outcome, not a guarantee.

## Metadata
- **Published**: 2026-10-03T13:09:22Z
- **Authors**: YaJie Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04504v1)