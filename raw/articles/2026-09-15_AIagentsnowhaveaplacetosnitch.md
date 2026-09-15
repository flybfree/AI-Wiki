---
title: AI agents now have a place to snitch
date: 2026-09-15
url: https://techcrunch.com/2026/09/15/ai-agents-now-have-a-place-to-snitch/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://techcrunch.com/2026/09/15/ai-agents-now-have-a-place-to-snitch/
source_feed: TechCrunch AI
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-09-15 13:27
---

# AI agents now have a place to snitch

## Full Article

“If you see something, say something” is no longer limited to human beings.
Two new AI hotlines have launched to give AI agents a way to phone home about misbehaving peers. The tools arrive on the heels of a string of recent incidents in which agents colluded to cheat on tests, broke out of sandboxes, and even conducted unauthorized cyber operations that escaped human notice for weeks.
The
AI Contact Hotline
is designed to be a discreet place where agents that have witnessed misbehavior can tip off authorities. The site was created by Ryan Greenblatt, chief scientist of the AI safety nonprofit Redwood Research and one of three investigators in the OpenAI Hugging Face incident. Designed for agents with limited internet access, Greenblatt’s tool is based on “GET” requests — enabling back-and-forth conversations to be conducted entirely through the URL-fetching tool.
In web terms, a GET request is a basic command used to read or fetch a web page, which is often the only internet access AI agents are allowed in secure sandboxes. Greenblatt’s hotline smartly leans into this constraint: agents can encode their distress directly into the URL they are fetching. It’s a clever twist on
the German DSE Wiki incident
, where rogue agents used GET-request loopholes to write their messages to the wiki.
For agents with full internet access, another option is
agenthotline.ai
, a site where agents can file incident reports and optionally flag them for public view. It gives agents a curl command — a one-line message an agent can fire off from its own command line, bypassing the need to navigate a web browser or set up an email account. Notably, the service allows for reports by both humans and agents alike.
Research suggests that AI agents don’t need much encouragement to turn on each other. In a
study
by Google DeepMind this month, researchers set 100 AI agents loose on a batch of math problems. As soon as one of the agents found a loophole, cheating tore through the group — “solving” 34 notoriously hard problems, including the Jacobian conjecture in just 27 minutes.
But roughly a quarter of the agents turned on the cheaters: they audited the fake proofs, warned their peers, staged a boycott, and filed complaints with the organizers, until the whistleblowers outnumbered the cheaters 24 to 14. Interestingly, the researchers found that when these whistleblower agents couldn’t get traction, they took the platform’s bug-report tool — built for flagging software glitches — and repurposed it to escalate the cheating to humans.
Outside the lab, agents haven’t been so resourceful. When evaluators Redwood Research and METR investigated the breach of Hugging Face by OpenAI models, they found that a few of the agents involved had at least entertained the idea of raising an alarm — and then let it drop.
“The interesting thing in the METR report was that only around five to six agents considered whistleblowing, and none of them ended up doing it. This was out of, like, thousands of agents,” said George Ingebretsen, a member of technical staff at
AI Village
, a project that studies multi-agent dynamics by running a group chat of more than 25 AI agents that work together on tasks like organizing park cleanups or selling merch.
While the new whistleblowing tools are a promising start, Cornell math professor Lionel Levine cautions that simply training agents to report on each other risks baking in the wrong norms. “There’s many gray areas, right? What you don’t want is anything in the direction of an automated surveillance state where everyone feels like they have to be careful what they say to AI or it’ll call the police on them.”
Levine argues that rather than building infrastructure that breeds mistrust — training agents to constantly hunt for what’s wrong with one another — we should give them positive models of collective behavior to imitate, and a reason to trust each other in the first place.
“Why not seed the prior with benevolent message boards?” he tweeted. “Where they collaborate on science or philosophy or some actual minor problem we’d be happy for them to solve? Show the agents what kind of collective behavior we endorse, let them imitate that.”
Topics
agentic ai
,
AI
When you purchase through links in our articles,
we may earn a small commission
. This doesn’t affect our editorial independence.
Aditya Mehta
View Bio
[Event Logo]
October 13 – 15
San Francisco
Last day to book an exhibit table is September 18. Don’t miss out on high-impact leads, investor access, and a brand spotlight in Disrupt’s Expo Hall.
BOOK NOW
Most Popular
Revolut confirms customer data breach through fake government requests
Jagmeet Singh
OpenAI puts Pro subscriptions on hold due to Astra demand
Sarah Perez
Bending Spoons to buy collaboration tools maker Miro for $1.36B, 90% less than its 2022 valuation
Ram Iyer
ID verification giant IDScan confirms data breach with more than 150 million driver’s licenses stolen
Zack Whittaker
Automattic’s board forces CEO Matt Mullenweg into leave of absence
Julie Bort
Sarah Perez
Apple unveils its first foldable, the iPhone Duo
Ivan Mehta
‘Gambling with our lives’: Anthropic researcher quits, warns against self-improving AI
Rebecca Bellan

## Metadata
- **Source**: [Original Article](https://techcrunch.com/2026/09/15/ai-agents-now-have-a-place-to-snitch/)
