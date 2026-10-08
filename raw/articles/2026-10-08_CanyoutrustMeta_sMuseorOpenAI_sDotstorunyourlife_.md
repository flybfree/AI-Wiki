---
title: Can you trust Meta’s Muse or OpenAI’s Dots to run your life?
date: 2026-10-08
url: https://www.theverge.com/podcast/1007408/meta-muse-openai-dots-ai-agent-race-privacy-free
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.theverge.com/podcast/1007408/meta-muse-openai-dots-ai-agent-race-privacy-free
source_feed: The Verge AI
ai_relevance: include
ai_topic: model-release
ai_reason: watchlist match: Meta Muse
scraped: 2026-10-08 09:18
---

# Can you trust Meta’s Muse or OpenAI’s Dots to run your life?

## Full Article

Podcasts
AI
Tech
Can you trust Meta’s Muse or OpenAI’s Dots to run your life?
The future of computing might be always-on, autonomous agents, but should we hand Meta or OpenAI this much persona data?
by
Nilay Patel
Oct 8, 2026, 2:00 PM UTC
Link
Share
[Nilay Patel]
Nilay Patel
is editor-in-chief of The Verge, host of the
Decoder podcast
, and co-host of
The Vergecast
.
My
Decoder
guest today is Hayden Field,
The Verge
’s senior AI reporter, and we’re discussing the new wave of consumer-friendly AI agents.
If you’ve been paying attention to this space, you know AI enthusiasts have been using agents for a minute now — homebrew OpenClaw setups
led to a surge in Mac Mini sales
earlier this year. But the launch of Meta’s Muse, OpenAI’s Dots, and xAI’s Grok bot has brought easy to use agents to millions.
Muse and Dots have had the highest-profile product launches, and they’re fascinating to pit against each other. Both Meta and OpenAI have decided to pitch these agents to mainstream users and businesses
in the form of cute, animated mascots
.
Verge
subscribers, don’t forget you get exclusive access to ad-free
Decoder
wherever you get your podcasts. Head
here
. Not a subscriber? You can
sign up here
.
These can do everything from the boring — restaurant reservations and inbox triage — to more sophisticated tasks. In OpenAI’s cases, the company is even
offering “specialist” Dots
for marketing, legal work, and accounting.
Muse, notably, is free, while Dots are not. So you’ll hear Hayden and me get into why Meta, which still doesn’t have a frontier model of its own, might have a meaningful edge here because it’s so much better at making and distributing consumer products.
There’s also a huge
Decoder
-style tension wrapped up in the agent race: a conversation about what AI is good at today, what it still can’t do, and then the privacy and security implications of handing over your credit card information, your email inbox, and other sensitive hard drive data to an AI that
might be able to do things for you
without every requiring an app or a phone in your hand.
That might be the future of all computing, but it’s not at all clear if most people want to hand over the data to make it happen.
Okay:
The Verge
’s Hayden Field on Muse, Dots, and trusting AI agents. Here we go.
This interview has been lightly edited for length and clarity.
Hayden Field, you’re the senior AI reporter here at
The Verge
. Welcome back to
Decoder
.
Thanks so much.
I’m excited to talk to you. This time there isn’t any wild interpersonal drama. No one’s feelings have been hurt. I would say Elon Musk tried to hurt some feelings and didn’t get there. Alexandr Wang from Meta has maybe been taking some shots, but none of the
Real Housewives
stuff we usually end up talking about when you’re on the show.
It’s been a bit of a pause in the soap opera antics for now, which I’m really grateful for.
Yeah, just some good old-fashioned product competition in the marketplace. Let’s see who wins and loses, and maybe everything will kill us all in the end. But, for now, cute mascots.
There’s a lot going on. Let’s start at the start. Hayden, you were at OpenAI DevDay in San Francisco. The company announced Dots, which is their new agent platform with a cute mascot. That happened just a few weeks after Meta Connect, at which the company was all in on Muse, their agent platform with an adorable mascot.
Tell us about the state of the industry right now. Everyone’s very excited about agents. What’s going on?
It’s funny to me because I’ve been covering agents for so long. I remember that in 2022, it was the year of ideation — that’s what tech leaders called it, referring to agents. They were just ideating. They were thinking about what it could look like. There were a lot of references to Jarvis from the Marvel Universe.
They called 2023 the year of deployment: “Let’s try things, let’s deploy and learn more about what’s failing.” Which meant pretty much all of them were failing at the time. Then we had 2024 and 2025. They didn’t have any names for those years, but agents were still pretty bad, as we saw.
2026 seems, to me, like the year of the beginnings of actually useful AI agents for the consumer, like always-on autonomous agents. Obviously, OpenAI was the start of all of this. But what’s interesting to me is that one man, Peter Steinberger, was able to create an actually useful AI agent for the consumer with OpenClaw — an always-on tool, despite its privacy flaws. It had a lot of privacy and security issues.
But it was an agent that was useful enough that people still wanted to use it anyway and try to find ways around these privacy issues that it was having. That inspired these companies to say, “If one man can do this over the course of one weekend, we’ve really been slacking. We have to get it together.”
OpenAI hired that guy, and now we have Dots. Meta, of course, was working on its own version of this and put it out sooner with Muse. They’re basically both always-on, autonomous AI agents that these companies are peddling as a way to be your personal assistant in a lot of ways.
The idea is to use them for booking flights, booking dinner reservations, buying gifts for people, but not only that. Some of them, Dots in particular, are kind of going further to be your work personal assistant and we’ll get into that in a minute.
But this is where OpenAI and Meta are warring right now. They’re trying to present these two AI agents as a little bit different from each other, even though they’re essentially the same.
Just broadly speaking, to define some terms, we’re gonna keep saying “agent,” and what we mean here is an AI model wrapped in a harness that lets it use a computer.
Right. The way that I describe AI agents usually is an AI tool that can complete multi-step complex tasks on your behalf without you hand-holding it the whole time.
I was a personal assistant in one of my first jobs in New York, so I would’ve gotten fired if every time my boss asked me to book a flight for her, I said, “What time? Also, what’s your SkyMiles number? Also, what’s your loyalty number again, for this other thing? Oh, do you want me to try to get you first class?”
They want you to have common sense and just book the flight. This is what they’re pitching these AI agents as — things that can work on their own mental kind of scratchpad in the background and not ask you every single time there’s a step. They can complete multi-step processes in the background, doing their own reasoning, and then present you with a completed task.
That’s the big idea. Just to say it clearly, both Muse and Dots come out of the OpenClaw lineage, which is a technical approach to building an agent, right? There are a lot of different ways you might be able to accomplish “It’ll remember your SkyMiles number and book you a flight.” But the way everyone’s going at it now is the idea of a harness around a model. That was the big innovation in OpenClaw, and the computer OpenClaw was using was often your own Mac Mini on your own network using a wide-open browser with your own data, which is where a lot of their security problems came from.
It’s the same model with Muse, only it’s a little Linux computer that Meta’s giving you in the cloud. It’s the same model with Dots, although the way ChatGPT is set up with Codex is very complicated, and that computer could be in a lot of different places.
But this notion that what you really need is a computer with a browser and some harness is gonna direct a model to do a bunch of stuff for you using that computer, that’s what we’ve landed on today, and it just seems to be the default winning model.
Right.
Are all of these things just riffs on OpenClaw? Are they the same as OpenClaw?
You could say that. They’re different technically. Meta keeps saying, “We did build this from scratch, but it was inspired by OpenClaw.” There are
a lot of similarities there
, but they did say that they built it from scratch. Then, of course, OpenAI hired the creator of OpenClaw, so there’s probably a lot of similarities there as well for Dots.
The reason I wanted to stay there for one second is that I think it’s important to identify the fundamental technical approach that is happening with these agents, because there’s a lot of different ways it could have gone, and the whole industry has picked this approach. What you need is a web browser, a harness, and a model that can go use that web browser.
What’s really interesting to me is that Meta has done a really good job on top of that fundamental model of making a cute consumer product. Meta is good at consumer products. Obviously, Instagram and Facebook and the rest are undeniably good consumer products. People really like them.
For all of Meta’s failings in VR, I always thought the Meta Quest has been a great consumer product. You take it out of the box, it helps you use it, you can have fun with it right away. Whereas Dots seems like it’s kind of made for software engineers, but you can also plan a wedding in it.
I’m wondering if that’s how you see it. That one is an enterprise product with a little consumer gloss on it, and then Meta obviously is just a dead-ahead consumer product.
What’s different here is that OpenAI needs money a lot more than Meta needs money. The products are honestly pretty similar, it seems like. The difference is that OpenAI is marketing it to be an enterprise-friendly product a lot more than Meta is. Muse is just a consumer-facing product.
Meta is happy with that. The goal is to make Muse as easy to use as humanly possible. One-tap downloading, just putting it in your face literally everywhere. Even when I went to my Instagram profile the other day, there was a pop-up for using Muse. They’re trying to make it free, accessible, and super easy to broaden the audience.
They want anyone to be able to just use it with one click and get used to it. They’re trying to flood the market with AI agents and make it normal and have their own ChatGPT moment, if you will, for AI agents. They want Muse to be that. Now, with OpenAI, they’re still marketing it as a consumer-facing product. When you’re using ChatGPT, if you have the right subscription, it’s right there.
It says, “Use your Dot to do this, that, and the other.” They really want you to go for it as a consumer, as long as you’re paying. This is for their $100 to $200 a month subscription tier, unlike Meta. That’s why there’s a huge difference here. For OpenAI, it seems like they don’t have the money to just front-load all of this and say, “Use it for free. No problem. We’ll catch up with you later.”
OpenAI wants this to be a money-making product, and that’s why they’re marketing it to the enterprise. They talked a lot about privacy to try to set it apart from Meta’s Muse. They talked a lot about what you could do with this as a knowledge worker, whether you worked in marketing, graphic design, software engineering, product, and tons of different industries. They gave examples of how you could use this as an assistant, as a coworker. Sam Altman even referred to it as like a
“chief of staff.”
He didn’t want it to be just an assistant. He wanted it to be your chief of staff.
Something else that I thought was interesting is that Sam Altman seemed to subtly dig at Meta on stage a few times during DevDay. One of the times he said, “Look, I don’t want this to be just something that’s used to book flights or plan things with friends and look at your calendar. I want this to go beyond that and to really do knowledge worker tasks, things that you in your industry would need a niche assistant to perform.”
That’s why they also introduced specialist Dots that are good at marketing, legal analysis, and things like that. They’re really going for the enterprise angle here, but I think it’s also because they need money ahead of their IPO, obviously.
Yeah, the revenue piece — that it’s only for paid customers at their higher tiers — is really interesting. OpenAI’s tiers are very confusing, but it’s $100 and up, and that’s just going to keep a lot of people from using Dots at first.
The flip side of that is OpenAI does have a lot of customers who are paying them a lot of money, and if they can get those customers to start using Dots, then those customers will be on their agent platforms and maybe you will get some lock-in.
You’ve given those agents a lot of data. They’re part of your workflows, and that might solve the problem I think we’ve seen all the frontier labs have, where a new model comes out and it’s slightly better than the competitor model, and everyone switches for six months, and the next new model comes out and everyone switches back.
Is there some thought that these agent platforms create lock-in — create actual loyalty on top of just the models being better?
Yes. They’re basically hoping that they can build a moat with their users for these things. If Meta and Google already have super easy integrations with all of each company’s existing tools and services, they can easily keep you there.
For example, I have an Apple iPhone, but I use almost exclusively Google apps. So if Google had an AI agent that I was using every day, it would be a little tough for me to switch. That’s what they’re hoping for here.
Meta is hoping that they can get you so into the Muse ecosystem that it would be tough for you to switch, and maybe one day you do have to pay. With OpenAI, they’re trying to get you locked into their ecosystem right away. Even though you have to pay up front, they’re thinking, “We have integrations with almost every tool and service. Maybe it’s not as good as the company that owns that tool and service, but we have the variety and the breadth.”
They’re going for quantity here. One of their employees told me that. They said, “Maybe our Gmail integration, for example, isn’t gonna be as good as Google’s, but we have a Gmail integration and an Outlook integration and X, Y, and Z.” They’re going for just the power of choice and the fact that power users will hopefully stay in this moat.
It’s funny, you mentioned Google. Google
announced
an agent called Gemini Spark. We should mention that SpaceXAI, the very coherent company that everyone understands, has an
agent called Grok Bot,
which it is promoting heavily. People seem to like it. It was built by the Cursor team, which SpaceX acquired.
There’s a lot of this going around, but it seems like Meta really got there first with a consumer product that people could understand.
Obviously, Grok Bot and Dots are much more enterprise-focused, coding-focused. Why was Meta able to get there first?
From all my reporting on Meta, they’ve been behind in AI for a while, and Mark Zuckerberg basically said, “We’ve got to lock in and make a product that people are gonna use on our platforms.” Alexandr Wang apparently was more looking to create a frontier model that was gonna compete with the other leading frontier models.
He says, “We have to think long-term. We have to think superintelligence.” But Zuckerberg says, “No, we gotta think cold hard cash, as in getting people to use stuff on our own platform.” Where they met in the middle was an AI agent that people would use on the Meta platforms, but that still represented a huge step forward, they hoped, for AI systems and what they could do in the everyday world.
This is a fascinating dynamic in that Meta still doesn’t have a frontier model. I don’t think anyone at Meta is claiming that the Muse Spark model competes at the frontier of GPT-6, but their product is better, and certainly they have a massive distribution advantage. They don’t have to pay for advertising on Meta platforms, and OpenAI does, and certainly they have a consumer design advantage. Meta is just better at consumer products.
Does that change how you feel about the dynamics of competition in AI at all? For so long, it’s just been about the capabilities at the frontier, but now it’s a little bit about marketing. It’s a little bit about product design.
You don’t have the best model, but you made a consumer agent product and you connected it to giving everybody a computer in the cloud, so now it can actually do things for you, and its frontier capability is actually not the important thing. It’s its capability.
I think the more money and power you have at one of these companies, the more get mentally farther away from what the average consumer wants. Let’s say the average consumer does want an AI agent, which many of them don’t, as we know.
But let’s say they do. If they do, they’re going to want it to be free or cheap, and they are going to want it to be safe to use without creeping them out too much. They’re willing to deal with a little bit of creepiness in order for it to be free, but not too much. Meta’s Muse has made headlines about
some of its privacy issues
that have gotten a little bit above that comfort level for some users.
That’s probably why OpenAI at DevDay made a lot of remarks about privacy and the importance of that, especially if they’re trying to court enterprise users with their AI agents. Right now these companies, especially Meta, are trying to flood the market and create a mass market appeal for this stuff. Similar to how ChatGPT became the default AI chatbot, Meta wants to be that for AI agents, and they feel very hungry about it. They want to create a ChatGPT moment for this technology by making Muse the default for the general public.
There’s something really interesting about the idea that a less-than-frontier model wrapped in a better product is actually going to be the success story here versus a bleeding-edge frontier model that is a little bit harder to use.
There’s some dynamic in there that is the history of all consumer tech products, right? The worst product that’s easier to use often wins, but we haven’t seen that yet in AI.
Right. That’s really important to note here because not everyone needs the bleeding-edge frontier model. Software engineers do. They see a huge difference with coding prowess from one model to another, and that’s why they’re always switching. But the general public, if they’re using an AI agent, as long as it’s useful, they’re good.
However, not many of them are useful yet. We’re still testing Muse and Dots ourselves. For Muse, I saw a couple anecdotes yesterday that it had a big flop for a day or so. People felt like the capabilities got a lot worse. For Dots, the jury’s still out. We’re still testing it.
It depends on what industry you’re in and what you’re really using this stuff for. That’s why OpenAI is going for enterprise, because it makes money and they’re confident that their agent is going to be more and more helpful in these niche industries.
That’s also why they launched specialist Dots, because as we know, the more specialized, niche info you feed into an agent or model, the better it’s going to perform. They don’t want to have that imbued into every single general-purpose agent. It’s just too pricey and too compute heavy, so they say, “You know what? Let’s launch these specialists.”
I feel like you and I talk about consumer versus enterprise adoption of AI every time you’re on this show, and here it seems very important to note that OpenAI asking people to pay a lot of money and asking people to use it primarily in enterprise context is gonna overcome what I think of as the brittleness problem, just because enterprise and business customers have a lot of economic incentives to figure out how to make something work.
If I’m paying OpenAI $100 a month, and I’m using the marketing Dot to solve some marketing automation, and it doesn’t work the first time, it is very likely I will try again. Because if I get it right, then maybe I’ve saved some money or some time in my business that is really good, and I’ll do it again, and eventually that will lead to more revenue for me, the business owner. What I know about consumers is that the first time it doesn’t work, they just walk away. They have no incentive to try again to overcome frustration or brokenness.
We’ve seen this happen with Muse now a few times. I’ve seen it myself with Muse, where it pops open a browser and tries to do something, and it runs into a brick wall or a CAPTCHA or
Amazon blocking it
, and it says, “I can’t do it that way. Do you want me to try another way?” And I say, “Whatever. I was just screwing around, and I’m never gonna try it again.”
These are very different markets. OpenAI has vacillated between wanting to be the big consumer company and knowing that the revenue is in enterprise. Do you see any focus in Dots, or do you see that personality shift back and forth in the product itself?
So far, I’m a little bit more impressed with Dots than Muse, just because everyone was impressed with Muse right away, but since then there have been a lot of ups and downs, plus the privacy stuff has been really interesting. Even the fact that it’s
building profiles on your family and closest friends
.
Meta has never been a super trusted company. None of these companies are very trusted, but Meta has made a lot of missteps with user privacy. Dots seems to be a little bit more helpful to me right now, but I’m still testing, I’m not fully sure yet.
I need to run through all my typical things that I do to compare. Everyone has their own short list of tasks. Right now, for example, I’m trying to create an album of my bachelorette photos, and it’s been unbelievably hard to get any agent to try to do that, so I say, “I’ll just do it myself.”
But that’s a pretty easy thing to do. Once again, how useful are these things for our everyday lives, really? We’ll see. They’ve gotten a lot better, I will say, over the past few years. I’ve been shocked at how slow they’ve been moving, but they have gotten better. Dots is a little bit more impressive to me right now, but we’ll see.
I have Muse plugged into my Instagram because I don’t worry about sharing my metadata with Meta in the way that I worry about maybe everything else, but they already have my Instagram. So I have Muse plugged into my Instagram, and it’s just doing all kinds of stuff. It surfaces interesting comments that I should reply to on Instagram posts. It tracks follower counts. It suggests things I should make videos about.
It has horrible ideas. Muse is absolutely convinced I should make a video almost every single day about obscure Australian tech regulation. I don’t know why it has this idea. I’m up on it now. I’m deep in the weeds on Australian tech regulation just because I see it every morning.
But there’s something about all that that still feels like work to me. I’ve just assigned it work, and then it tells me what work I should do, and I haven’t found some great consumer use for it yet. Organizing my photos is a consumer use. It kind of still rhymes with work, but it at least is not actually work.
Have you found a great consumer use for these yet?
Not one that works, and that’s the problem. I’ll try to have it do something for me for my wedding or for my personal life, and they haven’t been good yet. That’s why I’m still kind of running through and testing these, because so far it’s always interesting factually when they can do something, but I haven’t been able to trust them end-to-end with something that I really, really need done.
It reminds me of the analogy for AI agents. People always say right now they’re a bad intern, and what you want them to be is a really good assistant, or in Sam Altman’s words, a really good chief of staff. They’re no longer a bad intern, but I think maybe they’re an okay or “eh” assistant.
I don’t think they’ve reached the point of being a really, really good assistant yet, but I still need to run through the rest of my tests to see. It seems they’re not super consistent yet, which is something that you need in a really good assistant.
That ties into trust. You’ve mentioned trust several times now. I’m only willing to give Muse access to, again, the Meta platforms that Meta already has access to. I can’t worry too much about that. I’ve given it access to my spam Gmail, so it is collecting a lot of ideas about my spam Gmail.
But Meta really wants my credit cards. It wants to go through all of my credit card receipts. This is one of the suggestions in Muse. One of its suggestions is, “Let me log into your credit cards and I’ll cancel streaming services you’re not using,” or, “I’ll negotiate your Verizon bill for you.” I am absolutely not ready to give Meta one ounce of data more than it already has.
This feels like a big issue for every agent. There’s an argument that you should give Meta all that data, one, because they already have it, and two, because they’re a big company that you could sue if they get something wrong. Whereas if I gave all of my data to OpenClaw, it’s just my own fault if it gets leaked.
If I gave all my data to one of the hot startups like Instinct and they go out of business, well, that’s just the end of that. How d

## Metadata
- **Source**: [Original Article](https://www.theverge.com/podcast/1007408/meta-muse-openai-dots-ai-agent-race-privacy-free)
