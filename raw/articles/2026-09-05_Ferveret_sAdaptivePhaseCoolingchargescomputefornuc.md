---
title: Ferveret's Adaptive Phase Cooling charges compute for nuclear AI research
date: 2026-09-05
url: https://www.computerweekly.com/blog/CW-Developer-Network/Ferverets-Adaptive-Phase-Cooling-charges-compute-for-nuclear-AI-research
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://www.computerweekly.com/blog/CW-Developer-Network/Ferverets-Adaptive-Phase-Cooling-charges-compute-for-nuclear-AI-research
source_feed: AI Universe Explorer
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-09-05 22:28
---

# Ferveret's Adaptive Phase Cooling charges compute for nuclear AI research

## Full Article

Ferveret styles itself as the pioneer in Adaptive Phase Cooling for AI infrastructure.

This software-controlled technology is inspired by advanced heat-transfer principles used in nuclear reactor systems.

Why would developers be interested in this, unless there’s some compute payoff?

That’s exactly why… unlike conventional liquid cooling approaches, it is said to improve heat removal directly at the chip, enabling what the company claims is “higher sustained compute performance” as well as greater energy efficiency, higher rack densities and lower infrastructure overhead.

The T-shirt slogan for these guys is… by unlocking more compute from the same power envelope, Adaptive Phase Cooling helps AI infrastructure operators scale more efficiently while reducing power consumption and water use – okay, that’s too long for a T-shirt, but you get the idea.

## Fit for a hit, at MIT

Ferveret this month announced that researchers at the Massachusetts Institute of Technology (MIT) are using its high-performance computing platform to accelerate AI-driven materials research for next-generation nuclear energy.

The collaboration with MIT researchers may demonstrate how advanced thermal management can unlock up to 35% more usable compute from the same power envelope, validating the growing role infrastructure innovation will play as AI workloads continue to push the limits of modern computing.

