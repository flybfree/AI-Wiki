---
title: "Summary: Daily AI Intelligence Briefing — 2026-11-22"
date: "2026-11-22"
type: briefing
status: "canonical full-day AI-only final through 23:59 CST; 4 Nov 22 confirmed paper keeps; Brave unavailable; arXiv discovery incomplete"
tags: [ai-intelligence, daily-briefing, models, security, infrastructure, governance, research]
sources:
  - "https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers"
  - "https://novita.ai/blog/minimax-requests-privacy-notice/"
  - "https://openai.com/index/perplexity-and-intelligence/"
  - "https://www.sarvam.ai/blogs/sarvam-105b-1711"
  - "https://huggingface.co/sarvamai/sarvam-105b-1711"
  - "https://fortune.com/2026/11/22/ai-data-centers-power-grid-capacity/"
  - "https://www.nga.org/news/press-releases/governors-call-for-ai-action/"
  - "https://www.theneuron.ai/newsletter/who-really-wins-from-anthropic-s-ipo/"
  - "https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/papers/2026-11-17_06-55-41Z_HarnessesThatImproveThemselves_AUnifyingFra_summary.md"
  - "https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/papers/2026-11-17_18-59-07Z_TrainingLanguageModelsforIntrospectiveOvers_summary.md"
  - "https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/papers/2026-11-19_02-47-44Z_TowardaScienceofAIAgentSocieties_summary.md"
  - "https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/papers/2026-11-18_18-32-14Z_Whoareyou_ThePersonalImitationGame_summary.md"
---
# Summary: Daily AI Intelligence Briefing — 2026-11-22

**Coverage window: Sunday, November 22, 2026, 00:00–23:59 CST (America/Chicago, UTC−06:00); canonical full-day final.** The clearest pattern is that AI deployment is increasingly shaped by the infrastructure around models: inference providers’ handling of prompts, the power grid, access controls, and governance. OpenRouter disclosed enforcement after prompt-handling failures; Sarvam released an open-weight, post-trained checkpoint for enterprise agents; and OpenAI’s chief scientist proposed pretraining perplexity as one input to shared safety pacing. Governors also asked Congress for a federal AI framework that preserves state deployment protections. These are company claims, analysis, and nonbinding policy recommendations—not new laws or independently validated model rankings. The complete local curation query confirms four research papers approved on November 22 CST; their titles link to canonical summaries. Paper discovery remains incomplete, so this is a final edition for verified available coverage, not a claim of exhaustive literature or news discovery.

## Key Themes

### 1. Inference-provider privacy claims are moving from attestations toward testing

OpenRouter’s [November 22 first-party notice](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers) says its investigation, prompted by [Dragos’s canary-token study](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens), led it to off-board **three unnamed providers**, remove **125 endpoints** from Zero Data Retention (ZDR) eligibility, and notify potentially affected customers. Some endpoint removals were precautionary; the count does not mean 125 confirmed breaches. OpenRouter says the findings did not show a breach of its own systems. It plans ongoing canary-style checks, technical verification for hidden request forwarding, and validation before restoring ZDR status. Its announcement links public statements from Atlas Cloud, Novita, Phala, and Together—but does **not** identify those four as the three providers it off-boarded.

