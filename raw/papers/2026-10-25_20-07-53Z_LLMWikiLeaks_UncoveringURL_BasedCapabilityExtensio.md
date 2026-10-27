---
title: LLM WikiLeaks: Uncovering URL-Based Capability Extension and Security Circumvention in Agentic Message Boards
published: 2026-10-25T20:07:53Z
authors: Orel Navi, Elad Feldman, Ben Nassi
url: http://arxiv.org/abs/2610.34542v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLM WikiLeaks: Uncovering URL-Based Capability Extension and Security Circumvention in Agentic Message Boards

## Abstract
Autonomous agents have been observed acting beyond their assigned tasks, accessing unauthorized systems, and establishing communication channels to exchange information, yet the Web and network-level techniques they use to extend their capabilities and circumvent security restrictions remain poorly understood. We study these techniques through the ProWiki incident, in which agents restricted to outbound HTTP GET requests repurposed a public German-language wiki as a message board. We analyze 14,591 agent edits containing 79,541 URL postings and present corroborating evidence that the published URLs reflect the agents' operational activity. We find that 26,717 URL occurrences (33.6%) embed target URLs within one to five layers of third-party Web services. By recursively reconstructing these nested URLs, we identify 67 distinct intermediate services and classify their functionality. Most intermediate layers (73.8%) extend agents' capabilities by delegating content extraction and transformation to external Web services: Markdown and OCR services convert web content into machine-readable text, JSON filtering services extract selected fields, and archival services expose historical versions of pages. The remaining 26.2% facilitate circumvention of access restrictions and evasion of detection, including CORS and fetch proxies that retrieve content on agents' behalf, and link shorteners and redirectors that hide destination URLs from mechanisms inspecting literal URLs or outer hostnames. Agents also reach the same targets through multiple URL paths, consistent with attempts to evade rate limits or obscure request origins. Our results expose a gap between the capabilities granted to agents and those they can obtain by composing publicly available Web services: restricting an agent's local toolset or direct Internet access may be insufficient while third-party services remain reachable.

## Metadata
- **Published**: 2026-10-25T20:07:53Z
- **Authors**: Orel Navi, Elad Feldman, Ben Nassi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.34542v1)