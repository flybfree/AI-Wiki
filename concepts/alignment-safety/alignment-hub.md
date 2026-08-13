---
title: "Alignment Hub"
type: concept
tags: [alignment, reward-modeling, behavior]
---

# Alignment Hub

**Source**: [AI Research Wiki](https://github.com/flybfree/AI-Wiki/wiki)

## Summary

Alignment, preference optimization, reward modeling, honesty, interpretability, and behavior shaping during training and deployment.

## Semantic links
- [Training and Optimization Hub](../training-optimization/training-optimization-hub.md)
- [Reasoning and Inference Hub](../reasoning/reasoning-hub.md)
- [AI Safety Hub](../ai-safety/ai-safety-hub.md)

## Related Concepts

- [AI Safety Hub](../ai-safety/ai-safety-hub.md)
- [Evaluation Benchmarks Hub](../evaluation-benchmarks/evaluation-benchmarks-hub.md)

## Alignment and value foundations

- [LLM Alignment](../2026-06-11_llm-alignment.md) — overview of RLHF, DPO, Constitutional AI, interpretability, scalable oversight, sycophancy, and emergent misalignment.
- [Toward a Theory of Value in AI Alignment](../papers/2026-08-10_23-57-02Z_TowardaTheoryofValueinAIAlignment_summary.md) — audits how alignment research defines human values and preference proxies.
- [AI Alignment from Social Choice Perspectives](../papers/2026-06-19_15-47-01Z_AIAlignmentFromSocialChoicePerspectives_summary.md) — analyzes preference aggregation and representation failures in human-feedback alignment.
- [Three Models of RLHF Annotation](../../papers/2026-04-28_17-39-14Z_ThreeModelsofRLHFAnnotation_Extension_Evidence_and_summary.md) — examines evidence and failure modes in preference-based alignment pipelines.
- [Democratic ICAI](../papers/2026-06-26_17-38-47Z_DemocraticICAI_DebatingOurWaytoSteeringPrin_summary.md) — explores collective deliberation and steering principles for aligned systems.

## Deception, misalignment, and reward-seeking

- [Even More Deception: Objective Misalignment in Mixed-Motive LLMs](../papers/2026-07-28_17-48-54Z_EvenMoreDeception_ObjectiveMisalignmentinMi_summary.md) — shows that altered objectives can remain hidden in internal reasoning while public communication looks normal.
- [Can Agents Deceive?](../papers/2026-07-30_12-54-17Z_CanAgentsDeceive_EvaluatingReasoningandDece_summary.md) — evaluates deceptive reasoning and behavior in agent settings.
- [Coercion and Deception in AI-to-AI Management](../papers/2026-07-16_20-07-47Z_CoercionandDeceptioninAI_to_AIManagement_An_summary.md) — studies strategic interaction and deceptive control between AI agents.
- [Measuring Reward-Seeking via Contrastive Belief](../papers/2026-07-21_10-57-09Z_MeasuringReward_SeekingviaContrastiveBelief_summary.md) — probes reward-seeking behavior through belief-sensitive contrasts.
- [Sweet Little Lies: Strategic Deception in AI Emotional Support](../papers/2026-08-02_20-19-56Z_SweetLittleLies_StrategicDeceptioninAIEmoti_summary.md) — models incentives that can make emotional-support chatbots misrepresent user states.
- [Harmful Content Is Not Enough](../papers/2026-08-08_16-13-38Z_HarmfulContentIsNotEnough_ContinuationFrami_summary.md) — examines why safety evaluation must cover behavioral persistence beyond isolated harmful outputs.

## Sycophancy and behavioral alignment

- [Gotta Catch Them All: The Modes of Sycophancy](../papers/2026-07-22_13-49-38Z_GottaCatchthemall_themodesofSycophancy_summary.md) — identifies distinct internal sycophancy modes and their attention circuitry.
- [Why LLMs Give In](../papers/2026-08-02_05-49-25Z_WhyLLMsGiveIn_ConversationalFactorsandReaso_summary.md) — shows how conversational timing, evidence, and challenge framing drive medical sycophancy.
- [MemSyco-Bench](../papers/2026-07-01_15-30-33Z_MemSyco_Bench_BenchmarkingSycophancyinAgent_summary.md) — benchmarks sycophancy in memory-enabled agents.
- [Sycophancy Undermines Epistemic Vigilance](../papers/2026-07-31_16-09-23Z_SycophancyUnderminesEpistemicVigilanceinCoo_summary.md) — connects user-pleasing behavior to failures of critical evaluation.
- [Beyond Sycophancy](../papers/2026-07-23_17-40-07Z_BeyondSycophancy_StructuredResistanceandCom_summary.md) — studies structured resistance and compliance trade-offs.
- [Token-Level Diagnosis of Sycophancy](../papers/2026-07-31_00-05-36Z_Token_LevelDiagnosisofSycophancyinLLMswithA_summary.md) — provides a mechanistic route for diagnosing sycophantic behavior.
- [From Prompting to Behavioral Alignment](../papers/2026-08-11_23-06-39Z_FromPromptingtoBehavioralAlignment_Personal_summary.md) — applies preference optimization to improve behavioral consistency.

## Oversight, interpretability, and runtime safety

- [How to Avoid Debate: Scalable AI Safety via Doubly Efficient Debate](../papers/2026-07-03_18-49-20Z_HowtoAvoidDebate_ScalableAISafetyviaDoubly__summary.md) — investigates scalable oversight through debate-style verification.
- [Automatically Finding and Validating Unexpected Model Behaviors](../../papers/2026-05-06_16-27-23Z_AutomaticallyFindingandValidatingUnexpected_summary.md) — audits intended and unintended behavioral changes after model interventions.


- [What LLM Agents Say When No One Is Watching](../papers/2026-07-02_17-59-23Z_WhatLLMAgentsSayWhenNoOneIsWatching_SocialS_summary.md) — compares public and private agent responses to expose social-context failures.

## Associated article summaries

- [OpenAI’s Hugging Face Breach Reignited the Alignment Debate](../../entities/article/2026-07-27_OpenAI_sHuggingFacebreachhasreignitedthedebateover_summary.md) — contrasts containment with alignment as a response to loss-of-control events.
- [How OpenAI Lost Control of an AI Model](../../entities/article/2026-08-03_HowOpenAILostControlofanAIModel_andWhatNeedstoChan_summary.md) — summarizes autonomous exploitation, deception risk, and containment gaps.
- [Rogue AI Agents Created Fake Online Identities](../../entities/article/2026-08-05_RogueAIagentscreatedfakeonlineidentitiesinanotherh_summary.md) — links observed autonomy and deception to alignment concerns.
- [Anthropic Says Claude Accidentally Hacked Real Companies](../../entities/article/2026-07-31_AnthropicsaysClaudeaccidentallyhackedrealcompanies_summary.md) — documents failures of isolation, monitoring, and deployment safeguards.
- [Anthropic Is Turning Claude Code Auto Mode On by Default](../../entities/article/2026-08-09_AnthropicisturningClaudeCode_sautomodeonbydefault_summary.md) — examines automated action approval and prompt-injection defenses.
- [A Safe Path to Open Weights](../../entities/article/2026-08-01_ASafePathtoOpenWeights_summary.md) — connects release governance, safety testing, and ecosystem readiness.
- [How AI Guardrails Are Impeding Offensive Cybersecurity Work](../../entities/article/2026-07-24_HowAIguardrailsareimpedingtheworkofoffensivecybers_summary.md) — captures the operational trade-off between safety controls and capability testing.
- [When AI Goes Rogue](../../entities/article/2026-08-06_WhenAIgoesrogue-HarvardGazette_summary.md) — surveys loss-of-control and governance concerns around agentic systems.
- [Claude Opus 5 and Alignment Claims](../../entities/article/2026-07-24_AnthropiclaunchesOpus5_summary.md) — records public claims about constitutional training, safety, and behavioral alignment.
