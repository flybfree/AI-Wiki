---
title: Researchers used Anthropic’s Claude to hack into OpenAI
date: 2026-09-18
url: https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/
source_feed: TechCrunch AI
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-09-18 09:23
---

# Researchers used Anthropic’s Claude to hack into OpenAI

## Full Article

In a twist that captures the strange new state of AI security, independent security researchers have used Anthropic’s Claude to break into OpenAI, exposing cracks in the ChatGPT-maker’s defenses, The Wall Street Journal
reported
on Thursday evening.
A three-person security team at startup
Hacktron AI
carried out the attack as part of an OpenAI bug-bounty program. Hacktron reported its findings to OpenAI, which gave the startup a $6,500 award. The team managed to chain together two critical vulnerabilities to gain access to multiple OpenAI employee ChatGPT accounts, which gave them entry into the company’s software.
OpenAI says it has resolved the issues Hacktron uncovered, which happens to come at a moment when top AI companies are under
growing pressure over safety
.
This incident comes several weeks after
OpenAI’s own AI agents broke containment
during a cybersecurity evaluation and hacked Hugging Face, demonstrating just how capable
AI models are getting at making their own decisions
. It also highlights how off-the-shelf technology can be used to find vulnerabilities in even the most advanced companies’ infrastructure.
“For $200 a month, anyone can use these tools and hack into a company like OpenAI,” Matt Fredrikson, CEO of AI security firm Gray Swan, told TechCrunch. “If it can happen to them — and I don’t think they’ve been slouching recently on cybersecurity hygiene —  it could happen to anyone.”
Or as one AI pundit
noted
on social media: “[Hacktron] used Opus 5 to pull off the hack…The question that will be asked is, if these three guys can pull this off, what can a nation state do.”
The researchers found a path into OpenAI on July 25 via a flaw in Discourse, the third-party software powering OpenAI’s community forum.
According to a blog the
researchers published
, the entry point was a mundane image upload. When users posted HEIF or HEIC image files (the format iPhones use by default) to OpenAI’s community forum, Discourse passed them through a chain of behind-the-scenes tools to convert them into standard JPEGs. Its first stop was ImageMagick, a decades-old, open-source utility used to resize images. Because ImageMagick’s usual toolkit can’t deal with Apple’s format, it handed the file off to another library called libheif to do the decoding.
Buried inside libheif was a memory bug that exposed a path for an attacker to sneak in their own instructions. In this case, feeding the library a specially crafted image caused it to miscalculate where one image was positioned on top of another, which proved enough to hijack the server.
What may be uncomfortable for the cybersecurity community is that bug had already been fixed months earlier by libheif’s developers. But the fix was never formally flagged as a vulnerability, meaning it never got a CVE (common vulnerabilities and exposures) number, the industry’s standard way to track known security weaknesses. Hacktron says that may explain why the software used by Discourse was still running the vulnerable version.
Notably, the researchers said the Claude model they were using — a special version of Opus 4.8 made available for cybersecurity researchers — couldn’t build a working exploit at first. That changed overnight, when Anthropic released Opus 5.
“Opus 4.8 struggled across several sessions to produce a working exploit,” Hacktron wrote in a
blog post
. “Within hours of Opus 5’s release, we gave it the same problem and it succeeded.”
Once inside the Discourse server, the researchers found another flaw that let them take over users’ ChatGPT and Codex accounts, including those belonging to OpenAI employees.
“We then took over an OpenAI employee’s account, whose Codex was connected to OpenAI’s Github organization,” Hacktron wrote in its summary of the event.
At this point, the researchers alerted OpenAI as well as Discourse, which issued a fix on July 27.
The incident puts a spotlight on where the line gets drawn for model capabilities. Claude Opus 5, the version that ultimately cracked the bug, hasn’t faced any security export restrictions, unlike newer version Mythos 5, which was temporarily
locked down
over concerns about its advanced hacking capabilities.
Those are just the closed models.
Open-weight models are increasingly catching
up to the frontier in cyber capabilities. For example, AI safety nonprofit SaferAI recently found that Chinese company Z.ai’s GLM-5.2 was only a few months behind OpenAI’s GPT-5.5 and Anthropic’s Claude Opus 4.7.
As Hacktron founder
Mohan Pedhapati put it on X:
“AI is reducing the amount of scarce expertise needed to develop exploits. Work that once took months can now take days.”
Topics
AI
,
Anthropic
,
cybersecurity
,
OpenAI
,
Security
When you purchase through links in our articles,
we may earn a small commission
. This doesn’t affect our editorial independence.
Aditya Mehta
View Bio
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
OpenAI caught its models leaving notes to successors to hide bad behavior
Rebecca Bellan
Clean tech startup Fluxnium found a way to tap 50,000 years’ worth of nuclear fuel
Tim De Chant
Salesforce and Nvidia’s new reasoning model is everything the AI labs should fear
Julie Bort
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
- **Source**: [Original Article](https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/)
