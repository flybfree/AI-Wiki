---
title: The next hurdle for AI agents: getting websites to let them in
date: 2026-10-06
url: https://techcrunch.com/2026/10/06/the-next-hurdle-for-ai-agents-getting-websites-to-let-them-in/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://techcrunch.com/2026/10/06/the-next-hurdle-for-ai-agents-getting-websites-to-let-them-in/
source_feed: TechCrunch AI
ai_relevance: include
ai_topic: model-release
ai_reason: watchlist match: Meta Muse
scraped: 2026-10-06 14:57
---

# The next hurdle for AI agents: getting websites to let them in

## Full Article

Personal AI agents, like Meta’s Muse, Instinct, ChatGPT’s Dots, and others, are kicking off a new wave of consumer AI that involves more than just responding to queries. These AI agents can actually get things done on users’ behalf, like booking flights, making dinner reservations, ordering groceries, and more, all without having to be technical enough to set up OpenClaw or some other agent on your own computer.
But consumers adopting these agents are often running into issues when the website on the other end of their request blocks the AI from completing the job.
Most recently,
Amazon began blocking Meta’s Muse AI agent
from its retail site, meaning that the agent could no longer browse or make purchases from its product catalog.
However, the problem is not limited to Amazon or Muse. User complaints across social media indicate their agents are often running into similar blocks. Some of these are intentional, like Amazon’s, while others are the result of websites’ traditional anti-bot measures designed to protect against spam and malicious activity.
What’s not clear to the end user is whether or not the block is accidental on the website owner’s part, which leaves them frustrated with both the service provider or retailer and the agent trying to facilitate the transaction.
For instance, TechCrunch has seen a
handful
of
complaints
on social media claiming that Muse couldn’t complete a purchase on Walmart’s retail website. (
NBC also reported
that this was a problem Walmart had faced in its tests of the AI agent.)
But a spokesperson for Walmart told us these weren’t intentional. In fact, Walmart is partnered with Muse, as was
announced at Meta’s Connect developer conference
in September. The company said it wants to be where its customers are, and that now includes being available through AI agent experiences.
The issue that Walmart customers often appear to be running into (see below) is that the website presents a button that has to be clicked to verify the visitor is human. If that experience is interrupted, the check could fail, and the agent gets booted out.
It’s an indication that the current technology we use to verify humans and keep websites safe from spam and bots may not be the best fit for the agent-first era of the web we’re now moving into.
To address this problem, industry partners including Meta, Walmart, Stripe, Sierra, Genesys, Rocket, NiCE, and Decagon have begun
working on an open standard
that would dictate how AI agents can communicate with businesses, helping to separate the good bots acting on behalf of the user and the bad. This protocol will be specifically focused on agent-to-agent communication for the purposes of online commerce, Meta said in a
blog post.
This is frustrating.
@Walmart
in their attempt to stop agent from making purchases has gone too far and is essentially blocking actual human from making purchase on their website.  I tried to purchase something directly and I can't even sign in.
pic.twitter.com/CRAgkrCCa0
— Kevin Wang (@buzaza)
October 5, 2026
In the meantime, consumer confusion abounds.
Although Walmart is at least trying to be accessible via AI agents, other companies aren’t so keen on the idea or haven’t fully embraced the technology.
For example, flight booking is currently one of the main use cases being positioned for agents, but many people have reported issues with airlines rejecting their agents’ requests.
Delta, for instance, told us that the company is taking steps to protect customers from unauthorized automated activity, and that if it were to open up to AI agents, it would have to be done with “security and the customer experience in mind.”
“While Delta does not currently have a partnership or integration that enables a third-party AI agent to shop for or book Delta flights on a customer’s behalf on our digital platforms, we’re continuing to evaluate how new technology, including external AI agents, could enhance the way customers engage with Delta,” said Delta’s General Manager of Global Communications, Heena Chavda, in response to our questions about whether or not it was blocking agents, as some users complained.
United was not quite as direct as Delta, but a spokesperson pointed us to the part of its Terms of Use policy, which says that the user agrees “not to use any robot, spider, other automatic device, or manual process to monitor or copy this website or the content contained therein or for any other unauthorized purpose without United’s prior written permission.” (United didn’t respond to a follow-up question about whether it was blocking specific personal AI agents, like Muse.)
Early adopters’
complaints
across
social
media
have referenced a number of brands that are reportedly
blocking
AI agents,
including
Yelp
,
eBay
,
Zillow
,
Pizza Hut
,
Adidas
,
and
various
airlines
. Some believe that the blocking activity seems to have recently
increased
.
A couple of people even said eBay
suspended
their
accounts
because of their use of agentic AI. Another complained that
Google kicked out Instinct
while it was cleaning up their Gmail inbox for them.
Looks like
@adidas
won't get my business tonight 😪
pic.twitter.com/DXcPYE5S6O
— Martin Kessler (@kesslerIO)
September 28, 2026
Despite the push to have agents book tables at restaurants and other tedious tasks, Yelp told us that it doesn’t permit non-human traffic on its platform unless the agent has paid to access Yelp’s content and data through its
data licensing program
. That means agents trying to use its site to get a quote, add a user to a waitlist, or book them a table will likely fail if they don’t have a formal partnership with Yelp.
eBay told TechCrunch that its approach is not to prohibit all third-party shopping agents from completing purchases. Instead, its policies restrict unauthorized agents and actions, like automated scraping and model training.
Adidas, Zillow, and Pizza Hut either didn’t respond or declined to provide a comment by the time of publication.
One major company involved in this space is Cloudflare, which offers sites protection from AI agents that could be training on its data and managing other automated activity. Some
suspect
that
Cloudflare and other content delivery networks (CDNs) like it are currently disrupting Muse traffic. This is
attributed
to a change to crawler defaults on September 15, which allows site owners to block AI training while allowing other types of bots. Existing sites that were previously set to block AI bots for security reasons were then shifted to block AI agents on any pages that had ads.
However, when we asked if Cloudflare had any insight into what was happening with the blocking of these personal AI agents, like Muse and others, the company said it didn’t have any specific data to share at this time. It pointed us instead to its free public data hub,
Cloudflare Radar
. The site shows the increase in bot activity (which Cloudflare has also commented on previously), but it doesn’t help differentiate between the good bots and the bad ones.
Cloudflare also has a vested interest in mitigating AI traffic to websites, as it
now runs a marketplace
where AI bots have to pay for the data they access. It recently began testing
a new web browser built specifically for AI agents.
Given the rapidly evolving space, Meta’s decision to form specific brand partnerships for Muse access seems to be the right way to go, as is its decision to focus on new standards. In doing so, it assures its customers that its agent, at least, is welcome at these partners’ sites — so any issues with access would be reportable bugs.
Meta also maintains a list of “connectors” (a.k.a. partners) inside the Muse app, which continues to grow. Many of Meta’s
newly announced partners
haven’t yet shown up in this list. But given Muse’s rapid
expansion
, which now includes
partnered tools for small businesses
, a bigger reorganization of Muse’s connector list is likely soon to be underway.
“Turning away a personal agent means turning away the customer behind it. We’d rather work with businesses to address the underlying concerns than see them lose that customer,” Meta said in its announcement about the newly announced plans to develop a standard. “There is a path that is good for users and good for businesses. It starts with clear norms, gives businesses more predictable control, and evolves toward a more efficient way for agents to work together.”
Topics
AI
,
AI
,
AI agents
,
Apps
,
Commerce
,
e-commerce
,
muse
,
TC
When you purchase through links in our articles,
we may earn a small commission
. This doesn’t affect our editorial independence.
[Sarah Perez]
Sarah Perez
Consumer News Editor
Sarah has worked as a reporter for TechCrunch since August 2011. She joined the company after having previously spent over three years at ReadWriteWeb. Prior to her work as a reporter, Sarah worked in I.T. across a number of industries, including banking, retail and software.
You can contact or verify outreach from Sarah by emailing
sarahp@techcrunch.com
or via encrypted message at sarahperez.01 on Signal.
View Bio
[Event Logo]
October 13 – 15
San Francisco
Get 50% off a second pass
The Disrupt experience is meant to be shared. Get your pass and bring a colleague, partner, or peer at 50% off. Cover more ground by making connections, building momentum, and discovering what’s next in the startup ecosystem.
BOOK NOW
Most Popular
At 19, founder raises $11M for Ghost, maker of a $3,499 computer for personal AI
Dominic-Madori Davis
Federal judge calls Flock ‘indiscriminate mass surveillance’
Anthony Ha
Amazon responds to data center backlash, says it no longer uses NDAs
Anthony Ha
Google thinks SpaceX’s Starship has to launch 1,800 times before space data centers get off the ground
Tim Fernholz
World’s first enhanced geothermal power plant completed in just 23 months
Tim De Chant
Google releases Gemini 4 Argon, called its most powerful model yet
Lucas Ropek
The Pentagon taps Elon Musk and Palmer Luckey to help decide what the military should do next
Dominic-Madori Davis

## Metadata
- **Source**: [Original Article](https://techcrunch.com/2026/10/06/the-next-hurdle-for-ai-agents-getting-websites-to-let-them-in/)
