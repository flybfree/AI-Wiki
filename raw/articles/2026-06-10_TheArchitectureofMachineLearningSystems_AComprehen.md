---

title: "The Architecture of Machine Learning Systems: A Comprehensive Guide — Part 1 | by Rijul Dahiya | Medium"
date: 2026-06-10
url: https://medium.com/@rijuldahiya/the-architecture-of-machine-learning-systems-a-comprehensive-guide-part-1-7d5d9c3ac380
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://medium.com/@rijuldahiya/the-architecture-of-machine-learning-systems-a-comprehensive-guide-part-1-7d5d9c3ac380
scraped: "2026-06-10 20:58"

---

## Summary

The Architecture of Machine Learning Systems: A Comprehensive Guide — Part 1 Rijul Dahiya 5 min read Dec 7, 2025 Listen Share Press enter or click to view image in full size Photo by Ryan Unsplash The rapid ascent of Artificial Intelligence…



# The Architecture of Machine Learning Systems: A Comprehensive Guide — Part 1 | by Rijul Dahiya | Medium

**Source**: [Original Article](https://medium.com/@rijuldahiya/the-architecture-of-machine-learning-systems-a-comprehensive-guide-part-1-7d5d9c3ac380)

## Full Article

The Architecture of Machine Learning Systems: A Comprehensive Guide — Part 1
[Rijul Dahiya]
Rijul Dahiya
5 min read
·
Dec 7, 2025
--
Listen
Share
Press enter or click to view image in full size
Photo by
Ryan
on
Unsplash
The rapid ascent of Artificial Intelligence is not merely a triumph of algorithms; it is a triumph of systems. While the headlines focus on the generative capabilities of models like GPT-4 or Gemini, the engine driving this revolution is a complex stack of high-performance hardware, sophisticated software frameworks, and massive datasets.
This article provides a deep dive into the three pillars of modern AI: the fundamental models, the software frameworks that orchestrate them, and the hardware accelerators that power them.
Part 1: The Revolution of Scale
The “Perfect Storm”
Deep Learning (DL) is not a new idea. The perceptron was invented in 1957, and the foundations of backpropagation were crystallized in 1986. So why did the revolution wait until 2012 to break out?
The answer lies in the convergence of three ingredients:
Model, Data, and Hardware
.
Compute:
The release of NVIDIA’s CUDA in 2007 enabled General Purpose GPU (GPGPU) computing, providing the
massive throughput
required for training.
Data:
The release of ImageNet in 2010 provided the massive labeled datasets required for generalization.
Scale:
Since AlexNet in 2012, training compute has grown at a rate of
4.4x per year
.
This growth has spurred massive capital expenditure, with estimates suggesting hyperscale companies will spend nearly $400 billion by 2026 on infrastructure.
Representation Learning and the XOR Problem
At its core, Deep Learning is about
representation learning
— mapping raw inputs (like pixels) into abstract features (like edges, contours, and objects).
To understand why “Deep” networks are necessary, we look at the XOR problem. A single-layer linear model cannot solve the XOR classification problem because the data is not linearly separable.
If we attempt to model this with two linear layers:
$$h = xW_1 + b_1$$
$$y = hW_2 + b_2$$
The composition of two linear functions is simply another linear function:
$$y = x(W_1 W_2) + (b_1 W_2 + b_2)$$
To solve this, we must introduce
non-linearity
, such as the ReLU (Rectified Linear Unit) activation function ($g(z) = max(0, z)$). This allows the neural network to act as a
universal function approximator
, transforming the input space into a representation where classes are separable.
Training the Model
Training involves minimizing a
Loss Function
using gradient-based optimization. Common functions include:
Mean Squared Error (MSE):
Used for regression, calculated as $\frac{1}{d}\sum(y_i — \hat{y}_i)²$.
Cross Entropy Loss:
Used for classification, measuring the divergence between predicted probability distributions and true labels.
Gradients are calculated via
Backpropagation
, which utilizes the chain rule to propagate error derivatives from the output back to the weights.
Part 2: Deep Learning Frameworks
Implementing backpropagation manually is error-prone and complex. DL frameworks like TensorFlow and PyTorch were created to abstract this complexity.
The Core Abstraction: Dataflow Graphs
Frameworks represent computation as a
dataflow graph
where nodes are primitive operators (Add, MatMul) and edges are tensors (multidimensional arrays).
There are two dominant paradigms for executing these graphs:
1. Define-Before-Run (Static Graphs)
Used by TensorFlow v1.
Mechanism:
The user defines the entire graph symbolically using placeholders (e.g.,
x = tf.placeholder()
) before running it within a session.
Pros:
The graph can be optimized before execution, memory can be pre-allocated, and the model is easily portable to mobile devices.
Cons:
Hard to debug and difficult to implement control flow (loops/conditionals) because Python logic is separated from graph execution.
2. Define-By-Run (Dynamic Graphs)
Used by PyTorch and TensorFlow Eager.
Mechanism:
The graph is built on-the-fly as the code executes. Tensors are wrapped in objects (like
Value
) that track their history.
Auto-Differentiation:
As operations occur (e.g.,
c = a * b
), the framework records the operation and its inputs. When
.backward()
is called, the system traverses this history in reverse to calculate gradients.
Pros:
Highly “Pythonic,” intuitive debugging, and straightforward control flow.
Cons:
Can be less efficient due to the overhead of launching many small kernels and intensive memory management (allocating/freeing tensors constantly).
The industry is seeing a convergence: PyTorch has added
TorchScript
for static optimization, while TensorFlow has adopted eager execution as the default.
Part 3: The Hardware — GPU Architecture
While
CPUs
optimize for
latency
(handling sequential execution and irregular control flow),
GPUs
optimize for
throughput
(parallel execution of massive numerical data).
Inside the GPU
A GPU is composed of many
Streaming Multiprocessors (SMs)
. For example, the NVIDIA A100 contains 108 SMs.
Cores:
Each SM has numerous FP32 and INT32 units, plus specialized
Tensor Cores
for matrix math.
Memory Hierarchy:
Registers:
Fastest, local to threads.
L1 Cache / Shared Memory:
Fast (192KB per SM on A100), manually managed by programmers for optimization.
L2 Cache:
Larger (40MB), shared across SMs.
Global Memory:
Massive (80GB HBM), but very slow.
Execution Model: SIMT and Warps
Programmers write
kernels
(functions) that are executed by thousands of threads. Threads are grouped into
Warps
(fixed size of 32 threads).
SIMT (Single Instruction, Multiple Threads):
All threads in a warp execute the same instruction simultaneously.
Latency Hiding:
If a warp stalls (e.g., waiting for memory), the SM’s warp scheduler instantly switches to another active warp. This “cheap context switch” is how GPUs hide memory latency.
Performance Optimization
To achieve peak performance, ML systems must address three key bottlenecks:
Branch Divergence: Since a warp executes one instruction at a time, if threads within a warp diverge (some take an if path, others take else), the hardware must serialize the execution, disabling threads that aren’t on the current path. This effectively kills performance.
Memory Access: Global memory is slow. Optimization often involves “tiling” — loading a block of data into the fast Shared Memory so multiple threads can reuse it without hitting global memory.
Example:
In a sliding sum operation, utilizing shared memory drastically reduces global memory accesses compared to a naive implementation.
Occupancy: Occupancy is the ratio of active warps to the maximum possible warps. Higher occupancy allows better latency hiding. It is often limited by the register or shared memory usage of a specific kernel. If a kernel uses too many registers, fewer warps can fit on the SM.
Asynchronous Execution and Streams
CUDA kernel launches are
asynchronous
; the CPU issues the command and moves on without waiting for the GPU to finish.
Benefits:
Allows
overlapping
of CPU computation (e.g., data loading) with GPU computation.
CUDA Streams:
A sequence of operations that execute in order. Using multiple streams allows independent kernels to run concurrently, saturating the GPU.
Conclusion
The “magic” of modern AI is built upon a deep stack of technology. It starts with the mathematical foundations of
representation learning
and non-linear function approximation. It is enabled by
DL frameworks
that abstract complex differentiation and computation graphs. Finally, it is powered by
hardware architectures
designed explicitly for massive parallelism and throughput. Understanding ML Systems requires mastering the interplay between these three layers — optimizing the algorithm, the software, and the metal.

## Metadata
- **Source URL**: https://medium.com/@rijuldahiya/the-architecture-of-machine-learning-systems-a-comprehensive-guide-part-1-7d5d9c3ac380
