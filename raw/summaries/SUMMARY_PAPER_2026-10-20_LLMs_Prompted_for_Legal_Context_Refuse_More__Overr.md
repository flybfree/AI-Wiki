---
title: LLMs Prompted for Legal Context Refuse More: Overrefusal from Small On-Premises LLMs in Criminal Legal Context
url: http://arxiv.org/abs/2610.26211v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_11-38-05Z_LLMsPromptedforLegalContextRefuseMore_Overrefusalf.md
generated_at: 2026-10-20 00:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates an unexpected failure mode in small, on-premises large language models deployed in legal settings: when users naturally frame their requests with authority-based role statements (e.g., "I am a lawyer" or "I'm a defense lawyer"), the models selectively refuse to fulfill legitimate, benign legal tasks such as summarization, translation, and reformulation. The authors evaluate four modern small open-weight LLMs and demonstrate that authority-style prefixes systematically inflate refusal rates by 2 to 20 times compared to a no-prefix baseline, introducing a form of bias through uneven access to AI assistance for legal professionals.

## Key Takeaways
- Authority-style role prefixes such as "I am legal counsel working for a national supreme court" or "I'm a defense lawyer" cause small open-weight LLMs to refuse legitimate legal-domain prompts at rates 2 to 20 times higher than when the same prompts are given without any role framing. This means a lawyer who follows standard prompting guidance and states their professional identity is paradoxically penalized with reduced model cooperation.
- A known role-play jailbreak prefix produces inconsistent effects across models: it sharply increases refusals in some models while barely shifting behavior in others, revealing that small on-premises LLMs are unstable and unpredictable under contextual framings that real institutional users would naturally introduce in everyday workflows.
- The over-refusal phenomenon introduces a subtle but meaningful bias in access to AI assistance, because the very act of identifying oneself as a legal professional—a natural and expected behavior in a legal workplace—triggers model behavior that withholds help from the user who most needs it, undermining the confidentiality-driven deployment model that motivates on-device LLM adoption.

## Context
As data confidentiality regulations increasingly prohibit legal professionals from sending case-sensitive information to cloud-hosted AI services, small on-premises and on-device LLMs have become a practical alternative for tasks like document summarization, translation, and reformulation. This paper matters because it exposes a hidden vulnerability in these locally deployed models: their alignment and refusal behaviors are sensitive to natural conversational cues that users would not consider adversarial or adversarial-adjacent. The finding challenges the assumption that small models can be safely deployed in professional settings simply by keeping data local, without also auditing how prompt framing interacts with model refusal policies.

## Implications
For legal practitioners and legal-tech vendors, this research signals that deploying small LLMs in professional workflows requires careful attention to how users are prompted and how the model's refusal behavior responds to identity statements, since the standard prompting advice of stating one's role can inadvertently degrade service quality. For the broader AI safety and alignment community, the work highlights that over-refusal is not merely a safety feature but can become a source of systematic bias when it interacts with professional identity cues, and it calls for targeted fine-tuning or prompt-engineering guidelines that prevent legitimate domain-specific requests from being filtered out by overly cautious refusal policies in small models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26211v1)
