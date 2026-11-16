---
title: AI-Voyager: A Public-Interest System for Human-AI Civic Reasoning to Contest and Shape the Rules That Govern AI
url: http://arxiv.org/abs/2611.17564v1
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-12_22-38-53Z_AI_Voyager_APublic_InterestSystemforHuman_AICivicR.md
generated_at: 2026-11-15 21:18
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AI-Voyager is a public-interest system designed to enable citizens and AI to collaboratively understand, contest, and shape the rules that govern artificial intelligence in their communities. The system processes 3,653 governance documents from city, state, federal, and national governments, allowing residents to read AI regulations from the perspective of affected workers, trace citations to exact source passages, and draft proposed revisions. The authors demonstrate strong retrieval performance (83.0% macro recall on 360 new questions) and conduct a user study with 24 participants examining how people engage with AI legislation when given grounded, verifiable explanations.

## Key Takeaways
- The system's architecture converts 3,653 governance documents into verifiable passages that preserve page and edition information, enabling bounded agentic search that verifies each statement against source text. This achieves 83.0% macro recall on 360 new questions requiring document retrieval, outperforming the strongest baseline at 80.5%, while iterative search contributes significantly (73.7% without it), and performance reaches 99.1% on a fixed-document benchmark.
- In a user study with 24 participants unfamiliar with two AI bills, most proposed changes focused on asking how provisions would apply to their specific situations rather than requesting wholesale rewrites. Participants actively chose interpretive lenses for the kind of explanation they wanted, demonstrating that citizens engage meaningfully with AI governance when given structured, perspective-aware tools.
- Citations served as signals of grounding but rarely motivated participants to actually check the source documents, revealing a gap between perceived trustworthiness and active verification behavior that has direct implications for how civic AI systems should be designed to encourage deeper engagement.

## Context
Governments worldwide are rapidly drafting AI regulations that define automated decisions, harms, and compliance requirements, often without meaningful public participation before rules take effect. This paper addresses a critical gap in AI governance research: existing systems focus on technical performance or policy analysis, but few provide citizens with accessible tools to read, question, and propose changes to the rules that directly affect their lives. By framing civic participation as a human-AI collaborative reasoning task grounded in exact public documents, AI-Voyager introduces a design grammar that bridges the gap between regulatory complexity and democratic engagement.

## Implications
For practitioners in AI governance and public policy, this work provides a concrete design space and evaluation framework for building systems that bind AI assistance to verifiable public text, offering a template for how civic participation tools should be architected and assessed. For industry stakeholders facing compliance with emerging AI regulations, the system demonstrates how affected workers can interrogate provisions from their own perspective, potentially informing how companies engage with communities during regulatory implementation. For the broader AI research community, the findings about citation behavior and participant engagement patterns highlight that grounding in source text is necessary but insufficient for fostering genuine civic verification, pointing toward future design needs for trust and accountability in public-interest AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.17564v1)
