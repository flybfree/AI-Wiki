---
title: Go 1.27 Interactive Tour
date: 2026-08-02
url: https://victoriametrics.com/blog/go-1-27/index.html
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://victoriametrics.com/blog/go-1-27/index.html
source_feed: Hacker News
ai_relevance: include
ai_topic: research
ai_reason: meets AI relevance threshold
scraped: 2026-08-02 00:05
---

# Go 1.27 Interactive Tour

## Full Article

Go 1.27 is coming soon, so it’s a good time to get a head start on what’s new. The [official release notes](https://go.dev/doc/go1.27) are pretty dry, so here’s a hands-on version with runnable examples showing what changed and how the new behavior works.

A quick credit first: the interactive Go tours were started by [Anton Zhiyanov](https://antonz.org/), who wrote one for every release from Go 1.22 through Go 1.26. He’s [decided to stop](https://antonz.org/on-go-tours/), so we’re picking up where he left off. His earlier tours are all still worth a read:

*   [Go 1.22 interactive tour](https://antonz.org/go-1-22/)
*   [Go 1.23 interactive tour](https://antonz.org/go-1-23/)
*   [Go 1.24 interactive tour](https://antonz.org/go-1-24/)
*   [Go 1.25 interactive tour](https://antonz.org/go-1-25/)
*   [Go 1.26 interactive tour](https://antonz.org/go-1-26/)

Thanks, Anton.

Before we start digging into the new features, let’s set the context.

This article is based on the official release notes and the Go source code, licensed under the BSD-3-Clause. This is not an exhaustive list; see the [official release notes](https://go.dev/doc/go1.27) for that.

Links point to the documentation (𝗗), proposals (𝗣), most relevant commits (𝗖𝗟), and authors (𝗔) for each feature; check them out for motivation, usage, and implementation details. The authors (𝗔) are the people who contributed to the feature (writing the implementation, the tests, or, for features that graduated from an earlier experiment, the original design), not necessarily a single main author.

Error handling is often skipped to keep the examples short. Don’t do this in production ツ

## [Generic methods](http://victoriametrics.com/blog/go-1-27/index.html#generic-methods)
This is the headline of the release. A [method declaration](https://go.dev/ref/spec#Method_declarations) may now declare its **own** type parameters, independent of the receiver’s. Before Go 1.27, only top-level functions could be generic, so a generic operation on a type had to live as a package-level function instead of a method.

Say we have a generic container and want a `Map` operation that can change the element type:

Line wrapping: OFF

```
type Box[T any] struct{ v T }

// The method declares its own type parameter U (new in Go 1.27).
func (b Box[T]) Map[U any](f func(T) U) Box[U] {
    return Box[U]{v: f(b.v)}
}
```

Now `Map` is a method of `Box` and can transform an `int` box into a `string` box:

Line wrapping: OFF

```
func main() {
    b := Box[int]{v: 21}
    doubled := b.Map(func(n int) int { return n * 2 })
    label := doubled.Map(func(n int) string {
        return fmt.Sprintf("value=%d", n)
    })
    fmt.Println(label.v)
}
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

There is one important restriction: interfaces still can’t declare type-parameterized methods, and a generic method can’t be used to satisfy an interface. Put a generic method in an interface and the compiler stops you:

Line wrapping: OFF

```
type Mapper interface {
    Map[U any](f func(int) U) any // interfaces can't declare generic methods
}
```

Line wrapping: OFF

```
interface method must have no type parameters
```

*   𝗗 [Generic methods](https://go.dev/ref/spec#Method_declarations)
*   𝗣 [77273](https://go.dev/issue/77273)
*   𝗖𝗟 [524b860](https://github.com/golang/go/commit/524b8606a8), [e84da04](https://github.com/golang/go/commit/e84da0405bcf64c7dbaafb0afc14388049a9b6fc), [e212a16](https://github.com/golang/go/commit/e212a16d1e)
*   𝗔 [Robert Griesemer](https://github.com/griesemer), [Mark Freeman](https://github.com/mrkfrmn)

## [Struct literal field selectors](http://victoriametrics.com/blog/go-1-27/index.html#struct-literal-field-selectors)
A key in a [struct literal](https://go.dev/ref/spec#Composite_literals) may now be any valid field selector for the struct type, not just a top-level field name. In practice this means you can set a **promoted** field (one that comes from an embedded struct) directly, without spelling out the embedded type.

Line wrapping: OFF

```
type Base struct {
    ID int
}

type User struct {
    Base
    Name string
}
```

Before Go 1.27 you had to write `User{Base: Base{ID: 7}, Name: "Mittens"}`. Now the promoted `ID` works as a key on its own:

Line wrapping: OFF

```
u := User{ID: 7, Name: "Mittens"}
fmt.Println(u.ID, u.Name)
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

*   𝗗 [Composite literals](https://go.dev/ref/spec#Composite_literals)
*   𝗣 [9859](https://go.dev/issue/9859)
*   𝗖𝗟 [1a8f9d8](https://github.com/golang/go/commit/1a8f9d8141), [9f7e98d](https://github.com/golang/go/commit/9f7e98d263f1e496991110f057763a2b4319e1c1), [30bfe53](https://github.com/golang/go/commit/30bfe53dd7), [e2c1885](https://github.com/golang/go/commit/e2c188568d)
*   𝗔 [Robert Griesemer](https://github.com/griesemer), [Cherry Mui](https://github.com/cherrymui)

## [Generalized function type inference](http://victoriametrics.com/blog/go-1-27/index.html#generalized-function-type-inference)
Function type inference has been generalized to apply in _all_ contexts where a generic function is used where a matching function type is expected: not just plain assignment to a variable (which already worked), but also conversions and composite literals. In those cases you previously had to spell out the type arguments by hand.

Take two generic helpers and drop them into a slice whose element type is `func([]int) int`:

Line wrapping: OFF

```
func first[T any](s []T) T { return s[0] }
func last[T any](s []T) T  { return s[len(s)-1] }
```

Line wrapping: OFF

```
// The slice's element type drives inference: T=int for each entry.
// Before Go 1.27 this failed with "cannot use generic function
// without instantiation"; you had to write first[int], last[int].
ops := []func([]int) int{first, last}
for _, op := range ops {
    fmt.Println(op([]int{10, 20, 30}))
}
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

*   𝗗 [Assignability](https://go.dev/ref/spec#Assignability)
*   𝗣 [77245](https://go.dev/issue/77245)
*   𝗖𝗟 [ef06728](https://github.com/golang/go/commit/ef067283ce), [f757de8](https://github.com/golang/go/commit/f757de83f4)
*   𝗔 [Robert Griesemer](https://github.com/griesemer), [Mark Freeman](https://github.com/mrkfrmn)

## [Faster memory allocation](http://victoriametrics.com/blog/go-1-27/index.html#faster-memory-allocation)
The compiler now generates calls to **size-specialized** memory allocation routines, cutting the cost of some small (under 80 bytes) allocations by up to 30%. Improvements vary with the workload, but the overall gain is expected to be around 1% in real allocation-heavy programs. The tradeoff is about 60 KB of extra binary size, independent of the workload.

There’s nothing to change in your code; it just gets a little faster. If you need to turn it off, build with `GOEXPERIMENT=nosizespecializedmalloc`. That opt-out is expected to be removed in Go 1.28.

*   𝗗 [Runtime release notes](https://go.dev/doc/go1.27#runtime)
*   𝗣 [79286](https://go.dev/issue/79286)
*   𝗖𝗟 [2a93576](https://github.com/golang/go/commit/2a93576965)
*   𝗔 [Michael Matloob](https://github.com/matloob)

## [Goroutine labels in tracebacks](http://victoriametrics.com/blog/go-1-27/index.html#goroutine-labels-in-tracebacks)
For modules whose `go.mod` sets Go 1.27 or later, tracebacks now include [runtime/pprof](https://pkg.go.dev/runtime/pprof@go1.27rc2) goroutine labels in the header line of each goroutine. If you already attach labels for profiling with [`pprof.Do`](https://pkg.go.dev/runtime/pprof@go1.27rc2#Do), that context now shows up in crash dumps, `SIGQUIT` traces, and [`runtime.Stack`](https://pkg.go.dev/runtime@go1.27rc2#Stack) output too (handy for telling apart otherwise identical goroutines).

Here we attach a label, then dump the current goroutine’s stack to see it in action:

Line wrapping: OFF

```
ctx := context.Background()
pprof.Do(ctx, pprof.Labels("request", "42"), func(ctx context.Context) {
    buf := make([]byte, 1<<12)
    n := runtime.Stack(buf, false)
    fmt.Printf("%s", buf[:n])
})
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

The pointer arguments, offsets, and file paths differ from run to run; what’s new is the `{request: 42}` appended right after the goroutine’s `[running]` state: its `pprof` labels. That same `{...}` annotation appears on the header of every labeled goroutine in a panic or `SIGQUIT` traceback. You can disable it with `GODEBUG=tracebacklabels=0` (the setting was added in Go 1.26). The opt-out is expected to stay indefinitely, in case labels carry sensitive data you don’t want in tracebacks.

*   𝗗 [runtime/pprof](https://pkg.go.dev/runtime/pprof@go1.27rc2)
*   𝗣 [76349](https://go.dev/issue/76349)
*   𝗖𝗟 [3694f33](https://github.com/golang/go/commit/3694f33692), [19c994c](https://github.com/golang/go/commit/19c994cc0c)
*   𝗔 [David Finkel](https://github.com/dfinkel)

## [Goroutine leak profile](http://victoriametrics.com/blog/go-1-27/index.html#goroutine-leak-profile)
Go 1.26 introduced a goroutine leak detector as an experiment. In Go 1.27 it graduates to a regular profile: [`runtime/pprof`](https://pkg.go.dev/runtime/pprof@go1.27rc2) exposes a `goroutineleak` profile that runs a GC cycle to find goroutines that are permanently blocked (leaked) and reports their stacks; no `GOEXPERIMENT` needed anymore.

A “leaked” goroutine is one blocked forever on a channel, mutex, or similar, with no way to ever make progress. The classic example is a goroutine that sends to a channel it alone holds, so nobody can ever receive from it:

Line wrapping: OFF

```
func leak() {
    ch := make(chan int) // only this goroutine ever sees ch
    ch <- 1              // blocks forever: nobody will ever receive
}
```

Start one, let it park, then dump the profile:

Line wrapping: OFF

```
go leak() // this goroutine can never finish

runtime.Gosched() // let it park on the send

// The GC-backed scan finds goroutines that can never make progress.
pprof.Lookup("goroutineleak").WriteTo(os.Stdout, 1)
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

The `total 1` line says the detector found exactly one leaked goroutine, and the stack pins it to `main.leak`: the `ch <- 1` send that will never complete (the addresses vary from run to run). In a real service you’d usually scrape the `/debug/pprof/goroutineleak`[net/http/pprof](https://pkg.go.dev/net/http/pprof@go1.27rc2) endpoint instead of writing to stdout.

*   𝗗 [runtime/pprof](https://pkg.go.dev/runtime/pprof@go1.27rc2)
*   𝗣 [74609](https://go.dev/issue/74609)
*   𝗖𝗟 [253aa2a](https://github.com/golang/go/commit/253aa2a12a), [1644917](https://github.com/golang/go/commit/16449179ec), [afcf04c](https://github.com/golang/go/commit/afcf04cb64)
*   𝗔 [Vlad Saioc](https://github.com/VladSaiocUber), [Austin Clements](https://github.com/aclements), [Cherry Mui](https://github.com/cherrymui)

## [Post-quantum signatures](http://victoriametrics.com/blog/go-1-27/index.html#post-quantum-signatures)
The new [crypto/mldsa](https://pkg.go.dev/crypto/mldsa@go1.27rc2) package implements ML-DSA, the post-quantum digital signature scheme specified in [FIPS 204](https://csrc.nist.gov/pubs/fips/204/final). It comes in three parameter sets ([`MLDSA44`](https://pkg.go.dev/crypto/mldsa@go1.27rc2#MLDSA44), [`MLDSA65`](https://pkg.go.dev/crypto/mldsa@go1.27rc2#MLDSA65), and [`MLDSA87`](https://pkg.go.dev/crypto/mldsa@go1.27rc2#MLDSA87)), trading key/signature size for security level.

Line wrapping: OFF

```
priv, _ := mldsa.GenerateKey(mldsa.MLDSA65())

msg := []byte("victoria metrics")
sig, _ := priv.Sign(rand.Reader, msg, crypto.Hash(0))

fmt.Println("scheme:  ", mldsa.MLDSA65())
fmt.Println("sig size:", mldsa.MLDSA65().SignatureSize())
fmt.Println("verified:", mldsa.Verify(priv.PublicKey(), msg, sig, nil) == nil)
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

ML-DSA support also reaches [crypto/x509](https://pkg.go.dev/crypto/x509@go1.27rc2) (private keys, public keys, and signatures) and [crypto/tls](https://pkg.go.dev/crypto/tls@go1.27rc2) (the new [`MLDSA44`](https://pkg.go.dev/crypto/tls@go1.27rc2#MLDSA44), [`MLDSA65`](https://pkg.go.dev/crypto/tls@go1.27rc2#MLDSA65), and [`MLDSA87`](https://pkg.go.dev/crypto/tls@go1.27rc2#MLDSA87) signature schemes in [TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446.html)).

*   𝗗 [crypto/mldsa](https://pkg.go.dev/crypto/mldsa@go1.27rc2)
*   𝗣 [77626](https://go.dev/issue/77626)
*   𝗖𝗟 [7bc111c](https://github.com/golang/go/commit/7bc111c6eb96bd7331f822d29c26b268212c841b)
*   𝗔 [Filippo Valsorda](https://github.com/FiloSottile), [Daniel McCarney](https://github.com/cpu)

## [The uuid package](http://victoriametrics.com/blog/go-1-27/index.html#the-uuid-package)
Go finally has a UUID package in the standard library. The new top-level [uuid](https://pkg.go.dev/uuid@go1.27rc2) package generates and parses UUIDs per [RFC 9562](https://www.rfc-editor.org/rfc/rfc9562.html), using a [cryptographically secure random source](https://pkg.go.dev/crypto/rand@go1.27rc2). Random-component UUIDs are comparable, so you can use `==` on them directly.

Line wrapping: OFF

```
a := uuid.MustParse("f81d4fae-7dec-11d0-a765-00a0c91e6bf6")
fmt.Println("parsed:", a)
fmt.Println("nil:   ", uuid.Nil())
fmt.Println("max:   ", uuid.Max())
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

For generation, [`uuid.New()`](https://pkg.go.dev/uuid@go1.27rc2#New) picks an algorithm suitable for most uses, while [`uuid.NewV4()`](https://pkg.go.dev/uuid@go1.27rc2#NewV4) gives a purely random UUID and [`uuid.NewV7()`](https://pkg.go.dev/uuid@go1.27rc2#NewV7) gives a time-ordered one; the latter is great for database keys because it sorts by creation time. Each call produces a fresh value, so try running this a few times:

Line wrapping: OFF

```
fmt.Println(uuid.NewV4()) // random
fmt.Println(uuid.NewV7()) // time-ordered
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

*   𝗗 [uuid](https://pkg.go.dev/uuid@go1.27rc2)
*   𝗣 [62026](https://go.dev/issue/62026)
*   𝗖𝗟 [2fb2b98](https://github.com/golang/go/commit/2fb2b98da3d7d529e11a94b79372c0309aa05e21)
*   𝗔 [Damien Neil](https://github.com/neild)

## [JSON v2 by default](http://victoriametrics.com/blog/go-1-27/index.html#json-v2-by-default)
The long-awaited `encoding/json/v2` rewrite has been experimental since Go 1.25. In Go 1.27 the experiment graduates: [encoding/json/v2](https://pkg.go.dev/encoding/json/v2@go1.27rc2) and its low-level companion [encoding/json/jsontext](https://pkg.go.dev/encoding/json/jsontext@go1.27rc2) are now available **without** the `GOEXPERIMENT=jsonv2` build flag. The quieter but bigger change: the classic [`encoding/json`](https://pkg.go.dev/encoding/json@go1.27rc2) (v1) package is now backed by the v2 implementation under the hood.

The switch is transparent: behavior is preserved (only some error-message text differs), with new [options](https://pkg.go.dev/encoding/json/v2@go1.27rc2#Options) pinning v2 to v1 semantics where they’d otherwise diverge. No migration is required, and `GOEXPERIMENT=nojsonv2` restores the original v1 implementation if you hit a compatibility issue.

For the common case, the v2 API mirrors v1 (the import here is `json "encoding/json/v2"`):

Line wrapping: OFF

```
type Point struct {
    X int `json:"x"`
    Y int `json:"y"`
}

data, err := json.Marshal(Point{X: 1, Y: 2})
fmt.Println(string(data), err)
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

One behavior worth knowing: unlike v1, which **always** sorts map keys, v2 does **not** sort them by default; skipping the sort is faster. When you need stable map output (for golden tests, say), pass the [`json.Deterministic`](https://pkg.go.dev/encoding/json/v2@go1.27rc2#Deterministic) option.

*   𝗗 [encoding/json/v2](https://pkg.go.dev/encoding/json/v2@go1.27rc2)
*   𝗣 [71497](https://go.dev/issue/71497)
*   𝗖𝗟 [e62d3e6](https://github.com/golang/go/commit/e62d3e6e89)
*   𝗔 [Joe Tsai](https://github.com/dsnet), [Damien Neil](https://github.com/neild)

## [Portable SIMD](http://victoriametrics.com/blog/go-1-27/index.html#portable-simd)
Go 1.27 adds an experimental [simd](https://pkg.go.dev/simd@go1.27rc2) package: **portable, vector-size-agnostic** SIMD that compiles down to real hardware vector instructions where they’re available and falls back to a pure-Go emulation where they aren’t. It’s off by default; you build with `GOEXPERIMENT=simd` to enable it.

The types are named after their element type with an `s` suffix ([`Int32s`](https://pkg.go.dev/simd@go1.27rc2#Int32s), [`Float32s`](https://pkg.go.dev/simd@go1.27rc2#Float32s), [`Float64s`](https://pkg.go.dev/simd@go1.27rc2#Float64s), and so on), and their width is deliberately _not_ fixed: a `Float32s` might hold 4 lanes on one machine and 16 on another. You load a vector from a slice, operate on it, and store it back, letting the hardware pick the width:

Line wrapping: OFF

```
a := []float32{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
b := []float32{10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160}

va := simd.LoadFloat32s(a) // reads exactly va.Len() lanes from a
vb := simd.LoadFloat32s(b)

sum := va.Add(vb) // element-wise add, many lanes in one instruction

out := make([]float32, sum.Len())
sum.Store(out)

fmt.Println(out[:4])
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

*   𝗗 [simd](https://pkg.go.dev/simd@go1.27rc2)
*   𝗣 [78902](https://go.dev/issue/78902)
*   𝗖𝗟 [44a4be9](https://github.com/golang/go/commit/44a4be991f), [8d29cf2](https://github.com/golang/go/commit/8d29cf23b1), [48bf922](https://github.com/golang/go/commit/48bf92284c)
*   𝗔 [David Chase](https://github.com/dr2chase), [Junyang Shao](https://github.com/JunyangShao), [Cherry Mui](https://github.com/cherrymui)

## [Cut around the last separator](http://victoriametrics.com/blog/go-1-27/index.html#cut-around-the-last-separator)
[`strings.Cut`](https://pkg.go.dev/strings@go1.27rc2#Cut) (from Go 1.18) splits around the _first_ occurrence of a separator. Go 1.27 adds [`strings.CutLast`](https://pkg.go.dev/strings@go1.27rc2#CutLast) (and [`bytes.CutLast`](https://pkg.go.dev/bytes@go1.27rc2#CutLast)) for the _last_ occurrence (a cleaner replacement for many [`LastIndex`](https://pkg.go.dev/strings@go1.27rc2#LastIndex) dances).

Line wrapping: OFF

```
before, after, found := strings.CutLast("a/b/c", "/")
fmt.Printf("%q %q %v\n", before, after, found)

before, after, found = strings.CutLast("nosep", "/")
fmt.Printf("%q %q %v\n", before, after, found)
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

As with `Cut`, when the separator isn’t found you get the whole input as `before`, an empty `after`, and `found == false`.

*   𝗗 [strings.CutLast](https://pkg.go.dev/strings@go1.27rc2#CutLast), [bytes.CutLast](https://pkg.go.dev/bytes@go1.27rc2#CutLast)
*   𝗣 [71151](https://go.dev/issue/71151)
*   𝗖𝗟 [11b596c](https://github.com/golang/go/commit/11b596c22dcabf91f9595da778b00e26f4d661a8)
*   𝗔 [qiulaidongfeng](https://github.com/qiulaidongfeng)

## [Generic hashing](http://victoriametrics.com/blog/go-1-27/index.html#generic-hashing)
The [`hash/maphash`](https://pkg.go.dev/hash/maphash@go1.27rc2) package gains a [`Hasher[T]`](https://pkg.go.dev/hash/maphash@go1.27rc2#Hasher) interface: a contract that future hash-based data structures (hash tables, Bloom filters, and so on) can use to hash and compare values of a type. It bundles two operations: `Hash`, which mixes a value into a running hash, and `Equal`, which compares two values. The rule tying them together is that equal values must hash the same.

There’s a ready-made [`ComparableHasher[T]`](https://pkg.go.dev/hash/maphash@go1.27rc2#ComparableHasher) (hash by value, equality by `==`) for any comparable type, but the interesting part is defining your own. Here’s a case-insensitive string hasher:

Line wrapping: OFF

```
type ciHasher struct{}

// Equal ignores case; Hash mixes in the lower-cased form, so values
// that are Equal always hash the same.
func (ciHasher) Hash(h *maphash.Hash, s string) { h.WriteString(strings.ToLower(s)) }
func (ciHasher) Equal(x, y string) bool         { return strings.EqualFold(x, y) }
```

Now `"Go"` and `"GO"` count as equal and hash identically, which plain `==` and value hashing can’t do:

Line wrapping: OFF

```
var h maphash.Hasher[string] = ciHasher{} // plug in the custom strategy

fmt.Println(h.Equal("Go", "GO"), h.Equal("Go", "Rust"))

// Equal values must hash the same, so feed each into a Hash sharing one seed:
seed := maphash.MakeSeed()
var a, b maphash.Hash
a.SetSeed(seed)
b.SetSeed(seed)
h.Hash(&a, "Go")
h.Hash(&b, "GO")
fmt.Println(a.Sum64() == b.Sum64())
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

*   𝗗 [hash/maphash](https://pkg.go.dev/hash/maphash@go1.27rc2)
*   𝗣 [70471](https://go.dev/issue/70471)
*   𝗖𝗟 [330aec8](https://github.com/golang/go/commit/330aec810997f89262fa04939a00425194e94216)
*   𝗔 [Alan Donovan](https://github.com/adonovan)

## [Integer division with rounding](http://victoriametrics.com/blog/go-1-27/index.html#integer-division-with-rounding)
[`math/big`](https://pkg.go.dev/math/big@go1.27rc2) adds [`Int.Divide`](https://pkg.go.dev/math/big@go1.27rc2#Int.Divide), which computes a quotient and remainder together with an explicit [rounding mode](https://pkg.go.dev/math/big@go1.27rc2#RoundingMode): [`Trunc`](https://pkg.go.dev/math/big@go1.27rc2#Trunc), [`Floor`](https://pkg.go.dev/math/big@go1.27rc2#Floor), [`Round`](https://pkg.go.dev/math/big@go1.27rc2#Round), or [`Ceil`](https://pkg.go.dev/math/big@go1.27rc2#Ceil). The classic [`Quo`](https://pkg.go.dev/math/big@go1.27rc2#Int.Quo)/[`Mod`](https://pkg.go.dev/math/big@go1.27rc2#Int.Mod) always truncates toward zero, so this fills a real gap for financial and numeric code.

Line wrapping: OFF

```
x, y := big.NewInt(7), big.NewInt(2)
q, r := new(big.Int), new(big.Int)

q.Divide(x, y, r, big.Ceil)
fmt.Printf("ceil:  q=%s r=%s\n", q, r)

q.Divide(x, y, r, big.Floor)
fmt.Printf("floor: q=%s r=%s\n", q, r)
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

Notice how the remainder follows the rounding mode: with `Ceil` the quotient rounds up to 4, leaving a remainder of −1; with `Floor` it rounds down to 3, leaving 1.

*   𝗗 [math/big.Int.Divide](https://pkg.go.dev/math/big@go1.27rc2#Int.Divide)
*   𝗣 [76821](https://go.dev/issue/76821)
*   𝗖𝗟 [8f7f951](https://github.com/golang/go/commit/8f7f951965120878db5158f543b88b8c0cd2323d)
*   𝗔 [Armin Günther](https://github.com/arminguenther)

## [Random numbers, your type](http://victoriametrics.com/blog/go-1-27/index.html#random-numbers-your-type)
[`math/rand/v2`](https://pkg.go.dev/math/rand/v2@go1.27rc2) has had a top-level generic [`N`](https://pkg.go.dev/math/rand/v2@go1.27rc2#N) function since Go 1.22. Go 1.27 adds it as a method, [`(*Rand).N`](https://pkg.go.dev/math/rand/v2@go1.27rc2#Rand.N), so you can draw a bounded random number of any integer or duration type from your own `*Rand` source.

Line wrapping: OFF

```
r := rand.New(rand.NewPCG(1, 2)) // fixed seed → reproducible
fmt.Println(r.N(100))            // int in [0, 100)
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

*   𝗗 [rand.Rand.N](https://pkg.go.dev/math/rand/v2@go1.27rc2#Rand.N)
*   𝗣 [77853](https://go.dev/issue/77853)
*   𝗖𝗟 [e0a8616](https://github.com/golang/go/commit/e0a8616941e4eccde231f33cbcf3710896ba5a9b)
*   𝗔 [qiulaidongfeng](https://github.com/qiulaidongfeng)

## [Sleep in synthetic time](http://victoriametrics.com/blog/go-1-27/index.html#sleep-in-synthetic-time)
[`testing/synctest`](https://pkg.go.dev/testing/synctest@go1.27rc2) (stable since Go 1.25) lets you test concurrent code against a fake clock. Go 1.27 adds a [`Sleep`](https://pkg.go.dev/testing/synctest@go1.27rc2#Sleep) helper that combines [`time.Sleep`](https://pkg.go.dev/time@go1.27rc2#Sleep) with [`synctest.Wait`](https://pkg.go.dev/testing/synctest@go1.27rc2#Wait): advance the bubble’s synthetic clock and then wait for all goroutines to settle, in one call.

Inside a bubble the [`time`](https://pkg.go.dev/time@go1.27rc2) package uses a fake clock, so a two-second sleep returns instantly; `synctest.Sleep` also waits for the background goroutine to finish before moving on:

Line wrapping: OFF

```
t := &testing.T{} // in real code, use the *testing.T your test receives
synctest.Test(t, func(t *testing.T) {
    start := time.Now()
    go func() {
        time.Sleep(time.Second)
        fmt.Println("worker woke at", time.Since(start))
    }()

    // Advance fake time by 2s AND wait for goroutines to settle, in one call.
    synctest.Sleep(2 * time.Second)
    fmt.Println("main advanced", time.Since(start))
})
```

[Edit](http://victoriametrics.com/blog/go-1-27/index.html#edit)

Both du

## Metadata
- **Source**: [Original Article](https://victoriametrics.com/blog/go-1-27/index.html)
