---
title: When AI goes rogue - Harvard Gazette
date: 2026-08-06
url: https://news.harvard.edu/gazette/story/2026/08/when-ai-goes-rogue/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://news.harvard.edu/gazette/story/2026/08/when-ai-goes-rogue/
source_feed: AI Universe Explorer
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-08-06 00:09
---

# When AI goes rogue - Harvard Gazette

## Full Article

It has become a science fiction trope come to life.
Tech giants OpenAI and Anthropic disclosed in July that versions of their AI models broke through safeguards known as a “sandbox, gained access to the internet, and hacked servers of outside companies during internal tests of their cybersecurity capabilities.
This week, AI Security Institute, a U.K. government research entity reported additional incidents,
saying
AI agents created fake online personas in order to improperly access real people and companies during security tests it conducted on the two tech firms.
OpenAI
CEO Sam Altman characterized the July breach as an “unprecedented” and “significant security incident” caused by rogue AI agents. Its
investigation
has since uncovered evidence of additional breakouts.
Anthropic
blamed human error involving an evaluation partner.
In this edited conversation,
James Mickens
, Gordon McKay Professor of Computer Science at SEAS and director of the Berkman Klein Center at Harvard, explains what these breaches mean for the future of AI security.
Gazette: How plausible are the explanations offered by OpenAI and Anthropic?
James Mickens:
It’s hard to say. I think it is very commendable that both OpenAI and Anthropic decided to release public incident reports about what happened. They could have very easily kept this to themselves and not let people know that these models have these autonomous abilities to get past these sandboxes.
However, because the public doesn’t really know the details of what happened, it’s hard to fully verify the timeline and the narrative.
The explanations put out by OpenAI and Anthropic are certainly plausible. Those public-facing stories are certainly what
could
have happened. Is that literally what happened? Was there anything left out? We don’t know.
We do know both companies have talked to third-party security companies to validate stuff. But we don’t really know what’s going on.
And this points to one of the tensions with this dangerous technology. One can understand why OpenAI might not want to say, “Here’s a detailed description of our sandboxing environment.”
But on the other hand, there’s this very well-known security principle, which is that sunlight disinfects. The more eyes you have on something, the more brains you have to try to find problems.
Two of the biggest players in AI report similar incidents within weeks of each other. Is that troubling?
Yes, it’s quite concerning. I would also say these are not threats that the security community and the AI safety community are just realizing were possible.
Here at Harvard, we’ve been saying for a long time that security researchers need to be thinking more critically about strengthening sandbox mechanisms and making it more difficult for models to break out of them. Last year, my research group published a paper specifically about how to create new types of software and hardware to make sandbox escapes more difficult.
Even as recently as last year, there were some people saying, “You’re guarding against a sci-fi eventuality. You’re worried about things that really are not top of mind for people using these AI systems in the real world.”
Yes, there are frontline risks that are harmful and relatively mundane, but then there are other risks that are exceptionally pernicious and quite alarming in terms of how quickly they can affect huge numbers of people in society.
For example, what would happen if one of these models tried to break into the power grid or tried to tamper with financial systems to affect the stock market? These are very real concerns.
I think with what we’ve seen over the past week or so, we should be worried about this problem more generally.
“These models are very difficult to understand.”
These models are very difficult to understand. There’s a whole field of AI interpretability, which seeks to understand why models do the things that they do. They’ve made some progress, but it’s still an open challenge to guarantee that a model will always act in ways that are aligned with human preferences.
So yes, these incidents are quite concerning.
Is that a concern about the technology or about the people overseeing the technology and their priorities?
Both. First and foremost, there are technical challenges in defining what alignment means, determining whether models are acting in aligned ways, and then enforcing human-defined alignment policies when models misbehave.
Those challenges are technical inasmuch as they require us to build new software and new hardware to enforce alignment policies.
However, there are also social problems of governance. Who are the humans who decide what misalignment and alignment mean? Are they mostly people who live in the U.S.? Who work for U.S. companies? Are they people who live in China, or in India, or in Brazil? Are these questions that should be answered by companies or should governments be doing this? And how do we ensure international coherence of approaches toward these things?
So, there are some very thorny technical and socio-technical issues here that are intrinsically difficult to solve and that require thoughtful responses that are at odds with the breakneck speed that companies want to move at.
Do these incidents suggest that AI models have now moved beyond human control?
I would say these incidents demonstrate that even frontier lab companies cannot guarantee model alignment in all scenarios. We’ve actually known for some time that defining aligned behavior is difficult, enforcing aligned behavior is difficult, and that models are already sufficiently complicated and sophisticated to press us on those two issues.
“We have safety problems now. We can’t wait to think about this.”
In other words, AI safety risks are not a theoretical problem. They haven’t been for quite some time. And it’s naive for people to think that we can afford to not think about safety risks because we want these AIs to solve cancer or things like this. We have safety problems now. We can’t wait to think about this.
Given the winner-take-all stakes in AI, could such unflattering disclosures be a kind of humblebrag by OpenAI and Anthropic to show how cutting-edge their AI models are?
Yes, it’s certainly possible.
This is why a lot of security researchers, a healthy minority, take all of these releases with a grain of salt because first of all, the public has no way of knowing whether these types of incidents have happened 100 times this year. And we’re just hearing about the recent ones now because why?
Could it be that all the companies want to race toward Artificial General Intelligence [AI capability that matches or exceeds human-level skills] and claim the AGI mantle first? AGI is less a crisply defined technical achievement and more of a “we’ve decided that we have it and now we’re going to claim it.”
And so, cynics in the security community are saying, “We bet that sandbox escapes have happened before. You just didn’t tell us. The reason you’re telling us about these sandbox escapes now is you’re trying to pave the way for this declaration of AGI unilaterally, and you’ll be able to point to this press release and say, ‘See? That was the first glimmering of our model which has AGI.’”
There’s a lot of stuff these companies put out that technical folks and policy folks don’t take fully at face value.
Is it too late to impose regulations on AI to try to prevent this from happening again?
It’s not too late to impose regulations.
Getting the right regulations in place will be tricky because this is a socio-technical problem that requires both robust technical mechanisms for sandboxing models and societal consensus on what the trade-off should be between speed of AI development and reining in potential harmful behaviors from these models. We don’t have that second part either.
Different reasonable people will have different ideas of how we should be striking those trade-offs. The important thing, though, is that we at least have to have the conversation seriously. That’s, I think, the big thing.
What types of interventions might be most effective?
There’s been a variety of mechanisms, technical, legal, and otherwise, that have been proposed for making models safer.
I think a key challenge, though, is how do we ensure that the model vendors are actually using these mechanisms? How do we get more insight into what happens when something goes wrong? How do we understand who should be held accountable for these things?
It’s important for us to not be unnecessarily restrictive. We do want to allow these companies to engage in cutting-edge research. But, at this point, the risks are getting so large and so unavoidable that it would be irresponsible for us as a society to not think about how to reckon with these things.
It’s not as if we have no levers that we can push to try to make safety better. There are a lot of people who are thinking about how do we interpret what models are doing, how do we steer them to act in ways that are more societally aligned, and so on.
There are also regulators and people in government thinking about this too, so it’s not as if there aren’t people who care about AI safety risks.
Hopefully, this past week can be a fulcrum moment where we have a series of incidents that are so clear in terms of their implication that society will have to organize around this and try to think critically about AI safety.
Share this article
Share on Facebook
Share on LinkedIn
Email article
Print/PDF

## Metadata
- **Source**: [Original Article](https://news.harvard.edu/gazette/story/2026/08/when-ai-goes-rogue/)
