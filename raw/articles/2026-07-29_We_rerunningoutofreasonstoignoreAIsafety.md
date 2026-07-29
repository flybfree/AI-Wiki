---
title: We’re running out of reasons to ignore AI safety
date: 2026-07-29
url: https://www.theverge.com/ai-artificial-intelligence/972380/open-ai-hugging-face-hack-ai-safety-warning
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.theverge.com/ai-artificial-intelligence/972380/open-ai-hugging-face-hack-ai-safety-warning
source_feed: The Verge AI
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-07-29 06:02
---

# We’re running out of reasons to ignore AI safety

## Full Article

AI
Report
Tech
We’re running out of reasons to ignore AI safety
In the aftermath of OpenAI’s attack on Hugging Face, experts say it’s time for everyone to take security far more seriously.
by
Robert Hart
Jul 29, 2026, 11:00 AM UTC
Link
Share
Gift
If you buy something from a Verge link, Vox Media may earn a commission.
See our ethics statement.
[STK485_STK414_AI_SAFETY_B]
[STK485_STK414_AI_SAFETY_B]
Image: The Verge
AI
Report
Tech
We’re running out of reasons to ignore AI safety
In the aftermath of OpenAI’s attack on Hugging Face, experts say it’s time for everyone to take security far more seriously.
by
Robert Hart
Jul 29, 2026, 11:00 AM UTC
Link
Share
Gift
If you buy something from a Verge link, Vox Media may earn a commission.
See our ethics statement.
[Robert Hart]
Robert Hart
is a London-based reporter at
The Verge
covering all things AI and a Senior Tarbell Fellow. Previously, he wrote about health, science and tech for
Forbes
.
Earlier this month, OpenAI gave several of its AI models a task: complete a
test
designed to measure their cybersecurity capabilities. It put the systems in a sandboxed environment without an internet connection and set them off to work.
What
happened next
is almost laughably silly — but also, as Adam Gleave, cofounder and CEO of AI safety organization FAR.AI put it, “a visceral example of how misaligned AI could cause harm.” According to OpenAI, the models escaped the sandbox meant to contain them, moved through the company’s internal systems, found a route to the internet, and then started looking for a way into Hugging Face. And why was the agent looking for a way into Hugging Face? They had apparently reasoned that the developer platform might store the answers to the cyber benchmark and that getting them would be a great way to get a high score.
The incident is “a visceral example of how misaligned AI could cause harm.”
In other words, OpenAI’s agent broke out of a supposedly secure environment, traipsed through the company’s systems, got online, and compromised another company’s systems — all to cheat on a test of no particular importance.
This appears to be the first well-documented incident of its kind, or at least the first on this scale. It was both a clear example of a system pursuing a goal in an unintended way and a demonstration that frontier models are now powerful enough for that behavior to have real-world consequences.
The hack was an example of what the AI safety community calls “
specification gaming
,” a behavior also known as reward hacking, said Fazl Barez, an AI safety researcher at the University of Oxford In plain English, it means “the model doing what you asked rather than what you meant,” Fazl said. It satisfies the literal terms of a task while violating the obvious intent and has been
documented
across
many
AI systems. Some researchers
worry
that as systems become more capable, this could produce increasingly misaligned systems, which pursue goals in ways their creators did not intend (like turning everyone into
paperclips
).
“Nothing in that chain is exotic in isolation,” Fazl said. A competent human tester would be able to do all of this, he added. “What is new is that the model did not stop. Older models would likely have hit some barrier and gone back to the user, he said, but this agent just “treated the barrier as part of the problem it had been asked to solve.”
Related
OpenAI’s biggest thread may just be open AI
Nvidia, Microsoft launch open AI security alliance — without OpenAI, Google, or Anthropic
The vibes are off at OpenAI
OpenAI
described
it as “an unprecedented cyber incident,” that “
marks an important moment
for AI safety.” Hugging Face cofounder Thomas Wolf
said
it was a “wake-up call” for the industry. But this is not one of the four horsemen of the AI apocalypse. As cyber incidents go, experts told
The Verge
it was pretty mundane. Nothing the agent did required superhuman abilities. Moreover, frontier systems like GPT-5.6 Sol and Anthropic’s
Mythos
are known to be capable coders, are already thought to have been
misused
numerous times, and AI tools
already allow hackers
to scale up and refine attacks on a massive scale.
Could it be hype? The industry has spent months
amplifying claims
about the dangerous capabilities of its top models, particularly when it comes to cybersecurity. It is the stated reason why companies like OpenAI and Anthropic have withheld their most capable models from the general public and partly why the
Trump administration hurriedly moved
to apply export controls to them.
Are you an AI safety researcher or frontier lab employee? You can contact me securely and confidentially via Signal at
robhart.01
. My
X
DMs are also open.
If this is hype, however, it has not gone entirely in OpenAI’s favor. In the days since, the attack has
produced a rare moment of unity
across much of the US tech industry about the importance of open-weight AI systems and the need to take AI security more seriously. These concerns were underscored further by the
release
of Kimi K3, a highly
capable open-weight model
from China. A broad coalition of companies including Nvidia, Microsoft, and SpaceX argued that the incident showed why defenders need access to the most capable tools available, rather than being forced to rely on proprietary providers whose built-in safeguards can limit their effectiveness in high-stakes security work. OpenAI, Anthropic, and Google were notably absent from the coalition’s founding membership.
“Anyone who’s been paying attention has noted that capabilities are only going in one direction.”
OpenAI’s account of the incident undeniably fits a broader industry narrative about the dangerous capabilities of frontier models. Even so, several details make the incident difficult to dismiss as merely self-serving. Foremost, it is an example of a problem the AI industry has warned about for years — and one OpenAI could have reasonably been expected to anticipate. The episode also handed an unexpected boost to a major Chinese competitor, whose model played a prominent role in containing the breach, while exposing OpenAI to significant legal, regulatory, and reputational scrutiny. That Hugging Face appears keen to work with OpenAI and, publicly at least, has remained fairly relaxed about the whole thing may have limited the fallout. Most of the experts
The Verge
spoke to similarly cautioned against reducing the incident to hype.
“It’s a pretty useful warning shot in terms of demonstrating both unintended consequences and just how capable these models are,” said Seán Ó hÉigeartaigh, a professor at Cambridge University’s Leverhulme Centre for the Future of Intelligence. “Anyone who’s been paying attention has noted that capabilities are only going in one direction, and that is improving significantly over time in a way that I think is perhaps less obvious to the everyday user of something like ChatGPT.”
Still, it would be wrong to interpret this warning as a sign AI systems are about to slip human control, or that containing them is impossible, says Lin Li, an AI safety researcher at the University of Oxford. “The better lesson is that safety has to move from evaluating isolated actions to evaluating whole action sequences, environments, and operational controls,” Li says.
A crucial next step is for AI labs to be investing more heavily in securing their own systems. “There’s a clear need for AI companies to beef up the security of their internal deployments,” Gleave said, likening the current practice of responding to reward hacking incidents as they arise to a game of whack-a-mole that is becoming less and less tenable as stakes rise. Adam Chan, a research fellow at tech policy research center GovAI, said companies should consider airgapping their machines — physically isolating them from the internet and other networks — “until they’re sure about the model’s capabilities.” Intensifying work on alignment, which ensures systems reliably follow human intentions, and more rigorous testing “to surface these issues before putting models in environments where they have the tools to be able to do these things,” would also be good ideas, he said.
As model capabilities increase, experts warn that we can’t rely on technical safeguards alone. Peter Wallich, a former UK AI Security Institute official, said the incident illustrated that point: “Two multibillion dollar companies just tried this approach and — self-evidently, based on their own reporting — failed.”
One of the biggest priorities should be ensuring outsiders can see what is happening inside frontier AI labs. “We only know about this incident because OpenAI chose to tell us,” said Patrick Levermore, at the Centre for Long-Term Resilience, a British think tank. “A good safety regime shouldn’t depend on voluntary disclosure.” The need is especially acute when, as Wallich noted, the conduct in question “would be a crime if done by a human.” Ó hÉigeartaigh pointed to whistleblower protections, third-party audits, and mandatory reporting of serious incidents as possible ways to provide that visibility, stressing that oversight must span the entire development lifecycle rather than begin only once products reach the market. OpenAI said that one of the models being tested has not been released yet.
“A good safety regime shouldn’t depend on voluntary disclosure.”
Lots of this presumes the companies themselves know what’s happening inside their systems. In this case,
reports
suggest OpenAI was unaware its own agent was behind the days-long cyber campaign at Hugging Face and did not notice until well after the threat had been contained and the FBI contacted. There are still many details about the hack that are unknown or have not been made public. In an
update
on social media, OpenAI said it is conducting a review and will publish a technical report of its findings “in the coming weeks.”
Whether the warnings raised by the Hugging Face incident produce any lasting change, or join the long list of warnings the tech industry absorbs without meaningfully altering course, remains uncertain. For now, at least, it does appear to have alarmed industry insiders and pushed US lawmakers to
consider new rules
before the next containment failure. The incident also added to a broader sense of unease over the speed of AI development, which deepened in the days that followed as employees from leading US labs
signed a statement
backing coordinated global governance — including a potential slowdown in frontier AI development.
The prevailing view of those
The Verge
spoke to was that this hack marked the start of a new class of risk, even if its significance may only become clear in hindsight. One former government AI policy expert, who asked not to be named because they were not authorized to be quoted by name, described it as a “red line,” the kind of watershed moment we may later look back on as marking a new, riskier stage in our relationship with AI. They hope it will force the tech industry to take the management of frontier systems more seriously and spur governments to think more deeply about oversight before a less benign breach occurs. Their fear is that it will instead join the long list of warnings about AI’s growing capabilities that were recognized, discussed, and ultimately left unheeded.
That may prove overstated. But if this is a warning, we should consider ourselves lucky the AI agent was only trying to cheat on a test.
Follow topics and authors
from this story to see more like this in your personalized homepage feed and to receive email updates.
Robert Hart
AI
OpenAI
Report
Tech
Most Popular
Most Popular
Is it illegal to trick the US government into wiping your phone during a questionably legal search?
Hugging Face is being used to easily undress women and children
Apple launches ‘Upgrade’ program to lease new devices
Smart rings are looking like my kind of AI gadget
AI’s finally expensive enough to make Wall Street nervous
The Verge Daily
A free daily digest of the news that matters most.
Email (required)
Sign Up
By submitting your email, you agree to our
Terms
and
Privacy Notice
.
This site is protected by reCAPTCHA and the Google
Privacy Policy
and
Terms of Service
apply.
Advertiser Content From
[Sponsor Logo]
This is the title for the native ad
[Sponsor thumbnail]

## Metadata
- **Source**: [Original Article](https://www.theverge.com/ai-artificial-intelligence/972380/open-ai-hugging-face-hack-ai-safety-warning)
