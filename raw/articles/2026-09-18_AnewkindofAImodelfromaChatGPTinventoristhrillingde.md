---
title: A new kind of AI model from a ChatGPT inventor is thrilling developers
date: 2026-09-18
url: https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/
source_feed: TechCrunch AI
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-09-18 14:22
---

# A new kind of AI model from a ChatGPT inventor is thrilling developers

## Full Article

ChatGPT broke Diogo Almeida’s heart.
Almeida was an OpenAI researcher who helped build the chatbot and then invent reinforcement learning from human feedback (RLHF), the model-training technique perhaps most responsible for our current age of AI. But despite its capabilities, he was disappointed.
“We have lightning in a bottle, and yet it is not useful,” Almeida told TechCrunch. “I’ve been battling that problem since then. It took me a while to come to the conclusion: the problem is we are optimizing for human language  … We have been super good at human language for four years, but it’s not useful for automation because computers speak a different language.”
Two years ago, Almeida left OpenAI to start
TypeSafe AI
, a startup trying to fix that problem. This week, the company released a new transformer-based model,
Jev
, that is not a large language model (LLM). It doesn’t output text, but instead produces probabilities, or what the company calls “calibrated decisions.”
Eschewing language does a few things: It makes the model incredibly cheap and fast, and because users define the outputs in advance, it cannot hallucinate. Its output tokens are free, and input tokens are metered by the billion, not the million.
A screenshot shows a comparison of Jev and an OpenAI model responding to the same requests.
Image Credits:
TypeSafe AI / TypeSafe AI
Developers are taking a great interest in the product; the company briefly lost the ability to serve users from its API because demand was so high. Jev appears most useful for software automation. Thus far, software developers see it as a cheaper and more robust way to incorporate intelligence into their code.
For example, Pranit Sharma, a software engineer at Vercel, a company making agentic infrastructure,
said
his company had used OpenAI’s ChatGPT Luna 5.6 to run a classifier to review commands for safety. When Vercel replaced OpenAI’s Luna with Jev, it got results 5 to 18 times more quickly and with greater accuracy.
Another developer, Bryo AI CTO Nikhil Mudholkar,
tested
Jev against Gemini for classifying business emails. In his test, Gemini was slightly more accurate, but 10 to 20 times more expensive. More interesting to Mudholkar were Jev’s confidence scores — “it is the only one that hands back a real probability which makes it ideal for automating workflows!!”
Besides replacing LLMs in certain use cases, the new model can also augment them, acting as a smart check on misbehavior. Using agents to monitor agents can quickly become expensive, but using Jev to do so, Almeida argues, makes sense. He sees users deploying Jev to track LLM agent traces and prevent jailbreaks.
“At the end of the day, it delegates the hallucination problem a little bit to the user,” explained Armin Ronacher, the CTO of Earendil, which builds the open-source model harness Pi. “The user has to say, okay, if this only comes back with 50% probability, maybe this is a coin toss, and I disregard it. But if it’s 95%, sure, then I can do something with it.”
Another potential use for Jev is model routing, Ronacher said. Predicting whether a given workload requires a specific model would be useful, but using an LLM for the job would be expensive. Jev’s low cost and speed make that kind of real-time sorting possible.
And that’s Almeida’s hope. The model is named after William Stanley Jevons, the 19th-century economist whose eponymous paradox describes how the falling cost of a commodity can lead to it being used more and more. In this case, the falling cost of intelligence should lead to its widespread deployment.
“We think that there’s just going to be smart software all over the place in a way that’s emergent and distributed … much more like the early internet than you know like the the mega apps that people are trying to build right now,” Almeida said.
Almeida is tight-lipped about the model’s architecture, which outside observers suspect is built on top of an open-weight LLM. The company refers to Jev as a “System One model,” focused on intuition rather than reasoning, and
specifically focused
on the right task. Almeida says Jev is trained exclusively on synthetic data using a technique he calls “reinforcement learning from calibrated decisions.”
“We made an early bet that we will be making all of our data, and that has been one of the best bets I’ve ever made in my life—better than our launch, in my opinion, better than RLHF,” he told TechCrunch. “Half of [our company] is a lab that basically owns this entire subfield of statistically well-understood synthetic data, and that is now my life joy.”
For now, Jev stands alone as this kind of model, but Ronacher expects that competitors will spring up now that its utility is apparent.
“We should have seen this earlier in many ways, but presumably because the LLMs are so cheap and subsidized, you often don’t have to be creative yet,” he said.
TypeSafe itself will be building more versions of the model, in new modalities. Asked if TypeSafe is a frontier lab, Almeida said, “the main product of Frontier Labs is fear or hype. I would like our main product to be intelligence…[but we are] not a lab in the sense of, you know, like bet on infinite wealth, or a religion, or building God in a data center, or whatever is the thing of today.”
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

You can contact or verify outreach from Tim by emailing tim.fernholz@techcrunch.com or via an encrypted message to tim_fernholz.21 on Signal.
View Bio
[Event Logo]
October 13 – 15
San Francisco
Last day to book an exhibit table is September 18. Don’t miss out on high-impact leads, investor access, and a brand spotlight in Disrupt’s Expo Hall.
BOOK NOW
Most Popular
OpenAI caught its models leaving notes to successors to hide bad behavior
Rebecca Bellan
Microsoft exec called AI scraping ‘the largest theft of labor in human history,’ new unredacted filings reveal
Rebecca Bellan
Clean tech startup Fluxnium found a way to tap 50,000 years’ worth of nuclear fuel
Tim De Chant
Jensen Huang took a call from Trump, and showed off something else, too
Connie Loizos
The 9 buzziest startups from Y Combinator’s latest Demo Day, according to VCs
Marina Temkin
Dominic-Madori Davis
Tesla says it will finally unveil the second-generation Roadster on October 1
Anthony Ha
Revolut confirms customer data breach through fake government requests
Jagmeet Singh

## Metadata
- **Source**: [Original Article](https://techcrunch.com/2026/09/18/a-new-kind-of-ai-model-from-a-chatgpt-inventor-is-thrilling-developers/)
