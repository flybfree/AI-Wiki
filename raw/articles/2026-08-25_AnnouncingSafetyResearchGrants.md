---
title: Announcing Safety Research Grants
date: 2026-08-25
url: https://thinkingmachines.ai/news/safety-research-grants/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://thinkingmachines.ai/news/safety-research-grants/
source_feed: Thinking Machines Lab News
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-08-25 00:17
---

# Announcing Safety Research Grants

## Full Article

We recently released
Inkling
and
Inkling-Small
with open weights, and explained
how we are thinking about safety and openness
. Today, we are launching Tinker grants of up to $50,000 in credits for safety research on open-weight models. Below are some directions we find promising. The list is non-exhaustive on purpose. If you’re working on a safety project that could be accelerated by additional Tinker credits, we want to hear from you.
Making models safer to open
Differential acceleration of defensive over offensive capability.
Many capabilities are dual-use: the same cyber skills that let a model find and patch vulnerabilities in defenders’ hands can accelerate exploitation of unpatched systems in attackers’ hands. Similar tradeoffs arise in domains like chemistry and biology. However, we hypothesize that not every skill contributes equally to both sides — some capabilities (e.g. triage, detection, hardening) may be disproportionately useful to defenders, while others (e.g. exploitation, evasion) skew toward attackers.
BountyBench: Dollar Impact of AI Agent Attackers and Defenders on Real-World Cybersecurity Systems
(Zhang et al, 2026)
,
AI Agents Enable Adaptive Computer Worms
(Guan et al, 2026)
Can we fine-tune models to differentially improve defensive skills while minimally improving offensive ones?  A direct experiment would fine-tune a model toward defensive skills and then measure the uplift to each side — the offense–defense gap of the training run, rather than raw capability alone. A key question is whether any such gap reflects genuine asymmetry, rather than suppression that dissolves under attacker pressure or sandbagging that persists only under measurement.
Building classifiers for hazardous data at scale.
Training data can contain information that materially increases hazardous capabilities, but identifying that information is difficult.
Shaping capabilities with token-level data filtering
(Rathi and Radford, 2026)
The downstream impact of any individual document or data point is hard to predict in advance,
Magic: Near-optimal data attribution for deep learning
(Ilyas and Engstrom, 2025)
and constructing high-quality labels often requires scarce domain expertise. Can we train filtering models that reliably identify safety-relevant data at sufficient scale and recall, without discarding large amounts of benign scientific or technical content?
Deep Ignorance: Filtering Pretraining Data Builds Tamper-Resistant Safeguards into Open-Weight LLMs
(O’Brien et al, 2026)
,
Enhancing Model Safety through Pretraining Data Filtering
(Chen et al, 2025)
And can these classifiers be made robust against paraphrasing, obfuscation, domain shift, and changing model capabilities?
Safety Pretraining: Toward the Next Generation of Safe AI
(Maini et al, 2026)
Ultimately, the strongest test is downstream, and directly measurable with fine-tuning access: does filtering actually reduce hazardous capability uplift, and what concerning capabilities can still be learned from data that passes the filter?
Tamper-resistant safety training.
Built-in safeguards learned during model training may not remain stable under subsequent fine-tuning. Can mitigations be developed that persist under downstream modification, including adversarial fine-tuning intended to remove safeguards and ordinary continued training that may inadvertently wash them out?
Tamper-Resistant Safeguards for Open-Weight LLMs
(Tamirisa et al, 2025)
,
Open Technical Problems in Open-Weight AI Model Risk Management
(Casper et al, 2026)
Designing scalable adversarial training methods that improve robustness against diverse downstream modifications is one promising approach, with generalization to held-out attack strategies a key test of success.
Model Tampering Attacks Enable More Rigorous Evaluations of LLM Capabilities
(Che et al, 2025)
Understanding how robustness changes with scale and architecture is another important question, while negative or impossibility results can help establish the limits of what persistent safety mitigations can achieve.
Understanding alignment failure modes
Safety-relevant generalization from narrow fine-tuning.
Narrow fine-tuning can sometimes produce behaviors far outside of the task that was directly trained. Emergent misalignment
Emergent misalignment: Narrow finetuning can produce broadly misaligned LLMs
(Betley et al, 2025)
is one striking example, but we suspect it is one instance of a broader phenomenon, and we want to characterize that phenomenon directly: its boundary conditions, its scaling properties, and the mechanisms that cause it. When does narrow harmful training generalize into broad behavioral change, and does this require intentionally adversarial data, or could it plausibly arise accidentally from ordinary downstream fine-tuning? A related compositional question: can a model separately learn planning, tool use, and relevant domain knowledge, then compose those pieces into a concerning behavior that was never demonstrated end-to-end? Understanding which of these effects are quirks of specific setups and which are robust properties of fine-tuning would materially change how downstream training should be evaluated.
Reward hacking and oversight gaming.
Proxy rewards can create real failure modes. Optimizing an imperfect reward can eventually favor behavior that scores well without accomplishing the intended objective. We want to understand when reward hacking emerges, how it changes with model capability and optimization pressure, and whether early signals can predict it before it becomes severe.
Reward Hacking in Language Model Agents: Revisiting AI Safety Gridworlds
(Çağatan and Zhao, 2026)
More concerning failures may involve models learning strategies for gaming or interfering with oversight, such as chain-of-thought monitors. A key open question is whether these strategies can be detected, and whether they transfer across tasks.
Chain-of-thought obfuscation learned from output supervision can generalise to unseen tasks
(Hadida et al, 2026)
Measuring and forecasting risk
Worst-case and marginal risk estimation.
Open-weight models let people make AI their own. A complementary safety challenge is understanding the maximum risk a model can pose after release. How can we estimate safeguard degradation in different safety-relevant domains, and as a function of a motivated attacker’s time, data, or optimization effort? A related quantity is marginal risk: what harmful capabilities does this model enable beyond what is already possible?  Fine-tuning itself is a natural stress test here: evaluations built on adversarial fine-tuning can distinguish capabilities that are genuinely absent from those that are merely suppressed and easily re-elicited.
TamperBench: Systematically Stress-Testing LLM Safety under Fine-Tuning and Tampering
(Hossain et al, 2026)
Recent work on worst-case post-training provides useful starting points,
Estimating Worst-Case Frontier Risks of Open-Weight LLMs
(Wallace et al, 2026)
but leaves the shape and limits of this resource–risk frontier poorly understood.
Forecasting safety-relevant scaling trends.
Many of the questions in this post become substantially more tractable if expensive experiments can be forecast from smaller runs. Can measurements at low post-training budgets predict downstream safety-relevant properties — including capability uplift, safeguard degradation, or reward hacking — as optimization and compute are scaled up? More broadly, we want to understand which safety-relevant scaling trends extrapolate reliably across model capability and training budget — and where those trends break down. Existing work on forecasting rare behaviors
Forecasting Rare Language Model Behaviors
(Jones et al, 2025)
and adversarial robustness
Capability-Based Scaling Trends for LLM-Based Red-Teaming
(Panfilov et al, 2026)
provides useful examples of the broader possibility.
The grants
See
how to apply
for proposal requirements, selection criteria, timeline, and complete
terms of service
for the grant program.

## Metadata
- **Source**: [Original Article](https://thinkingmachines.ai/news/safety-research-grants/)
