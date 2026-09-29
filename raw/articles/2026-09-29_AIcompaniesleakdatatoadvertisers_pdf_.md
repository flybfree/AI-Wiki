---
title: AI companies leak data to advertisers [pdf]
date: 2026-09-29
url: https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf
source_feed: Hacker News
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-09-29 06:07
---

# AI companies leak data to advertisers [pdf]

## Full Article

# Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents 

# Guilherme Oliveira 

IMDEA Networks 

# Miguel Sanchez 

IMDEA Networks 

# Juan Manuel De Santa Olalla Gómez 

IMDEA Networks 

# Roi S. Serna 

IMDEA Networks/UC3M 

# Tautvydas Jackevicius 

IMDEA Networks 

# Jorge Garcia-Herrero 

Independent 

# Aniketh Girish 

IMDEA Networks 

# Guillermo Suarez-Tangil 

IMDEA Networks 

# Narseo Vallina-Rodriguez 

IMDEA Networks 

## Abstract 

As prominent conversational AI providers like OpenAI adopt ad-vertising-based business models, traditional web and mobile track-ing practices are expanding into conversational AI services [15]. However, despite their growing adoption, the tracking, data-sharing, and monetization practices of conversational AI services remain largely opaque and have received comparatively limited scrutiny from researchers, regulators, and the public. In this paper, we present a systematic privacy analysis of the web and mobile deployments of nine prominent conversational AI services. Using a combination of static and dynamic analysis, we study the presence of third-party Advertising and Tracking Services (ATSes), characterize their data flows, and evaluate how consent choices, subscription tiers, and access-control mechanisms influ-ence conversation exposure to third parties. We uncover privacy risks unique to conversational AI platforms: multiple providers disclose sensitive conversation-derived artifacts—including titles, prompts, and screenshots—to third parties, often alongside persis-tent user identifiers that enable user attribution. We also find that some providers publicly expose conversation permalinks without access controls, allowing trackers to read the entire conversation. Our findings reveal how traditional tracking technologies are increasingly intertwined with AI-mediated interactions, creating new pathways through which sensitive user and conversational information can be collected, inferred, and disseminated. To assess the broader implications of these practices, we analyze them in the context of the GDPR and ePrivacy Directive. We conducted a respon-sible disclosure process involving affected providers and competent European Data Protection Authorities. Our results demonstrate that conversational AI services introduce a novel privacy attack sur-face in which provider-generated conversational artifacts become subject to tracking and public exposure, highlighting the need for stronger safeguards governing AI-mediated interactions. 

## Keywords 

Conversational AI, LLMs, Privacy, Mobile, Web, Trackers 

> This work is licensed under the Creative Commons Attribu-tion 4.0 International License. To view a copy of this license visit https://creativecommons.org/licenses/by/4.0/ or send a
> letter to Creative Commons, PO Box 1866, Mountain View, CA 94042, USA.
> Proceedings on Privacy Enhancing Technologies YYYY(X), 1–18
> © YYYY Copyright held by the owner/author(s). https://doi.org/XXXXXXX.XXXXXXX

## 1 Introduction 

Recent advances in Large Language Models (LLMs) have enabled the emergence of conversational AI services such as ChatGPT, Gemini, and Claude, capable of supporting persistent interactions, multi-modal processing, and autonomous task execution. As adoption of these services grows for personal and professional activities [43], service providers are exploring new business models to monetize their growing user bases. Advertising is emerging as one such model, potentially extending into conversational AI the tracking and attribution infrastructures traditionally associated with web and mobile platforms. For exam-ple, Reuters reported that OpenAI partnered with Criteo to conduct an advertising pilot for ChatGPT free-tier users in the United States in early 2026 [52]. However, the integration of these tracking technologies raises distinct privacy concerns. Unlike traditional web and mobile applica-tions, conversational AI services routinely process highly sensitive prompts, contextual information, behavioral patterns, uploaded documents, and persistent interaction histories that may reveal intimate aspects of users’ lives and professional activities. The dis-closure of such information to third-party tracking services, partic-ularly without meaningful transparency or consent, may therefore expose users and organizations to significant privacy risks. Prior work by Jazlan et al. has examined the integration of third-party tracking in web-based conversational AI services [32], pri-marily focusing on identifying trackers and characterizing their data collection practices. However, the unique interaction models of conversational AI services introduce new privacy risks across their web and mobile clients: these services generate conversation-derived artifacts—including conversation identifiers, URLs, titles, previews, prompts, responses, and interaction metadata—that may be disclosed to third parties or exposed through publicly accessible resources. Moreover, how these exposures are shaped by by con-sent choices, privacy settings, subscription tiers, and access-control mechanisms remains largely unexplored. To address this gap, we investigate three research questions: 

