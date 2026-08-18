---
title: LLMs Can Predict Failure Risk, But Struggle to Predict Which Collaboration Protocol Pays Off: Cost-Aware Protocol Routing Across Reasoning Tasks
published: 2026-08-14T22:35:37Z
authors: Chih-Hsuan Yang, Jingyan Jiang, Cheng-Hau Yang, Vikram Vasudevan, Huihuo Zheng, Venkatram Vishwanath, Rajeev Thakur
url: http://arxiv.org/abs/2608.14927v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLMs Can Predict Failure Risk, But Struggle to Predict Which Collaboration Protocol Pays Off: Cost-Aware Protocol Routing Across Reasoning Tasks

## Abstract
Multi-agent large language model (LLM) systems can improve reasoning by spending more computation, but deployment requires deciding when extra collaboration is worth its cost. We isolate this decision by running every problem under four protocols while holding the solver fixed within each setting: direct solving (Baseline), iterative self-correction (Single), planner-executor-reviewer collaboration (PER), and multi-agent deliberation (Broadcast). The primary benchmark comprises 4,181 competition-level math problems; paired robustness checks cover four benchmarks spanning competition math, biology, and broader science with two solver families. Across fixed policies, trained routers, and frozen LLM routers, conservative policies under-escalate, whereas higher-solve frozen routers often over-escalate. A post-answer, pre-collaboration gpt-oss-120b probe ranks Baseline failures with 0.8847 AUROC (4,151 parseable cases; 95% CI [0.8732, 0.8955]). The same score remains informative for predicting whether any collaboration helps (0.7683 AUPRC), but is much weaker for identifying PER- or Broadcast-specific value (0.1674 and 0.1041 AUPRC). Separately, the pre-answer self-confidence gate reaches 78.0% solve at 45K tokens, compared with 73.8% at 71.3K for a frozen gpt-oss-120b router and 92.4% for a retrospective fixed-order oracle. Across 10 paired model-condition settings, the oracle adds 23.2-58.3 points of retrospective coverage over Baseline, but protocol profiles vary by task. In the six settings with held-out router evaluations, oracle gaps remain 18.5-28.9 points. Confidence can therefore support initial escalation, while protocol-specific cost-aware routing remains unresolved.

## Metadata
- **Published**: 2026-08-14T22:35:37Z
- **Authors**: Chih-Hsuan Yang, Jingyan Jiang, Cheng-Hau Yang, Vikram Vasudevan, Huihuo Zheng, Venkatram Vishwanath, Rajeev Thakur
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14927v1)