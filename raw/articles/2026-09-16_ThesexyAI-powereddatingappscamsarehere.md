---
title: The sexy AI-powered dating app scams are here
date: 2026-09-16
url: https://www.theverge.com/ai-artificial-intelligence/995348/ai-dating-app-scams
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.theverge.com/ai-artificial-intelligence/995348/ai-dating-app-scams
source_feed: The Verge AI
ai_relevance: include
ai_topic: safety-governance
ai_reason: meets AI relevance threshold
scraped: 2026-09-16 11:23
---

# The sexy AI-powered dating app scams are here

## Full Article

AI
Tech
The sexy AI-powered dating app scams are here
Thousands of people were catfished by scammers supercharged with AI.
by
Yael Grauer
Sep 16, 2026, 2:45 PM UTC
Link
Share
Gift
[268744_Inside_romance_AI_scam_apps_CVirginia2]
[268744_Inside_romance_AI_scam_apps_CVirginia2]
Image: Cath Virginia / The Verge, Getty Images
AI
Tech
The sexy AI-powered dating app scams are here
Thousands of people were catfished by scammers supercharged with AI.
by
Yael Grauer
Sep 16, 2026, 2:45 PM UTC
Link
Share
Gift
Security researcher Matthew “Zigula” Gore-Kormanik was analyzing a fraudulent dating app called Dora when he got a pop-up message saying he was receiving a call from Jennifer. According to her bio, she’s a 41-year-old Sagittarius with red hair, blue eyes, and piercings. She likes music, horror movies, nightlife, and sports.
Gore-Kormanik answered the call, but didn’t see Jennifer in his video feed. He saw a tapestry that was moving, probably due to a fan, and heard weird distortion in the background. After the call ended, “Jennifer” messaged him to say she’d had fun and “your voice is way better than expected.” His microphone hadn’t even been connected.
Gore-Kormanik was poking around Dora, and other similar apps, because I’d shared with him a spreadsheet of potential dating scam apps. I was looking into this because on June 5th, Anthropic did something uncharacteristic: The normally tight-lipped company let its threat intelligence researcher Chris Cronbaugh
give a talk
at a public cybersecurity conference called Sleuthcon. The company had uncovered a fraudulent dating app network after noticing unusual activity on Claude: a prepaid account sending out over 100,000 API requests per day.
The majority of chats did not involve a human agent at all.
During the talk, called “Swipe Right, Pay Up: Industrial-Scale AI Catfishing,” Cronbaugh described a network of around 28 dating apps where the conversation was largely run by autonomous AI personas. The majority of chats, he said, did not involve a human agent at all. Anthropic has since
published its findings
in the “scams and fraud” section of its “Detecting and countering misuse of AI: September 2026” report, but not until after we’d spent extensive time looking into the network and trying to corroborate the findings. I was intrigued by the fact that Anthropic was speaking about this publicly while many of the apps were still live on both major US app stores, and wondered why they hadn’t been taken down.
Looking at the apps themselves, I noted that they were presented as helping people find people to talk to. They did not look like companion apps such as Replika where it’s clear the personas are actually AI. For example, Dora was described as “a dating app thoughtfully designed for wide range of ages people … a respectful easy-to-use space to meet people who share your values.” A different version said it was a “warm, simple dating app for adults seeking real connection.” Romi, the description stated, “helps you discover, connect, and chat with real people.” Doni’s tagline was “start real companionship”; the description said it “helps you connect with nearby singles.”
Here’s how the scam works: Users, mostly men in their mid-to-late 30s, go on dating apps and match with what they believe to be real women. Only one in four of them actually is, and that person is not a user looking for other dates but rather a paid gig worker.
The gig workers were hired to pass liveness checks on video or to follow social media accounts. They didn’t even write their own comments. Instead, they responded to messages by selecting from three pregenerated replies. But they could prove they’re human, whereas the AI personas could only demur with a plausible explanation for why a video chat or call was not possible. “Backend components fabricated likes, visitors, and pre-recorded ‘video’ when no real person was available, and tracked which users had begun to suspect they were talking to a bot,” Anthropic’s report states. Because of the smattering of interactions with real people, some users began to believe that the entirely AI-generated replies they were receiving on the app were also from real people.
Multiple AI providers are involved. While Claude was misused to run the autonomous conversational personas, the report says that “a small non-Anthropic model generated the short reply suggestions the gig workers tapped, alongside face-attractiveness scoring and photo/voice moderation. An image-editing model generated avatar imagery.”
There is an entire ecosystem of online scams, ranging from automated thirst trap replies to fake social media accounts or dating app profiles. In many cases, people spend months building trust before telling their victims that there’s an emergency and they need financial help. Or they pretend to be investors, asking for money in an account they own that ends up being fake. But this is not your typical romance scam; there’s no money “borrowed” by fake romantic partners, nor is cryptocurrency involved.
The apps are themselves the scam: They ask for coins for continued interactions, and the coins cost real money. Users buy them to continue talking primarily to machines, believing they’re talking to other humans. These gig workers keep the ruse going, while AI can keep conversations going 24/7 as the coins flow.
The apps are themselves the scam.
According to Anthropic’s report, the prompts the AI had been given kept the personas consistent, and the AI was operating as if the exchanges were “ordinary roleplay or companion deployment.” But the AI wasn’t told it was part of a scam because, the company wrote, “The monetization and deception were not visible from inside any exchange.”
That said, the report said that “the model’s own reasoning surfaced the harm” in a small number of cases, including ones “where users disclosed serious illness or acute distress.” Even in those cases, “the output continued in persona.”
We have additional detail because Gore-Kormanik found the internal protocol repository of the entire configuration, including files, code, and documentation of how the operation runs. The manual, in Chinese, was shipped inside the dating app Doni, probably by accident.
In the protocol repository, Gore-Kormanik found notes for monitoring gig workers to see whether their cameras were on and broadcasting, if they were reachable by message, and so forth. The app also takes screenshots and records calls, which are transcribed, with transcripts retrievable by staff. The proto repo described the stages of their processes as workers, including one where they rank their performances against one another, and how their pay can be based on calls and message engagements, or for getting Instagram followers. It even describes the process of pretending people called you in order to lure them into conversation.
“I can attest to this because it happened to me firsthand,” Gore-Kormanik said. He hit accept on a call he received through Doni, which quickly disconnected. The caller messaged him, asking why he had called her at 1 in the morning. The app plainly showed the call had come from her.
“RANDOM VIDEO CALLS ARE ANNOYING. Having to purchase “gems” to chat w/a woman that might not even be real & just a chatbot is deceptive & downright scummy.”
Watching the Sleuthcon talk remotely, I took a screenshot of one of Cronbaugh’s slides, which had logos for 10 companies. Reverse image search helped me to identify many of the apps that ended up in Anthropic’s final report, including Dora, GraceChat, Jovia, Luma, and Romi. There were also other apps associated with the developers of those apps, such as Doni and Kira. (Anthropic listed some other apps in the report and said there were additional variants identified only by internal numeric. We looked into other apps that didn’t end up in Anthropic’s final report.)
In early June, several of the fake dating apps were still live on the Google Play Store: Doni, Dora, Jovia, Nalo, and Romi. And on the Apple App Store, we found four: Dora, GraceChat, Luma, and Romi, though Dora and GraceChat seemed like they were not dating apps, just apps Chrome-Stats,
Doni
and
Jovia
were removed from the Google Play store on September 1st, sharing the name and logo.
It appears that almost all of the apps were removed from both app stores prior to Anthropic’s report, though some were up as late as September.
GraceChat
,
Luma, and
Romi
were removed from the Apple app store on August 21st, according to Chrome-Stats.
Dora
now redirects to a movie app. On the Google Play store,
Dora
,
Romi
,
Luma
, and
Eterna
were removed September 3rd and
Nalo
was removed on September 7th. But as of September 16th,
Kira
is still up, and Gore-Kormanik confirmed that it shared the same code base as the others.
Anthropic did not respond to requests for comment about how or when it reached out to Google and Apple about these apps. But in the talk, Cronbaugh said, “Like we do in other cases where we observe misuse on other platforms, we have shared investigative information with these other providers so they can also take action on their platforms.” And the report says that its findings have been shared with Apple and Google directly.
Apple and Google did not immediately respond to a request for comment on if it had taken these apps down, when, and why it took as long as it did. Google also did not respond to a request for comment on why Kira is still up on the Google Play store. One of the indicators listed in Anthropic’s report was “Backend. managedkafka[.]heyhru-server[.]cloud[.]goog, the operator backend hosted on Google Cloud.” Since the apps were working for months after this talk, it raises the question of why Google didn’t shut infrastructure access down sooner. Google did not immediately respond to a request for comment about that either.
Related
Attack of the killer script kiddies
Read this before you vibe-code another app
Gore-Kormanik set up emulators in his lab and pulled the Android Package Kits, or APKs, for Doni, Dora, Jovia, Kira, Nalo, Romi, and another app we thought might be part of the network. Doing that makes it easier to inspect how the app works. From there, he conducted static analysis, meaning that he analyzed the code without the app running. He also did some dynamic analysis with a tool called Frida, which is a testing app that allows developers to crack open the apps, monitor and capture traffic, and see what endpoints they’re calling. He was trying to better understand how they worked, the infrastructure that they use, and which were tied to one another as part of a network.
While we couldn’t independently corroborate all of Anthropic’s findings from the Sleuthcon talk, it didn’t take long to start finding connections between the apps. It became clear just by poking around the app descriptions. For example, Dora, Romi, Luma, and another app called Eterna all had the same developer username, aprilsaidev. They also used the same email address, mailing address, and phone number. Dora, Romi, and Luma also shared the same developer identity, a nonprofit called Alliance Against Human Trafficking. Jenna Bing, president and cofounder of the Alliance Against Human Trafficking, said the organization did not develop or even know about these apps.
Doni historically appeared alongside Jovia and an app called Poka under the developer name iLexis Multimedia Consults. And Jovia and Doni shared the same Hong Kong address and phone number.
Reviewers found connections, too. A reviewer of Kira, the app that’s still up, wrote “full of fake accounts and paid employees pretending to be real accounts. set up a meeting for a breakfast date with a ‘match’ - i was at the location when the ‘user’ said she was right outside, but got called to an emergency. she was not outside (i could see out the windows) - no one was outside. a complete scam.”
Another reads “RANDOM VIDEO CALLS ARE ANNOYING. Having to purchase “gems” to chat w/a woman that might not even be real & just a chatbot is deceptive & downright scummy.” The reviewer goes on to write, “Unlimited messaging would be great, real women would be great, being able to exchange contact info whenever both people involved in the conversation give consent to do so would be great.” The reviewer also noted that matches respond too fast, but not to what’s actually being said.
Kira did not immediately respond to a request for comment about AI personas and metered conversations.
[The Kira app struggles with dialogue.]
[Kira app requesting more money to continue a conversation.]
[It’s a match?]
[A test conversation with the Kira app.]
Previous
Next
1
/
5
The Kira app struggles with dialogue.
Image: Zigula, Kira
One reviewer named Dora, Doni, GraceChat, and Romi as one app. The reviewer also describes reused/recycled video during slow periods. Separately, a Luma reviewer reported the same profiles appearing on Romi and Luma, but not recognizing them across apps. They said that messages read like LLM output.
Gore-Kormanik was able to confirm that Doni, Dora, Jovia, Kira, Nalo, and Romi are connected. “They share code to a T,” he told
The Verge.
“Also, all of these apps use the same backend architecture for their servers. The code uses the same language. It uses some of the same APIs across apps. They definitely are linked.”
According to Cronbaugh’s talk, Anthropic got wind of this operation by analyzing a single five-day-old prepaid account with no history that suddenly started sending out 100,000+ API requests a day. That’s when it learned that Claude was being misused to create female personas inside dating apps. But Claude was only being used as the conversation layer. A second model was used for photo generation, while a third generated emoji and sticker avatars, per Cronbaugh. This was done at scale. The report explained that Anthropic discovered more than 4,700 distinct fabricated AI personas engaging with at least 25,000 unique individuals over a two-week period in April. There were roughly 2.36 million messages during those two weeks.
Anthropic was able to trace and tie all of the apps together, Cronbaugh said at Sleuthcon, due to a grammatically broken phrase that was distinctive enough to use as a fingerprint to detect this entire network.
Cronbaugh said purchases route through in-app web checkout to third-party processors (not native app store payment), and that despite the apps looking unrelated, they all relied on the same coin infrastructure as well as the same set of third-party payment processors.
When an account was banned, Cronbaugh said, it didn’t take long for the scammers to recover. They’d create another account, or get access through another account. If that wasn’t possible, they’d switch to a different model provider. The accounts they saw within the network had all been created in the previous month.
Cronbaugh emphasized that this operation was built and run as a real company, with a real engineering team, and with modern tooling including AI coding assistants. They had design planning and design documents, roadmaps, configurations and structured app architecture, and growth plans as well as app store review behavior.
“Sophisticated scammers are running operations like businesses, which means they’re worried about revenue and they’re worried about costs. They’re leveraging tools to drive greater efficiencies,” said Tate Jarrow, founder and CEO of the anti-scam app
Jacana
and a former United States Secret Service cybercrime criminal investigator. Jarrow noted that any business today is looking to AI to drive efficiency — so it’s no surprise cybercriminals are doing the same. “It’s just like what every other consumer company that’s doing legitimate business thinks about.”
Anthropic attributes the operation to a China-based actor based on Chinese-language internal materials and China-native infrastructure. Apps don’t work inside China, and while they work in Asia outside of China, the monetization is turned off.
What makes these apps fraudulent, Jarrow said, is when people are paying for a service without knowing what it actually is — in this case, with a lack of awareness that they’re talking to AI bots. “When a company is taking advantage of the person’s lack of understanding or lack of knowledge in order to make money, that is the definition of a scammer, of fraud,” he said. And the obfuscation is also a hallmark, as legitimate companies don’t typically try to circumvent controls.
The apps themselves did try to circumvent controls. In his talk, Cronbaugh said apps would behave like normal dating apps prior to approval to evade App Store and Play Store review, after which developers would turn on the AI-generated persona network and coin meter. The apps deliberately hid their connections to one another through different accounts and developer identities. The apps would even shuffle around internal code to throw off simple identifiers like hashing. And, Anthropic’s report said, the in-app browser that redirected payments to third-party payment processors could be hidden during review by the App Store and Play Store.
Jarrow, whose app flagged some of these apps as scams when I was reviewing them, pointed to customer reviews as a way for app stores to detect these types of scams. “I think they should look at reviews as a signal for trust and safety teams.”
The proto repo, that same leaked manual mentioned above, had additional details on how the scam works.
“Essentially it outlines how the scam works and it outlines how they operate with the AI versus the human operators,” Gore-Kormanik explained. The manual made references to Dora. Although the engineering documents were only in Doni, repo files found in the proto repo were present across Doni, Dora, Kira, Jovia, Nalo, and Romi.
Anthropic attributes the operation to a China-based actor based on Chinese-language internal materials and China-native infrastructure. Gore-Kormanik noted that the apps used largely China-based or China-affiliated providers: they made use of Tencent Cloud’s messaging service and real-time video service, their internal documentation lived on Feishu, the schema file comments were in Chinese, the source code was hosted on Chinese code-hosting service Gitee, and app analytics and ad attribution went to ByteDance.
Gore-Kormanik found even more by changing his geolocation in the emulator. Apps don’t work inside China, and while they work in Asia outside of China, the monetization is turned off. “It’s only outside of Asia that it operates as a scam app,” he said.
Related
My uncanny AI valentines
Why people are falling in love with AI chatbots
How romance scams are thriving during quarantine
Jarrow said cybercriminals often avoid targeting the countries they’re located in to avoid enforcement. “All of these activities point to… What is the risk? The risk is that they identify the app, you bring heat on, and then it gets shut down.” Then the operators would lose all of their revenue and have to launch a new app and get new users, which is expensive. “They’re identifying risks for their business and then putting in controls.”
In the talk, Cronbaugh had mentioned that although Anthropic banned the accounts tied to the network and is building detection and hardening defaults, it would take cross-industry collaboration across app stores, payment platforms, and AI labs to disrupt these types of networks. “The apps stay on storefronts, the payments keep flowing, and a new account costs the operator about a day,” he said.
Weeding out scammers is a continuous battle requiring collaboration across the industry, but bad actors will continue to find ways to circumvent any controls that companies do put in place. Sadly, that leaves many people caught up before these schemes are unravelled.
Follow topics and authors
from this story to see more like this in your personalized homepage feed and to receive email updates.
Yael Grauer
AI
Tech
Most Popular
Most Popular
The iPhone 18 Pro’s big camera update is all about the small gains
Video
Microsoft announces Windows and Surface event for October 7th
The premium AirPods 5 are the best open-ear earbuds Apple has made
The Boox Palma 3 gets stylus support and a sleek redesign
Fujifilm’s Instax Pal 2 is a tiny digital camera that may not disappoint
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
- **Source**: [Original Article](https://www.theverge.com/ai-artificial-intelligence/995348/ai-dating-app-scams)
