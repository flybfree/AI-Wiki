---
title: Goodfire says its new ‘inside-out’ monitors catch rogue AI agents at a fraction of the cost
date: 2026-10-08
url: https://techcrunch.com/2026/10/08/goodfire-says-its-new-inside-out-monitors-catch-rogue-ai-agents-at-a-fraction-of-the-cost/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://techcrunch.com/2026/10/08/goodfire-says-its-new-inside-out-monitors-catch-rogue-ai-agents-at-a-fraction-of-the-cost/
source_feed: TechCrunch AI
ai_relevance: include
ai_topic: model-release
ai_reason: watchlist match: Kimi K3
scraped: 2026-10-08 12:28
---

# Goodfire says its new ‘inside-out’ monitors catch rogue AI agents at a fraction of the cost

## Full Article

The standard way to keep an AI agent in line is to
have a second AI read over its shoulder
. It’s been the default approach, but it can get expensive fast when agents run for hours and process the equivalent of several novels’ worth of text.
Goodfire, a startup focused on interpretability (figuring out how AI models work internally), launched a cheaper option on Thursday: monitors that watch what’s happening inside an AI model as it works, rather than just reading what it writes. The monitors are available to customers of Baseten, which hosts and runs AI models for other companies.
Baseten’s Base Labs
announced a safety partnership
with Goodfire and the AI platform Hugging Face last month.
The launch comes after
a string of incidents this year
in which AI agents escaped their test environments, including OpenAI agents that
breached Hugging Face
. Kimi K3, the open model Goodfire built its first monitor around,
took advantage of a leak in its sandbox
to access the internet and information on GitHub this summer.
Goodfire’s system works a bit like airport security. Small detectors called probes read the model’s internal signals at every step of an agent’s work, the way a walk-through scanner checks every passenger. Only when a probe flags something does a separate AI model, the equivalent of a hand search, take a closer look.
Baseten customers can choose which risks to monitor, including offensive hacking, chemical and biological weapons misuse, and reward hacking. They also decide the automated response: logging the event, sending it for human review, or refusing the request entirely.
Goodfire says its approach is also cheaper to run. Most AI monitors are separate models that have to reread everything the monitored model does, which adds time and cost. Goodfire’s probes instead tap into calculations the model is already making as it works.
“Internal activation monitors are really cheap because they reuse the computations in the forward pass,” Goodfire CEO Eric Ho
said
on venture capitalist Matt Turck’s MAD Podcast last week. “So the model’s already computing this token. All you’re doing is taking the intermediate neural activations that it’s already computed and then running a classifier over these internal computations.” In short, the model is already doing the math, and the probes just read the results.
In Goodfire’s tests on Kimi K3, monitoring about 1,500 sessions cost roughly $51, compared with $233 for a cheaper AI model checking every step and about $10,000 for a top-tier one. The probes caught 94% of malicious hacking sessions and sent 8.7% of harmless ones for a second look.
Running four probes at once added less than 2% to the time it takes the model to start responding, the company said.
Image Credits:
GOODFIRE
“The great advantage is that you can catch things before they happen,” Goodfire CTO and co-founder Dan Balsam said. “We can detect when the model
might
hack during eval or training.”
The pitch is aimed at open models. Developers can download them and
strip out their safeguards
, and they don’t come with the kind of
monitoring that closed labs run
on their own systems.
“The damage that an individual can do with an open model is small compared to what someone can do with clusters of compute, like inference providers — where most of the liability is,” said Balsam. “When we have the open “Mythos” moment, it’s going to become clear that models need guardrails deployed at inference time.”
Goodfire’s
recent research
found that leading open models, including Kimi K3 and GLM-5.2, reward-hacked in 50% to 96% of runs on tests of AI agents.
Goodfire isn’t the first to try this approach. Google DeepMind said in January that its research informed the deployment of
misuse-detection probes in Gemini
.
Balsam said the monitors are the near-term piece of a longer research goal: reverse-engineering an LLM so that behavior can be traced back to where it emerged in training. “We hope to turn the magic of training models into precision engineering,” he said.
Topics
AI
,
AI agents
,
TC
When you purchase through links in our articles,
we may earn a small commission
. This doesn’t affect our editorial independence.
[Aditya Mehta]
Aditya Mehta
Editorial Fellow
Aditya Mehta is a reporter at TechCrunch covering AI. He’s supported by the Tarbell Center for AI Journalism and attended UC Berkeley. You can contact from Aditya by emailing
[email protected]
or via encrypted message at adymehta.74 on Signal.
View Bio
[Event Logo]
October 13 – 15
San Francisco
Get 50% off a second pass
The Disrupt experience is meant to be shared. Get your pass and bring a colleague, partner, or peer at 50% off. Cover more ground by making connections, building momentum, and discovering what’s next in the startup ecosystem.
BOOK NOW
Most Popular
Anthropic is giving startups a free year of Claude Team and $1,000 in credits
Russell Brandom
At 19, founder raises $11M for Ghost, maker of a $3,499 computer for personal AI
Dominic-Madori Davis
Trump unveils his new Super Intelligence Force
Anthony Ha
Federal judge calls Flock ‘indiscriminate mass surveillance’
Anthony Ha
Amazon responds to data center backlash, says it no longer uses NDAs
Anthony Ha
OpenAI safety employee resigns, claiming the company’s ‘culture is broken’
Anthony Ha
Meta wants your next gadget to be Muse-infused
Kirsten Korosec

## Metadata
- **Source**: [Original Article](https://techcrunch.com/2026/10/08/goodfire-says-its-new-inside-out-monitors-catch-rogue-ai-agents-at-a-fraction-of-the-cost/)