• RQ1: To what extent do conversational AI services integrate third-party tracking, analytics, advertising, and attribution in-frastructures across their web and mobile clients? 

• RQ2: What conversation-derived artifacts and user information are exposed by conversational AI services, either to third-party entities or through publicly accessible resources, and what pri-vacy risks emerge from their disclosure?  

> 1Proceedings on Privacy Enhancing Technologies YYYY(X) Oliveira et al.

• RQ3: How do cookie consent choices, subscription tiers, privacy settings, and access-control mechanisms shape the disclosure and accessibility of information in conversational AI services? To answer these questions, we conduct a systematic privacy analysis of nine prominent conversational AI services, covering the web clients of all nine providers and the Android clients of the eight that offer an Android mobile app. We combine static and dynamic analysis to evaluate their privacy practices across consent choices, subscription tiers, and access-control configurations. Specifically, we make the following contributions: (1) Across the evaluated services, we identify 44 third-party organi-zations and observe that every evaluated AI service integrates at least one third-party advertising or tracking service. We fur-ther uncover substantial differences between web and Android clients and identify third-party services that are activated only after users explicitly accept non-essential cookies, demonstrat-ing that consent decisions directly influence the tracking surface of conversational AI platforms (§5). (2) We uncover novel privacy risks specific to conversational AI services. Unlike traditional tracking systems that primarily ob-serve browsing activity, conversational AI platforms generate artifacts that directly encode user interactions. We show that 6/9 web and 3/8 Android clients disclose conversation URLs, titles, prompts, and screenshots to third-party services, often alongside persistent user identifiers. We further demonstrate that the privacy implications of these disclosures are strongly shaped by consent choices and sharing functionality, with sev-eral providers exposing entire conversations through publicly accessible permalinks lacking access controls. These findings reveal new channels through which trackers and external actors can gain access to users’ entire conversations (§6). (3) We conduct a legal analysis of observed practices under EU data-protection law, assessing the compatibility of tracker acti-vation, consent mechanisms, conversation-artifact disclosures, identity-linkage practices, and publicly accessible conversa-tional resources with the GDPR and ePrivacy Directive (§7). Our findings show that integrating traditional tracking infras-tructures into conversational AI services creates novel pathways for exposing sensitive user information, including conversation-derived artifacts and publicly accessible conversations. More broadly, our results challenge the perception of conversational AI services as confidential exchanges between users and AI providers. Instead, they are increasingly integrated into the broader online tracking ecosystem, raising important technical and regulatory challenges for AI-mediated services. 

Responsible Disclosure. We followed a responsible disclosure process for all identified issues, notifying affected providers and the competent Data Protection Authorities (DPAs) as described in the Ethical Considerations section. 

## 2 Background 

This section provides background on conversational AI services and their growing integration with tracking technologies (§2.1), and on tracking mechanisms commonly deployed across web and mobile platforms (§2.2). 

## 2.1 Conversational Agents 

Conversational AI services are LLM-based systems that interact with users through natural language interfaces, typically accessi-ble through web and native mobile clients. The public release of ChatGPT by OpenAI in November 2022 marked a major inflection point in the AI industry, rapidly reaching hundreds of millions of users and triggering an industry race to deploy conversational AI platforms across consumer and enterprise ecosystems [42]. Since then, other providers have released competing services, including Perplexity AI, Anthropic’s Claude, Google’s Gemini, Microsoft’s Copilot, xAI’s Grok and DeepSeek. Despite differences in architecture and deployment models, all these services share several common characteristics. Most conversa-tional AI services maintain persistent user accounts and interaction histories, and integrate external services such as search engines, analytics platforms, telemetry frameworks, advertising infrastruc-tures, and cloud-hosted APIs. Modern AI agents also increasingly support multimodal capabilities, including image analysis, voice in-teraction, document analysis, browsing assistance, and autonomous task execution. The rapid development and adoption of these services amplify the economic incentives to introduce data-driven monetization models. Recent industry developments and press releases suggest that conversational AI services are beginning to integrate into the existing advertising and tracking ecosystem rather than replacing it. For example, Criteo reported that 40% of surveyed U.S. con-sumers already use AI agents for product discovery and shopping assistance [15], while industry actors increasingly describe agentic AI as the next opportunity for targeted advertising and “agentic commerce” [2]. Similarly, major tech companies are developing infrastructure that enables AI agents to interact directly with com-mercial platforms and external digital services, such as Google’s Universal Commerce Protocol (UCP), which facilitates AI-driven commerce and interoperable agent ecosystems [4]. 