A new [Novita notice](https://novita.ai/blog/minimax-requests-privacy-notice/) adds a distinct failure mode: a routing configuration sent some MiniMax requests to MiniMax’s official API rather than processing them on Novita infrastructure. Requests made through Novita, including through OpenRouter, from May 28 to November 11 may have been accessed or retained by a third party. The researcher saw access to test URLs and hostnames, but no use of the planted AWS test keys. Novita suspended affected models, is checking retention and deletion with MiniMax, and advises rotating any live secrets included in those prompts. This is a routing/retention exposure, not evidence that every endpoint or customer was affected.

**Source discrepancy:** AI Weekly’s [November 22 live digest](https://aiweekly.co/ai-news-today) says OpenRouter off-boarded Novita, Phala, and Together. OpenRouter’s own post does not name the three and lists four provider notices; the named roster in the digest is therefore not verified by the primary source. The distinction matters: a public incident notice, a removed ZDR designation, and an off-boarding decision are different facts.

**Why it matters:** a router-level privacy setting cannot control every downstream host, reseller, model developer, or logging system. Treat routing, retention, and onward transfer as separate trust boundaries. Do not send credentials in prompts; affected customers should follow provider-specific notice windows and rotate any secrets that may have been included.

### 2. Industrial cyber testing shows useful AI assistance, not autonomous exploitation

A [Financial Times report published November 22](https://www.ft.com/content/3cf882c6-0be6-43f5-b01e-b6f765686c8b) revisits AI-assisted operational-technology (OT) attack planning. In the underlying [Forescout/Vedere Labs experiment, published September 1](https://www.forescout.com/blog/can-ai-create-plc-attacks-yes-but-it%E2%80%99s-not-that-easy-yet/), a researcher used Claude Code to port a known remote-code-execution exploit between two WAGO programmable logic controller (PLC) models. The hands-on work required substantial researcher direction, took 8 hours 32 minutes, and used $535.74 in API tokens; an attempted command-and-control extension bricked the target. The FT also describes a separate Booz Allen exercise in which AI models moved from a perimeter compromise to actions inside an industrial control network in just over 16 minutes. These are separate tests, not a single autonomous operation or evidence of a live AI-run infrastructure attack.

**Why it matters:** AI can reduce time spent on technical analysis and attack planning, but the current boundary still includes human expertise, access, and operational decisions. Defenders should keep internet-facing OT exposure low and rehearse incident response for AI-assisted exploitation without assuming that an experimental benchmark demonstrates real-world autonomous capability.

### 3. OpenAI proposes a common pretraining signal for safety and pacing

In [“Perplexity and Intelligence,” dated November 22](https://openai.com/index/perplexity-and-intelligence/), OpenAI Chief Scientist Jakub Pachocki argues that perplexity—the average difficulty a model has predicting the next token—could help compare pretraining progress and underpin shared safety norms. He publishes OpenAI’s internal log-perplexity trend on a held-out code dataset: about 0.99 for GPT-3.5, 0.91 for GPT-4, below 0.8 for recent models, and about 0.76 for a model associated with striking mathematical results. He says lower values have coincided with capabilities such as fluent chat, useful reasoning, and stronger cybersecurity or mathematics performance, while stressing that exact capability thresholds were not predictable in advance.

The proposal is more than a metric: Pachocki calls for frontier developers to establish common evaluation and transparency norms and agree not to cross capability limits until concrete monitoring milestones—such as improved chain-of-thought monitors—are met. He also says a major acceleration in deep-learning research could conceivably arrive as soon as 2027; that is his scenario, not a forecast or an announced industry commitment. The post itself notes important limits: datasets differ between labs, perplexity does not directly measure task performance, and gains from reasoning or other post-training may not appear in the metric.

**Why it matters:** the proposal gives labs a potentially comparable training-stage indicator, but the dataset and evaluation protocol would need independent agreement before cross-lab comparisons are meaningful. The policy question is whether a metric can be linked to verifiable monitoring readiness rather than treated as a standalone proxy for safety.

### 4. Sarvam turns an existing 105B model into a more deployable agent checkpoint

Sarvam’s [November 22 release post](https://www.sarvam.ai/blogs/sarvam-105b-1711) and [Hugging Face model card](https://huggingface.co/sarvamai/sarvam-105b-1711) describe Sarvam-105B-1711 as a new open-weight checkpoint of an existing 105-billion-parameter mixture-of-experts model, with 10.3B active parameters—not a wholly new foundation-model architecture. The Apache-2.0 weights add post-training for instruction following, tool use, enterprise-agent tasks, and Indian languages. Sarvam reports a 160K-token context and offers BF16 weights plus a 65GB NVFP4 checkpoint intended to run on one workstation-class GPU, enabling on-premises deployment where data should not go to a third-party API. In the day’s model landscape, no new closed-frontier launch was verified; this is an open-heavyweight checkpoint, while customization options and dated model context remain tracked in the [open-model snapshot](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/llm-models/OpenSourceModelsStateOfTheArt.md).

Sarvam’s own eight-benchmark average is 73.9 at a blended $0.15 per million tokens, compared with 74.0 at $0.85 for Gemini 3.5 Flash-Lite and 73.0 at $0.54 for Gemma 4 31B. The company also reports gains over its February checkpoint on IFBench (32.5 to 82.5), Tau2 customer-service tool use (46.2 to 85.5), and its Indic suite (30.1 to 79.1). These comparisons and costs are publisher-reported, use Sarvam’s evaluation setup, and need matched independent replication; the attractive trade-off is a testable claim, not settled ranking.

**Why it matters:** open weights, a permissive license, and a single-workstation deployment path make this a meaningful new option for local or India-language workloads. The footprint is still substantial, and active-parameter counts do not describe the memory needed to load all weights or serve long contexts.

### 5. Data-center electricity demand is becoming an AI deployment and ratepayer constraint

[Fortune’s November 22 analysis](https://fortune.com/2026/11/22/ai-data-centers-power-grid-capacity/) cites Howden’s estimate that U.S. data-center electricity demand has grown about 19% annually since 2000 while grid capacity grew around 2% annually. These are data-center figures broadly, not an AI-only measurement, though the current buildout is being driven in significant part by AI. Lawrence Berkeley National Laboratory projects data centers could account for as much as 12% of U.S. electricity use by 2028, versus 1.9% in 2018. In four grids studied by Cornell researchers, data centers paid only 38% of the 2025 infrastructure costs attributed to their growth ($3.12 billion of $8.25 billion); the study estimated uneven local wholesale-price increases.

Fortune also reports political resistance: data-center proposals lost 40 of 41 local ballot measures where they appeared on November 3. The figures point to a mismatch between fast-moving project plans and slow grid buildout, plus a dispute over who pays for generation and connection upgrades. The article reports announced on-site generation as a proposed pipeline, not operating capacity, and its emissions and delay estimates remain attributed projections.

**Why it matters:** access to power, grid connection timelines, and cost allocation may constrain AI compute as much as chips or model efficiency. Watch whether projects bring new generation, shift costs onto households, or face permitting delays; do not treat announced gigawatts as delivered capacity.

### 6. Governors offer Congress a nonbinding federal–state framework

The [National Governors Association’s November 22 release](https://www.nga.org/news/press-releases/governors-call-for-ai-action/) sets out bipartisan principles for a national AI approach. It calls for federal attention to national and international risks in AI development, while preserving state flexibility to govern deployment and protect workers, consumers, children, civil rights, and privacy. Other priorities include evidence-based, proportionate safeguards, clearer and more consistent roles, and competition rules that do not entrench large incumbents. The release is a set of recommendations intended to shape congressional work—not legislation, a regulation, or a new legal duty. Its public summary does not specify detailed audit or incident-reporting requirements.

**Why it matters:** the debate is not only how much to regulate frontier systems, but how to divide authority between federal model-development rules and state protections against deployment harms. The next signal is whether Congress incorporates governors’ principles and how any federal preemption language treats existing state safeguards.

### 7. The IPO story is shifting from listing day to who captures the upside

A [November 22 newsletter from The Neuron](https://www.theneuron.ai/newsletter/who-really-wins-from-anthropic-s-ipo/) follows up on Anthropic’s earlier IPO close with an ownership-and-compute analysis. It argues that Amazon and Google benefit both from their reported Anthropic stakes and from supplying computing capacity; it cites Anthropic’s reported commitment to spend at least $110 billion with Amazon from May 2026 through April 2036. The newsletter notes that Amazon’s and Google’s shares are nonvoting, so the economic exposure does not itself imply governance control. This is an analysis of the already completed IPO, not a second listing or a new financing event. It complements yesterday’s safety-governance discussion by adding the infrastructure and investor incentives behind the company’s growth.

## What Changed Today

- OpenRouter publicly disclosed provider-enforcement actions: three unnamed providers off-boarded, 125 endpoints removed from ZDR eligibility (including precautionary removals), and potentially affected customers notified.
- Novita acknowledged that some MiniMax requests were forwarded to MiniMax’s official API from May 28 through November 11; its notice says test URLs were accessed but test AWS keys were not used.
- The FT published a new industrial-cyber report, but its Forescout PLC exploit example dates to September and required substantial human guidance; it is not evidence of a new live incident.
- OpenAI’s chief scientist published a pretraining-perplexity proposal and previously internal model trend data; this is not yet a shared industry standard.
- Sarvam released an Apache-2.0 open-weight 105B checkpoint, extending an existing model rather than introducing a new architecture.
- The NGA issued bipartisan AI-governance principles, while Fortune connected AI-linked data-center growth with grid capacity, local permitting, and who pays.
- The Neuron’s IPO analysis is a new interpretation of last week’s listing, not a new IPO event.
- No additional closed-frontier model launch was verified during the target day. Four research papers were approved in the local curation workflow at about 18:25 CST and are included below; other generated candidate summaries remain unapproved.

## Why It Matters

The common thread is that AI’s impact is increasingly shaped by infrastructure around the model. A prompt can be routed through multiple providers despite a privacy label; a human-guided coding agent can lower the effort required to adapt an industrial exploit; the cost and pace of pretraining may become a governance signal; and power, financing, and regulatory authority affect which systems can be deployed and under what conditions. None of the evidence supports collapsing these into one claim that models are autonomously acting in the world. Stronger decisions depend on accurate scope, independent evaluation, technical controls, and clear attribution.

## What to Watch Next

1. Whether OpenRouter identifies the three off-boarded providers, publishes the affected endpoint list, or supplies a customer-by-customer exposure explanation; do not infer the roster from its linked notices.
2. Novita’s follow-up with MiniMax on whether forwarded prompts were retained, reviewed, or deleted; customers should rotate any exposed live credentials.
3. Whether other frontier developers publish comparable pretraining metrics and agree on datasets, safety-monitoring milestones, or common limits. Treat the 2027 acceleration scenario as a hypothesis.
4. Independent tests of Sarvam-105B-1711 using matched agent tasks, Indian-language evaluation, full cost, and the exact NVFP4 hardware/runtime configuration.
5. U.S. grid connection, project-delay, and ratepayer-cost developments; separate proposed on-site generation from capacity actually brought online.
6. Congressional response to the governors’ principles and any concrete state/federal allocation or preemption language.
7. A fresh arXiv scout that reaches the November 22 local-date window, and page-level review of the 12 generated candidate summaries that remain unapproved.

## Research Curation and Coverage Limits

The local intake contained one target-date article capture, [OpenAI’s “Perplexity and Intelligence”](https://openai.com/index/perplexity-and-intelligence/), and 12 generated raw paper-summary candidates; those candidates have no matching curation decisions and are not presented as approved. A read-only query of the complete SQLite decision store found **929 keep rows overall** and **4 keep approvals dated November 22 in America/Chicago**, after converting stored UTC timestamps. Stable summary identities were compared against earlier dated briefings; all four target-date approvals were uncovered and each has one canonical summary link below. The four canonical summaries are present and now expose visible original arXiv URLs. Direct Brave search could not run because `BRAVE_SEARCH_API_KEY` was unavailable. A general web-search fallback was used only as a discovery aid, with target-day claims checked against primary sources where available; the fallback is not represented as a Brave sweep. The saved arXiv scout fetched 14 query families / 21 pages / 1,200 entries, but its newest result was dated November 20 06:45 UTC, before the November 22 CST target window; several topic queries also stopped at their page caps. The research discovery pass is therefore **incomplete**, not evidence that no other relevant paper was submitted. Unreviewed candidates are omitted.

## Approved Research Papers — 4 Confirmed Keeps

All four items below were approved on November 22 CST. Approval date is distinct from each paper’s submission date. Each title links to its canonical rendered summary, which now contains a visible original-paper URL.

- [Harnesses That Improve Themselves: A Unifying Framework for Self-Improving Agent Harnesses](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/papers/2026-11-17_06-55-41Z_HarnessesThatImproveThemselves_AUnifyingFra_summary.md) — The paper separates runtime bugs from model limitations, then proposes a four-stage loop for diagnosing, patching, validating, and deploying modular harness changes. Its reported SWE-bench Lite results favor gated modular updates over prompt reflection and full rewrites; this makes runtime verification and rollback central to agent improvement rather than treating the model as the only optimization target.
- [Training Language Models for Introspective Oversight](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/papers/2026-11-17_18-59-07Z_TrainingLanguageModelsforIntrospectiveOvers_summary.md) — A separately trained observer role reached mean AUROC 0.907 across five held-out oversight evaluations, ahead of the paper’s honesty-training, transcript-monitoring, and activation-oracle baselines. This suggests that verifiable behavioral reporting can improve oversight, while the reported result remains bounded to the tested model and evaluation set.
- [Toward a Science of AI Agent Societies](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/papers/2026-11-19_02-47-44Z_TowardaScienceofAIAgentSocieties_summary.md) — The authors define agent societies through individualized objectives, rules/governance, autonomy, and scale/complexity, then classify economic, conflict, unsafe, and system-level behaviors. The framework gives researchers a way to distinguish genuine societal dynamics from simple multi-agent coordination and to expose gaps in today’s platforms.
- [Who are you? The Personal Imitation Game](https://raw.githubusercontent.com/flybfree/AI-Wiki/master/concepts/papers/2026-11-18_18-32-14Z_Whoareyou_ThePersonalImitationGame_summary.md) — A proposed benchmark tests whether models can imitate a specific person, not merely sound generally human. Its 20-person deception study was statistically inconclusive, which is important: personal-AI identity claims need larger evaluations and explicit privacy/consent analysis rather than anecdotal demonstrations.

## Sources / References

- Inference routing and provider statements: [OpenRouter’s November 22 response](https://openrouter.ai/blog/announcements/data-processing-incidents-on-inference-providers) · [Dragos canary-token investigation](https://www.dragos.com/blog/ai-supply-chain-security-canary-tokens) · [Novita’s MiniMax privacy notice](https://novita.ai/blog/minimax-requests-privacy-notice/) · [Phala’s preliminary report (November 10)](https://phala.com/posts/phala-november-preliminary-incident-report) · [Together AI’s incident notice (November 21)](https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026) · [Atlas Cloud statement](https://www.atlascloud.ai/blog/ai-updates/security-and-privacy-commitment)
- Industrial cyber testing: [Financial Times, November 22](https://www.ft.com/content/3cf882c6-0be6-43f5-b01e-b6f765686c8b) · [Forescout/Vedere Labs, September 1](https://www.forescout.com/blog/can-ai-create-plc-attacks-yes-but-it%E2%80%99s-not-that-easy-yet/)
- Pretraining and safety pacing: [OpenAI — “Perplexity and Intelligence”](https://openai.com/index/perplexity-and-intelligence/)
- Open-weight release: [Sarvam-105B-1711 announcement](https://www.sarvam.ai/blogs/sarvam-105b-1711) · [NVFP4 model card and Apache-2.0 license](https://huggingface.co/sarvamai/sarvam-105b-1711) · [BF16 weights](https://huggingface.co/sarvamai/sarvam-105b-1711-bf16)
- Power and permitting: [Fortune, November 22](https://fortune.com/2026/11/22/ai-data-centers-power-grid-capacity/)
- Governance: [National Governors Association, November 22](https://www.nga.org/news/press-releases/governors-call-for-ai-action/)
- IPO economics: [The Neuron newsletter, November 22](https://www.theneuron.ai/newsletter/who-really-wins-from-anthropic-s-ipo/)
- Aggregator date and mismatch check: [The Neuron Atom feed](https://www.theneuron.ai/feed/) · [AI Universe Explorer](https://aiuniverseexplorer.com/ai-news-aggregator/) · [AI Weekly live digest](https://aiweekly.co/ai-news-today)

