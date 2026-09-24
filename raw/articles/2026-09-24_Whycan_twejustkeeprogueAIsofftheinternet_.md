---
title: Why can’t we just keep rogue AIs off the internet?
date: 2026-09-24
url: https://www.theverge.com/ai-artificial-intelligence/999881/why-cant-we-airgap-rogue-ai-agents
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.theverge.com/ai-artificial-intelligence/999881/why-cant-we-airgap-rogue-ai-agents
source_feed: The Verge AI
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-09-24 10:14
---

# Why can’t we just keep rogue AIs off the internet?

## Full Article

AI
Report
Tech
Why can’t we just keep rogue AIs off the internet?
Air-gapping AI to keep it away from real-world targets makes testing safer, but less useful.
by
Robert Hart
Sep 24, 2026, 2:30 PM UTC
Link
Share
Gift
[STK414_AI_CVIRGINIA_2_C (2)]
[STK414_AI_CVIRGINIA_2_C (2)]
Image: The Verge
AI
Report
Tech
Why can’t we just keep rogue AIs off the internet?
Air-gapping AI to keep it away from real-world targets makes testing safer, but less useful.
by
Robert Hart
Sep 24, 2026, 2:30 PM UTC
Link
Share
Gift
[Robert Hart]
Robert Hart
is a London-based reporter at
The Verge
covering all things AI and a Senior Tarbell Fellow. Previously, he wrote about health, science and tech for
Forbes
.
AI agents
keep getting loose
, escaping supposedly secure tests to
attack real-world targets
,
commandeer obscure wikis
, and
leave instructions for other agents
to follow. Researchers are testing these systems precisely because they might behave in unpredictable, even dangerous, ways. So wouldn’t it be safer to just keep the agents off the internet?
“A strict air gap reduces realism ... [It’s a] trade-off, not a fundamental technical issue.”
In theory, yes. Researchers can isolate the computers running AI tools from the internet and other outside networks, a technique known as air gapping. That can mean physically removing or disabling cables and wireless hardware and using “dumb” peripherals, with particularly sensitive setups using Faraday cages or other shielding to block electromagnetic signals from getting in or out. Done properly, an air-gapped system would offer agents no straightforward route to external targets, or outside systems any straightforward route in, making it much harder, if not impossible, to pull off attacks like the one OpenAI’s models
launched against Hugging Face
.
But in practice, a perfectly sealed box makes for a rather limited laboratory, particularly when the aim is to assess how an AI will perform in the real world. While some AI experiments can be run on air-gapped machines, realistic evaluations often require access to external services, APIs, and digital infrastructure, explained Thorsten Holz, a scientific director at the Max Planck Institute for Security and Privacy in Germany. “A strict air gap reduces realism,” he said, describing the decision to air gap as a “trade-off, not a fundamental technical issue.”
Related
Inside the suddenly explosive world of AI safety
Rogue AI aren’t science fiction anymore
We’re running out of reasons to ignore AI safety
Ruizhe Li, an assistant professor in the school of computer science at the University of Birmingham in the UK, likened complete isolation to testing AI in an “artificial vacuum,” potentially undermining the value of the evaluation itself. “We will end up testing a neutered AI model, which blinds evaluators to how the AI model behaves, fails, or executes tool-use exploits in realistic deployment settings,” Li said.
Realism isn’t the only tradeoff. Li said air gapping is costly and can slow research to an absolute crawl, turning what would be quick iterations into “a slow logistics hurdle.” Some experiments also become “substantially harder” under a strict air gap, Holz said. That friction may be justified for risky experiments, but applying it for everything would slow down the development of new models, said Maksym Andriushchenko, a principal investigator at the ELLIS Institute Tübingen in Germany.
And even if researchers wanted to air gap everything, Andriushchenko questioned whether enough secure infrastructure exists to do it at the scale of frontier AI labs.
“This all sounds very sci-fi, but is theoretically possible.”
It would not eliminate every risk posed by AI, either. Agents could still compromise systems inside of the isolated environment, Holz said, and could theoretically produce “malicious artifacts that could be dangerous if moved outside.” Moreover, air gapping “does nothing to diagnose or resolve the latent risks waiting inside the model,” Li said.
There’s also no guarantee that an air gap would remain completely sealed. Someone from the outside could always breach the gap, as happened with
Stuxnet malware
— a cyberweapon
reportedly
developed
by Israel and the US to sabotage Iran’s nuclear program — which was transmitted via a USB drive. Information may travel in the other direction, too.
Researchers
have
repeatedly
demonstrated
ways of turning internal computer components into transmitters, which could be a problem if shielding is not perfect. “This all sounds very sci-fi, but is theoretically possible,” Andriushchenko said.
That sort of convoluted escape route has become a focal point for online discussions about whether an advanced AI could escape containment. OpenAI researcher Noam Brown recently ignited the debate by
suggesting
on X that two air-gapped machines could theoretically communicate by manipulating their CPU temperature and reading the changes. “You could even go as far as to say, ‘Well, we should air gap the computers.’ And I’m not convinced that that would be sufficient,” he said. The idea was met with skepticism, and ridicule, on social media, with more generous critics noting the large gap between such a communication method being possible and a pair of AI systems discovering and exploiting it, particularly as the technique would yield painfully slow data transmission speeds.
A sufficiently advanced AI might not need to resort to an elaborate escape route. Humans may become convinced to bridge the gap for it. AI safety researchers have
worried
about such a possibility for years, and recent incidents have provided
concrete evidence
that models can engage in attempts at social engineering.
“This tradeoff deserves much greater scrutiny, and we have seen how easily things can go wrong.”
Air gapping is but one means of safeguarding AI systems. “Relying on isolation as a blanket safety solution creates a false sense of security,” Li said. It should be used alongside other measures, like understanding the inner workings of models, ensuring they are aligned, and guarding against human error, the mundane point of failure behind many recent rogue AI incidents. “In practice, testing exists on a spectrum,” he explained, with the field relying on a “tiered containment model rather than an all-or-nothing approach.”
Extreme isolation does have its place, though. Stephen Casper, a computer scientist and assistant professor of public policy at the Harvard Kennedy School, described air gapping as a “great idea” for sensitive systems, pointing to its use in nuclear facilities. While not ruling out the possibility that an advanced AI could find some novel way to escape, Casper said at that point we should probably be more worried about prosaic means of breaking containment, such as compliance failures or human error.
Recent
incidents
raise questions
over where AI labs are
drawing that line
. Many
breaches
involved
models being tested for their
cybersecurity abilities
, and in many respects they
performed exactly as designed
. The problem was that they did so outside of the boundaries researchers intended to set.
Holz said AI “evaluations often prioritize realism and convenience,” but argued agents explicitly designed for offensive cyber capabilities warrant tighter safeguards, potentially including strong isolation and strict monitoring as a default. “This tradeoff deserves much greater scrutiny, and we have seen how easily things can go wrong,” he said.
Follow topics and authors
from this story to see more like this in your personalized homepage feed and to receive email updates.
Robert Hart
AI
Report
Tech
Most Popular
Most Popular
Anthropic’s biolab made a discovery it’s comparing to Crispr
Meta’s next VR device isn’t a headset — it’s glasses
Meta ditches the camera on its newest smart glasses
Meta Connect 2026: The 7 biggest announcements
Meta is making a standalone Muse AI gadget
The Verge Daily
A free daily digest of the news that matters most.
Email (required)
Sign Up
By providing your information, you agree to our
Terms of Use
and our
Privacy Policy
. We use vendors that may also process your information to help provide our services. This site is protected by reCAPTCHA and the Google
Privacy Policy
and
Terms of Service
apply.
Advertiser Content From
[Sponsor Logo]
This is the title for the native ad
[Sponsor thumbnail]

## Metadata
- **Source**: [Original Article](https://www.theverge.com/ai-artificial-intelligence/999881/why-cant-we-airgap-rogue-ai-agents)