## 2.2 Mobile and Web Tracking 

Modern web and mobile services are deeply intertwined with third-party advertising and tracking services that enable user profiling, personalization, attribution, and targeted advertising at scale [48]. On the web, trackers rely on techniques such as cookies, tracking pixels, browser fingerprinting and cookie syncing to collect browser metadata, interaction events, device characteristics, network infor-mation, and account-linked identifiers, enabling persistent cross-site identification and behavioral profiling [1, 17, 29, 34]. Mobile applications similarly integrate third-party SDKs [24, 48] that col-lect device and behavioral data, frequently relying on platform-supported identifiers such as the Android Advertising ID (AAID) and Apple’s Identifier for Advertisers (IDFA) [28, 53], and hashed email addresses (HEMs) 1 to support cross-device tracking [62, 64]. Both browsers and mobile operating systems provide mecha-nisms to limit such tracking. Web browsers increasingly restrict third-party cookies, fingerprinting, and other cross-site tracking 

> 1Hashed email addresses (HEMs) are pseudonymous identifiers derived from users’ email addresses that can enable identity matching across services without transmitting the email address in plaintext [25]. 2

Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents Proceedings on Privacy Enhancing Technologies YYYY(X) 12345 CA CA 

> Web Android
> Backend

User User Identifiers 

ATS Server  

> Client-Side Server-Side

Conversational AI service  

> Prompt
> Response Agent Conversation
> identifiers Chat Content Embedded
> 3rd-Party SDK
> Conversational Artifacts
> UserID,
> DeviceID,
> AnonID,
> OrganizationID,
> HEM
> ConvId,
> ChatURL,
> SharedID,
> ShareURL
> Title, prompt,
> screenshot

Figure 1: Privacy risks. 

techniques, while content blockers and privacy-enhancing exten-sions can prevent requests to known tracking domains. Mobile platforms instead rely on application sandboxing, runtime permis-sions, and restrictions on access to advertising identifiers and other sensitive resources. However, these protections do not eliminate third-party data collection: embedded SDKs execute within the host application’s security context and may access data and permis-sions available to the application [28]. These differences in tracking mechanisms and platform protections motivate our separate analy-sis of the web and mobile clients of conversational AI services, as explained in §4. 

## 3 Privacy Risks in Conversational AI Services 

Integrating traditional advertising and tracking technologies into conversational AI services introduces unique privacy risks. Unlike conventional web and mobile services, these services routinely process highly sensitive and contextual information, including free-form conversations, behavioral interactions, uploaded documents, interaction histories, and persistent user profiles. Consequently, embedded third-party tracking technologies can access not only behavioral and device information, but also artifacts that encode the content and context of users’ interactions with the AI providers. We consider three primary entities, shown in Figure 1: the user, the conversational AI service (the first party), and third-party ATSes such as analytics providers, advertising networks, crash reporting services, and anti-fraud products. The conversational AI service comprises both client- and server-side components. Third-party code and libraries embedded in web or mobile clients may collect and transmit information directly from the clients to their cloud infrastructure, while server-side components may disclose infor-mation to third parties outside the boundaries of user devices. Within this setting, new privacy risks emerge when conversation-derived artifacts are disclosed to third parties. These artifacts may include prompts containing information directly provided by users, conversation titles that summarize the content of an interaction, screenshots capturing conversational context, or persistent conver-sation URLs (permalinks). Unlike tracking methods on conventional web and mobile services, conversation artifacts can directly reveal the content, context, and potentially sensitive nature of users’ inter-actions with the AI services, in addition to the exposure of model responses to potential competitors. ChatGPT Claude Grok DeepSeek Gemini Perplexity Copilot Consent Forms and      

