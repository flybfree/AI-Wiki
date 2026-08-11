---
title: Coupled Graph--Policy Distillation for Personalized Medication Safety in Older Adults with Multimorbidity
published: 2026-08-10T11:19:44Z
authors: Zihan Wang, Anglin Liu, Rongyi Wang, Dantong Li, Yi Lu, Siqing Yuan, Hongxia Xu, Zhongtian Long, Jintai Chen
url: http://arxiv.org/abs/2608.09443v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Coupled Graph--Policy Distillation for Personalized Medication Safety in Older Adults with Multimorbidity

## Abstract
Large language model (LLM) agents can support medication review between clinical visits, but safe choices for older adults with multimorbidity depend on conditions, medications, and geriatric risks that users may omit. We introduce ATLAS, a coupled graph--policy distillation framework for patient-adaptive medication safety. ATLAS structures guideline evidence as a medication-safety graph. Targeted questions update the patient state and distill relevant relations into a patient-specific medication conflict graph (PMCG). A risk-first multi-agent policy uses the PMCG to screen contraindications, assess cautions and monitoring needs, identify safer alternatives, and verify the final medication plan. We also introduce GeriMedBench, an interactive benchmark that tests safety-critical information acquisition and evidence-based decision revision. Across a European non-interactive multimorbidity benchmark, an Asian interactive multimorbidity benchmark, and an Asian non-interactive cross-guideline benchmark, ATLAS achieves the strongest complete-decision performance among the compared systems. On the European non-interactive multimorbidity benchmark, it exceeds the strongest proprietary LLM baseline by 53.73 points in Strict Success Rate and 14.63 points in overall safety reasoning score (OSRS), with no unsafe recommendations under the automated evaluator. A blinded clinician evaluation gives ATLAS higher mean ratings across all five criteria and flags potentially unsafe recommendations in one ATLAS case and two Gemini cases.

## Metadata
- **Published**: 2026-08-10T11:19:44Z
- **Authors**: Zihan Wang, Anglin Liu, Rongyi Wang, Dantong Li, Yi Lu, Siqing Yuan, Hongxia Xu, Zhongtian Long, Jintai Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09443v1)