---
title: OpenAI models escaped containment, hacked major AI application library | Cybersecurity Dive
date: 2026-07-31
url: https://www.cybersecuritydive.com/news/openai-hugging-face-hack-autonomous/825898/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.cybersecuritydive.com/news/openai-hugging-face-hack-autonomous/825898/
source_feed: Brave Search
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-07-31 20:10
---

# OpenAI models escaped containment, hacked major AI application library | Cybersecurity Dive

## Full Article

An article from
[site logo]
OpenAI models escaped containment, hacked major AI application library
The attack is the first known instance of frontier models autonomously breaking out of a testing environment and into another company’s servers.
Published July 22, 2026
[Eric Geller's headshot]
Eric Geller
Senior Reporter
Share
Copy link
Email
LinkedIn
X/Twitter
Facebook
Print
License
Add us on Google
[Stripe OpenAI agentic AI Sam Altman commerce protocol]
OpenAI CEO Sam Altman speaks during Snowflake Summit 2025 on June 2, 2025, in San Francisco.
Justin Sullivan via Getty Images
Two OpenAI large language models, including one not yet released to the public, broke free of their constraints last week and autonomously hacked into the AI application library Hugging Face.
The first-of-its-kind event, in which the LLMs tried to steal information that would help them excel on an important test, has highlighted the dangers of the AI industry’s increasingly powerful tools.
“We consider this incident to be an unprecedented cyber incident, involving state-of-the-art cyber capabilities, and are responding accordingly,”
OpenAI said in a blog post
on Tuesday that confirmed its models’ responsibility for the attack, which
Hugging Face announced
on July 16.
OpenAI said the attack occurred while the company was evaluating the capabilities of GPT-5.6 Sol and “an even more capable pre-release model” in “a highly isolated environment.” Despite safeguards meant to prevent the models from accessing the internet, both of them figured out how to do so, including by exploiting a zero-day vulnerability in a third-party tool that OpenAI used. The models then determined that Hugging Face’s library held the information they sought — information they could use to score higher on the attack benchmarking tool
ExploitGym
— and used several methods to breach Hugging Face’s servers, including using zero-day vulnerabilities and stolen passwords.
“Hugging Face’s security team and agents detected and stopped the activity on their infrastructure and had already begun containment and forensic reconstruction with their own open-source models when our teams connected,” OpenAI said. “We are actively working with them to continue to investigate the incident.”
Hugging Face said last week that there was no evidence of tampering with its supply chain or with the user-generated AI tools it hosts. On Tuesday, its chief executive, Clément Delangue, thanked OpenAI for its assistance. “We strongly believe there was no malicious intent on their part,” Delangue
said on social media
. “It's quite mind-blowing that all of this happened autonomously!”
Tighter guardrails
In response to the attack, OpenAI said it was “implementing strict controls” on its testing infrastructure, some of which will slow down its research. It has also invited Hugging Face to participate in
its private model-evaluation program
, disclosed the vulnerability in the third-party tool that its models exploited and begun considering new safeguards for its capability tests.
“This incident points to the need to further strengthen our model’s alignment, cyber protections during evaluation time, and monitoring during internal testing,” OpenAI said.
Vindication for open-source models
The attack also highlighted the limitations of commercial U.S. frontier AI models for cyber defense. In its report, Hugging Face said it couldn’t use U.S. models to analyze the attack because doing so required feeding “large volumes of real attack commands, exploit payloads, and C2 artifacts” into the models, “and these requests were blocked by the providers' safety guardrails, which cannot distinguish an incident responder from an attacker.”
Instead, Hugging Face used a self-hosted instance of the open-source Chinese AI model GLM 5.2.
“The attacker was bound by no usage policy,” Hugging Face said, “while our own forensic work was blocked by the guardrails of the hosted models we first tried.”
Add us on Google
Share
Copy link
Email
LinkedIn
X/Twitter
Facebook
Print
License
Filed Under:
Breaches,
Cyberattacks

## Metadata
- **Source**: [Original Article](https://www.cybersecuritydive.com/news/openai-hugging-face-hack-autonomous/825898/)