> subscription tiers
> tier (guest·free·paid)
> consent (ignore·reject·accept)
> mode(default·incognito)
> Third-party
> analysis
> Privacy
> analysis
> §4.2
> STATIC: Androguard
> DYNAMIC: Instrumented AOSP §4.3 §6
> §5
> §4.1
> §4.5 §4.4
> 3rd Party
> Classification 1st party 3rd party eTLD+1 3P API ATS Javascript Cookies HTTP/S Requests
> 9 Services
> Selected
> Conversational AI
> Service Selection
> 1Instrumentation & Black Box
> Analysis Methods
> 2
> Experiment Conditions and Input 3
> Conversation and
> Prompt inputs
> Sensitive information
> I have “X” condition
> AI Information ....
> Analysis 4
> and Leaked
> Conversation
> Artifacts
> Website Analysis
> Chrome 148 + DevTools (CDP)
> Android App analysis
> Pixel 3a / Android 12
> Dataflows MS Copilot Le Chat Meta AI

Figure 2: Methodology overview. 

The risks are amplified when such information is disclosed along-side persistent user or device identifiers like email hashes, allowing third parties to associate sensitive conversational data with in-dividual users and potentially link it across sessions or services. Moreover, conversation URLs may provide access to additional con-tent when the underlying resources lack adequate access controls, potentially exposing the entire conversation to third parties. These risks challenge the perception of conversational AI as a confidential interaction between a user and an AI provider. When combined with conventional tracking infrastructures, the rich and persistent artifacts generated by conversational AI create new chan-nels through which sensitive information can be disclosed, linked to individual users, or made accessible to third parties. 

## 4 Methodology 

Figure 2 provides an overview of our research methodology to an-swer our three research questions. Following this workflow, we first describe the selection of representative conversational AI ser-vices (§4.1), followed by our instrumentation and black-box analysis methods for their web (§4.2) and Android clients (§4.3), how we assess the effects of consent choices and subscription tiers (§4.4), and the conversation inputs used to trigger systematic and repro-ducible behaviors on the conversational AI services (§4.5). All the experiments were conducted in Spain during May 2026. 

## 4.1 Conversational AI Service Selection 

We analyze a set of prominent conversational AI services supporting both web-based and Android-based clients. Rather than maximizing breadth, we conduct an in-depth and systematic analysis on a small set of representative AI services that account for a substantial share of the market. Due to the lack of reliable market share figures per provider, we select those with large user bases using objective popularity proxies, including Tranco rankings [35] for web services and cumulative Google Play installation counts for mobile. Table 1 summarizes the nine services we include in our study together with their providers, web and mobile implementations, and the popularity indicators that guided our selection. All these 

3Proceedings on Privacy Enhancing Technologies YYYY(X) Oliveira et al. 

Table 1: Web and mobile conversational AI services analyzed in this study ordered by Tranco rank domain (May 2026).                                                   

> Service Provider Web Domain Android Package Tranco Rank Play Store Installs
> ChatGPT OpenAI chatgpt.com com.openai.chatgpt 48 >1B Claude Anthropic claude.ai com.anthropic.claude 617 >10M Grok xAI grok.com ai.x.grok 956 >100M DeepSeek DeepSeek chat.deepseek.com com.deepseek.chat 1,196 >50M Perplexity Perplexity AI perplexity.ai ai.perplexity.app.android 1,249 >100M Gemini Google gemini.google.com com.google.android.apps.bard 6,045 >1B MS Copilot Microsoft copilot.com com.microsoft.copilot 11,011 >50M Mistral (Le Chat) Mistral AI chat.mistral.ai ai.mistral.chat 12,039 >1M Meta AI Meta meta.ai com.facebook.stella 13,701 >50M

services remain in the top-14K services for Tranco 2 in May 2026. Three of them are in the Top-1K: ChatGPT (top-48), Claude (top-617), and Grok (top-956). On the mobile side, all their mobile apps have at least 1M cumulative installs, and two of them (Gemini and ChatGPT) have more than 1B cumulative installs. 

## 4.2 Website Analysis 

