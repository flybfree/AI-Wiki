---

title: The best large language models (LLMs) in 2026
date: 2026-05-13
url: https://zapier.com/blog/best-llm/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://zapier.com/blog/best-llm/
scraped: "2026-05-13 19:00"

---

## Summary

Large language models (LLMs) are the main kind of text-handling AIs. ChatGPT, Google's AI answers, and Apple Intelligence are just a tiny handful of the apps that rely on them.



# The best large language models (LLMs) in 2026

**Source**: [Original Article](https://zapier.com/blog/best-llm/)

## Full Article

Large language models (LLMs) are the main kind of text-handling AIs. ChatGPT, Google's AI answers, and Apple Intelligence are just a tiny handful of the apps that rely on them. If something has a
chatbot
or some kind of
text generator
or text summarization built in, it almost certainly uses an LLM.
LLMs have been studied in research labs since the late 2010s, but after the release of ChatGPT (which showcased the power of GPT), they've burst out of the lab and into the real world.
We're now a few years into the widespread availability of LLMs, and with that, they're increasingly useful and powerful.
Reasoning models
that take extra time to work through hard problems and
large multimodal models (LMMs)
, which are able to handle other input and output modalities, like images, audio, and video, as well as text, are two of the biggest developments. Of course, the rapid pace of AI complicates things even more. So here, I'll break down some of the most important LLMs, LMMs, and reasoning models on the scene right now.
Table of contents:
The best LLMs
What is an LLM?
What is an open source LLM?
How do LLMs work?
What are reasoning models?
What can LLMs be used for?
Why are there so many LLMs?
What to expect from LLMs in the future
The best LLMs
There are dozens of major LLMs, and hundreds that are arguably significant for some reason or other. Listing them all would be nearly impossible, and in any case, it would be out of date within days because of how quickly LLMs are being developed.
(I'm updating this list now for the first time in a few months and I have to make some pretty significant changes to add new models, update existing ones, and remove others that are now out of date.)
Take the word "best" with a grain of salt here: I've tried to narrow things down by offering a list of the most significant, interesting, and popular models, not necessarily the ones that outperform on benchmarks (though most of these do). I've also mostly focused on LLMs, LMMs, and reasoning models that you can actually use—rather than ones that are the subjects of super interesting research papers or just teased in marketing materials—since we like to keep things practical around here.
Click on any app in the list below to learn more about it.
LLM
Developer
Multimodal?
Reasoning?
Access
GPT-5.5
OpenAI
Yes
Yes
API, Chatbot
gpt-oss
OpenAI
No
Yes
Open
Gemini
Google
Yes
No
API, Chatbot
Gemma
Google
No
No
Open
Llama
Meta
Yes
No
Open
R1
DeepSeek
No
Yes
Open, API, Chatbot
V3.2
DeepSeek
No
Yes
Open, API, Chatbot
Claude
Anthropic
Yes
Yes
API, Chatbot
Command
Cohere
No
Yes
API
Nova
Amazon
Yes
No
API
Mistral
Mistral
No
Yes
API, Chatbot, Open weight
Qwen
Alibaba Cloud
No
Yes
Open, API, Chatbot
GLM-5
Z.ai
No
Yes
Open, API, Chatbot
Kimi K2.5
Moonshot AI
No
Yes
Open, API, Chatbot
MiniMax M2.5
MiniMax
Yes
Yes
Open, API, chatbot
MiMo-V2-Flash
Xiaomi
No
Yes
Open, API
Phi
Microsoft
Yes
Yes
Open
Grok
xAI
Yes
Yes
API, Chatbot
To learn which AI model your team should use, check out the
AutomationBench leaderboard
. AutomationBench is Zapier's open evaluation tool for measuring how well models handle real, complex business workflows.
What is an LLM?
An LLM, or large language model, is a general-purpose AI text generator. It's what's behind the scenes of all AI chatbots,
AI writing generators
, and most other AI-powered features like
summarized search answers
.
Stripped of fancy interfaces and other workarounds, LLMs take a
prompt
and generate an answer. The chatbots built on top of LLMs aren't looking for keywords so they can answer with a canned response—instead, they're doing their best to understand what's being asked and reply appropriately.
This is why LLMs have really taken off: the same models (with or without a bit of extra training) can be used to respond to customer queries, write marketing materials, summarize meeting notes, and do a whole lot more.
But LLMs can only work with text, which is why LMMs are increasingly popular: they can incorporate images, handwritten notes, audio, video, and more. Many of the biggest models are now LMMs.
What is an open source LLM?
There are three major categories of LLM: proprietary, open, and
open source
.
Proprietary models
like GPT-5.5 and Claude Opus 4.7 are some of the most popular and powerful models available, but they're developed and operated by private companies. The source code, training strategies, model weights, and even details like the number of parameters they have are all kept secret. The only ways to access these models are through a chatbot or app built with them, or through an API. You can't just run GPT-5.5 on your own server.
Open and open source models
are more freely available. You can download Llama 4, gpt-oss-20b, Gemma 3, and DeepSeek V3 from Hugging Face and other model platforms and run them on your own devices—and even re-train them with your own data to create your own model. They're also available from multiple third-party API providers so developers can build their own chatbots and apps on top of them. You can dig deep into things like the model weights and system architecture to understand how they work (as best as anyone can).
So what's the difference between open and open source? Well, companies like Meta and Google say that Llama 4 and Gemma 3 are open as though it's the same as open source, but there's a major distinction.
Open source licenses
are incredibly permissive. Mostly, you have to agree to make anything you build with it open source as well—and give attribution to the original developers. If you want to build a multi-billion dollar company off open source software or create a crime chatbot that tells people how to rob a bank, you're absolutely free to do so. The police might have some issues with the latter project, but you wouldn't be breaking any software licenses.
Open licenses are still permissive, but they have some additional limits. For example, Llama 4's license allows commercial use
up to 700 million monthly users
and
blocks certain uses
. You or I could build something with it, but Apple and Google can't. Similarly,
Gemma 3's prohibited use policy,
among other things, bans "facilitating or encouraging users to commit any type of crimes." Understandably, Google doesn't want to see unsavory bots "powered by Google Gemma" plastered all over the news.
It's also worth noting that there's a bit of a divide growing between where the different kinds of models are being developed. Western companies are mostly training proprietary models, while a huge amount of the
boom in open models comes from Chinese tech companies
. There are, of course,
huge political issues to all of this
—though they aren't actually that relevant to the discussion at hand.
How do LLMs work?
Early LLMs, like GPT-1, would fall apart and start to generate nonsense after a few sentences, but today's LLMs, like GPT-5.5, can generate tens of thousands of words that all make sense or write computer code while taking the context of the whole codebase into account.
To get to this point, LLMs were trained on huge corpuses of data. The specifics vary a little bit between the different LLMs—depending on how careful the developers are to fully acquire the rights to the materials they're using—but as a general rule, you can assume that they've been trained on something like
the entire public internet
,
every book, newspaper, and magazine that's ever been published
, and the
synthetic output of earlier AI models
at a bare minimum. This is why LLMs can generate text that sounds so authoritative on such a wide variety of subjects.
From this training data, LLMs are able to model the relationship between different words (or really, fractions of words called tokens) using high-dimensional vectors. This is all where things get very complicated and mathy, but the basics are that every individual token ends up with a unique ID and that similar concepts are grouped together. This is then used to generate a neural network, a kind of multi-layered algorithm based on how the human brain works—and that's at the core of every LLM.
The neural network has an input layer, an output layer, and multiple hidden layers, each with multiple nodes. It's these nodes that compute what words should follow on from the input, and different nodes have different weights. For example, if the input string contains the word "Apple," the neural network will have to decide to follow up with something like "Mac" or "iPad," something like "pie" or "crumble," something like "by Charli XCX," or something else entirely. When we talk about how many parameters an LLM has, we're basically comparing how many layers and nodes there are in the underlying neural network. In general, the more nodes, the more complex the text a model is able to understand and generate—though many LLMs use a
mixture-of-experts architecture
, which makes straight comparisons based on size impossible.
LMMs are even more complex because they also have to incorporate data from additional modalities, but they're typically trained and structured in much the same way.
Of course, an
AI model
trained on the open internet with little to no direction sounds like the stuff of nightmares. And it probably wouldn't be very useful either, so at this point, LLMs undergo further training and fine-tuning to guide them toward generating safe and useful responses. One of the major ways this works is by adjusting the weights of the inputs and outputs of different nodes, though there are other aspects of it too.
[Infographic showing how natural language processing works]
All this is to say that while LLMs are black boxes, what's going on inside them isn't magic. Once you understand a little about how they work, it's easy to see why they're so good at answering certain kinds of questions. It's also easy to understand why they tend to make up (or
hallucinate
) random things.
What are reasoning models?
Reasoning models are LLMs that are trained to generate a response using
Chain-of-Thought (CoT) reasoning
.
When they're given a prompt, instead of replying as quickly as possible, they break the problem down into multiple simple steps and attempt to work through them. If they encounter issues, they can reassess and approach problems from a different angle.
[DeepSeek reasoning through a problem]
This kind of reasoning requires more computing resources, but it tends to lead to more powerful AI models. It's especially useful for complex real-world tasks, like coding and computer-use.
What can LLMs be used for?
LLMs are powerful mostly because they're able to be generalized to so many different situations and uses. The same core LLM (sometimes with a bit of fine-tuning) can be used to do dozens of different tasks. While everything they do is based around generating text, the specific ways they're prompted to do it changes what features they appear to have.
Here are some of the tasks LLMs are commonly used for:
General-purpose chatbots (like ChatGPT and Google Gemini)
Summarizing search results and other information from around the web
Customer service chatbots that are trained on your business's docs and data
Translating text from one language to another
Converting text into computer code, or one language into another
Generating social media posts, blog posts, and other marketing copy
Sentiment analysis
Moderating content
Correcting and editing writing
Data analysis
And hundreds of other things. We're still in the early days of the current AI revolution.
But there are also plenty of things that LLMs can't do, but that
other
kinds of AI models can. A few examples:
Interpret images
Generate images
Convert files between different formats
Create charts and graphs
Perform math and other logical operations
Of course, some LLMs and chatbots
appear
to do some of these things. But in most cases, there's another AI service stepping in to assist—or you're actually using an LMM.
With all that context, let's move on to the LLMs themselves.
The best LLMs
GPT-5.5
Developer:
OpenAI
Parameters:
Unknown, but likely in the hundreds of billions
Context window:
1 million
Access:
API, chatbot
OpenAI's Generative Pre-trained Transformer (GPT) models kickstarted the latest AI hype cycle. GPT-5.5, the company's latest flagship model (here's a list of
all the OpenAI models
), is both multimodal and capable of reasoning. It aims to combine all the features of GPT-4o, o3, and Codex (OpenAI's general purpose, reasoning, and coding models) into a single general purpose model.
GPT-5.5 is available through ChatGPT and as
an API for developers
. As a reasoning model, the options available through the API can get complicated as you have to set how much effort the model can expend to work through difficult problems as well as select whether to use the full model, or the nano or mini versions.
You can pull the power of GPT-5.5 and other OpenAI models into your work by
connecting them to Zapie
r
, making AI a core part of complex, multi-step workflows across your enterprise tech stack. For example, you can route customer support tickets from Zendesk into ChatGPT for summarization and sentiment analysis, then automatically log structured insights in Salesforce and trigger a Slack alert for high-priority cases. Learn more about
how to automate ChatGPT
, or get started with one of these pre-made workflows.
Automatically reply to Google Business Profile reviews with ChatGPT
Automatically reply to Google Business Profile reviews with ChatGPT
Try it
[Google Business Profile logo]
[ChatGPT (OpenAI) logo]
[Google Business Profile logo]
Google Business Profile, ChatGPT (OpenAI)
Google Business Profile + ChatGPT (OpenAI)
Send prompts to ChatGPT for Google Forms responses and add the ChatGPT response to a Google Sheet
Send prompts to ChatGPT for Google Forms responses and add the ChatGPT response to a Google Sheet
Try it
[Google Forms logo]
[ChatGPT (OpenAI) logo]
[Google Sheets logo]
Google Forms, ChatGPT (OpenAI), Google Sheets
Google Forms + ChatGPT (OpenAI) + Google Sheets
Create email copy with ChatGPT from new Gmail emails and save as drafts in Gmail
Create email copy with ChatGPT from new Gmail emails and save as drafts in Gmail
Try it
[Gmail logo]
[ChatGPT (OpenAI) logo]
[Gmail logo]
Gmail, ChatGPT (OpenAI)
Gmail + ChatGPT (OpenAI)
Zapier is the most connected AI orchestration platform—integrating with thousands of apps from partners like Google, Salesforce, and Microsoft. Use forms, data tables, and logic to build secure, automated, AI-powered systems for your business-critical workflows across your organization's technology stack.
Learn more
.
gpt-oss
Developer:
OpenAI
Parameters:
21 billion, 117 billion (as mixtures-of-experts)
Context window:
128,000
Access:
Open
OpenAI also has a state-of-the-art open LLM. gpt-oss-20b and gpt-oss-120b are both open reasoning models that were trained using the same techniques as OpenAI's other models like o3 and GPT-4o.
Anyone can download, fine-tune, and use these models for almost any purpose (though OpenAI has taken steps to limit the ways they can be used for malicious purposes or to generate harmful information). This is a big deal because since 2019, all of OpenAI's models have been proprietary.
Gemini
Developer:
Google
Parameters:
Unknown
Context window:
Up to 1 million
Access:
API
, chatbot
Google Gemini
is a family of AI models from Google. The main models—Gemini 3.1 Pro, Gemini 3.1 Flash, and Gemini 3.1 Flash-Lite—are designed to operate on different devices, from smartphones to dedicated servers, and cover a wide variety of uses.
While capable of generating text like an LLM, the Gemini models are also natively able to handle images, audio, video, code, and other kinds of information. They're optimized for a
long context window
, which means they can process larger volumes of text.
The latest models also power
AI features throughout Google's apps
, like Docs and Gmail, as well as Google's chatbot, which is confusingly also called
Gemini
. Google's Gemini models are available to developers through Google AI Studio or Vertex AI.
With Zapier's
Google Vertex AI
and
Google AI Studio
integrations, you can access Gemini from all the apps you use at work. Here are a few examples to get you started, or you can learn more about
how to automate Google AI Studio
.
Create a Slack assistant with Google Vertex AI
Create a Slack assistant with Google Vertex AI
Try it
[Slack logo]
[Google Vertex AI logo]
[Slack logo]
Slack, Google Vertex AI
Slack + Google Vertex AI
Send prompts in Google Vertex AI every day using Schedule by Zapier
Send prompts in Google Vertex AI every day using Schedule by Zapier
Try it
[Schedule by Zapier logo]
[Google Vertex AI logo]
Schedule by Zapier, Google Vertex AI
Schedule by Zapier + Google Vertex AI
Generate draft responses to new Gmail emails with Google AI Studio (Gemini)
Generate draft responses to new Gmail emails with Google AI Studio (Gemini)
Try it
[Gmail logo]
[Google AI Studio (Gemini) logo]
[Gmail logo]
Gmail, Google AI Studio (Gemini)
Gmail + Google AI Studio (Gemini)
Create a Slack assistant with Google AI Studio (Gemini)
Create a Slack assistant with Google AI Studio (Gemini)
Try it
[Slack logo]
[Google AI Studio (Gemini) logo]
[Slack logo]
Slack, Google AI Studio (Gemini)
Slack + Google AI Studio (Gemini)
Gemma
Developer:
Google
Parameters:
270 million, 1 billion, 4 billion, 12 billion, and 27 billion
Context window:
128,000
Access:
Open
Google Gemma is a family of open AI models from Google based on the same research and technology it used to develop Gemini. The latest version, Gemma 3, is available in five sizes: 270 million, 1 billion, 4 billion, 12 billion, and 27 billion parameters. There is also a version called
Gemma 3n
designed for mobile architectures.
Llama
[Using Llama 2 with Llama Chat]
Developer:
Meta
Parameters:
109 billion, 400 billion, 2 trillion (all as mixtures-of-experts)
Context window:
10 million
Access:
Open
Llama
is a family of open LLMs from Meta, the parent company of Facebook and Instagram. The newest Llama 4 models (including Scout, Maverick, and Behemoth [in preview]) are multimodal and use a mixture-of-experts structure. Scout has a 10M context window, which is bigger than anything else available at the moment.
In addition to powering most AI features throughout Meta's apps, the Llama "herd" is one of the most important open LLM families, and you can download the source code yourself
from GitHub
. Because it's free for research and commercial uses, a lot of other LLMs use a Llama model as a base.
R1
Developer:
DeepSeek
Parameters:
671 billion (as a mixture-of-experts)
Context window:
128,000
Access:
Open, chatbot, API
DeepSeek R1
caused a major stir when it launched, as it was the first state-of-the-art reasoning model developed by a Chinese tech company. It was created on more limited computer hardware with a far smaller budget and released as an open model.
R1 has been continually updated since launch, though it has been somewhat deprecated in favor of DeepSeek V3.2.
V3.2
Developer:
DeepSeek
Parameters:
671 billion
Context window:
128,000
Access:
Open, chatbot, API
DeepSeek V3.2 is DeepSeek's equivalent of GPT-5.5. It's a state-of-the-art open LLM that can reason and use tools, although it doesn't have any multimodal features. It now offers more powerful reasoning features than R1. It was also developed using more limited computer hardware and for less financial investment than typical LLMs.
Claude
[Claude, the best AI chatbot for writing and coding]
Developer:
Anthropic
Parameters:
Unknown
Context window:
1 million
Access:
API, chatbot
Claude
is arguably one of the most important competitors to GPT. Its three hybrid reasoning models—Claude Sonnet 4.6, Claude 4.5 Haiku, and Claude Opus 4.7—are designed to be helpful, honest, harmless, and crucially, safe for enterprise customers to use. As a result, companies like Slack, Notion, and Zoom have all partnered with Anthropic. Claude Sonnet 4.6 is now considered one of the best AI coding models available.
Like all the other proprietary LLMs, Claude is only available as an API or through its official chatbot and other products, though it can be further trained on your data and fine-tuned to respond how you need.
And when you
connect Claude to Zapier
, you can embed advanced AI directly into your enterprise workflows. For example, you can have Claude analyze long-form research reports stored in Google Drive, generate concise executive summaries, and automatically distribute them to stakeholders in Slack or Notion. Learn
how to automate Claude
, or get started quickly with one of these pre-built workflows.
Generate an AI-analysis of Google Form responses and store in Google Sheets
Generate an AI-analysis of Google Form responses and store in Google Sheets
Try it
[Google Forms logo]
[Anthropic (Claude) logo]
[Google Sheets logo]
Google Forms, Anthropic (Claude), Google Sheets
Google Forms + Anthropic (Claude) + Google Sheets
Write AI-generated email responses with Claude and store in Gmail
Write AI-generated email responses with Claude and store in Gmail
Try it
[Gmail logo]
[Anthropic (Claude) logo]
[Gmail logo]
Gmail, Anthropic (Claude)
Gmail + Anthropic (Claude)
Create LinkedIn posts with Claude and post to LinkedIn
Create LinkedIn posts with Claude and post to LinkedIn
Try it
[Airtable logo]
[Anthropic (Claude) logo]
[LinkedIn logo]
Airtable, Anthropic (Claude), LinkedIn
Airtable + Anthropic (Claude) + LinkedIn
Command
Developer:
Cohere
Parameters:
Command R7B has 7 billion; the other models are unknown
Context window:
Up to 128,000
Access:
API
Like Claude, Cohere's Command models are designed for enterprise users. Command A Max, Command A Reasoning, Command R7B, Command R, and Command R+ offer an API and are optimized for
retrieval augmented generation (RAG)
so that organizations can have the model respond accurately to specific queries from employees and customers.
As a result, companies like Oracle, Accenture, Notion, and Salesforce use Cohere's models.
Nova
Developer:
Amazon
Parameters:
Unknown
Context window:
Up to 1 million
Access:
API
Amazon Nova is a family of frontier models available on Amazon Web Services. Despite a slow start from Amazon, the current models—including Amazon Nova 2 Pro, Lite, and Omni—perform competitively in a range of benchmarks. Given AWS's prominence in cloud computing, Amazon Nova models may end up proving popular.
Mistral
Developer:
Mistral
Parameters:
3 billion, 8 billion, 14 billion; Mistral 3 Large is a MoE model with 41 billion active and 675 billion total parameters.
Context window:
256,000
Access:
API, chatbot, open weight
Mistral is one of the largest European AI companies. Mistral 3 is its latest non-reasoning frontier model; it uses a mixture-of-experts architecture with 41 billion active and 675 billion total parameters.
Mistral also has the
Magistral models
that support reasoning, and the Ministral models with 3 billion, 8 billion, and 14 billion parameters. Ministral focuses on the enterprise market.
Qwen
Developer:
Alibaba Cloud
Parameters:
0.5 billion, 1.5 billion, 3 billion, 7 billion, 14 billion, 32 billion, 72 billion, 235 billion
Context window:
Up to 1 million
Access:
Open, API, chatbot
Qwen
is a family of AI models from Chinese tech giant Alibaba. There are dozens of open models available across the different Qwen3.5 and Qwen3 families, including models tailored for vision, coding, math, and a million-token context window.
The highest performing model,
Qwen3.5
Max, matches or exceeds models like DeepSeek V3.2, Grok 4, and Claude 4.6 Opus (in normal mode) across a wide range of benchmarks.
GLM-5
Developer:
Z.ai
Parameters:
744 billion (as mixtures-of-experts)
Context window:
128,000
Access:
Open, API, chatbot
GLM-5 (and before that, GLM-4.5 and GLM-4.5-Air) is Chinese AI developer
Z.ai
's flagship models. They all use a mixture-of-experts architecture, support reasoning, and are designed for agentic workflows. They're among the top performing open models.
Kimi K2.5
Developer:
Moonshot AI
Parameters:
1 trillion (as a mixture-of-experts)
Context window:
Up to 256,000
Access:
Open, API, chatbot
Kimi K2.5 is Chinese AI developer Moonshot AI's flagship model. It uses a mixture-of-experts architecture, supports reasoning, and is designed for tool use and other agentic tasks. It is among the highest performing open models.
MiniMax M2.5
Developer:
MiniMax
Parameters:
230 billion (as a mixture-of-experts)
Context window:
Up to 204,800
Access:
Open, API, chatbot
MiniMax M2.5 is the latest flagship model from titular Chinese AI developer MiniMax. Like most flagship models, it uses a mixture-of-experts architecture, supports reasoning, and is designed for tool use and other agentic tasks. It's among the highest performing open models.
MiMo-V2-Flash
Developer:
Xiaomi
Parameters:
309 billion (as a mixture-of-experts)
Context window:
Up to 256,000
Access:
Open, API
Xiaomi is better known for its consumer electronics and (at least in Ireland) its budget Android phones,

## Metadata
- **Source URL**: https://zapier.com/blog/best-llm/
