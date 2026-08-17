---
title: Anthropic explains how Claude&#8217;s invisible text watermarks will work
date: 2026-08-17
url: https://www.theverge.com/ai-artificial-intelligence/980869/anthropic-claude-watermarks-synthid-text-system
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.theverge.com/ai-artificial-intelligence/980869/anthropic-claude-watermarks-synthid-text-system
source_feed: The Verge AI
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-08-17 06:05
---

# Anthropic explains how Claude&#8217;s invisible text watermarks will work

## Full Article

AI
News
Tech
Anthropic explains how Claude’s invisible text watermarks will work
﻿It’s using ‘a version’ of the open-source SynthID-Text system Google developed.
﻿It’s using ‘a version’ of the open-source SynthID-Text system Google developed.
by
Jess Weatherbed
Aug 17, 2026, 10:57 AM UTC
Link
Share
Gift
[STKB364_CLAUDE_2_C_96d15c]
[STKB364_CLAUDE_2_C_96d15c]
Image: Cath Virginia / The Verge, Getty Images
[Jess Weatherbed]
Jess Weatherbed
is a news writer focused on creative industries, computing, and internet culture. Jess started her career at TechRadar, covering news and hardware reviews.
Anthropic has clarified how it’s planning to apply invisible watermarks to Claude-generated text in order to comply with Europe’s AI transparency rules. On Friday,
Anthropic announced
that Claude’s text marking system is “a version of the SynthID-Text approach” — an open-source watermarking technology
developed by Google DeepMind
that creates detectable patterns using wording probabilities.
This watermarking feature,
alongside C2PA support
for Claude-processed images, is being introduced to meet Anthropic’s obligations under the
European Union’s AI Act
, which requires synthetic audio, image, video, and text to include machine-readable marks that enable the content to be detected as artificially generated or manipulated. Anthropic says the text watermarks won’t make Claude more expensive for users, or “have any practical impact on the quality or content of Claude’s outputs.” Here’s Anthropic’s explanation for how it works:
Take the sentence “The weather today was cold and…”. The next word is very unlikely to be “sugary.” But it is quite likely to be “overcast” or “grey.” Under most circumstances, it doesn’t matter much to the reader which of these latter two words the model ultimately chooses—the meaning of the sentence is largely the same either way. In cases like this, the choice is settled by a random number.
Watermarking uses low-stakes choices like these—which occur many times over a piece of generated text—to leave a pattern in Claude’s responses. That pattern is undetectable to the reader, but is detectable to anyone who has a key that encodes it. When watermarking is used, choices are still made at random, but the source of the randomness is different. Instead of using an arbitrary random number generator to pick the next word, watermarking uses the key and a few words that come before to settle what word the model should pick.
As Anthropic notes, the EU’s AI transparency requirements also impact other major AI developers, so Claude won’t be the only model introducing text watermarks. Google’s Gemini chatbot has supported the
SynthID Text solution since 2024
, and while OpenAI hasn’t detailed any
text watermarking plans
for ChatGPT in its
AI Act compliance roadmap
, it will also be subject to the law’s requirements.
Follow topics and authors
from this story to see more like this in your personalized homepage feed and to receive email updates.
Jess Weatherbed
AI
Anthropic
News
Tech
Most Popular
Most Popular
Flock CEO: ‘We got this one wrong’
I finally found a magnetic phone grip I never want to remove
ChatGPT’s Computer History tracks your clicks and keystrokes
OpenAI reportedly disbanded its preparedness team
Marvel reveals the new X-Men cast, including Inde Navarrette and Adam Driver
The Verge Daily
A free daily digest of the news that matters most.
Email (required)
Sign Up
By submitting your email, you agree to our
Terms
and
Privacy Notice
.
This site is protected by reCAPTCHA and the Google
Privacy Policy
and
Terms of Service
apply.
Advertiser Content From
[Sponsor Logo]
This is the title for the native ad
[Sponsor thumbnail]

## Metadata
- **Source**: [Original Article](https://www.theverge.com/ai-artificial-intelligence/980869/anthropic-claude-watermarks-synthid-text-system)
