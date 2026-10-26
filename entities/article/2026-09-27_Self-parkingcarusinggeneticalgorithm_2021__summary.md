# Summary: Self-parking car using genetic algorithm (2021)
Saved: 2026-10-25
Source: 2026-09-27_Self-parkingcarusinggeneticalgorithm_2021_.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://trekhleb.dev/blog/2021/self-parking-car-evolution/)

---

## Summary
This article details a project that trains autonomous vehicles to perform self-parking using a genetic algorithm implemented in TypeScript. The core methodology involves evolving a "brain" function, represented as a genome of 180 bits, which maps sensor inputs to motor control signals for the engine and steering wheels. Through iterative generations, starting from random behaviors, the simulated cars learn to navigate obstacles and park successfully, with significant improvement observed around the 40th generation.

## Key Takeaways
- The project simplifies autonomous driving into a low-level optimization problem by reducing car behavior to finding an optimal combination of 180 bits, which constitute the car's genome. This approach breaks down complex navigation tasks into manageable genetic parameters.
- The simulation architecture is divided into distinct components: "muscles" (engine and steering actuators), "eyes" (sensors for obstacle detection), and a "brain" (a pure function mapping sensor data to movement signals). The brain evolves over time, while the physical constraints remain fixed.
- Learning progress is gradual; initial generations exhibit random, erratic behavior, but by approximately the 40th generation, the cars begin to understand self-parking mechanics. However, performance remains imperfect, with collisions and imprecise parking still occurring, highlighting the limitations of early-stage evolutionary training.

## Context
This work serves as an educational demonstration of genetic algorithms applied to robotics and autonomous systems. It illustrates how evolutionary computation can solve control problems without traditional supervised learning or complex neural networks. By providing a browser-based simulator and open-source code, the article positions itself within the broader context of accessible AI education, allowing users to experiment with hyperparameters and observe evolution in real-time. It touches on the basics of genetic algorithms but explicitly states it is not a comprehensive guide, suggesting its primary value lies in practical, hands-on understanding rather than theoretical depth.

## Implications
The project highlights the potential of evolutionary strategies for solving control problems in constrained environments where traditional programming might be difficult to hand-code. For the field of autonomous driving research, this approach offers insights into how simple agents can learn complex behaviors through trial and error, potentially informing hybrid AI systems that combine evolutionary optimization with other machine learning techniques. Furthermore, by making the simulation accessible via TypeScript and a web interface, it lowers the barrier to entry for developers interested in AI robotics, fostering community engagement and experimentation with genetic algorithms outside of specialized research labs.
