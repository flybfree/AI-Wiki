---

title: "Summary: DIRECT: When and Where Should You Allocate Test-Time Compute in Embodied Planners?"
url: http://arxiv.org/abs/2606.12402v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-10_17-58-49Z_DIRECT_WhenandWhereShouldYouAllocateTest_TimeCompu.md
generated_at: "2026-06-11 10:57"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces DIRECT, a routing framework that allocates test‑time compute to embodied agents based on multimodal scene context. Experiments across chain‑of‑thought depth, model size, and memory history show that test‑time scaling is not uniform; instead, different axes yield distinct capability gains. The router can match or exceed the performance of stronger models while reducing average latency by up to 65 %.

## Key Takeaways
- Test‑time compute is not a one‑size‑fits‑all lever: its effectiveness varies with chain‑of‑thought depth, model size, and memory history.  
- The DIRECT router improves the success–cost Pareto frontier by allocating resources where they matter most, rather than uniformly scaling up.  
- Naively increasing test‑time compute is wasteful; DIRECT delivers frontier‑level embodied planning at a fraction of the cost.

## Context
Vision‑Language Models are increasingly used as high‑level planners for robotic agents, and researchers have explored scaling test‑time compute to boost performance. However, this approach often inflates latency, token usage, and FLOPs without delivering proportional gains, limiting real‑world deployment.

## Implications
The findings suggest that efficient resource allocation is crucial for practical AI systems in robotics and beyond. Practitioners can achieve comparable or better outcomes with lower computational expense by using context‑aware routing instead of blanket scaling.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.12402v1)
