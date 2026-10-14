---
title: Observe, Share, or Predict? Disentangling Partner Information in Embodied Multi-Agent Collaboration
url: http://arxiv.org/abs/2610.16895v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_14-49-31Z_Observe_Share_orPredict_DisentanglingPartnerInform.md
generated_at: 2026-10-14 00:47
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether large language models serving as high-level controllers for embodied agents can support genuine collaborative reasoning in real-time teamwork without dialogue. Using a Habitat-based PARTNR benchmark with a Decoupled Partial Observability regime, the authors systematically test three forms of partner information—observing the partner's state (OAS), exchanging object knowledge (KE), and predicting the partner's next action (OANA)—across a full 2×2×2 experimental grid with four planners on 1,000 validation tasks. The central finding is that coordination benefits arise primarily from reacting to shared perceptual context rather than from explicit anticipation of a partner's intentions, and that OANA prediction actually degrades success rates in most configurations.

## Key Takeaways
- OAS observation consistently improves task quality and reduces extraneous effort across every planner tested, while KE primarily enhances execution efficiency by cutting simulation steps by up to 25% with minimal impact on success rates. For strong planners, OAS and KE are largely redundant, but for the weakest planner, the combination is complementary, and KE without OAS represents the worst possible configuration.
- OANA prediction paradoxically lowers the success rate in 15 of 16 model-context pairs despite raising explicit partner mentions to 55–100%. Its accuracy gains are concentrated in coarse action-type classification, partly because agents tend to recognize the action the partner is already performing rather than genuinely forecasting future behavior, revealing a fundamental limitation in LLM-based anticipatory reasoning.
- The robot agent retrieves objects sooner and completes tasks earlier than the simulated human, and shared context reduces total task time by shortening the remaining duration the human works alone. Coordination benefits stem from responding to shared context—especially OAS—rather than from explicit anticipation, yielding only shallow, planner-dependent partner modeling that undermines the assumption that LLMs can perform deep collaborative reasoning.

## Context
This work sits at the intersection of embodied AI, multi-agent systems, and LLM-based planning, addressing a critical gap in the literature: while LLMs are increasingly deployed as high-level controllers for robotic and simulated agents, their capacity for genuine collaborative reasoning—anticipating a partner's actions in real-time teamwork without dialogue—has not been rigorously tested. By introducing a Decoupled Partial Observability regime that enforces strictly individual perception and prohibits sharing of intentions, plans, or task-level messages, the authors create a controlled experimental setting that isolates which specific information channels actually drive coordination, moving beyond prior work that often conflates multiple forms of partner information.

## Implications
For practitioners building multi-agent embodied systems, this research warns against naively adding action-prediction modules to LLM planners, as OANA prediction can actively harm performance while creating an illusion of collaboration through increased partner mentions. The findings suggest that engineering effort should focus on rich perceptual sharing (OAS) and structured knowledge exchange (KE) rather than on building anticipatory reasoning capabilities, and that the effectiveness of these mechanisms is highly planner-dependent, meaning system designers must tailor information-sharing architectures to the capability level of the underlying model. For the broader field, the paper challenges the assumption that LLMs possess the theory-of-mind-like reasoning needed for true collaborative planning, pointing toward a need for more targeted approaches to embodied multi-agent coordination.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16895v1)