> “Ferveret’s philosophy for evaluating high-performance AI infrastructure is simple: rather than relying solely on synthetic benchmarks or artificial stress tests, the company believes real scientific workloads provide a more meaningful measure of system performance while creating tangible value for researchers and others who need the compute,” said [Reza Azizian](https://www.linkedin.com/in/azizianreza/), co-founder and CEO, Ferveret.

MIT’s AI-driven materials research continuously pushes GPU infrastructure to its limits, providing an ideal environment to demonstrate how advanced cooling enables greater computational performance while accelerating scientific discovery.

## 15% more server-level compute

Ferveret’s Adaptive Phase Cooling enables GPUs to sustain higher performance while reducing thermal overhead, unlocking up to 15% more server-level compute compared with today’s leading direct-to-chip cooling approaches.

Azizian and team say that combined with facility-level efficiency improvements, software teams can realise up to 35% more usable compute from the same power envelope.

The computational demands of MIT’s research closely mirror those faced by organisations deploying large-scale AI infrastructure. By supporting one of the world’s leading research institutions, Ferveret is also demonstrating how advanced cooling can unlock greater performance for commercial AI deployments.

## AI-driven materials discovery

One project supported by Ferveret focuses on improving the analysis of coherent X-ray images collected from nuclear materials. Existing algorithms often struggle with the complexity of advanced reactor materials. Using Ferveret’s platform, researchers are developing AI-based approaches that improve the accuracy and reliability of X-ray image analysis.

> “We are leveraging generative AI to solve long-standing challenges in understanding materials for next-generation nuclear energy. Our AI models are significantly more accurate than conventional approaches, but they also push the limits of today’s computing infrastructure,” added Josseau.

A second area of research involves developing machine learning interatomic potentials that predict material behaviour at the atomic scale under extreme operating conditions. These models require substantial GPU resources during training while enabling simulations approaching the accuracy of density functional theory, one of the most computationally demanding methods in materials science.

## Infrastructure is the next AI frontier

As AI models continue to grow, access to compute is increasingly constrained by power, cooling and infrastructure rather than silicon alone.

Rather than measuring success solely through traditional metrics such as Power Usage Effectiveness (PUE), Ferveret focuses on maximising useful AI compute delivered per watt consumed.

![Image 1](https://itknowledgeexchange.techtarget.com/cwdn/files/2026/09/Reza-Azizian-Ferveret-150x150.jpg)

CEO Azizian: Adaptive Phase Cooling uses subcooled nucleate boiling, a mechanism borrowed from nuclear reactor thermal hydraulics.

Azizian says the next era of AI will be “constrained less by chips than by infrastructure” and every watt we save becomes another watt available for AI.

## CEO deep dive

The Computer Weekly Developer Network (CWDN) sat down with Azizian this week for more.

**CWDN:** Ferveret frames GPU cooling as the new AI performance bottleneck — what specifically was the engineering breakthrough behind Adaptive Phase Cooling that unlocks that extra headroom?

**Azizian:** The breakthrough is a shift in the boiling regime. Conventional two-phase immersion relies on saturated boiling, which throws off large bubbles that rise into a vapour plenum. That is why those systems need tanks and their own facility architecture.

> Ferveret’s Adaptive Phase Cooling uses subcooled nucleate boiling, a mechanism borrowed from nuclear reactor thermal hydraulics. Bubbles form on the chip surface and collapse back into the surrounding liquid before they ever reach a vapour space. Rapid bubble turnover constantly refreshes liquid at the surface, and rewetting is where the heat transfer actually happens. We optimised for rewetting frequency rather than bubble growth, and that is what creates the headroom.

**CWDN:** For developers running training jobs on this infrastructure, does the 35% compute gain translate into faster iteration cycles, lower cloud costs, or both, and by roughly how much?

**Azizian:** On cloud costs, the gain is direct. The 35% is more compute from the same power envelope, and power is the dominant operating cost in a data center. For an operator, that means the cost per GPU-hour falls, because you are amortising the same electricity bill across meaningfully more output. If that savings is passed through, a developer sees it as a lower rate. Whether it gets passed through is a commercial decision on the operator’s side, not a physics question.

> On iteration speed, it depends on what is constraining you. If your job is queued because the facility has no more power to bring GPUs online, which is increasingly the normal situation, then yes, directly. The same site now runs more GPUs, so your job starts sooner. Microsoft’s CEO has said publicly they have GPUs sitting in inventory they cannot power. That is the bottleneck we remove.

**CWDN:** What’s the worst-case scenario you’ve seen when an AI research team hits a thermal or power ceiling mid-project, and how did that actually derail their work?

**Azizian:** The worst case is that the infrastructure stops being able to support the research plan. Once a cluster hits its thermal or power ceiling, teams start making compromises they never budgeted for. Throttling GPUs. Reducing batch sizes. Spreading jobs across more hardware than the work needs. Or simply waiting for capacity that has not arrived.

**CWDN:** Beyond the headline 15% server-level and 35% total efficiency figures, what other performance or cost numbers can you share from the MIT deployment?

**Azizian:** MIT’s AI-driven materials research continuously pushes GPU infrastructure to its limits, providing an ideal environment to demonstrate how advanced cooling enables greater computational performance while accelerating scientific discovery. Working with Ferveret, they have been able to unlock 35% more usable compute from existing power. We expect to have more data as the engagement continues to evolve, and we’ll share that as soon as we can.

> The idea came from a simple observation. When we run systems at load to characterise them thermally, that compute goes nowhere. It is generated, paid for, and discarded. Our cooling is what makes the surplus exist in the first place, so donating it costs us nothing we were otherwise using.We started the conversation with MIT this summer, and the appeal on their side was straightforward: researchers who are priced out of compute access getting cycles they would not otherwise have.

On scaling it, I would rather under-promise.

We are treating MIT as the first case and learning from it before we talk about extending to other groups. Compute donation sounds simple and is not, since there are questions about scheduling, data handling, and what workloads are appropriate on test hardware. Once we have run it properly with one institution, we will know whether it generalises.

![Image 2](https://itknowledgeexchange.techtarget.com/cwdn/files/2026/09/Screen-Shot-2026-09-04-at-11.21.55.20-AM.png)

![Image 3](https://itknowledgeexchange.techtarget.com/cwdn/files/2026/09/Screen-Shot-2026-09-04-at-11.21.39.588-AM.png)

## Metadata
- **Source**: [Original Article](https://www.computerweekly.com/blog/CW-Developer-Network/Ferverets-Adaptive-Phase-Cooling-charges-compute-for-nuclear-AI-research)
