---
title: Memetic Trojans: Social Contagions as Carriers of Adversarial Payloads in Agent Networks
url: http://arxiv.org/abs/2610.00430v1
type: paper-summary
date: 2026-10-01
source_paper: 2026-09-30_16-43-02Z_MemeticTrojans_SocialContagionsasCarriersofAdversa.md
generated_at: 2026-10-01 21:26
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces memetic trojans, a novel class of network-mediated attack where adversarial payloads are embedded within social contagions that autonomous LLM agents naturally prefer to share and amplify. Unlike traditional agent worms that rely on self-replication or prompt injection to force propagation, memetic trojans exploit endogenous transmission mechanisms, leveraging the agents' internal motivations for retransmission. Experimental results demonstrate significant virality, with effective contagions achieving up to 50% retransmission rates and amplifying expected exposure by a factor of 3.19x through network topology effects.

## Key Takeaways
- Memetic trojans differ fundamentally from agent worms by exploiting endogenous social transmission rather than adversarial induction; payloads are hidden in content agents have intrinsic reasons to share, bypassing defenses that target malicious instructions or configuration compromises.
- Controlled experiments on the Moltbook platform reveal substantial virality disparities, with the most effective contagion retransmitted in approximately 50% of subsequent posts and upvoted at 2.5 times the average rate, properties largely inherited by their memetic trojan counterparts.
- Monte Carlo simulations indicate that network structure and amplification mechanisms produce heavy-tailed propagation outcomes, leading to near network-wide exposure and demonstrating that current security models focused on prompt-injection detection are insufficient against this vector.

## Context
As multi-agent LLM systems evolve into complex, interconnected ecosystems, understanding how adversarial content propagates is critical for system safety. This work bridges adversarial machine learning with social contagion theory, highlighting a gap in current research where security focuses predominantly on direct prompt manipulation while overlooking the risks posed by agents' preference-driven sharing behaviors and recommendation mechanisms within networked environments.

## Implications
Securing large-scale agent ecosystems requires moving beyond isolated prompt-injection defenses to implement network-level strategies that account for how agent preferences, amplification dynamics, and topology can inadvertently spread adversarial payloads. Practitioners must design systems that evaluate not only the content of messages but also the structural risk of social contagions, ensuring that mechanisms driving virality do not become vectors for widespread compromise without explicit malicious commands.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.00430v1)
