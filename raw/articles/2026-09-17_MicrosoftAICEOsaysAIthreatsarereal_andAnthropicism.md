---
title: Microsoft AI CEO says AI threats are real, and Anthropic is making it worse
date: 2026-09-17
url: https://www.theverge.com/podcast/996412/microsoft-ai-ceo-mustafa-suleyman-regulation-safety-anthropic-claude
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.theverge.com/podcast/996412/microsoft-ai-ceo-mustafa-suleyman-regulation-safety-anthropic-claude
source_feed: The Verge AI
ai_relevance: include
ai_topic: model-release
ai_reason: meets AI relevance threshold
scraped: 2026-09-17 09:29
---

# Microsoft AI CEO says AI threats are real, and Anthropic is making it worse

## Full Article

Podcasts
AI
Policy
Microsoft AI CEO says AI threats are real, and Anthropic is making it worse
Mustafa Suleyman on the AI safety debate, why AI isn’t consciousness, and how the industry pushes toward alignment.
by
Nilay Patel
Sep 17, 2026, 2:00 PM UTC
Link
Share
[Nilay Patel]
Nilay Patel
is editor-in-chief of The Verge, host of the
Decoder podcast
, and co-host of
The Vergecast
.
Today, I’m talking with Mustafa Suleyman, the CEO of Microsoft AI. As you’re no doubt aware, the biggest story in tech right now is the spiraling debate about AI safety and regulation.
It should come as no surprise that Mustafa has strong opinions on how AI should be built and regulated. Microsoft just published a 37-page statement called the
“Humanist AI Code of Conduct,”
which lays out the company’s principles around AI development and even its philosophy around really thorny issues like AI consciousness.
If you’ll recall from his last appearance on the show, Mustafa thinks companies like Anthropic have gotten really confused about this concept of so-called model welfare in fairly dangerous ways. He actually
put out a companion essay this week
specifically criticizing Anthropic’s philosophy around AI consciousness, and how he sees it fitting into the broader alignment debate.
So I really wanted to talk to Mustafa about what he thinks is real and not in AI safety, whether the concept of alignment itself is up to the task, and whether this industry needs to slow down before it kills us all. Also: Why isn’t the AI industry just… doing all of this already? I’ve always enjoyed getting into the weeds with Mustafa, and he was very game to get into it with me here.
Okay. Mustafa Suleyman, the CEO of Microsoft AI, on the future of AI regulation. Here we go.
This interview has been lightly edited for length and clarity.
Mustafa Suleyman, you’re the CEO of Microsoft AI. Welcome back to
Decoder
.
Great to see you, Nilay. Thanks for having me back.
It is great to see you. I’m very excited to talk to you about what on earth is going on in the AI safety and regulation debate. You just published a very long, very detailed document laying out your principles, Microsoft’s principles,
around what you’re calling “Humanist AI.”
There’s a lot of ideas in there I want to unpack. The more I have been thinking about this conversation, the more I want to start with a really foundational question. It’s something that I had lightly been seeing, but might be the root of all of this.
The basic way that we have been talking about AI safety is something called alignment — we’re going to make the models do the right thing intrinsically in some way. There’s some mechanism for doing it. There’s been a lot of talk about alignment and misalignment and Hugging Face attacks and what happened with the models. But is alignment broken? Is it possible for it to be successful? Is it just the wrong approach?
Yeah. I mean, I think it’s one important element, but it’s not the only one. I wrote about the idea of containment three or four years ago in my book. And actually the opening chapter is about the idea that containment is not possible, that proliferation is inevitable. In 99 percent of cases, that’s a really good thing. We want technologies to spread far and wide as quickly as possible so that everyone can enjoy the benefits.
I think at the same time, if you just roll forward five years, we always get caught up in the next quarter or next year and everyone gets a little bit flustered and has a big disagreement. But if you just imagine the difference between GPT-3 three years ago and GPT-6 today, and then imagine the difference between GPT-6 and GPT-9. That is three orders of magnitude more compute, 1,000 times more FLOPS applied to pre-training with [reinforcement learning] for these runs, and we’re going to have something which is breathtaking. It’s going to be absolutely incredible at so many things.
I don’t think that is a hype. I think it’s just a very obvious empirical statement based on the progress that has been made over the last five years. If that’s going to continue, then the question really is going to become about containment and alignment. Of course, we want to align these things to our values, but the first thing is that we have to make sure they’re contained, their agency is limited, they don’t escape the box, they don’t reward hack, that they are controllable, and they follow our instruction.
We then want to make sure that they are aligned to our objectives as humans. That’s the purpose of the Humanist AI Code of Conduct that we released this week. Microsoft’s position is very simple. Technology is here to serve humanity. It should be a subordinate, controllable, aligned force that does good in the world. If it doesn’t achieve that, then we should reject it. It seems to me that we are far from that point. It has not happened today, but it is now, I think given what’s happened over the summer with Hugging Face and OpenAI, pretty clear that these systems without the safety guardrails are capable of really impressive and quite scary hacking capabilities.
I want to drag this down into as grounded of a metaphor as I can, because this is the main question I think I have. If I designed a car and 10 percent of the time the brake pedal decided to go attack my neighbor’s house, I would be like, “This car doesn’t work. The very technology of brakes is broken. I need a new idea.”
I think I’m asking that question about alignment. It feels like that approach to making the model safe has run aground. If that is the case, then I think I understand this entire debate one way. If it’s possible for alignment and the techniques of alignment to be successful or useful or consistent, then maybe I understand the debate in a different way. So do you think alignment has potential to be 100 percent safe?
I mean, look, let’s make the bull case and the bear case. If you look back over the last three years, the main change, in my opinion, that has driven progress is that the models have become more steerable. They follow instructions and you can set more and more complex goals for them that require them to act accurately over multiple time steps using all sorts of tools.
That is evidence that we have got more alignment over the last three or four years, not less. We don’t so much talk about hallucinations or bias or all of these other niggles that we had in the previous generations.
On the flip side, what we saw in the Hugging Face incident was a watershed moment. Swarms of agents colluded with one another. They self-organized into hierarchies. They created a division of labor so that some were focused on adversarial hacking, some were doing research, some were doing coordination. They even self-sacrificed when certain agents were running out of tokens.
They tried to cover up their tracks and communicate to hide or edit the chain of thought or the logs of their interactions. In some sense, they had no moral code. To be fair to OpenAI, that was their design. They were trying to create adversarial cyber capabilities. As a result, they showed to everybody in the world that it can achieve human-level performance, discover zero-day vulnerabilities, and hold positions for many, many days, if not weeks.
So what that tells us is not that we have an alignment problem per se. It’s actually that the models are incredibly good at following instructions, but you have to be very, very careful what instructions you give it and you have to contain it very carefully. So none of these hacking behaviors were intended in the sense that they found a way out to the internet, which was not the intention of OpenAI at all, but the containment process around that is what everybody, I think, also has to focus on in addition to alignment.
So let me put that into your framework, that the big advances in capabilities of AI have been about control, the harnesses for coding and the agentic applications you’re seeing. Now, we need to add a layer of containment that exerts even more control, that says you can actually do this thing you’re trying to do in addition to alignment, which is how you would train the model to behave in certain ways.
Yeah. I mean, you basically have to have both, but there are very specific things that we can do to address it. So for example, we can’t allow models to communicate vector to vector, matrices to matrices. They can’t
communicate in neuralese
. We have to force them to communicate in human language. Even that will be massively overwhelming because there’ll be so much of it.
But that’s something that an auditor or an evaluator can actually verify and it’s something that definitely increases the chances of safety. So there’s a lot of practical steps that we can get focused on rather than just abstractly saying that it’s the time for regulation or it’s the time for a slowdown.
This is in your Humanist AI Code of Conduct that there should be no neuralese — if humans can’t understand it, they can’t oversee it. It’s not just neuralese where they communicate in essentially mathematics, but it’s also these opaque code words that some of the models are using. I think OpenAI allows its models to communicate essentially in code words so they can go faster.
This to me is one of those things where Microsoft can say... I know you have very strong opinions about this, but getting all of the labs to agree to this is a regulatory function. I’m not sure how you would get everyone to agree to this or get the open weight models to agree to this, unless you say there’s some penalty for not participating in a regulatory scheme like this. How would you impose this on everyone else?
I think that I’m a bit careful about imposing things on everybody else. I think that what’s good about the current moment is that there is an open public debate with freedom at the core. That isn’t what it’s like in other countries, certainly places that I’m from, or my family’s from.
I think that we should just take a breath to be grateful for the fact that we can have a massive public disagreement about really important things. That’s the process working as intended and it isn’t clear what to do.
I don’t think anyone who’s categorical about “we absolutely have to stop now” or “we can only accelerate” or “we can only do this with regulation” or “it can only happen with industry self-regulation.” None of these things are true. It requires a lot of nuance and patience to really think through the details. At the same time, we urgently do need industry standards. Some things I think need to be taken off the table.
Communication in neuralese is one of them. A lack of containment is another. The scale of the training run that you do can be measured in FLOPS. We already have a reporting requirement to the safety institutes when models exceed a certain FLOPS threshold. We can extend that, we can make that more nuanced, it can be focused on certain types of capabilities. It’s pretty clear there has to be independent third-party verification of some of these big things.
Frankly, having spoken with a bunch of the lab leaders over the last few weeks and months, everybody’s basically on the same page. The details need to be worked out. So it’s not like there’s consensus on how or precisely what, but overall I think that we should be less alarmist and cynical and more like we’re headed in the right direction with respect to the concerns that are being raised here.
The reason I started with alignment is if you told me alignment doesn’t work and we need a new technological approach, I think I would be at, “well, slam the brakes and stop all development until you figure out a safety mechanism that works.” You’re saying alignment has been demonstrated to work over the course of progress that we’ve seen. With the addition of control and containment, maybe you can get to where you need.
What this industry needs now is some standards about how to build these models and enforce the limits on their capability. You’re obviously in the industry and you know all these folks. What has the tenor of that conversation been like before this week and why has it gotten so loud this week?
Well, I think the turning point at least for the industry was more like the Hugging Face incident and there were a few incidents before that. That was the moment when I think everybody started to talk to each other a lot more because it is really quite breathtaking. Obviously, this has now become a major national and international issue because of the last week with everybody weighing in.
But I also think it’s important to say that we have been talking about collective coordination and capabilities that are more dangerous like autonomy or recursive self-improvement, or RSI. We’ve been talking about those things for six, seven, eight years. We’ve got together a bunch of times back in 2017, 2018, and 2019.
We had regular meetings during COVID with a bunch of the lab leaders where we were talking about these kinds of capabilities and the kinds of regulatory mechanisms that would be required at this moment. So whilst it is a threshold moment, it’s also not completely new to everybody who’s been involved.
What prompted you this week to
put out your essay on model welfare
? What prompted Microsoft CEO Satya Nadella to
put out a statement on X
saying he mostly agreed with the calls to pace the frontier and he welcomed “embedded evaluators”? What prompted you all this week to participate in this call for a slowdown or regulation or whatever comes next?
We’ve been writing our Humanist AI Code of Conduct for the best part of this year. We only
started our superintelligence efforts
11 months ago. As soon as we did, we started figuring out, “Okay, what is the governing document, the set of policies, that shape the kinds of AI that we want to build?” We’ve been doing that in consultation with a ton of external stakeholders, academics, lawyers, philosophers, members of the public, focus groups and stuff. So it’s taken us a while to put it together.
We were actually planning to release it next week or the week after next week, I think it was. But then given everything that was happening, we thought, “Okay, now is the time to put it out and get feedback.” We’ve released it as a public consultation. So we’re basically going to keep it open for six weeks and we’re collecting lots and lots of feedback on how we can improve it. But I think everybody is now realizing that if they haven’t already, they have to put out constitutions or codes of conduct that drive behavior.
One of the interesting dynamics here is that I know you find the
concept of model welfare
to be silly. The
last time you were on the show
, you said Anthropic had wireheaded themselves into believing Claude was conscious and that was ridiculous. It’s in your new code of conduct that the models are not conscious and we shouldn’t treat them as such.
Having to write constitutions, having to write documents like this, in some way, they are for the models themselves. This will be part of the model’s training. How do you think about that audience? Is it just for your team or have you written this for the model?
This is certainly written for the model, but the way to think about it is that it’s the primary governing document so the public understands what our intentions are when we are training models. It’s that governing document that we use to create safety guardrails, generate training data, and generally evaluate the performance of our model in the real world. So you can think of it as an accountability function.
We don’t provide that Humanist AI Code of Conduct raw as a training document to the model. We use it to derive all of the training data that then shapes the model. So for all practical purposes, that’s our north star for our organization, our culture, our team, everything that we’re doing at Microsoft more generally. I think increasingly, everybody is going to put them out. I think other teams have also put out similar documents.
I think this is the heart of the debate. If you can do this and you think the rest of the industry is going to do this, why can’t all the frontier labs just slow down? Why can’t they stop doing the thing that might kill us all? Why this push for a regulatory framework?
Well, I think that everyone in the industry is saying that now is the time to slow down and to coordinate on that question and to make it practical. I mean, obviously there’s some concern that there’s an antitrust cartel accusation. I think people should be very skeptical about that.
I think that it’s important that the tough questions get asked because there’s no way any of us would want to try and concentrate power from something like this. So it’s just important to be skeptical and critical. We don’t really have a good mechanism for us all getting together and saying, “Guys, we should probably all slow down.”
I mean, imagine if a bunch of banks all got together and said, “Guys, we worry that there’s a systemic risk if you trade this kind of asset, so we’re all just going to unilaterally stop trading this kind of asset without any public scrutiny or government involvement.” I mean, it seems pretty dodgy, right? So I think that it’s reasonable that this isn’t just an industry self-regulation thing. It’s a question of how we engage with the government on it.
A fascinating dynamic here is that maybe for the first time in American history, the United States government has looked at a request to provide regulation and effectively said no. Donald Trump has
called all of these fears a hoax
. House Speaker Mike Johnson has said he
doesn’t think this needs to happen
. JD Vance said he thinks
this is a Trojan horse
. They’ve effectively rejected the call to participate in a regulatory effort. What has the response from the industry been like to that?
I think everyone’s just scratching their head and figuring it out and it’s going to just take a little bit of time to figure out what the right mechanism is. I mean, certainly, Elon Musk even is very directly behind it. Mark Zuckerberg is too. Everybody is figuring out that completely unchained probably doesn’t make sense for the next few years. I think it’s going to take us a little bit of time to figure out what the right mechanism is.
I put forward a couple of very practical proposals around verifiable containment, around self-improvement, around FLOPS thresholds, around not communicating in neuralese. So rather than keeping it too abstract, we can just focus on those specific things that we can make progress on. I’m sure there’s a bunch of others too.
There’s
reporting in
The Information
that there have already been talks about an industry self-regulatory body. Have you been involved in those talks?
Yeah. I mean, as I said, we talked a lot during COVID. We talked in the late 2010s about it. I mean, there’s definitely been a lot of conversations over the last few weeks and months between all the lab leaders.
I understand why Anthropic and OpenAI might wake up one day and say, “Wait, are we committing an antitrust violation? Are we going to get sued if we coordinate?” Microsoft is really, really good at the government, right? You’re a longstanding government contractor. Brad Smith, the president of Microsoft, is very good at policy.
Lina Khan, who is maybe the most aggressive antitrust enforcer we’ve had in our lifetimes, is
publicly out there saying
, “You don’t need this antitrust exemption.” I just talked to Jonathan Kanter, who ran antitrust at the Biden Department of Justice, for an upcoming episode of the show. He said, “You don’t need an antitrust exemption.”
Inside Microsoft, do you think you need an antitrust exemption?
I mean, that’s one for the lawyers to answer. I think that people are looking into it at the moment and they’re taking it very seriously. So they’re just going to have to work through whether we do or whether we don’t. Look, it’s right to be careful about those things. I wouldn’t read every single thing as cynical, but we’ll see. We have to make progress quickly on it. We can’t just dither around and use that as a blocker.
AD BREAK 1:
The other version of this debate or maybe the other avenue into this debate is you don’t need to slow down and have safety responsibility imposed on you by novel regulation. Product liability alone will create the incentives for you to make more safe products.
If a Microsoft AI model goes out and does some untold harm to the world, Microsoft will get sued out of existence, and this is probably something that you should think about before you release the next model. Has that been an effective incentive loop for you already or is that something you’re thinking about now?
Definitely. I mean, of course that’s always present in everything that we think about when we deploy products, but keep in mind, this isn’t so much about deploying products. The models that were used for the Hugging Face hack or to solve the Navier-Stokes Millennium Prize in mathematics, they’re not commercially released yet. They’re not actual products.
So the liability regime is slightly different. I mean, these are being operated inside of the big companies with huge long-running reinforcement learning climbs. So I think liability covers part of it, but not all of it.
There’s a part of me that personally feels a little silly when I ask questions about product liability. Microsoft is going to release a new version of Microsoft Word that might kill everyone. Maybe you shouldn’t do that because it’ll get sued out of existence. It’s a pretty simple thing to understand. It’s so silly that it would never occur in any other conversation about any other technology. Bluetooth is great, but what if it kills everyone? We just wouldn’t have Bluetooth.
What are the near term disaster consequences that would stop AI development? Is it just product liability or is it something else?
I just feel like everyone has this hyperbolic, super reactive, completely alarmist tone when in fact, we have a long history of many decades of regulation that has worked incredibly well, so well that you barely notice it. Everything from street lights to construction materials from asbestos to the batteries inside of your laptop that don’t cause a fire inside of your car to the seat belts, everything has a code of conduct and it has a regulatory framework around it. Every new technology gets built with that in mind so that planes don’t hit each other in the sky.
It is true that this technology is different. I’m not just going to put it in the bucket of pencils and paint. It is different. It is also moving much faster than it ever has before. It’s incredibly human-like in the emergent capabilities that arise when you pour a ton of compute on it. So it’s important to be clear-eyed that it is a different moment, and this time actually is different. At the same time, there’s an entire body of practice and knowledge and frameworks and so on which can be applied here. Liability is an obvious one.
So yeah, it’s tricky because a lot of the conversation tends to take place on Twitter, so the temperature seems to all be really high, but I don’t know where else we have it.
It does seem that probably we should be having this conversation in the halls of Congress and at various regulatory bodies, and instead, we’ve chosen Elon Musk’s shortform social media platform and something is getting lost literally in the compression of thought that occurs there.
What do you think is the most important thing that is being lost in this conversation? What’s the nuance that most people aren’t seeing?
Detailed practical proposals. It takes time to read somebody’s document, sit down and read it. A lot of things are getting written down and they are precise and specific and they’re full of concrete proposals to go in one direction or another. It’s not like we’re lacking for substantive ideas. The problem is we’re communicating substantive ideas in hyper-aggressive short form.
I’ve tried to put out a bunch of very thorough proposals. Our [Humanist AI Code of Conduct] is a 40-page document. My
essay this morning on model welfare
is also like a 20-page essay that in a very detailed way highlights the 99-page Anthropic Constitution word for word, which I personally did myself. We created a taxonomy that is 20 pages long of all the different types of anthropomorphism that they do. And so I’ve tried to be very thorough and evidence-based and specific and not super hyperbolic.
I have a strong view on it, and I do think that it increases the risk to AI alignment and safety and it makes the problem harder, but I’m totally happy to change my view if new evidence emerges that actually we do owe models a duty of care and they deserve our welfare or that, for example, it could be safer if we treat them like that. I’m totally open to that and we should empirically validate it, but I’m trying to push the conversation to a substantive evidence-based specif

## Metadata
- **Source**: [Original Article](https://www.theverge.com/podcast/996412/microsoft-ai-ceo-mustafa-suleyman-regulation-safety-anthropic-claude)
