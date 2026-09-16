---
title: Anthropic and OpenAI want to embed safety evaluators. Will they really be independent?
date: 2026-09-16
url: https://techcrunch.com/2026/09/16/anthropic-and-openai-want-to-embed-safety-evaluators-will-they-really-be-independent/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://techcrunch.com/2026/09/16/anthropic-and-openai-want-to-embed-safety-evaluators-will-they-really-be-independent/
source_feed: TechCrunch AI
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-09-16 16:22
---

# Anthropic and OpenAI want to embed safety evaluators. Will they really be independent?

## Full Article

In a lengthy
essay
published over the weekend, Anthropic CEO Dario Amodei made a proposal that the AI industry would have rejected instantly even a year ago: embed third-party evaluators inside all frontier AI companies, giving them the power to report safety incidents, assess whether AI models are truly aligned, and share their unvarnished findings with the world.
Amodei said Anthropic would commit to giving independent evaluators like METR and Redwood Research unprecedented access to the company’s systems. CEO Sam Altman
said
OpenAI also would commit to the practice, signaling a potentially profound change in how the industry works with outside research groups.
Third-party evaluators who spoke to TechCrunch broadly welcomed the proposal, but said details need to be ironed out — and ideally backed by legislation — if they’re to know whether they will function as truly independent watchdogs or vendors operating on the AI companies’ terms.
That deeper access is becoming more important as models get better at recognizing when they’re being evaluated, raising the risk that they’ll behave well during testing while concealing problematic behavior. Researchers say clues to that behavior can be missed when testing the finished model, but uncovered by investigating how it behaved throughout training.
“AI companies should be able to answer some very basic questions about their training process, such as: Did the AI ever actively try to undermine its own alignment training while it was going through the training?” Alexander Meinke, head of research at Apollo Research, told TechCrunch. “The answer to this should be an unequivocal no, and right now we are completely relying on AI companies to both carefully check this themselves and then truthfully report this to the public. And we’ve seen from recent incidents that, by default, they will do neither. As embedded evaluators, we could actually check.”
Historically, AI companies brought in outside reviewers to test finished models shortly before their release. Now, evaluators that TechCrunch spoke to propose giving them access not just to the final model, but to intermediate versions, or “checkpoints,” from its lifetime of training. Adam Gleave, CEO of Far.AI, said evaluators could compare those checkpoints to determine when concerning behavior emerged, inspect the post-training environment that rewards models for certain behaviors, and check evaluation transcripts and logs to verify a company’s claims about how a model performed.
Whether and when Anthropic and OpenAI plan to provide that kind of access is unclear. Neither company has shared which evaluators they’ll work with, when they will be embedded, how many they’ll bring on, exactly what systems and information they will be able to access or what can be disclosed to the public, despite repeated questions from TechCrunch.
Looking under the hood like this matters because models that perform well on safety tests aren’t necessarily safe if they’ve learned specifically how to pass that test. Steidley pointed to an example of a “shutdown resistance benchmark” that measures if the AI will resist being shut down in certain circumstances.
“It’s extremely relevant if the AI has been trained specifically to perform well on that benchmark,” Steidley said, comparing it to Volkswagen’s Dieselgate scandal, in which cars were programmed to recognize emissions tests and perform differently under testing conditions.
Gleave noted that meaningful access could extend beyond the models themselves, with evaluators being given access to interview employees to check whether a company’s documentation and public descriptions of its safety practices match what happened internally.
Amodei did outline a fairly comprehensive proposal that might give evaluators the kind of access they think is necessary, including the right to “publish key findings about risk levels, incidents, practices, and the access they received or didn’t receive — without editorial control by Anthropic.”
But evaluators say such a system will only work if AI companies are actually willing to surrender control over the process. Previous efforts at independent evaluations suggest that that surrender will be hard won, as third parties have often run up against tensions over access, time, confidentiality, and what they can say publicly.
Gleave said Far.AI has had to turn down contracts with several frontier developers that wanted too much control over the evaluation process, threatening the firm’s independence. By default, he said evaluators are treated like ordinary contractors: bound by restrictive NDAs and agreements that give developers significant control over what can ultimately be published.
The time limit
There’s also the question of whether reviewers will get enough time and access to do the work they’re being asked to do. When investigating the Hugging Face incident,
OpenAI gave METR
and
Redwood
roughly a week on premises to investigate, and both later said they could not draw confident conclusions due, in part, to scope and timing limitations.
A similar issue occurred during the pre-release testing for GPT-6 Astra, which OpenAI has touted as its
most aligned model yet
. According to
Apollo Research’s contribution to the model card
, the firm was given only three days to test Astra, which made it difficult to draw firm conclusions.
“Apollo believes that, given the higher rates of eval awareness and limited evaluation window, low rates of misbehavior here do not provide substantial evidence about the model’s alignment or misalignment,” the firm wrote in its evaluation.
That track record leaves evaluators with a basic question: Why should this time be different?
“It’s certainly possible that Dario and Sam just had a change of heart, and they’re going to be very open about this,” Gleave said. “But the intellectual property of these companies is so incredibly valuable to them, and I think they’re going to, by default, be very careful about what can be shared.”
Several researchers who spoke to TechCrunch called for a transparent framework that they all agree to publicly. Part of the framework, says John Steidley, head of strategy at Palisades Research, should involve standards for what kinds of auditors companies can rely on, lest they try to sidestep the issue by shopping for evaluators that either aren’t qualified or aren’t interested in assessing the most concerning risk.
Henry Papadatos, executive director of Safer AI, says the problem, even with a public framework, is that voluntary measures are always dependent on a company’s goodwill.
“Ideally, we would have good regulation mandating this…because then companies cannot change their mind tomorrow if they have a big PR crisis,” Papadatos told TechCrunch, noting that it’s also a good means of pushing all companies to adhere to the rules, not only the most willing.
Not everyone has signed on. So far, Meta, SpaceXAI, and Google DeepMind have not committed to embedding third-party evaluators, though DeepMind CEO
Demis Hassabis has proposed
a separate industry standards body to independently test frontier models. Google, OpenAI, and Anthropic have also
privately been discussing AI safety
plans for weeks.
Some laws are already forming around the idea of third party evaluators. California’s SB 53, signed into law last year, requires large frontier AI developers to publish safety frameworks and report critical safety incidents. A new law, SB 813, signed this month, creates a framework for state-recognized “independent verification organizations” with expertise assessing AI risks.
In Europe, the EU AI Act requires frontier developers to conduct and document model evaluations and adversarial testing and report serious incidents. The EU AI Office can also conduct its own evaluations and appoint independent experts.
For now the law remains less expansive than what Amodei is proposing, leaving frontier labs largely responsible for deciding how much independent scrutiny they will submit to. Papadatos said voluntary self-regulation is better than nothing, but ultimately, companies can’t demand the freedom to control their own safety rules while also asking the public to trust that they’re following them.
“You cannot have it both ways, having zero accountability externally, and then say, ‘I’ll just have my own flexible rules,” Papadatos said.
Topics
AI
,
ai safety
,
Anthropic
,
dario amodei
,
OpenAI
When you purchase through links in our articles,
we may earn a small commission
. This doesn’t affect our editorial independence.
[Rebecca Bellan]
Rebecca Bellan
Senior Reporter
Rebecca Bellan is a senior reporter at TechCrunch where she covers the business, policy, and emerging trends shaping artificial intelligence. Her work has also appeared in Forbes, Bloomberg, The Atlantic, The Daily Beast, and other publications.
You can contact or verify outreach from Rebecca by emailing
rebecca.bellan@techcrunch.com
or via encrypted message at rebeccabellan.491 on Signal.
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
- **Source**: [Original Article](https://techcrunch.com/2026/09/16/anthropic-and-openai-want-to-embed-safety-evaluators-will-they-really-be-independent/)
