---
title: Best Open-Source LLM May 2026: Llama 4 vs Qwen vs DeepSeek
date: 2026-05-04
url: https://codersera.com/blog/best-open-source-llm-2026-llama-4-qwen-3-5-deepseek-v4-gemma-4-mistral/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://codersera.com/blog/best-open-source-llm-2026-llama-4-qwen-3-5-deepseek-v4-gemma-4-mistral/
scraped: 2026-05-04 02:00
---

# Best Open-Source LLM May 2026: Llama 4 vs Qwen vs DeepSeek

## Full Article

In the last 30 days, five frontier-class open-weight LLMs shipped: Meta's Llama 4 (Scout + Maverick), Alibaba's Qwen 3.5, DeepSeek V4 (Pro + Flash), Google's Gemma 4, and — most recently — Mistral Medium 3.5 on April 29. The frontier between open-weights and closed-weights has never been thinner, and the buyer's question has flipped from
"can we get away with open?"
to
"which open-weight model do we deploy?"
Updated 2026-05-03:
Added
Kimi K2.6
(Moonshot AI, released April 20) and
GLM-5.1
(Z.ai / Zhipu, released April 7) — both have moved into the open-weight frontier in the last three weeks and any 2026 shortlist that omits them is already stale.
This is the canonical comparison post-Mistral 3.5 (today is May 3, 2026). We've pulled real benchmark numbers from each lab's model card, the
NIST CAISI evaluation of DeepSeek V4 Pro
, and live leaderboards. No hand-waving — if a number isn't published, we say so.
If you're a CTO or infra lead trying to lock down the LLM layer of your stack for the next 12 months, this is your buyer's guide.
Want the bigger picture?
Read our continuously-updated
Open-Source LLMs Landscape (2026)
— every notable open-weights model, license, hosting cost, and deployment pattern.
Deep-diving Meta? Bookmark our
Llama 4 Complete Guide (2026)
.
Evaluating Alibaba's release? See our
Qwen 3.5 Complete Guide (2026)
.
Looking at DeepSeek? Read the
DeepSeek V4 Complete Guide (2026)
.
For Google's open weights, see our
Gemma 4 Complete Guide (2026)
.
Want the full picture?
Read our continuously-updated
GPT-5.5 Complete Guide (2026)
— benchmarks, pricing, agent capabilities, and migration notes.
The 30-second answer
Best raw capability, willing to run a big cluster:
DeepSeek V4 Pro.
80.6 SWE-Bench Verified, 90.1 GPQA Diamond, 1M context
.
Best coding agent, single-vendor stack, EU-friendly:
Mistral Medium 3.5.
77.6% SWE-Bench Verified on a 128B dense model
.
Best long-context + fits on a single H100:
Llama 4 Scout.
10M tokens, 17B active / 109B total MoE
.
On-device or laptop-class:
Gemma 4 — Google's efficiency play, designed to run locally.
Best $/intelligence at hosted-API scale:
DeepSeek V4 Flash — 13B active, "reasoning closely approaches V4-Pro" per
DeepSeek
.
Best agentic + long-horizon coding (new entrant):
Kimi K2.6
— Moonshot’s 1T/32B MoE under Modified MIT,
80.2 SWE-Bench Verified, 96.4 AIME 2026, 90.5 GPQA-Diamond, 256K context
.
Best SWE-Bench Pro score, smallest deploy footprint of the frontier MoEs:
GLM-5.1
— Z.ai’s 744B/40B MoE under MIT,
58.4 SWE-Bench Pro (state-of-the-art), ~77.8 SWE-Bench Verified, 200K context
.
The matrix
Model
Params (active / total)
Architecture
Context
License
SWE-Bench Verified
Smallest deploy
Llama 4 Scout
17B / 109B
MoE, 16 experts
10M
Llama 4 Community License
Not officially published
1× H100
Llama 4 Maverick
17B / 400B
MoE, 128 experts
1M+
Llama 4 Community License
Not officially published
1× H100 host (distributed)
Qwen 3.5 (235B-A22B)
~22B / 235B
MoE
128K (extendable)
Tongyi Qianwen / Apache-2.0 (varies by size)
Mistral cites Qwen 3.5 397B A17B in their comparison; Alibaba's official SWE-Bench number not loaded for this post
2-4× H100
DeepSeek V4 Pro
49B / 1.6T
MoE + Hybrid CSA/HCA attention
1M
MIT
80.6
8× H200 (FP4/FP8 mixed)
DeepSeek V4 Flash
13B / 284B
MoE
1M
MIT
Not separately published
1× H100 host
Gemma 4
Multiple sizes (≤27B class)
Dense
128K
Gemma Terms of Use
Not in scope (efficiency model)
Laptop / single GPU
Mistral Medium 3.5
128B
Dense
256K
Modified MIT
77.6
2× H100
Kimi K2.6
32B / 1T
MoE
256K
Modified MIT
80.2
Multi-host (1T total weights)
GLM-5.1
40B / 744B
MoE
200K
MIT
~77.8 (self-reported);
58.4 SWE-Bench Pro
4–8× H100
Sources inline below. Where a number is "not published," we won't fill the cell with a guess.
Llama 4 (Scout + Maverick)
Meta released Llama 4 on April 5 with two production-ready sizes and a Behemoth preview still in training. Both Scout and Maverick are
MoE with 17B active parameters
; Scout has 16 experts (109B total) and Maverick has 128 experts (400B total). Both are natively multimodal via "early fusion" — vision tokens are concatenated and routed through the same transformer rather than bolted on via a separate vision encoder.
The headline:
Scout's
10-million-token context window
via the iRoPE architecture (interleaved attention with rotary embeddings). That's the longest context window of any production-grade open-weight model as of writing — by a factor of 10. For RAG-replacement, codebase-scale retrieval, and long-document workflows, nothing else open is in the same league.
Reported benchmarks
(per
llama.com
): Maverick scores
80.5 MMLU-Pro
,
73.4 MMMU
,
43.4 LiveCodeBench
; Scout scores
74.3 MMLU-Pro
and
32.8 LiveCodeBench
. Meta has not published an official SWE-Bench Verified score for either model.
Pick Llama 4 if:
you need long-context for RAG-on-everything workflows, you want a multimodal-native model, and you're OK with the Llama Community License (commercial use is fine for most companies; the >700M MAU clause excludes hyperscalers).
Skip if:
you need elite coding scores. Maverick's 43.4 LiveCodeBench trails DeepSeek V4 Pro's 93.5 by a country mile.
Qwen 3.5
Alibaba's Qwen 3.5 family ships in dense sizes (0.5B → 32B) and MoE configurations including the flagship 235B-A22B (22B active / 235B total). The official Qwen blog at
qwenlm.github.io/blog/qwen3.5/
returned 404 at fetch time — Alibaba may have moved it — but Mistral's own
Medium 3.5 announcement
directly compares against "Qwen3.5 397B A17B," confirming a larger MoE flavor exists in the family.
Strengths:
Qwen has been the strongest open Chinese-language family for two generations running, and the 3.5 line continues the pattern with the strongest multilingual coverage of any model in this comparison. Coding scores are competitive with DeepSeek on Chinese-language coding tasks specifically.
License caveat:
Smaller Qwen sizes ship under Apache-2.0; the larger flagship sizes ship under the Tongyi Qianwen license, which is generally permissive for commercial use but not OSI-approved. Read the model card for the specific size you're deploying.
Pick Qwen 3.5 if:
you have meaningful non-English usage, especially Chinese/Japanese/Korean, or you want the broadest size ladder (0.5B → 235B+) from a single family for fleet standardization.
DeepSeek V4 (Pro + Flash)
Released April 24, 2026, DeepSeek V4 is the most architecturally interesting model in this comparison. The
Pro model card
documents:
1.6T total / 49B active
MoE parameters
FP4 + FP8 mixed precision
— MoE expert weights in FP4, the rest in FP8
Hybrid Compressed Sparse Attention (CSA) + Heavily Compressed Attention (HCA)
— reducing single-token inference FLOPs by 27% vs V3.2 at 1M tokens, and KV cache by 90%
1M token context
MIT license
— the most permissive of any model here
Benchmarks (Pro Max mode):
87.5 MMLU-Pro, 90.1 GPQA Diamond, 93.5 LiveCodeBench, Codeforces 3206,
80.6 SWE-Bench Verified
, 89.8 IMOAnswerBench. These are state-of-the-art numbers for any open-weight model, and competitive with closed frontier models in coding and math.
The
NIST CAISI evaluation
released this week is more measured: it pegs V4 Pro as roughly 8 months behind frontier closed models on aggregated capability (Item Response Theory across 9 benchmarks), with notable gaps on ARC-AGI-2 (46% vs GPT-5.5's 79%) and PortBench software engineering (44% vs 78%). However, CAISI also confirms V4 is "more cost efficient than other models of similar capability" — cheaper than GPT-5.4 mini on 5 of 7 benchmarks tested.
V4-Flash
(13B active / 284B total) is the practical workhorse. DeepSeek claims its "reasoning capabilities closely approach V4-Pro" at a fraction of the inference cost.
Pick V4 if:
you want the best coding/math open-weight model, MIT license is a hard requirement, or you're cost-sensitive at scale (and have the GPU budget for the Pro tier — Flash for everyone else).
Gemma 4
Google's Gemma 4 leans into efficiency rather than peak capability. Both the
blog.google
and HuggingFace blog landing pages we tried returned 404, suggesting the announcement post moved — but the family remains live on HuggingFace under the Gemma terms.
The Gemma play has consistently been: a dense model that
actually runs
on a developer laptop or a single consumer GPU, with quantizations down to int4 that make on-device inference practical. If you're building features that need to ship inside a desktop app, an iOS/Android app, or an air-gapped enterprise environment, Gemma is in a category of one within this comparison set.
Pick Gemma 4 if:
you need on-device inference, you have strict data-residency/air-gap requirements, or you're building a privacy-first product where the model has to live on the user's hardware.
Skip if:
you're optimizing for capability per dollar at server scale — Gemma is not trying to win that fight.
Mistral Medium 3.5
Released April 29 — four days ago — Mistral Medium 3.5 is a
128B dense model with a 256K context window
, released under a modified MIT license per
Mistral's announcement
. The headline result:
77.6% on SWE-Bench Verified
, which Mistral specifically positions as ahead of Devstral 2 and Qwen 3.5 397B A17B.
The other interesting move is "Vibe" — Mistral's remote coding agents that run asynchronously in the cloud, executable from CLI or Le Chat, with native integrations for GitHub, Linear, Jira, and Sentry. Sessions are parallel and transferable from local to cloud while preserving history and approvals. This is the most polished agentic story of any of the five labs.
Pricing:
$1.5/M input, $7.5/M output via the Mistral API — though the open weights mean self-hosting is on the table.
Pick Medium 3.5 if:
you want strong agentic coding, EU data residency matters (Mistral is the only EU-headquartered lab in this comparison), or you want a dense model (operationally simpler than MoE — fewer expert-routing surprises).
Kimi K2.6 (Moonshot AI)
Released April 20, 2026,
Kimi K2.6
is Moonshot AI’s flagship open-weight MoE:
1 trillion total parameters with 32B active per token
, a
256K context window
, and a
Modified MIT license
covering both code and weights. The Hugging Face card is the primary source; a deeper writeup lives on the
Moonshot tech blog
.
Reported benchmarks
(thinking mode, temperature 1.0, per the
model card
):
80.2 SWE-Bench Verified
,
58.6 SWE-Bench Pro
, 76.7 SWE-Bench Multilingual,
96.4 AIME 2026
, 92.7 HMMT 2026 (Feb),
90.5 GPQA-Diamond
, 89.6 LiveCodeBench v6, 79.4 MMMU-Pro, 66.7 Terminal-Bench 2.0. SWE-Bench scores are averaged over 10 independent runs using an in-house SWE-agent-derived harness. Independent confirmation from
Artificial Analysis
positions K2.6 as the leading open-weight model on their composite Intelligence Index, with notable agentic strength: τ²-Bench Telecom 96%.
The differentiator
is long-horizon agentic coding. Per
MarkTechPost’s release coverage
, K2.6 supports agent swarms scaling to 300 sub-agents and 4,000 coordinated steps — the largest explicitly-supported agentic horizon of any open-weight model in this comparison.
Pick Kimi K2.6 if:
you want the strongest open-weight agentic-coding model right now, you can absorb the operational cost of a 1T-parameter MoE, and Modified MIT is acceptable to your legal team. Hosted API is also available via Moonshot directly and through providers like
Cloudflare Workers AI
.
Skip if:
you can’t justify a multi-host serving cluster and you don’t need the 256K context or 300-agent swarms — GLM-5.1 or DeepSeek V4 Flash will run cheaper on smaller footprints.
GLM-5.1 (Zhipu / Z.ai)
Released April 7, 2026 by Z.ai (formerly Zhipu AI / THUDM),
GLM-5.1
is a post-training upgrade to the GLM-5 foundation model: a
744B total / 40B active MoE
with a
200K context window
and a
131,072-token max output length
, released under the
MIT license
. Full technical docs are on
Z.ai’s developer portal
.
Reported benchmarks
(per the
Hugging Face model card
):
58.4 SWE-Bench Pro
— a state-of-the-art open-weight result on that benchmark, ahead of every other model in this comparison —
~77.8 SWE-Bench Verified
(per Z.ai’s own writeup,
summarized here
),
95.3 AIME 2026
, 94.0 HMMT Nov 2025,
86.2 GPQA-Diamond
, 69.0 Terminal-Bench 2.0 (with Claude Code harness), 68.7 CyberGym, 68.0 BrowseComp, and 52.3 HLE with tools.
Honesty note:
the SWE-Bench Verified figure and several other coding scores are self-reported by Z.ai. Independent third-party confirmation across every benchmark is not yet published — treat the headline numbers as Z.ai-reported until leaderboards like Vellum, Artificial Analysis, or BenchLM verify them.
Pick GLM-5.1 if:
you want the smallest active-parameter footprint in this frontier comparison (40B active, vs DeepSeek V4 Pro’s 49B and Kimi K2.6’s 32B but with much larger total weights), you need MIT-license simplicity, and SWE-Bench Pro performance is on your scorecard. The lower active-parameter count makes it the cheapest of the three frontier MoEs to serve at sustained throughput.
Skip if:
you need verified third-party benchmark numbers before committing, or you specifically need the 1M+ contexts that Llama 4 Scout and DeepSeek V4 Pro offer.
Coding shootout
Coding is where buyers feel the differences fastest. SWE-Bench Verified is the cleanest measure — it tests real GitHub issue resolution, not toy puzzles.
Model
SWE-Bench Verified
LiveCodeBench
Source
DeepSeek V4 Pro (Pro Max)
80.6
93.5
HF model card
Mistral Medium 3.5
77.6
Not published
Mistral
Kimi K2.6
80.2
(58.6 on SWE-Bench Pro)
89.6 (v6)
HF model card
GLM-5.1
~77.8 self-reported (
58.4 SWE-Bench Pro — SOTA open-weight
)
Not published
HF model card
Llama 4 Maverick
Not officially published
43.4
llama.com
Llama 4 Scout
Not officially published
32.8
llama.com
Qwen 3.5 (largest MoE)
Not loaded for this post (blog 404)
—
—
Gemma 4
Out of scope
—
—
The two-horse race for production coding is DeepSeek V4 Pro and Mistral Medium 3.5. If you can run V4 Pro, do — it's three points higher on the harder benchmark. If you can't, Mistral 3.5 is the simpler operational story (dense, smaller, well-documented agentic harness).
For deeper context on agent harnesses, see our
AI Coding Agents Complete Guide (2026)
.
Reasoning + math
DeepSeek V4 Pro again leads on the published numbers:
90.1 GPQA Diamond
and
89.8 IMOAnswerBench
in Pro Max mode. NIST's CAISI report cites "competitive performance (96–97% across multiple tests)" on mathematics specifically, which closes most of the gap to GPT-5.5 on math even where ARC-AGI-2 reasoning still lags.
Llama 4 Maverick reports
80.5 MMLU-Pro
; the rest of the field has not published official MMLU-Pro/AIME numbers as of writing — we're not going to fabricate them.
Hosting economics
The math has shifted. A single H100 at on-demand pricing runs ~$2-4/hr; H200 ~$3-5/hr. At sustained throughput, self-hosting beats hosted API pricing once you cross roughly:
~5M tokens/day
of consistent traffic for a single-H100 model (Llama 4 Scout, V4-Flash on a single host, Mistral Medium 3.5 on 2× H100)
~50M tokens/day
for a multi-host MoE deployment (V4 Pro, Llama 4 Maverick distributed)
Below those thresholds, hosted APIs win on TCO once you account for ops time. Mistral's
$1.5/$7.5 per M input/output
is roughly mid-market; DeepSeek V4 Pro lists at around $2.2/M tokens on Artificial Analysis. Llama 4 Maverick is quoted at
~$0.19/Mtok blended for distributed inference, $0.30-0.49 single-host
— the cheapest of the bunch if Meta's projections hold.
For a deeper dive into self-hosting tradeoffs, see
our self-hosting LLMs guide
.
Licenses + commercial use
Model
License
Commercial use
Gotchas
DeepSeek V4 (Pro + Flash)
MIT
Yes, unrestricted
None
Mistral Medium 3.5
Modified MIT
Yes
Read the modifications — minor field-of-use clauses may apply
Llama 4
Llama 4 Community License
Yes, with caveats
>700M MAU clause; attribution required; use restrictions on certain applications
Qwen 3.5 (small)
Apache-2.0
Yes
None
Qwen 3.5 (large)
Tongyi Qianwen License
Generally yes
Not OSI-approved; check size-specific terms
Gemma 4
Gemma Terms of Use
Yes
Use-policy restrictions; not OSI-approved
If your legal team requires OSI-approved licenses, your shortlist is
DeepSeek V4 (MIT)
and
small Qwen sizes (Apache-2.0)
. Everyone else ships custom licenses you'll need to read.
Decision matrix
Need 1M+ context for codebase-scale RAG?
Llama 4 Scout (10M) or DeepSeek V4 Pro (1M).
Lowest cost-per-token at scale?
Llama 4 Maverick (per Meta's own pricing projections) or DeepSeek V4 Flash.
Best coding model (SWE-Bench Verified)?
DeepSeek V4 Pro (80.6). Effectively tied: Kimi K2.6 (80.2). Runner-up: Mistral Medium 3.5 (77.6); GLM-5.1 self-reports ~77.8.
Best on the harder SWE-Bench Pro benchmark?
GLM-5.1 (58.4)
, narrowly ahead of
Kimi K2.6 (58.6)
— both open-weight models now top the closed frontier on that benchmark per
Artificial Analysis
.
Best long-horizon agent (300+ sub-agents, 4,000+ steps)?
Kimi K2.6.
Cheapest active-parameter footprint among frontier MoEs?
GLM-5.1 (40B active) or Kimi K2.6 (32B active) — both lighter to serve than DeepSeek V4 Pro’s 49B active.
EU data residency / EU vendor relationship?
Mistral Medium 3.5.
Runs on a laptop / on-device?
Gemma 4.
Best agentic tool use out of the box?
Mistral Medium 3.5 (Vibe agents with GitHub/Linear/Jira/Sentry integrations).
Strictest license requirements (OSI-approved only)?
DeepSeek V4 (MIT) or small Qwen (Apache-2.0).
Multilingual, especially CJK?
Qwen 3.5.
The hiring angle
Picking the model is the easy part. Running it in production is where teams burn six-figure quarters. Self-hosting a frontier MoE like DeepSeek V4 Pro means: provisioning multi-node H200 clusters, managing FP4/FP8 mixed-precision quantization, tuning expert routing, building a serving stack (vLLM, SGLang, or TensorRT-LLM), wiring up evals against your real workload, and operating the whole thing 24/7 with on-call rotation.
The labs that win with open weights are the ones with engineers who've shipped this before. They know that "it works on a single H100" and "it serves 200 RPS at p99 < 800ms" are very different problems. They've debugged CUDA OOMs at 3 AM. They know which inference engine handles MoE expert imbalance gracefully and which one falls over.
FAQ
Which open-weight model is closest to GPT-5.5 today?
DeepSeek V4 Pro on aggregated benchmarks, but per
NIST CAISI
, it still lags the closed frontier by roughly 8 months on Item Response Theory aggregation across 9 benchmarks.
Can I run any of these on a single H100?
Yes — Llama 4 Scout, DeepSeek V4 Flash (single host with quantization), Gemma 4, and quantized versions of Mistral Medium 3.5. Llama 4 Maverick and DeepSeek V4 Pro need multi-host setups.
Is Llama 4's Community License truly "open"?
It's source-available with commercial-use rights, but not OSI-approved. The most-cited restriction is the >700M MAU clause, which only bites hyperscalers. For most companies it's effectively open, but your legal team should review.
Why is DeepSeek V4 so much cheaper than equivalent closed models?
Three reasons: aggressive MoE sparsity (only 49B of 1.6T active per token), FP4/FP8 mixed-precision serving, and CSA/HCA attention that cuts FLOPs and KV cache. Combined, these compound into roughly 7× cheaper inference at similar capability.
Should I use V4-Pro or V4-Flash?
Flash for almost everything. DeepSeek themselves describe Flash's reasoning as "closely approaching" Pro at a fraction of the inference cost. Reach for Pro only when you need the elite math/coding ceiling.
Is Mistral Medium 3.5 production-ready four days after release?
The hosted API is. Self-hosting fresh weights always carries some risk for the first few weeks while inference engines catch up — but Mistral has a strong track record of clean releases.
What about safety and alignment?
NIST CAISI's report on DeepSeek V4 Pro flagged some safety/cyber capability gaps relative to closed frontier models. For internal/B2B use this is generally fine; for public consumer products you'll want a safety layer regardless of which model you pick.
Is the open-weights gap to closed models closing or widening?
Closing on math and coding (DeepSeek V4 Pro is within striking distance of GPT-5.5 on multiple math benchmarks). Still meaningfully open on agentic reasoning and long-horizon tasks per CAISI's PortBench and ARC-AGI-2 results.
Need engineers who can actually run these models in production?
Picking a model is a one-week decision. Operating a self-hosted LLM stack — multi-node serving, quantization, eval pipelines, on-call — is a year-long engineering investment.
Codersera
matches you with vetted remote developers who've shipped this before: ML infra, inference optimization, agentic coding harnesses, the whole stack. Start a risk-free trial and have an engineer working with your team in days, not months.
Start hiring with Codersera →

## Metadata
- **Source URL**: https://codersera.com/blog/best-open-source-llm-2026-llama-4-qwen-3-5-deepseek-v4-gemma-4-mistral/
