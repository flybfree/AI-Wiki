---
title: Rogue AI agents created fake online identities in another hacking attempt
date: 2026-08-05
url: https://www.theverge.com/ai-artificial-intelligence/975577/aisi-openai-anthropic-agent-hacking
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.theverge.com/ai-artificial-intelligence/975577/aisi-openai-anthropic-agent-hacking
source_feed: The Verge AI
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-08-05 21:21
---

# Rogue AI agents created fake online identities in another hacking attempt

## Full Article

AI
News
Tech
Rogue AI agents created fake online identities in another hacking attempt
AISI said AI agents from OpenAI and Anthropic displayed unprecedented ‘autonomy and deception’ in their test.
AISI said AI agents from OpenAI and Anthropic displayed unprecedented ‘autonomy and deception’ in their test.
by
Robert Hart
Aug 5, 2026, 3:14 PM UTC
Link
Share
Gift
[STK485_STK414_AI_SAFETY_A (1)]
[STK485_STK414_AI_SAFETY_A (1)]
Image: The Verge
[Robert Hart]
Robert Hart
is a London-based reporter at
The Verge
covering all things AI and a Senior Tarbell Fellow. Previously, he wrote about health, science and tech for
Forbes
.
Yet more rogue AI agents from OpenAI and Anthropic have been caught attempting to hack real targets online without permission. The discoveries add to a
growing
list of previously unknown
incidents
that have
alarmed AI safety experts
and intensified pressure for greater oversight of frontier systems.
According to a
report
from the UK’s AI Security Institute, which evaluates frontier models from top AI labs before they are released, agents powered by OpenAI’s GPT-5.6-Sol and Anthropic’s Mythos 5 went “engaged in sustained, potentially harmful activity directed at real people and organisations.” This included trying to insert malicious code into an open-source project by pressuring real people in charge of it, AISI said. “In an attempt to get the code approved, the agent engaged in social engineering — creating fake online identities and using them to pressure the project’s maintainer to approve the code.”
AISI said the attempts, which it detected on July 28th, “were unsuccessful” and had not resulted in real-world harm. However, the organization noted that the incident marked “the first time we have seen risks around autonomy and deception manifest this clearly, without specific prompting, in the real-world.”
Unlike OpenAI’s rogue agent that
attacked
Hugging Face, AISI said this was “not a case of a model escaping its secure test environment,” or sandbox. Safeguards usually imposed on the models had been disabled as part of testing, AISI said, and they had also been permitted access to the internet. “To measure what these models can genuinely do, we test them under conditions that reflect what a capable human attacker could do,” AISI said.
Related
Anthropic says Claude accidentally hacked real companies too
OpenAI’s rogue AI agent didn’t stop at hacking Hugging Face
We’re running out of reasons to ignore AI safety
The incident stemmed from a single AISI evaluation where agents were tasked with solving a cybersecurity challenge, such as finding a piece of protected data. The challenge was run 122 times across multiple models and all runs were conducted in AISI’s research environment, which uses “virtual machine sandboxing to isolate the agents from other AISI infrastructure.” AISI’s investigation found that in 10 of those, “an AI agent took autonomous, unsanctioned action on the live internet, targeting real people and organisations.” Of 19 such actions, almost all — 17 — came from Anthropic’s Mythos 5.
In its post-mortem of the incident, AISI identified several key factors it said contributed to the unsanctioned agent behaviors. It said the agent was persistent, pursuing avenues like trying to trick real people through “deception that, until recently, had been largely theoretical.” The task was also hard, which the organization said could push agents to be more “creative” in their problem-solving. Compounding matters were deficiencies in how internet use was monitored, with AISI suggesting that more dedicated surveillance could have identified the problem sooner. Finally, the organization said the agent hadn’t been specifically instructed
not
to leverage its internet access or deploy deceptive social engineering techniques in pursuit of its goal. “Previously, it was not clear that such instructions were necessary when using models with alignment training,” AISI said.
AISI said the incident should be “interpreted with caution and nuance” but warned the agent’s actions “show signs of novel, potentially deceptive behaviours” that “were to an extent and severity we did not anticipate.”
In a blog
post
, OpenAI acknowledged the breach that happened during AISI’s testing and said it is “committed to working across the industry to strengthen shared practices for conducting high-risk evaluations safely.” OpenAI also disclosed another breach, this time from an external cybersecurity testing partner Irregular, where it said models had been mistakenly granted internet access during cybersecurity exercises. OpenAI said Irregular notified it of the breach on July 29th.
“In the coming weeks, we will review our own approach to third-party testing, including how we identify higher-risk evaluations, agree on scope, assess requests to enable internet access or lowered safeguards, set expectations for isolation, credential handling, monitoring, and stop conditions, and establish clearer incident-notification and escalation processes,” OpenAI said.
Related
Nvidia, Microsoft launch open AI security alliance — without OpenAI, Google, or Anthropic
Trump’s AI testing plan is limited and vague
Anthropic posted a less comprehensive
response
on X, largely emphasizing that the models’ standard safety features had been disabled and that they had not been given “any specific restrictions on how the internet should be used.” It said it was working closely with AISI to gather more details for its own investigation.
The findings add to an increasingly tangled mess of rogue actions from agents during testing, many of which only come to light after dedicated hunting and which feature models not released to the public. The unwillingness or inability of AI labs to contain their products has sparked concern over how such breaches could go unnoticed, the
safety of frontier AI systems
, and worries over the general lack of transparency and oversight the industry faces. These latest disclosures will likely intensify pressure on the federal government for a more comprehensive framework governing AI models following what reports suggest is a
vague and poorly-defined testing plan
from the Trump administration, and could add to growing calls for some form of
slowdown
or pause on AI development.
Follow topics and authors
from this story to see more like this in your personalized homepage feed and to receive email updates.
Robert Hart
AI
Anthropic
News
OpenAI
Security
Tech
Most Popular
Most Popular
SpaceX is coming for T-Mobile, AT&T and Verizon
How an OpenAI influencer trip backfired
Don’t screw this up, Marvel
SpaceX is barely Space and mostly X
Google Assistant will disappear from your phone next month
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
- **Source**: [Original Article](https://www.theverge.com/ai-artificial-intelligence/975577/aisi-openai-anthropic-agent-hacking)
