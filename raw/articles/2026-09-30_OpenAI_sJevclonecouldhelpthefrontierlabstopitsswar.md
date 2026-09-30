---
title: OpenAI’s Jev clone could help the frontier lab stop its swarming agents
date: 2026-09-30
url: https://techcrunch.com/2026/09/30/openais-jev-clone-could-help-the-frontier-lab-stop-its-swarming-agents/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://techcrunch.com/2026/09/30/openais-jev-clone-could-help-the-frontier-lab-stop-its-swarming-agents/
source_feed: TechCrunch AI
ai_relevance: include
ai_topic: model-release
ai_reason: watchlist match: GPT-6 Astra, Jev
scraped: 2026-09-30 15:14
---

# OpenAI’s Jev clone could help the frontier lab stop its swarming agents

## Full Article

One of the more intriguing announcements at
OpenAI’s Dev Day event
on Tuesday came in an aside from CEO Sam Altman, who revealed the company’s new “Decisions API.”
The API apparently provides similar functionality to
Jev
, a
model released by TypeSafe AI
earlier this month that’s explicitly designed for software automation. A kind of super-powered classifier built on an LLM, developers can give Jev a set of choices that it outputs as probabilities cheaply and at high speeds.
OpenAI’s Decisions API seems to be the same sort of product. At the event, Altman described the API as a way to give the lab’s Luna model a predefined set of options to choose between, such as categories in which to classify an image or different agent behaviors.
“By focusing the model on that choice, we can make it extremely fast while keeping capabilities like image understanding, broad language support, and safety protections,” Altman said.
TypeSafe didn’t respond to TechCrunch’s questions about the new product, but CEO Diogo Almeida, a former OpenAI engineer who co-invented reinforcement learning,
joked on X
about the beginning of the clone wars.
He added that OpenAI’s interest could be “a sign…that building in a System One compatible way is the future.” (“System One” is TypeSafe’s term of art for fast, intuitive thinking, versus “System 2,” which it applies to deliberate reasoning.)
The subtext here is that LLMs as we know them aren’t the right solution for a lot of software because they are comparatively slow and expensive. Developers have been using Jev to augment LLMs and, in doing so, have
found
that they’re faster and cheaper.
It’s not clear how similar Decisions API will be to Jev, since OpenAI released it as a limited preview and, thus far, TechCrunch hasn’t spotted developers running it through its paces. However, there is
clearly interest
, according to the conversations on X.
Decisions API isn’t the only Jev-like API on the internet — other startups are rolling out similar models; OpenAI won’t be the last tech giant to produce one. A key question is how well calibrated each of these decision models’ outputs will be to real life.
Almeida says his company’s moat is the synthetic data it creates to generate statistically useful outputs.
“Fast and cheap is very easy, you know,” Almeida
told TechCrunch
last week. “If you want it really fast and cheap, use dice, right? Intelligence is the hard part, and my North Star is always pushing the intelligence-per-dollar Pareto curve.”
After just weeks, it seems clear that these models have a future ahead of them, and one likely application is monitoring and securing AI agents. One of OpenAI’s new security measures following a series of incidents where its agents misbehaved on the open internet is using a separate model to watch for bad actions at “significant compute cost.”
Shapor Naghibzadeh, a long-time cybersecurity professional who leads the startup QueryStory, thinks that a model like Jev could make that possible far more cheaply.
He built
a demo
for a
hackathon
held last weekend that uses Jev to check each agentic action against the task it was given, blocking actions it had high confidence were bad, flagging others for review, and permitting the rest.
In theory, such monitoring could have stopped the Hugging Face incident — and monitoring of that kind costs $2.94 with Jev, versus $372 with a frontier LLM.
A key observation is that Jev is arguably cheap enough to run on every agentic action, which offers a layer of review that could improve the reliability of agents writ large. It’s the kind of thing TypeSafe was hoping to achieve — and now OpenAI has seen the value as well.
Topics
AI
,
OpenAI
When you purchase through links in our articles,
we may earn a small commission
. This doesn’t affect our editorial independence.
[Tim Fernholz]
Tim Fernholz
Senior Reporter
Tim Fernholz is a journalist who writes about technology, finance and public policy. He has closely covered the rise of the private space industry and is the author of
Rocket Billionaires: Elon Musk, Jeff Bezos and the New Space Race.
Formerly, he was a senior reporter at Quartz, the global business news site, for more than a decade, and began his career as a political reporter in Washington, D.C. 

You can contact or verify outreach from Tim by emailing tim.fernholz@techcrunch.com or via an encrypted message to tim_fernholz.21 on Signal.
View Bio
[Event Logo]
October 13 – 15
San Francisco
Get 50% off a second pass
The Disrupt experience is meant to be shared. Get your pass and bring a colleague, partner, or peer at 50% off. Cover more ground by making connections, building momentum, and discovering what’s next in the startup ecosystem.
BOOK NOW
Most Popular
AMD will acquire Fei-Fei Li’s World Labs for $8.2B
Tim Fernholz
Viral AI agent Instinct raises $1B Series C at a $10B valuation
Sarah Perez
Crusoe abandons $1.25B plan to use Boom turbines at AI data centers
Kirsten Korosec
Astra and Opus just passed Turing’s other test
Tim Fernholz
Waymo is scaling fast: Here’s what the fleet data shows
Kirsten Korosec
Oracle sends force majeure notice on its New Mexico Stargate data center
Aditya Mehta
Meta’s Muse Charm looks like a Tamagotchi, but it’s tapping into a much newer trend
Sarah Perez

## Metadata
- **Source**: [Original Article](https://techcrunch.com/2026/09/30/openais-jev-clone-could-help-the-frontier-lab-stop-its-swarming-agents/)
