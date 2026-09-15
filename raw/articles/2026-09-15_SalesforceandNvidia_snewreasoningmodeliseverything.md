---
title: Salesforce and Nvidia’s new reasoning model is everything the AI labs should fear
date: 2026-09-15
url: https://techcrunch.com/2026/09/15/salesforce-and-nvidias-new-reasoning-model-is-everything-the-ai-labs-should-fear/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://techcrunch.com/2026/09/15/salesforce-and-nvidias-new-reasoning-model-is-everything-the-ai-labs-should-fear/
source_feed: TechCrunch AI
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-09-15 07:26
---

# Salesforce and Nvidia’s new reasoning model is everything the AI labs should fear

## Full Article

A new AI model called
Koa
is one of the biggest announcements from Salesforce this week at its giant Dreamforce tech conference. Koa is the company’s first reasoning model, built on Nvidia’s
open-weight Nemotron
model. The two companies worked together to post-train Koa to excel at sales, marketing, and customer-support-related tasks.
Koa is a shining example of how the enterprise world’s needs for AI are diverging from what the frontier labs are offering. Proprietary AI labs would rather have enterprises uploading files, code, prompts, and feedback directly into their models and agents,
and spending millions
to do so.
But with the model, Salesforce is offering its enterprise customers:
an open-weight alternative to closed frontier models
a model trained to do specific work tasks (rather than to
solve impossible math problems
)
one that has not ingested any actual customer data and therefore cannot leak it to others
a model that helps reduce AI spending, since it uses fewer tokens to do the same work
one that can be automatically routed through an AI “gateway,” depending on the need
and a model that follows all of a customer’s data requirements and security embedded within Salesforce.
Koa will be provided as an alternative to the other models Salesforce offers in its Agentforce platform, where its customers build agents to handle rote tasks like answering customer service questions or scheduling appointments.
“We’ve built many small task-specific language models, which are part of Agentforce’s portfolio,” Jayesh Govindarajan, EVP of Salesforce AI, told TechCrunch. “But reasoning has always been something that we’ve relied on the frontier model providers for. Until now.”
Before Koa, if an agent needed to reason through a long-running or multi-step task, those prompts would be routed to a frontier model like Claude or ChatGPT through Agentforce’s AI gateway (the system that decides which model handles which request).
“One of the reasons we hadn’t done this before, train our own enterprise-grade frontier model — we always wanted to — but the challenge has always been the lack of a pre-trained base model to start with. Until Nemotron came along, there was no sovereign American pre-trained model that was available, one, and two, that was state of the art, and, three, that had clear data provenance. We have no idea what Qwen trains on,” Govindarajan said, referring to the popular Chinese open-weight model produced by Alibaba.
Post-training a model like this means taking it from a general-purpose system to one well-versed in sales and customer support knowledge, and to do that, Salesforce and Nvidia did not use any actual data from Salesforce’s customers. Instead, they crafted synthetic data that mimicked customers’ patterns.
“We actually simulated a customer service environment with a persona customer service professional, including irate customers that call into the customer service center, all the way to a sales professional who’s trying to close a deal,” Govindarajan described.
Koa is meant to be better at the work tasks Salesforce customers want an agent to do — and cheaper, in terms of tokens burned — than sending those same tasks to Claude or ChatGPT.
With Nemotron, “we have a unique architecture for inference to be token efficient,” Kari Ann Briski, Nvidia’s VP of Generative AI Software for Enterprise, told TechCrunch. “It’s kind of the trifecta of things that you need to have: sovereign AI, time to first token, efficient reasoning, for the tokenomics of it all.”
However, Salesforce isn’t exactly abandoning Anthropic or OpenAI. It just announced a partnership with Anthropic
called ClaudeForce
that allows companies to use Claude as their AI interface, while their data remains in Salesforce’s system of records, secured by its infrastructure.
Topics
AI
,
Enterprise
,
nvidia
,
Salesforce
,
TC
When you purchase through links in our articles,
we may earn a small commission
. This doesn’t affect our editorial independence.
[Julie Bort]
Julie Bort
Venture Editor
Julie Bort is the Startups/Venture Desk editor for TechCrunch.
You can contact or verify outreach from Julie by emailing
julie.bort@techcrunch.com
or via
@Julie188
on X.
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
- **Source**: [Original Article](https://techcrunch.com/2026/09/15/salesforce-and-nvidias-new-reasoning-model-is-everything-the-ai-labs-should-fear/)
