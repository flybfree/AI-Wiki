---
title: A Mathematical Framework for Transformer Circuits (2021)
date: 2026-09-12
url: https://transformer-circuits.pub/2021/framework/index.html
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://transformer-circuits.pub/2021/framework/index.html
source_feed: Hacker News
ai_relevance: include
ai_topic: benchmark-eval
ai_reason: meets AI relevance threshold
scraped: 2026-09-12 10:17
---

# A Mathematical Framework for Transformer Circuits (2021)

## Full Article

### Contents

*   [Model Simplifications](http://transformer-circuits.pub/2021/framework/index.html#model-simplifications)
*   [High-Level Architecture](http://transformer-circuits.pub/2021/framework/index.html#high-level-architecture)
*   [Virtual Weights and the Residual Stream as a Communication Channel](http://transformer-circuits.pub/2021/framework/index.html#residual-comms)
*   [Attention Heads are Independent and Additive](http://transformer-circuits.pub/2021/framework/index.html#architecture-attn-independent)
*   [Attention Heads as Information Movement](http://transformer-circuits.pub/2021/framework/index.html#architecture-attn-as-movement)

*   [The Path Expansion Trick](http://transformer-circuits.pub/2021/framework/index.html#onel-path-expansion)
*   [Splitting Attention Head terms into Query-Key and Output-Value Circuits](http://transformer-circuits.pub/2021/framework/index.html#splitting-attention-head-terms-into-circuits)
*   [Interpretation as Skip-Trigrams](http://transformer-circuits.pub/2021/framework/index.html#interpretation-as-skip-trigrams)
*   [Summarizing OV/QK Matrices](http://transformer-circuits.pub/2021/framework/index.html#summarizing-ovqk-matrices)
*   [Do We "Fully Understand" One-Layer Models?](http://transformer-circuits.pub/2021/framework/index.html#do-we-fully-understand-one-layer-models)

*   [Three Kinds of Composition](http://transformer-circuits.pub/2021/framework/index.html#three-kinds-of-composition)
*   [Path Expansion of Logits](http://transformer-circuits.pub/2021/framework/index.html#path-expansion-of-logits)
*   [Path Expansion of Attention Scores QK Circuit](http://transformer-circuits.pub/2021/framework/index.html#path-expansion-of-attention-scores-qk-circuit)
*   [Analyzing a Two-Layer Model](http://transformer-circuits.pub/2021/framework/index.html#analyzing-a-two-layer-model)
*   [Induction Heads](http://transformer-circuits.pub/2021/framework/index.html#induction-heads)
*   [Term Importance Analysis](http://transformer-circuits.pub/2021/framework/index.html#term-importance-analysis)
*   [Virtual Attention Heads](http://transformer-circuits.pub/2021/framework/index.html#virtual-attention-heads)

Transformer language models are an emerging technology that is gaining increasingly broad real-world use, for example in systems like GPT-3 , LaMDA , Codex , Meena , Gopher , and similar models. However, as these models scale, their open-endedness and high capacity creates an increasing scope for unexpected and sometimes harmful behaviors. Even years after a large model is trained, both creators and users routinely discover model capabilities – including problematic behaviors – they were previously unaware of.

One avenue for addressing these issues is mechanistic interpretability, attempting to reverse engineer the detailed computations performed by transformers, similar to how a programmer might try to reverse engineer complicated binaries into human-readable source code. If this were possible, it could potentially provide a more systematic approach to explaining current safety problems, identifying new ones, and perhaps even anticipating the safety problems of powerful future models that have not yet been built. A previous project, the [Distill Circuits thread](https://distill.pub/2020/circuits/), has attempted to reverse engineer vision models, but so far there hasn’t been a comparable project for transformers or language models.

In this paper, we attempt to take initial, very preliminary steps towards reverse-engineering transformers. Given the incredible complexity and size of modern language models, we have found it most fruitful to start with the simplest possible models and work our way up from there. Our aim is to discover simple algorithmic patterns, motifs, or frameworks that can subsequently be applied to larger and more complex models. Specifically, in this paper we will study transformers with two layers or less which have only attention blocks – this is in contrast to a large, modern transformer like GPT-3, which has 96 layers and alternates attention blocks with MLP blocks.

We find that by conceptualizing the operation of transformers in a new but mathematically equivalent way, we are able to make sense of these small models and gain significant understanding of how they operate internally. Of particular note, we find that specific attention heads that we term “induction heads” can explain in-context learning in these small models, and that these heads only develop in models with at least two attention layers. We also go through some examples of these heads operating in action on specific data.

We don’t attempt to apply to our insights to larger models in this first paper, but in a [forthcoming paper](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html), we will show that both our mathematical framework for understanding transformers, and the concept of induction heads, continues to be at least partially relevant for much larger and more realistic models – though we remain a very long way from being able to fully reverse engineer such models.

* * *

## Summary of Results

#### Reverse Engineering Results

To explore the challenge of reverse engineering transformers, we reverse engineer several toy, attention-only models. In doing so we find:

*   Zero layer transformers model bigram statistics.The bigram table can be accessed directly from the weights.
*   One layer attention-only transformers are an ensemble of bigram and “skip-trigram” (sequences of the form "A… B C") models.The bigram and skip-trigram tables can be accessed directly from the weights, without running the model. These skip-trigrams can be surprisingly expressive. This includes implementing a kind of very simple in-context learning.
*   Two layer attention-only transformers can implement much more complex algorithms using compositions of attention heads. These compositional algorithms can also be detected directly from the weights. Notably, two layer models use attention head composition to create “induction heads”, a very general in-context learning algorithm.We’ll explore induction heads in much more detail in a forthcoming paper.
*   One layer and two layer attention-only transformers use very different algorithms to perform in-context learning.Two layer attention heads use qualitatively more sophisticated inference-time algorithms — in particular, a special type of attention head we call an induction head — to perform in-context-learning, forming an important transition point that will be relevant for larger models.

#### Conceptual Take-Aways

We’ve found that many subtle details of the transformer architecture require us to approach reverse engineering it in a pretty different way from how the InceptionV1 Circuits work . We’ll unpack each of these points in the sections below, but for now we briefly summarize. We’ll also expand on a lot of the terminology we introduce here once we get to the appropriate sections. (To be clear, we don't intend to claim that any of these points are necessarily novel; many are implicitly or explicitly present in other papers.)

*   Attention heads can be understood as independent operations, each outputting a result which is added into the residual stream.Attention heads are often described in an alternate “concatenate and multiply” formulation for computational efficiency, but this is mathematically equivalent.
*   Attention-only models can be written as a sum of interpretable end-to-end functions mapping tokens to changes in logits.These functions correspond to “paths” through the model, and are linear if one freezes the attention patterns.
*   Transformers have an enormous amount of linear structure.One can learn a lot simply by breaking apart sums and multiplying together chains of matrices.
*   Attention heads can be understood as having two largely independent computations: a QK (“query-key”) circuit which computes the attention pattern, and an OV (“output-value”) circuit which computes how each token affects the output if attended to.
*   Key, query, and value vectors can be thought of as intermediate results in the computation of the low-rank matrices W_Q^TW_K and W_OW_V. It can be useful to describe transformers without reference to them.
*   Composition of attention heads greatly increases the expressivity of transformers. There are three different ways attention heads can compose, corresponding to keys, queries, and values. Key and query composition are very different from value composition.
*   All components of a transformer (the token embedding, attention heads, MLP layers, and unembedding) communicate with each other by reading and writing to different subspaces of the residual stream. Rather than analyze the residual stream vectors, it can be helpful to decompose the residual stream into all these different communication channels, corresponding to paths through the model.

* * *

## Transformer Overview

Before we attempt to reverse engineer transformers, it's helpful to briefly review the high-level structure of transformers and describe how we think about them.

In many cases, we've found it helpful to reframe transformers in equivalent, but non-standard ways. Mechanistic interpretability requires us to break models down into human-interpretable pieces. An important first step is finding the representation which makes it easiest to reason about the model. In modern deep learning, there is —for good reason! —a lot of emphasis on computational efficiency, and our mathematical descriptions of models often mirror decisions in how one would write efficient code to run the model. But when there are many equivalent ways to represent the same computation, it is likely that the most human-interpretable representation and the most computationally efficient representation will be different.

Reviewing transformers will also let us align on terminology, which can sometimes vary. We'll also introduce some notation in the process, but since this notation is used across many sections, we provide a detailed description of all notation in the [notation appendix](http://transformer-circuits.pub/2021/framework/index.html#notation) as a concise reference for readers.

### Model Simplifications

To demonstrate the ideas in this paper in their cleanest form, we focus on "toy transformers" with some simplifications.

In most parts of this paper, we will make a very substantive change: we focus on “attention-only” transformers, which don't have MLP layers. This is a very dramatic simplification of the transformer architecture. We're partly motivated by the fact that circuits with attention heads present new challenges not faced by the Distill circuits work, and considering them in isolation allows us to give an especially elegant treatment of those issues. But we've also simply had much less success in understanding MLP layers so far; in normal transformers with both attention and MLP layers there are many circuits mediated primarily by attention heads which we can study, some of which seem very important, but the MLP portions have been much harder to get traction on. This is a major weakness of our work that we plan to focus on addressing in the future. Despite this, we will have some discussion of transformers with MLP layers in later sections.

We also make several changes that we consider to be more superficial and are mostly made for clarity and simplicity. We do not consider biases, but a model with biases can always be simulated without them by folding them into the weights and creating a dimension that is always one. Additionally, biases in attention-only transformers mostly multiply out to functionally be biases on the logits. We also ignore layer normalization. It adds a fair amount of complexity to consider explicitly, and up to a variable scaling, layer norm can be merged into adjacent weights. We also expect that, modulo some implementational annoyances, layer norm could be substituted for batch normalization (which can fully be folded into adjacent parameters).

### High-Level Architecture

There are several variants of transformer language models. We focus on autoregressive, decoder-only transformer language models, such as GPT-3. (The original transformer paper had a special encoder-decoder structure to support translation, but many modern language models don't include this.)

A transformer starts with a token embedding, followed by a series of “residual blocks”, and finally a token unembedding. Each residual block consists of an attention layer, followed by an MLP layer. Both the attention and MLP layers each “read” their input from the residual stream (by performing a linear projection), and then “write” their result to the residual stream by adding a linear projection back in.Each attention layer consists of multiple heads, which operate in parallel.

![Image 1](blob:http://localhost/2abf4fa8197fdfc85bc2fe79f4c5d804)
### Virtual Weights and the Residual Stream as a Communication Channel

One of the main features of the high level architecture of a transformer is that each layer adds its results into what we call the “residual stream.”Constructing models with a residual stream traces back to early work by the Schmidhuber group, such as highway networks and LSTMs, which have found significant modern success in the more recent residual network architecture . In transformers, the residual stream vectors are often called the “embedding.” We prefer the residual stream terminology, both because it emphasizes the residual nature (which we believe to be important) and also because we believe the residual stream often dedicates subspaces to tokens other than the present token, breaking the intuitions the embedding terminology suggests. The residual stream is simply the sum of the output of all the previous layers and the original embedding. We generally think of the residual stream as a communication channel, since it doesn't do any processing itself and all layers communicate through it.

![Image 2](blob:http://localhost/35ced6528a8bb717dda8c6dc3d37b7cc)
The residual stream has a deeply linear structure.It's worth noting that the completely linear residual stream is very unusual among neural network architectures: even ResNets , the most similar architecture in widespread use, have non-linear activation functions on their residual stream, or applied whenever the residual stream is accessed! Every layer performs an arbitrary linear transformation to "read in" information from the residual stream at the start,This ignores the layer normalization at the start of each layer, but up to a constant scalar, the layer normalization is a constant affine transformation and can be folded into the linear transformation. See discussion of how we handle layer normalization in the appendix. and performs another arbitrary linear transformation before adding to "write" its output back into the residual stream. This linear, additive structure of the residual stream has a lot of important implications. One basic consequence is that the residual stream doesn't have a ["privileged basis"](http://transformer-circuits.pub/2021/framework/index.html#def-privileged-basis); we could rotate it by rotating all the matrices interacting with it, without changing model behavior.

#### Virtual Weights

An especially useful consequence of the residual stream being linear is that one can think of implicit "virtual weights" directly connecting any pair of layers (even those separated by many other layers), by multiplying out their interactions through the residual stream. These virtual weights are the product of the output weights of one layer with the input weights Note that for attention layers, there are three different kinds of input weights: W_Q, W_K, and W_V. For simplicity and generality, we think of layers as just having input and output weights here. of another (ie. W_{I}^2W_{O}^1), and describe the extent to which a later layer reads in the information written by a previous layer.

![Image 3](blob:http://localhost/89da513eccc33f700156bd74ae1538e3)
#### Subspaces and Residual Stream Bandwidth

The residual stream is a high-dimensional vector space. In small models, it may be hundreds of dimensions; in large models it can go into the tens of thousands. This means that layers can send different information to different layers by storing it in different subspaces. This is especially important in the case of attention heads, since every individual head operates on comparatively small subspaces (often 64 or 128 dimensions), and can very easily write to completely disjoint subspaces and not interact.

Once added, information persists in a subspace unless another layer actively deletes it. From this perspective, dimensions of the residual stream become something like "memory" or "bandwidth". The original token embeddings, as well as the unembeddings, mostly interact with a relatively small fraction of the dimensions.We performed PCA analysis of token embeddings and unembeddings. For models with large d_\text{model}, the spectrum quickly decayed, with the embeddings/unembeddings being concentrated in a relatively small fraction of the overall dimensions. To get a sense for whether they occupied the same or different subspaces, we concatenated the normalized embedding and unembedding matrices and applied PCA. This joint PCA process showed a combination of both "mixed" dimensions and dimensions used only by one; the existence of dimensions which are used by only one might be seen as a kind of upper bound on the extent to which they use the same subspace. This leaves most dimensions "free" for other layers to store information in.

It seems like we should expect residual stream bandwidth to be in very high demand! There are generally far more "computational dimensions" (such as neurons and attention head result dimensions) than the residual stream has dimensions to move information. Just a single MLP layer typically has four times more neurons than the residual stream has dimensions. So, for example, at layer 25 of a 50 layer transformer, the residual stream has 100 times more neurons as it has dimensions before it, trying to communicate with 100 times as many neurons as it has dimensions after it, somehow communicating in superposition! We call tensors like this ["bottleneck activations"](http://transformer-circuits.pub/2021/framework/index.html#def-bottleneck-activation) and expect them to be unusually challenging to interpret. (This is a major reason why we will try to pull apart the different streams of communication happening through the residual stream apart in terms of virtual weights, rather than studying it directly.)

Perhaps because of this high demand on residual stream bandwidth, we've seen hints that some MLP neurons and attention heads may perform a kind of "memory management" role, clearing residual stream dimensions set by other layers by reading in information and writing out the negative version.Some MLP neurons have very negative cosine similarity between their input and output weights, which may indicate deleting information from the residual stream. Similarly, some attention heads have large negative eigenvalues in their W_OW_V matrix and primarily attend to the present token, potentially serving as a mechanism to delete information. It's worth noticing that while these may be generic mechanisms for "memory management" deletion of information, they may also be mechanisms for conditionally deleting information, operating only in some cases.

![Image 4](blob:http://localhost/e5935e7a5477858c6ef3b01891f10d22)
### Attention Heads are Independent and Additive

As seen above, we think of transformer attention layers as several completely independent attention heads h\in H which operate completely in parallel and each add their output back into the residual stream. But this isn't how transformer layers are typically presented, and it may not be obvious they're equivalent.

In the original Vaswani et al.paper on transformers , the output of an attention layer is described by stacking the result vectors r^{h_1}, r^{h_2},..., and then multiplying by an output matrix W_O^H. Let's split W_O^H into equal size blocks for each head [W_O^{h_1}, W_O^{h_2}...]. Then we observe that:

W_O^H \left[\begin{matrix}r^{h_1}\\r^{h_2}\\... \end{matrix}\right] ~~=~~ \left[W_O^{h_1},~ W_O^{h_2},~ ... \right]\cdot\left[\begin{matrix}r^{h_1}\\r^{h_2}\\...\end{matrix}\right] ~~=~~ \sum_i W_O^{h_i} r^{h_i}

Revealing it to be equivalent to running heads independently, multiplying each by its own output matrix, and adding them into the residual stream. The concatenate definition is often preferred because it produces a larger and more compute efficient matrix multiply. But for understanding transformers theoretically, we prefer to think of them as independently additive.

### Attention Heads as Information Movement

But if attention heads act independently, what do they do? The fundamental action of attention heads is moving information.They read information from the residual stream of one token, and write it to the residual stream of another token. The main observation to take away from this section is that which tokens to move information from is completely separable from what information is “read” to be moved and how it is “written” to the destination.

![Image 5](blob:http://localhost/cc2ad55cdf9b6a869322adbd53923d7c)
To see this, it’s helpful to write attention in a non-standard way. Given an attention pattern, computing the output of an attention head is typically described in three steps:

1.   Compute the value vector for each token from the residual stream (v_i = W_V x_i).
2.   Compute the “result vector” by linearly combining value vectors according to the attention pattern (r_i = \sum_j A_{i,j} v_j).
3.   Finally, compute the output vector of the head for each token (h(x)_i = W_O r_i).As discussed above, often multiplication by the output matrix is written as one matrix multiply applied to the concatenated results of all heads; however this version is equivalent.

Each of these steps can be written as matrix multiply: why don’t we collapse them into a single step? If you think of x as a 2d matrix (consisting of a vector for each token), we’re multiplying it on different sides. W_V and W_O multiply the “vector per token” side, while A multiplies the “position” side. Tensors can offer us a much more natural language for describing this kind of map between matrices (if tensor product notation isn't familiar, we've included a [short introduction](http://transformer-circuits.pub/2021/framework/index.html#notation-tensor-product) in the notation appendix). One piece of motivation that may be helpful is to note that we want to express linear maps from matrices to matrices: [n_\text{context},~ d_\text{model}] ~\to~ [n_\text{context},~ d_\text{model}]. Mathematicians call such linear maps "(2,2)-tensors" (they map two input dimensions to two output dimensions). And so tensors are the natural language for expressing this transformation.

Using tensor products, we can describe the process of applying attention as:

h(x)~=~(\text{Id} \otimes W_O)~~\cdot~~

Project result vectors out for each token

(h(x)_i = W_O r_i)

~(A \otimes \text{Id})~~\cdot~~~

Mix value vectors _across_ tokens to compute result vectors

(r_i = \sum_j A_{i,j} v_j)

~(\text{Id} \otimes W_V)~~\cdot~~~

Compute value vector for each token

(v_i=W_V x_i)~~

x

Applying the mixed product property and collapsing identities yields:

h(x) ~=~(A ~~\otimes~~ W_O W_V) ~~~\cdot~~~~~~

A
mixes across tokens while

W_OW_V
acts on each vector independently.

x

What about the attention pattern? Typically, one computes the keys k_i = W_K x_i, computes the queries q_i = W_Q x_i and then computes the attention pattern from the dot products of each key and query vector A = \text{softmax}(q^T k). But we can do it all in one step without referring to keys and queries: A = \text{softmax}(x^T W_Q^T W_K x).

It's worth noting that although this formulation is mathematically equivalent, actually implementing attention this way (ie. multiplying by W_O W_V and W_Q^T W_K) would be horribly inefficient!

#### Observations about Attention Heads

A major benefit of rewriting attention heads in this form is that it surfaces a lot of structure which may have previously been harder to observe:

*   Attention heads move information from the residual stream of one token to another.

*   A corollary of this is that the residual stream vector space — which is often interpreted as a “contextual word embedding” — will generally have linear subspaces corresponding to information copied from other tokens and not directly about the present token.

*   An attention head is really applying two linear operations, A and W_OW_V, which operate on different dimensions and act independently.

*   A governs which token's information is m

## Metadata
- **Source**: [Original Article](https://transformer-circuits.pub/2021/framework/index.html)
