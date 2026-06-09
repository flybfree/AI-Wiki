---
title: New LLM Releases April 2026: Every Major Model Launch This Month - Fazm Blog
date: 2026-05-19
url: https://fazm.ai/blog/new-llm-releases-april-2026
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://fazm.ai/blog/new-llm-releases-april-2026
scraped: 2026-05-19 00:00
---

# New LLM Releases April 2026: Every Major Model Launch This Month - Fazm Blog

## Full Article

M
Matthew Diakonov
,
Written with AI
·
Published
April 11, 2026
·
9 min read
Update, May 13
Looking back from mid-May: Spud landed on April 23, but OpenAI relabelled it as GPT-5.5, not GPT-6. Three variants shipped (GPT-5.5, GPT-5.5 Thinking, GPT-5.5 Pro) with API prices doubled (Thinking $5 in / $30 out, Pro $30 in / $180 out). The 1M context window is real in the API; Codex caps at 400K. 88.7% on SWE-Bench Verified, 82.7% on Terminal-Bench 2.0, MRCR v2 at 1M jumped from 36.6% to 74.0%. True GPT-6 has no architecture, no parameter count, and no date. The April 30 retirement of the 1M context beta on Claude Sonnet 4.5 / Sonnet 4 has now landed; if you were on the beta, you should already have migrated to Sonnet 4.6 or Opus 4.6.
For readers on macOS
Skip the roundup, plug any of these models into a real Mac agent.
Fazm is a local, open-source computer-use agent. Bring your own API key for GPT-5.5, Claude, Gemma 4, GLM-5.1, or point it at a local model. Voice-first, works on the apps you already use.
Download for macOS
Free, macOS 14+, no credit card. Source at
github.com/m13v/fazm
.
Quick Reference: April 2026 LLM Releases
Model
Company
Release Date
Parameters
Context
License
Pricing /1M tokens
GPT-5.5 (Spud)
OpenAI
Apr 23
Undisclosed
1M (400K in Codex)
Proprietary
$5 in / $30 out
GPT-5.5 Pro
OpenAI
Apr 24 (API)
Undisclosed
1M
Proprietary
$30 in / $180 out
Claude Mythos
Anthropic
Apr 7 (preview)
Undisclosed
TBA
Proprietary (gated)
$25 in / $125 out
Gemma 4 31B
Google
Apr 2
31B dense
256K
Apache 2.0
Free (open weights)
Gemma 4 26B MoE
Google
Apr 2
26B MoE
256K
Apache 2.0
Free (open weights)
Gemma 4 E4B
Google
Apr 2
~4B effective
256K
Apache 2.0
Free (open weights)
Gemma 4 E2B
Google
Apr 2
~2B effective
256K
Apache 2.0
Free (open weights)
GLM-5.1
Zhipu AI
Early Apr
744B MoE (40B active)
200K
MIT
Free (open weights)
Qwen 3.6-Plus
Alibaba
Early Apr
Undisclosed
1M
Open
Free (open weights)
Llama 4 Scout
Meta
Apr (rolling)
Undisclosed
10M
Llama License
Free (open weights)
Llama 4 Maverick
Meta
Apr (rolling)
400B
1M
Llama License
Free (open weights)
Arcee Trinity
Arcee AI
Early Apr
400B
TBA
Apache 2.0
Free (open weights)
Want the link by email?
Get a one-click macOS install of Fazm sent to your inbox.
Free, open source, runs locally. Plug in any of the keys above (GPT-5.5, Claude, Gemma 4, GLM-5.1, Llama 4) and it drives your real Mac. On Windows or Linux? We will email you when it lands.
Subscribe and download
No spam. We send the download link, then leave you alone.
GPT-5.5 ("Spud"): What Actually Shipped on April 23
OpenAI originally framed Spud as GPT-6, with an April 14 launch date. Spud actually landed nine days late on April 23, and OpenAI relabelled it as GPT-5.5. The reading among partners is that the gap over GPT-5.4 (released March 5) was meaningful but not generation-defining, and that the version-number conservatism is consistent with how OpenAI now frames progress around incremental capability gains rather than major leaps. True GPT-6 has no architecture, no parameter count, and no date.
What actually shipped, as of mid-May:
Three variants in a single rollout.
GPT-5.5 (standard), GPT-5.5 Thinking, and GPT-5.5 Pro went live April 23 in ChatGPT and rolled into the API on April 24. Pro is gated to Pro, Business, and Enterprise tiers.
Pricing doubled.
GPT-5.5 Thinking lists at $5 input / $30 output per million tokens, up from GPT-5.4's $2.50 / $15. GPT-5.5 Pro lists at $30 / $180. The Batch and Flex tiers cut 50%; Priority adds 150% on top. The price hike is the sharpest in the GPT-5.x line and ends the year-long downward trend in frontier-model cost per token.
1M token context in the API, 400K in Codex.
Not the 2M figure that leaked from partner briefings in early April. The 400K Codex cap is the practical ceiling for whole-codebase workflows.
88.7% SWE-Bench Verified, 82.7% Terminal-Bench 2.0.
Intelligence Index of 59, second only to Grok 5 in published third-party rollups. The headline result is on long context: MRCR v2 at 1M tokens jumps from GPT-5.4's 36.6% to 74.0%, and at 128K to 256K tokens it scores 87.5% versus Claude's 59.2%.
Super-app remains the strategic story.
GPT-5.5 is the engine OpenAI is pointing at the merge of ChatGPT, Codex, and the Atlas browser into a single desktop surface. The 1M context plus the recall numbers make a credible argument for that direction.
Practical read:
GPT-5.5 Thinking is the new frontier default if you can absorb the doubled cost and your workload benefits from the long-context jump. For everyday agent work where tool-call latency dominates, GPT-5.4 stays competitive and is now meaningfully cheaper than its successor. Claude Opus 4.6 and GLM-5.1 still hold their ground on coding-heavy benchmarks; the field is no longer two horses.
Claude Mythos: Anthropic's Gated Preview
Anthropic announced Claude Mythos Preview on April 7, available exclusively through Project Glasswing to roughly 50 partner organizations. The focus is on cybersecurity vulnerability detection, reasoning, and coding.
Mythos is described as a step change above Claude Opus 4.6, which has been the top-performing model on many benchmarks since its February 2026 release. Preview pricing is steep at $25/$125 per million input/output tokens, reflecting the gated early-access nature of the program.
No public release date has been announced. For most developers, Claude Opus 4.6 and Sonnet 4.6 remain the current Anthropic options.
Google Gemma 4: Open-Source Gets Serious
Google released the Gemma 4 family on April 2 under Apache 2.0, delivering four models purpose-built for different deployment scenarios:
Gemma 4 31B Dense
the flagship, with benchmark scores that outperform models 20 times its size
Gemma 4 26B MoE
mixture-of-experts variant for efficient inference
Gemma 4 E4B
consumer GPU and edge deployment
Gemma 4 E2B
smartphones and Raspberry Pi devices
All four models support 256K context windows, native vision and audio processing, and fluency in over 140 languages. They are purpose-built for advanced reasoning and agentic workflows.
With over 400 million cumulative Gemma downloads, this release under Apache 2.0 (upgraded from earlier, more restrictive licenses) represents a strategic shift in Google's open model approach.
Context Window Comparison (tokens)
Llama 4 Scout (10M)
10,000,000
GPT-5.5 (1M)
1,000,000
Llama 4 Maverick (1M)
1,000,000
Qwen 3.6-Plus (1M)
1,000,000
Gemma 4 (256K)
256,000
GLM-5.1 (200K)
200,000
Proprietary
Open weights
Zhipu GLM-5.1: China's MIT-Licensed Giant
Zhipu AI released GLM-5.1 under the MIT license, a 744-billion parameter mixture-of-experts model with 40 billion parameters active per forward pass and a 200K context window.
The headline claim: on SWE-Bench Pro, GLM-5.1 reportedly beat both Claude Opus 4.6 and GPT-5.4. Alongside GLM-5.1, Zhipu also released GLM-5V-Turbo, a multimodal variant optimized for coding tasks.
The MIT license makes this one of the most permissive releases of a frontier-scale model to date. No usage restrictions, no registration required.
Alibaba Qwen 3.6-Plus: 1M Context for Agents
Alibaba's Qwen 3.6-Plus targets agentic coding workflows with a 1 million token context window. The model is designed for tasks that require understanding and modifying large codebases in a single pass.
This positions Qwen 3.6-Plus as a direct competitor to Claude Opus 4.6 and GPT-5.4 for the growing market of AI-powered coding agents.
Meta Llama 4: The 10M Token Context Window
Meta's Llama 4 family includes two headline models:
Llama 4 Scout
with a 10 million token context window, the largest of any model released this month
Llama 4 Maverick
with 400 billion parameters, 1 million token context, and native multimodal capabilities
Both models use a mixture-of-experts architecture and are natively multimodal from training (not bolted-on vision after the fact). Meta is using controlled licensing agreements for Llama 4, distinguishing its approach from fully permissive open-source releases.
Arcee Trinity: 400B Under Apache 2.0
Arcee AI released Trinity, a 400 billion parameter model under Apache 2.0. Trinity is designed for enterprise use cases where teams need a large, capable model they can run and modify without licensing restrictions.
Which Model Should You Actually Pick This Month?
With Spud shipped and the open-weight side of the field crowded, which one do I use today is the question that matters more than the headline benchmark numbers. Practical picks by use case, as of mid-May:
Long-context coding (whole-codebase analysis, multi-file refactors).
GPT-5.5 Thinking is the new frontier default; the MRCR v2 jump from 36.6% to 74.0% at 1M tokens makes whole-repo passes meaningfully more reliable, but the price doubled. Claude Opus 4.6 still wins on procurement and steady tool-call behaviour. GLM-5.1 is the value pick if you want frontier-level capability at open-weight cost. Qwen 3.6-Plus is a strong tool-calling alternative with a 1M context and a different token bias.
Local model on a Mac.
Gemma 4 31B Dense for any machine with 64GB+ unified memory (M3 Max, M4 Pro/Max). Drop to Gemma 4 26B MoE on 36-48GB. E4B and E2B are the picks for 16-24GB MacBook Airs; both run at usable speeds via mlx and llama.cpp. Llama 4 Scout is the one to load when you need the 10M context for a single document and can absorb the disk footprint.
Agentic browser and desktop work.
Tool-call reliability and latency matter more than raw IQ here. Claude Opus 4.6 and GPT-5.4 still lead on per-call reliability for production agents, and GPT-5.4 is now the cheaper-than-its-successor sweet spot. GPT-5.5 Thinking helps when a single task spans more than a handful of tool calls. GLM-5.1 is competitive enough to A/B on your real workflows. The harness matters more than the model. Fazm's custom API endpoint accepts any of these, so you can swap GPT-5.4 for GPT-5.5 Thinking or GLM-5.1 mid-task and watch the failure rate change in place.
Privacy-sensitive workflows (legal, medical, internal HR data).
Local Gemma 4 31B Dense or Llama 4 Maverick via Ollama or LM Studio. The cost stops scaling with usage the moment you stop paying per million tokens, which makes large-volume document review and inbox triage economically reasonable for the first time. The GPT-5.5 price hike makes this calculus more obvious, not less.
Frontier reasoning, "I just need the smartest thing in the room."
GPT-5.5 Pro at $30/$180 if cost is no object and you want the highest published Intelligence Index outside Grok 5. Claude Opus 4.6 for steady-state work. Claude Mythos is still Glasswing-partners-only with no public timeline, and the $25/$125 preview pricing is not the everyday-default tier.
ChatGPT-Atlas-style "browse + code + converse" super-app.
GPT-5.5 is the engine OpenAI is pointing at this surface. The architecture story is now real, but the migration cost is real too: at $5/$30 you should profile your actual token mix before assuming the doubled price is paid back by the long-context performance.
What This Means for Developers
The open-source gap is closing fast
Three months ago, proprietary models held a clear lead on reasoning and coding benchmarks. In April 2026, GLM-5.1 claims to beat the best proprietary models on SWE-Bench Pro, and Gemma 4's 31B dense model outperforms models 20x its size. The cost advantage of running open weights on your own infrastructure keeps growing.
Context windows are no longer a differentiator
When the smallest context window in this list is 200K tokens and the largest is 10M, context length alone is not a selling point. The question shifts to how well models actually use long contexts. Retrieval accuracy at 1M+ tokens matters more than the raw number.
Agent capabilities are the new battleground
Every release this month emphasizes agent workflows: GPT-5.5 explicitly aims at the ChatGPT-Codex-Atlas super-app merge, Gemma 4 ships an agentic design out of the box, Qwen 3.6-Plus targets coding agents with a 1M context. If you are building AI products, agent reliability (tool calling accuracy, multi-step planning, error recovery) is now the primary differentiator between models.
The catch is that none of these models do anything useful sitting in a chat window. They need an agent loop, a tool layer, and a surface to actually act on. For anything that touches a real desktop (opening a browser tab, editing a Google Doc, filling a CRM, moving files between apps), that layer has to live on the machine. Browser-only agents and cloud sandboxes cover a small slice of what most small businesses actually do in a day.
Pricing compression broke this month
For a year, the frontier price-per-token line went one way: down. GPT-5.5 reversed it. Thinking went from $2.50/$15 on GPT-5.4 to $5/$30, the sharpest single-release hike in the GPT-5.x line. Pro debuted at $30/$180. The justification is the long-context recall jump (MRCR v2 36.6% to 74.0% at 1M tokens), but the message to anyone running production workloads is clear: do not assume the next major model will cost less than the last.
The flip side is that open-weight cost did not move. Gemma 4, GLM-5.1, Qwen 3.6-Plus, Llama 4, Arcee Trinity are still free to run on hardware you already own. The relative case for running locally on a Mac just got stronger, not weaker. Whole-codebase analysis, document processing at scale, and batch inbox triage stay economically reasonable for small teams; the proprietary tier of the same workloads got more expensive on April 23.
model-agnostic
“
A 1M token context window and 95% HumanEval do not matter if the thing cannot open your browser, read your screen, and click the right button.
”
The harness matters more than the model
Running Any Of These Models On Your Mac
If you are reading this list trying to pick which model to actually use for day-to-day work, the blocker is almost never the model. It is the harness. A 1M token context window and 95% HumanEval do not matter if the thing cannot open your browser, read your screen, and click the right button.
Fazm is the macOS-side answer to that harness problem. It is a local computer-use agent that drives your actual Mac through the accessibility APIs (not screenshots), and it is model-agnostic:
Point it at any of the models in this post.
Fazm supports custom API endpoints, so you can route through GPT-5.5 Thinking, Claude Opus 4.6, a local Gemma 4 31B, or a GLM-5.1 instance hosted behind a corporate proxy. Same agent, different backend. Swap mid-task to A/B failure rates on your real workflow.
It works on the apps you already use.
Browser, Google Docs, Sheets, Calendar, your CRM, your invoicing tool, Mail, the Finder. Not a headless Chromium in a data center.
Voice-first.
You describe what you want and it does it. No prompt engineering chat loop.
Fully open source, runs locally.
Source is at
github.com/m13v/fazm
. Your screen and mic never leave your machine unless you explicitly point it at a hosted model.
It runs on macOS 14 or newer. Native Swift/SwiftUI, no terminal required.
Fazm - free, open source, local
Point any of these models at a real Mac and watch it do the work.
Native computer-use agent for macOS. Custom API endpoint field accepts GPT-5.5, Claude, Gemma 4, GLM-5.1, Llama 4, or any Anthropic-compatible gateway. Voice-first. Drives your real browser, Google Docs, Sheets, CRM, Mail, Finder through accessibility APIs - not screenshots.
- 10x faster than screenshot agents (skips the vision round-trip)
- Nothing leaves your machine unless you explicitly point it at a hosted model
- macOS 14+, native Swift/SwiftUI, no terminal required
Send me the macOS download link.
We email a one-click install. On Windows or Linux? Same form, you get on the launch list.
Subscribe and download
View source on GitHub →
or
Skip the email, download directly →
Why the harness matters more than the model
Every new benchmark in the tables above is measured in a sanitized sandbox. The moment you point a model at a messy real desktop, the failure modes change. Latency shifts to accessibility-tree queries and app focus transitions, not token generation. Errors cluster around stale UI state, modal dialogs, and half-loaded pages, not reasoning. A model that wins SWE-Bench Pro can still fail to close a Zoom notification blocking the Send button.
The practical bottleneck for small-business automation right now is whichever agent loop plus accessibility plumbing handles those failure modes most gracefully. That is what Fazm optimizes for. The model is a swappable component.
Looking Ahead From Mid-May: What Is Still Pending
Closed and open items now that the dust has settled:
GPT-5.5 (Spud) shipped April 23
, but as a 5.5 not a 6. True GPT-6 has no architecture paper, no parameter count, no pricing, no date.
Grok 5
from xAI is still in active training on Colossus 2. Public-beta consensus is late Q2 or Q3 2026; prediction markets give roughly a 33% chance of shipping by June 30. xAI's last on-record update was the January 28 Series E announcement.
Claude Mythos
remains gated to the Project Glasswing cohort with no public availability timeline. Anthropic has expanded the technical write-up at red.anthropic.com but has not committed to a wider release window.
The
1M token context window beta
for Claude Sonnet 4.5 and Sonnet 4 retired on April 30. Sonnet 4.6 and Opus 4.6 are the migration targets; anything still on the beta should be moved this month.
April 2026 is the month frontier pricing turned the other way for the first time in a year, and the month open-weight credibility finally caught up on coding benchmarks via GLM-5.1. The volume of shipped models means developers have more genuinely frontier-tier options at a wider cost spread than at any prior point. The best time to evaluate which one fits your use case is now, while the field is fresh and the pricing pages are still settling.
If you want to evaluate them actually doing things on your Mac (not in a chat window),
grab Fazm for free
. Plug in whichever of these models you are curious about and point it at a real workflow you would normally do by hand, invoicing, CRM updates, inbox triage, scheduling. That is the honest benchmark.
Related reading
Keep reading
Architecture
Accessibility APIs vs screenshots for computer control
Why accessibility-tree dispatch beats pixel-based screenshot agents on latency, accuracy, and cost.
Read
Comparison
AI agents vs copilots: when each wins
Side-by-side on the workflows that actually need an autonomous loop versus inline assistance.
Read
Long context
Does a 1M token context window actually work?
Recall accuracy at 1M tokens is the open question, not the marketing number on the spec sheet.
Read
Agents
Does a 3-tool-call problem still matter in 2026?
Tool-call reliability and latency dominate whether an agent is usable, more than raw model IQ.
Read

## Metadata
- **Source URL**: https://fazm.ai/blog/new-llm-releases-april-2026
