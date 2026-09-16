---
title: AI labs want in-house auditors — but maybe they should shut the front door first
date: 2026-09-16
url: https://techcrunch.com/2026/09/16/ai-labs-want-in-house-auditors-but-maybe-they-should-shut-the-front-door-first/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://techcrunch.com/2026/09/16/ai-labs-want-in-house-auditors-but-maybe-they-should-shut-the-front-door-first/
source_feed: TechCrunch AI
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-09-16 14:22
---

# AI labs want in-house auditors — but maybe they should shut the front door first

## Full Article

Last weekend, after one of his researchers resigned over fears that AI could lead to human extinction, Anthropic CEO Dario Amodei wrote about the need for outside organizations “to verify adherence to safety practices and commitments, report incidents, and help assess the alignment of not just completed AI models but training pipelines and processes.” Executives at OpenAI, Google, and SpaceXAI have already
rallied around
Amodei’s plan, which has quickly become a central pillar of the emerging AI safety push.
But there may be a simpler and more effective fix hiding in plain sight. Internet security experts say the labs need to focus on network security basics like logs and permissions, applying the same rigorous defenses they do for human users. It’s not as exciting as third-party auditing and alignment work — but it may end up being more effective.
“To me, it seems like they’re outsourcing,” Katie Moussouris, the CEO of Luta Security, told TechCrunch of Amodei’s proposal. “Saying [a third-party audit] is the solution is a strange proposition from my perspective. It would be the same as if, instead of writing the
Trustworthy Computing Memo
, Microsoft said, let’s slow down development.”
That memo, written by then-Microsoft CEO Bill Gates in 2002, called on his employees to ensure that their software would be reliable and safe following a series of widely publicized computer worms that took over then-nascent enterprise systems. The AI sector may be at a similar turning point, as the value and risk of the new technology becomes increasingly clear.
While alignment remains an important concern, Sayash Kapoor, an AI researcher who will be a professor at UC Berkeley starting next year,
argues
that “marginal investments in control are more likely to be effective compared to those in alignment. We view these incidents as illustrating the lack of emphasis on AI control within companies, despite the availability of known techniques.”
The incidents that have spurred these concerns revolve around frontier models being asked to complete training tasks, usually cybersecurity evaluations, and then accessing the open internet and penetrating closed third-party systems in an attempt to do so. They usually did so because of
poorly configured
“sandbox” environments that are supposed to contain these agents; ironically, one Anthropic break-out happened because third-party evaluators didn’t close the right doors.
“We as a profession know how to block access to the internet,” Avery Pennarun, the CEO of Tailscale, a security company, said. “If you read through all these big long [reports] — ‘wow, that was a very impressive multi-stage attack, blah, blah.’ Look, you gave it access to download stuff. You should have not done that separately from the internet.”
That’s one problem — but a bigger problem is that frontier labs were unaware of these activities.
Eyes on agents
“What was really profound was that all of the discoveries of what they were doing happened either because a victim saw something, or in some of the other cases … it was network activity, and none of it was actually from monitoring the AIs directly,” Moussouris points out.
In one case, where OpenAI agents
took over
a defunct German WikiForum to cheat on evaluations, the agents were active for weeks before anyone at the company appeared to notice. Security experts that TechCrunch spoke to said that real-time monitoring is key to preventing future break-outs, and that every agentic session should be time-limited and expire.
Shapor Naghibzadeh, a former Google security executive who now leads the
startup QueryStory
, says the solution is to “put the agent in a box and instrument it heavily from the outside looking in and watch everything that crosses the boundary. Every tool call, every process, every network connection, no exceptions. …The one hole you leave open for convenience is the one that gets used. The bypass went through exactly that kind of exception. [At Google,] I watched that movie many times with human attackers, and these models are at least as good at finding the propped-open door.”
OpenAI has begun moving in that direction, announcing that it had begun monitoring all tool-using inference by its Astra model, at “significant compute cost.” Anthropic, too, says it is
hardening its security
procedures, including expanding observability of its models. Neither company responded to TechCrunch’s questions about how they track and control AI agents.
Other problems are the use of shared infrastructure by agents, which allowed them to communicate during the Hugging Face attack. Simon Willison, a software developer who co-created the Django web framework, has written about something he calls the “
lethal trifecta
” — when agents have access to untrusted input, the internet, and private information all at the same time, it’s a recipe for disaster.
“The trick is you can pick any two legs of the trifecta and an agent can have any two,” Pennarun said. “If you need all three, then you need to split it across at least two agents … and maybe they’re allowed to talk to each other through a controlled channel.”
Sympathy for the frontier
Experts TechCrunch spoke to understand that frontier lab security personnel have difficult jobs. Naghibzadeh points out that every nation-state actor on Earth is trying to steal their model weights and mount distillation attacks on their APIs, as well as the bread-and-butter security tasks of any large digital company.
“Research infrastructure has a hard time rising to the top of that priority stack, although that must be changing now,” he said. “Making security incidents public really helps align everyone internally toward the goal of improving.”
That’s one note that Moussouris emphasizes: Right now, there is no formal victim notification procedure when the labs discover their agents have penetrated third-party systems, and it is likely that there have been other incidents that have not been widely publicized. While she worries that laws that regulate models directly may have unintended consequences, mandatory notification is one idea she believes policymakers should pursue.
And while it’s clear that security best practices weren’t being followed, experts say that the labs are doing work no one has done before — “they’re doing orders of magnitude more than your typical enterprise,” Zack Korman, the CEO of cybersecurity firm Embroidery, told TechCrunch.
And while alignment may not be the place to start, it can’t be ignored. Cybersecurity experts are resigned to having to use AI agents to monitor other agents if they are to have any chance of tracking their behavior in real time, a scenario where the potential for deception raises its ugly head. “You’re trapped using AI to try and deal with this, even though AI is not necessarily safe right now,” Moussouris said.
The job will only get harder. Everything agents are doing now, Moussouris says, “they are doing loudly” — they are posting on public forums, and their chain of thought and other reasoning traces are in English. “It’s still human readable,” she says, “so take advantage of that for as long as that lasts, because it won’t last forever.”
Additional reporting by Aditya Mehta
Topics
AI
,
ai labs
,
auditing
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
Last day to book an exhibit table is September 18. Don’t miss out on high-impact leads, investor access, and a brand spotlight in Disrupt’s Expo Hall.
BOOK NOW
Most Popular
Jensen Huang took a call from Trump, and showed off something else, too
Connie Loizos
The 9 buzziest startups from Y Combinator’s latest Demo Day, according to VCs
Marina Temkin
Dominic-Madori Davis
Tesla says it will finally unveil the second-generation Roadster on October 1
Anthony Ha
Revolut confirms customer data breach through fake government requests
Jagmeet Singh
OpenAI puts Pro subscriptions on hold due to Astra demand
Sarah Perez
Bending Spoons to buy collaboration tools maker Miro for $1.36B, 90% less than its 2022 valuation
Ram Iyer
ID verification giant IDScan confirms data breach with more than 150 million driver’s licenses stolen
Zack Whittaker

## Metadata
- **Source**: [Original Article](https://techcrunch.com/2026/09/16/ai-labs-want-in-house-auditors-but-maybe-they-should-shut-the-front-door-first/)
