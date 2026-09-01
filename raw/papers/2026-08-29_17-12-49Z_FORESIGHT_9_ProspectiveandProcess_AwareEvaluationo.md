---
title: FORESIGHT-9: Prospective and Process-Aware Evaluation of Adaptive Trading Agents
published: 2026-08-29T17:12:49Z
authors: Xiangxin Luo, Chengtian Hong, Haohua Li, Yongyi Xie
url: http://arxiv.org/abs/2608.29372v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FORESIGHT-9: Prospective and Process-Aware Evaluation of Adaptive Trading Agents

## Abstract
Retrospective backtests provide a limited test of adaptive trading agents: they cannot rule out historical contamination, expose sensitivity to a single realized market path, or reveal internal degeneration during long-horizon adaptation. We introduce FORESIGHT-9, a prospective and process-aware benchmark built from nine auditable counterfactual stress worldlines branching from a common July 2026 information boundary. Each worldline specifies staged macro-financial events and joint multi-asset anchors; a deterministic generator realizes the trajectories, while observations are disclosed according to in-world time. A common contract standardizes observations and execution while preserving each agent's native adaptation loop. We evaluate two adaptive trading-agent frameworks with two foundation-model backbones across 36 long-horizon runs. Agent rankings vary substantially across worldlines and backbones, and a fixed equal-weight policy outperforms 31 of 36 runs. Process telemetry exposes failures that terminal returns conceal: in one high-return run, the live factor library collapsed while executed holdings converged to the equal-weight fallback, even though decision records continued to report an active factor ensemble. FORESIGHT-9 therefore evaluates not only portfolio outcomes, but whether adaptive agent state and execution remain coherent across alternative futures. We release the worldlines, trajectories, audit traces, and regeneration scripts.

## Metadata
- **Published**: 2026-08-29T17:12:49Z
- **Authors**: Xiangxin Luo, Chengtian Hong, Haohua Li, Yongyi Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29372v1)