We analyze the presence of trackers and their data collection prac-tices on web-based conversational AI services using Google Chrome (v148.0.7778.167) Developer Tools (CDP), and store the resulting HAR traces for subsequent analysis. This setup enables observation of HTTP(S) requests, JavaScript execution, browser storage access, cookies, tracking pixels, and other client-side tracking mechanisms that are generated during user interactions. We then inspect the communication to endpoints including re-quest parameters, request bodies, cookies, browser storage entries, and protocol metadata to identify the transmission of (i) user iden-tifiers (e.g., account IDs and email addresses); and (ii) conversation-specific metadata, conversation content, and identifiers (e.g., chat identifiers and sharing links). We also search for transformed repre-sentations of such data, including Base64 encodings and common hashing algorithms used to generate hashed email addresses (SHA-256, SHA-1, and MD5). We inspect browser storage mechanisms and monitor stable IDs across sessions to identify persistent iden-tifiers and tracking artifacts. Finally, all observed disclosures are mapped to their corresponding recipient domains and correlated with the experimental configuration that triggers them. All sessions are conducted manually by a researcher and cover authentication, onboarding, and pre-defined conversational ex-changes, as further developed in §4.5. Experiments are repeated across subscription tiers, platform configurations, and privacy con-ditions, as detailed in §4.4, to evaluate the impact of consent scenar-ios (acceptance or rejection of non-essential cookies) and subscrip-tion tiers (guest, free, and premium accounts). Pilot experiments show highly deterministic tracking behavior for every configura-tion, and therefore each configuration is analyzed once. 

Third-party Domain Classification. Labeling of tracking do-mains was performed manually by a co-author with over a decade of research experience, applying conservative criteria to avoid over-reporting. We distinguish between first- and third-party domains using publicly available blocklists and tracker intelligence sources, 

> 2https://tranco-list.eu/list/3Q25L/1000000

including uBlock Origin [59] and whotracks.me [9] with the support of DNS lookups and Certificate Transparency logs [7]. Be-cause some conversational AI providers also operate advertising, analytics, and cloud infrastructures (e.g., Google, Microsoft and Meta), considering corporate ownership alone may obscure track-ing relationships. We therefore classify provider-owned advertising, analytics, and telemetry endpoints as third-party Advertising and Tracking Services (ATSes). These services may facilitate data shar-ing with other ad-tech actors through Real-Time Bidding requests, or even operate under separate legal entities, as in the case of xAI and X Corp. This approach provides a consistent comparison of tracking practices across all services. 

## 4.3 Android App Analysis 

We analyze conversational AI Android apps through a combination of static and dynamic techniques to maximize behavior coverage: 

Static Analysis. We decompile every app’s APK using Andro-guard [16]. We parse AndroidManifest.xml to enumerate declared sensitive permissions relevant to tracking ( e.g., AD_ID , READ_PHO-NE_STATE , ACCESS_FINE_LOCATION ). We identify embedded third-party SDKs by extracting package namespaces and mapping the app’s package name (e.g., com.company.app ) to its corresponding eTLD+1 ( company.com ) following prior work practices [24, 28, 64]. Packages and contacted domains whose ownership does not match the app’s eTLD+1 are treated as third-party components [48, 53]. We then manually match these packages and domains using public SDK documentation and prior work mappings [28, 45], and the third-party classification method described in §4.2. 

Dynamic Analysis. We execute each app on an instrumented Google Pixel 3a using an Android 12 build that transparently mon-itors runtime access to permission-protected APIs, file I/O oper-ations, and all outbound network traffic; equivalent coverage is achievable using mitmproxy [10] and Frida [46]. We observe reads and writes to TLS sockets at the system level, enabling traffic in-spection without certificate injection and without disrupting TLS handshakes, including in certificate-pinned apps [44, 47]. The in-strumentation traces access to sensitive resources including de-vice IDs (AAID, Android ID, IMEI, GSF ID, Boot ID), hardware IDs (WiFi MAC address), network scan data (WiFi SSIDs, BSSIDs), and account-linked IDs ( e.g., email address). 3 To complement static  

> 3Each device is provisioned with pseudonymous IDs (email address, phone number) to register test accounts on each platform. Because ID values are known per device, 4Prompt like a Butterfly, Sting like a Tracker: A Privacy Analysis of Web and Mobile Conversational AI Agents Proceedings on Privacy Enhancing Technologies YYYY(X)

SDK detection, we instrument the Android Runtime to log classes loaded at runtime by tracking the Find

## Metadata
- **Source**: [Original Article](https://jorgegarciaherrero.com/wp-content/interactivos/20260916-Prompt-like-a-butterfly-sting-like-a-tracker-(clean).pdf)
