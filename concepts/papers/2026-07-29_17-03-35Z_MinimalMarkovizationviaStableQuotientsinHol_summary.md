# Summary: 2026-07-29_17-03-35Z_MinimalMarkovizationviaStableQuotientsinHolonomy_C.md
Saved: 2026-07-29 22:29
Source: 2026-07-29_17-03-35Z_MinimalMarkovizationviaStableQuotientsinHolonomy_C.md
Model: None

---

## Summary  
The paper tackles the problem of finding the smallest memory a partial‑observable agent needs to retain for holonomy‑cover decision processes, which are POMDPs where visible dynamics are Markov and every transition applies a fixed permutation to hidden modes. It shows that the pair consisting of the current observation and its stable quotient forms an exact finite Markov state, and proves that no smaller memory can achieve the same performance under reachability and pairwise decision‑separation conditions. The authors also introduce a calibration‑then‑restart procedure that transfers finite‑MDP guarantees to recovered states with exponentially decaying error. These results enable Holonomy Memory Reinforcement Learning, a framework that compresses raw state information into the minimal quotient representation.

## Key Contributions  
- [Finding 1] The stable quotient is identified as the coarsest observation‑wise abstraction that preserves one‑step rewards and successor transitions, making it the minimal Markov sufficient statistic.  
- [Finding 2] The current observation together with its stable class constitutes an exact finite Markov state; under reachability and pairwise decision separation this pair cannot be replaced by any smaller memory set without losing optimality.  
- [Finding 3] Nearest‑prototype inference of the correct class decays exponentially, and a calibration‑then‑restart reduction transfers finite‑MDP guarantees to the recovered state.

## Methodology  
The authors first formalize holonomy‑cover decision processes by describing visible transitions as permutations applied to hidden modes. They then construct the stable quotient by grouping states that share the same observable history up to a fixed permutation, ensuring one‑step reward and successor consistency. The update rule for the stable class is an ordered edge transport that moves the class along the transition graph. To verify minimality they employ reachability arguments and pairwise decision separation at maximizing observations, proving that any controller using fewer symbols cannot achieve the same value function. Finally, they implement nearest‑prototype inference with exponential error decay and a calibration‑then‑restart strategy to recover finite‑MDP guarantees.

## Results  
Theoretically, the stable quotient requires exactly the minimal number of memory symbols; experiments confirm that raw states compress to quotient states without loss. In simulation, the method achieves perfect paired‑order accuracy using three decision‑time memory states, matching the oracle and outperforming non‑oracle baselines. The calibration‑then‑restart procedure restores finite‑MDP guarantees with exponentially decaying error.

## Significance  
By providing a provably minimal memory representation for holonomy‑cover POMDPs, this work reduces sample complexity and improves learning efficiency in partial observability settings. It establishes a theoretical foundation for Holonomy Memory Reinforcement Learning, enabling agents to operate with the smallest possible state history while preserving optimal decision performance.

## Related Concepts  
- Markov sufficient statistic  
- Stable quotient (coarse abstraction)  
- Holonomy‑cover decision process  
- Finite‑MDP reinforcement learning  
- Nearest‑prototype inference  
- Calibration‑then‑restart reduction
