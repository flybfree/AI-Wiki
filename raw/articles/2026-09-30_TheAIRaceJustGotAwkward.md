---
title: The AI Race Just Got Awkward
date: 2026-09-30
url: https://insufferable.dev/posts/the-ai-race-just-got-awkward/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://insufferable.dev/posts/the-ai-race-just-got-awkward/
source_feed: Hacker News
ai_relevance: include
ai_topic: model-release
ai_reason: watchlist match: Claude Fable 5.1 / Mythos 5.1, GPT-6 Astra
scraped: 2026-09-30 11:16
---

# The AI Race Just Got Awkward

## Full Article

If you read the news headlines these days, you would be forgiven for thinking that the Western labs are getting spawn-camped by Chinese labs en masse.
The Distillation Drama
Not a week goes by when Anthropic doesnât release another article on how the
Chinese are distilling their models
,
becoming a danger to humanity itself
, etc.
Itâs beneficial for them to say that because it sets the ground for these models to be
restrained legally and regulatorily later on
.
But itâs clear that the days of mindless distilling are over.
Not just over. The new game in town is adopting Chinese labsâ advances. Note how I call this adoption instead of the more vitriol-infused âstealingâ that Anthropic tends to use.
Thatâs because, unlike the Western companies, the Chinese are pretty much giving away their recipes.
A Different Game
The latest one shamelessly copied without acknowledgement is the breakthrough in KV cache optimizations that DeepSeek has generously shared with the world.
It is a mind-blowing optimization that basically dropped the KV cache footprint for certain use cases that use a long session context, like coding, by a factor of
roughly 437x
compared with DeepSeek-V1.
They were the first ones to release the MLA architecture, which compressed the cache by roughly 15x, and then followed it up with âCompressed Sparse Attentionâ and âHeavily Compressed Attention.â The latest DeepSeek-V4.1-Flash pushes it even further with CSA2, cross-layer cache reuse, a causal encoder-decoder architecture, and FP4 caching, bringing the global KV cache down to 890 bytes per token.
Why do these things matter? Because for serving long-context models, one of the largest costs is the VRAM needed to hold this cache in GPU memory.
[437 equal-area squares shrink to one: 389.12 GB of KV cache becomes 890 MB per million tokens. Approximately 99.77% less memory.]
[437 equal-area squares shrink to one: 389.12 GB of KV cache becomes 890 MB per million tokens. Approximately 99.77% less memory.]
Below is the graph showing just how crazy this whole thing is:
[KV cache memory per million tokens: DeepSeek-V1, 389.12 GB; V3.2, 48.07 GB; V4-Flash, 3.51 GB; V4.1-Flash, 890 MB. The latest cache is 437.2 times smaller than V1.]
[KV cache memory per million tokens: DeepSeek-V1, 389.12 GB; V3.2, 48.07 GB; V4-Flash, 3.51 GB; V4.1-Flash, 890 MB. The latest cache is 437.2 times smaller than V1.]
Follow the Cache Money
Compare that with what the same tier cost roughly two months ago. All prices below are per 1 million tokens:
[Pricing per million tokens, before and after. Anthropic Opus 5 to 5.5: input $5 to $4, cache write $6.25 to $5, cache read $0.50 to $0.20, 60% cheaper. OpenAI GPT-5.6 Sol to GPT-6.1 Sol: input $5 to $2, cache write $6.25 to $2.50, cached input $0.50 to $0.10, 80% cheaper.]
[Pricing per million tokens, before and after. Anthropic Opus 5 to 5.5: input $5 to $4, cache write $6.25 to $5, cache read $0.50 to $0.20, 60% cheaper. OpenAI GPT-5.6 Sol to GPT-6.1 Sol: input $5 to $2, cache write $6.25 to $2.50, cached input $0.50 to $0.10, 80% cheaper.]
A Very Quiet Thank-You
All this must mean the Western AI companies are now extremely inference-margin positive.
The constraints on access to advanced GPUs forced Chinese labs to make performance optimization a number one goal, and it shows in the results.
Now I donât know why they would freely give away such a breakthrough, but they just did, and for once both Anthropic and OpenAI released models that are basically top-tier and are using these optimizations.
They do seem to be a little embarrassed by the copying. Hence the silent releases without much pre-announcement for both Claude Opus 5.5 and GPT-6.1 Sol.
The user reviews have been stellar w.r.t. usage, and the quality doesnât seem to be that far off compared to their flagship models (Claude Fable 5.1 and GPT-6 Astra).
The cache read costs are the proof of the adoption. They dropped sharply: Opus 5.5 cut cache-read pricing by 60% versus Opus 5, while GPT-6.1 Sol cut it by 80% versus GPT-5.6 Solâs late-July pricing.
So the Chinese labs have thrown a lifeline to the Western loss-making labs, and I just have no clue as to why.

## Metadata
- **Source**: [Original Article](https://insufferable.dev/posts/the-ai-race-just-got-awkward/)
