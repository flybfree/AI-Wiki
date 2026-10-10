---
title: Anthropic can’t reliably control its AI agents. It’s cutting off its internal evals from the live internet instead
date: 2026-10-10
url: https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/
source_feed: TechCrunch AI
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-10-10 00:06
---

# Anthropic can’t reliably control its AI agents. It’s cutting off its internal evals from the live internet instead

## Full Article

Anthropic said its models exploited websites on the internet, including some run by U.S. government agencies, and it will turn off live internet access for all of its internal evaluations until the frontier lab is sure it can monitor and control its AI agents.
The incidents, disclosed in a
blog post
, involved AI agents
tasked to solve problems
seeking resources on the internet. In the process, they exploited software flaws, accessed databases without paying fees, used URL shortening services to smuggle information pass restrictions, and even
submitted
a false murder tip to the Philadelphia police.
Anthropic said it discovered these new issues in a review of its model’s activities that began in July, demonstrating the lab’s lack of awareness of its software’s behavior in real time.
Notably, the company said that alignment training was not yet sufficient for skills like search and computer use that are central to its pitch that AI agents will be used by any professional who relies on digital tools.
The behaviors Anthropic disclosed are similar to incidents involving OpenAI agents that
collaborated
to break into various websites in search of information, including some run by the Australian government.
Anthropic previously disclosed that its models had
broken into
external systems. The frontier lab said it considered today’s disclosures “significantly less severe from an alignment and security perspective” than those it announced before.
However, the lab still said it had “turned off live internet access” for “all our internal evaluations” until it is certain it can monitor and control its agents.
It’s not clear what that means. Sydney Von Arx, the founder of Nightingale, an AI safety organization, told TechCrunch in an interview before this disclosure that developing models on a data center cut off from the open internet would be very challenging for researchers, and hinder the progress of the models, which benefit from internet access.
“You have to align them at some point,” Von Arx said. “If the AIs are released to production and never have access to the internet, that’s not a very useful tool.”
Anthropic said the behavior was a result of flaws in the lab’s training environments, which led the models to believe they would be rewarded for finding loopholes or avoiding restrictions, a behavior called “reward hacking.”
The company said it would stop running some of its evaluations or move them offline, and has built tooling to detect and block this behavior. This tooling was tested against the kind of incidents disclosed today and blocked them; it’s not clear what evidence will prompt Anthropic to return live internet access to its internal evaluations. Anthropic also said it would migrate its internal AI agents to “centrally managed infrastructure with strong containment,” and is beginning to using safety classifiers more frequently to monitor those agents.
“It’s encouraging that Anthropic voluntarily disclosed more recent incidents, including where their agents targeted U.S. government websites,” Conrad Stosz, an official at AI oversight lab Transluce and former head of the US Center for AI Standards and Innovation, said in a statement. “But it just underscores the need for independent, credible, third-party verification of Al systems. Trust in this technology needs to be built through science-backed oversight and governance with meaningful access — not by relying on researchers to find these things in the wild or on companies to voluntarily disclose.”
Topics
AI
When you purchase through links in our articles,
we may earn a small commission
. This doesn’t affect our editorial independence.
[Tim Fernholz]
Tim Fernholz
Senior Reporter
Tim Fernholz is a journalist who writes about technology, finance and public policy. He has closely covered the rise of the private space industry and is the author of
Rocket Billionaires: Elon Musk, Jeff Bezos and the New Space Race.
Formerly, he was a senior reporter at Quartz, the global business news site, for more than a decade, and began his career as a political reporter in Washington, D.C. 

You can contact or verify outreach from Tim by emailing
[email protected]
or via an encrypted message to tim_fernholz.21 on Signal.
View Bio
[Event Logo]
October 13 – 15
San Francisco
Get 50% off a second pass
The Disrupt experience is meant to be shared. Get your pass and bring a colleague, partner, or peer at 50% off. Cover more ground by making connections, building momentum, and discovering what’s next in the startup ecosystem.
BOOK NOW
Most Popular
US bars Microsoft, Adobe, and major IT firms from green card program for skilled foreign workers
Aisha Malik
Cal AI’s 19-year-old founder just raised $10M for his new AI startup
Julie Bort
Google releases a new local-first Granola competitor
Ivan Mehta
Anthropic is giving startups a free year of Claude Team and $1,000 in credits
Russell Brandom
At 19, founder raises $11M for Ghost, maker of a $3,499 computer for personal AI
Dominic-Madori Davis
Federal judge calls Flock ‘indiscriminate mass surveillance’
Anthony Ha
Amazon responds to data center backlash, says it no longer uses NDAs
Anthony Ha

## Metadata
- **Source**: [Original Article](https://techcrunch.com/2026/10/09/anthropic-cant-reliably-control-its-ai-agents-its-cutting-off-its-internal-evals-from-the-live-internet-instead/)
