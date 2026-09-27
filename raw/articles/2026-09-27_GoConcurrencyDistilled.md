---
title: Go Concurrency Distilled
date: 2026-09-27
url: https://antonz.org/go-concurrency-distilled/
type: article-full-text
tags: [news, ai-research, full-text]
source_url: https://antonz.org/go-concurrency-distilled/
source_feed: Hacker News
ai_relevance: include
ai_topic: research
ai_reason: meets AI relevance threshold
scraped: 2026-09-27 00:13
---

# Go Concurrency Distilled

## Full Article

This mini-book provides a brief overview of many concurrency topics in Go. Each topic comes with interactive examples — feel free to experiment with them by changing the code and clicking
Run
. There's also a
PDF version
with static examples.
This is a quick refresher on Go concurrency, not a beginner's guide. If you want to learn concurrency from the ground up with practical exercises, check out my other book —
Gist of Go: Concurrency
.
The book is AI-free.
Goroutines
•
Channels
•
Select
•
Pipelines
•
Time
•
Context
•
Wait groups
•
Data races
•
Race conditions
•
Mutexes
•
Semaphores
•
Signaling
•
Run once
•
Object pool
•
Atomics
•
Testing
•
Scheduling
•
Diagnostics
•
Final thoughts
#
Goroutines
The foundation of concurrency in Go is
goroutines
– functions started with the
go
keyword:
func
main
()
{
var
wg
sync
.
WaitGroup
wg
.
Add
(
2
)
go
func
()
{
defer
wg
.
Done
()
fmt
.
Println
(
"worker 1"
)
}()
go
func
()
{
defer
wg
.
Done
()
fmt
.
Println
(
"worker 2"
)
}()
wg
.
Wait
()
}
worker 2
worker 1
The Go runtime juggles these goroutines and distributes them among operating system threads running on CPU cores. Compared to OS threads, goroutines are lightweight, so you can create hundreds or thousands of them.
Goroutines are completely independent. The main function is also a goroutine, but it starts implicitly when the program starts. When
main
ends, other goroutines also shut down.
We use a
wait group
(
sync.WaitGroup
) to wait for goroutines to finish in the example above. A wait group has a counter inside. Calling
Add(n)
increments it by
n
, while
Done()
decrements it by one.
Wait()
blocks the calling goroutine (in this case, main) until the counter reaches zero. This way, main waits for both workers to finish before it exits.
WaitGroup.Go
automatically increments the wait group counter, runs a function in a goroutine, and decrements the counter when it's done:
func
main
()
{
var
wg
sync
.
WaitGroup
wg
.
Go
(
func
()
{
fmt
.
Println
(
"worker 1"
)
})
wg
.
Go
(
func
()
{
fmt
.
Println
(
"worker 2"
)
})
wg
.
Wait
()
}
worker 2
worker 1
#
Channels
Goroutines can pass values to each other through
channels
. A channel is like a window where one goroutine can throw something and another can catch it:
func
main
()
{
messages
:=
make
(
chan
string
)
go
func
()
{
messages
<-
"ping"
}()
msg
:=
<-
messages
fmt
.
Println
(
msg
)
}
ping
Sending a value through a channel is a synchronous operation. When the sending goroutine writes a value to the channel (
ch <- val
), it blocks and waits for someone to receive that value (
<-ch
). Only then does it continue.
Output channel
Returning an output channel from a function and filling it within an internal goroutine is a common pattern in Go. This allows the caller to receive values through the channel while the owning function retains control of it:
func
generate
(
start
,
stop
int
)
chan
int
{
out
:=
make
(
chan
int
)
go
func
()
{
for
i
:=
start
;
i
<
stop
;
i
++
{
out
<-
i
}
}()
return
out
}
Closing a channel
To signal readers that all data has been sent, the writer goroutine
closes
the channel with
close()
:
func
generate
(
start
,
stop
int
)
chan
int
{
out
:=
make
(
chan
int
)
go
func
()
{
defer
close
(
out
)
for
i
:=
start
;
i
<
stop
;
i
++
{
out
<-
i
}
}()
return
out
}
The reader checks the channel's status with a second value ("comma OK") when reading:
func
main
()
{
in
:=
generate
(
5
,
10
)
for
{
num
,
ok
:=
<-
in
if
!
ok
{
break
}
fmt
.
Print
(
num
,
" "
)
}
}
5 6 7 8 9
While the channel is open, the reader receives the next value and a
true
status. If the channel is closed, the reader gets a zero value and a
false
status.
A channel can only be closed once. Closing it again or writing to a closed channel causes a panic.
The only reason to close a channel is to signal to its readers that all data has been sent. If this isn't important to the readers, then you don't need to close it. When a channel is no longer used, Go's garbage collector will free its resources, whether it's closed or not.
Channel iteration
range
automatically reads the next value from the channel and checks if it's closed. If the channel is closed, it exits the loop:
func
main
()
{
nums
:=
generate
(
5
,
10
)
for
n
:=
range
nums
{
fmt
.
Print
(
n
,
" "
)
}
}
5 6 7 8 9
Range over a channel returns a single value, not a pair, unlike range over a slice.
Directional channels
You can protect yourself from accidental write/close errors by setting the channel direction. Channels can be:
chan
(bidirectional): for reading and writing (default);
chan<-
(send-only): for writing only;
<-chan
(receive-only): for reading only.
You can't read from a send-only channel or write to a receive-only channel (nor can you close it).
Channels are usually initialized for both reading and writing, and specified as directional in function parameters. Go automatically converts a regular channel to a directional one:
stream
:=
make
(
chan
int
)
go
func
(
in
chan
<-
int
)
{
in
<-
42
}(
stream
)
func
(
out
<-
chan
int
)
{
fmt
.
Println
(
<-
out
)
}(
stream
)
42
Buffered channels
Buffered
channels work like a FIFO queue with a fixed-size buffer for storing values.
As long as the buffer has free space, writing to the channel doesn't block the goroutine. Similarly, as long as the buffer contains values, reading from the channel doesn't block the goroutine:
stream
:=
make
(
chan
int
,
3
)
stream
<-
11
stream
<-
12
stream
<-
13
fmt
.
Println
(
<-
stream
)
fmt
.
Println
(
<-
stream
)
11
13
By default, if you don't specify a buffer size, a channel is
unbuffered
(buffer size equals zero).
Buffered channels work with the built-in
len()
and
cap()
functions:
stream
:=
make
(
chan
int
,
3
)
stream
<-
11
fmt
.
Println
(
cap
(
stream
),
len
(
stream
))
3 1
Reading from a closed buffered channel returns values from the buffer and a
true
status. Once all values are taken, it returns a zero value and a
false
status, like a regular channel:
stream
:=
make
(
chan
int
,
1
)
stream
<-
11
close
(
stream
)
val
,
ok
:=
<-
stream
fmt
.
Println
(
val
,
ok
)
// 11 true
val
,
ok
=
<-
stream
fmt
.
Println
(
val
,
ok
)
// 0 false
11 true
0 false
nil channel
Like any type in Go, channels have a zero value, which is
nil
.
Writing to or reading from a nil channel blocks the goroutine indefinitely:
var
stream
chan
int
go
func
()
{
// blocks forever
stream
<-
1
}()
// blocks forever
<-
stream
Closing a nil channel causes a panic:
var
stream
chan
int
close
(
stream
)
// panic: close of nil channel
#
Select
The
select
statement is somewhat like
switch
, but specifically designed for channels. Here's what it does:
Checks which cases are not blocked.
If multiple cases are ready, randomly selects one to execute.
If all cases are blocked and there is a default case, executes it.
If all cases are blocked and there is no default case, waits until one is ready.
Select is used to manage data flow in pipelines:
// merge sends values from in1 and in2 to the output channel.
func
merge
(
in1
,
in2
<-
chan
int
)
<-
chan
int
{
out
:=
make
(
chan
int
)
go
func
()
{
defer
close
(
out
)
for
in1
!=
nil
||
in2
!=
nil
{
select
{
case
val1
,
ok
:=
<-
in1
:
if
ok
{
out
<-
val1
}
else
{
in1
=
nil
}
case
val2
,
ok
:=
<-
in2
:
if
ok
{
out
<-
val2
}
else
{
in2
=
nil
}
}
}
}()
return
out
}
// Suppose we send 10..12 to in1, 20..22 to in2,
// and call merge(in1, in2)
10 11 20 12 21 22
To cancel goroutines:
// process modifies values from in and send them to out
// until in is exhausted or cancel is closed.
func
process
(
cancel
chan
struct
{},
in
<-
chan
int
)
<-
chan
int
{
out
:=
make
(
chan
int
)
go
func
()
{
for
val
:=
range
in
{
select
{
case
out
<-
val
*
10
:
case
<-
cancel
:
fmt
.
Println
(
"canceled"
)
return
}
}
}()
return
out
}
// Suppose we send values 11 and 12 to in
// and then call close(cancel)
110
120
canceled
For non-blocking operations:
// multiplier returns a function that multiplies
// the input by 10 and sends it to the channel
// or returns an error if the channel is busy.
func
multiplier
(
ch
chan
<-
int
)
func
(
n
int
)
error
{
return
func
(
n
int
)
error
{
select
{
case
ch
<-
n
*
10
:
return
nil
default
:
return
errors
.
New
(
"busy"
)
}
}
}
func
main
()
{
nums
:=
make
(
chan
int
,
1
)
multiply
:=
multiplier
(
nums
)
err
:=
multiply
(
11
)
fmt
.
Println
(
<-
nums
,
err
)
// 110 <nil>
err
=
multiply
(
12
)
fmt
.
Println
(
<-
nums
,
err
)
// 120 <nil>
err
=
multiply
(
13
)
err
=
multiply
(
14
)
fmt
.
Println
(
err
)
// busy
}
110 <nil>
120 <nil>
busy
And for much more.
#
Pipelines
A
pipeline
is a sequence of operations where each step takes input data, processes it in a specific way, and outputs it. The input and output of each operation is a channel.
A typical pipeline looks like this:
Reader
: Reads input data from a file, database, or network.
N processors
: Transform, filter, aggregate, or enrich data using external sources.
Writer
: Writes the processed data to a file, database, or network.
func
read
[
T
any
]()
<-
chan
T
{
out
:=
make
(
chan
T
)
go
func
()
{
defer
close
(
out
)
for
{
// read data from somewere
data
:=
// ...
out
<-
data
}
}()
return
out
}
func
process
[
T
any
](
in
<-
chan
T
)
<-
chan
T
{
out
:=
make
(
chan
T
)
go
func
()
{
defer
close
(
out
)
for
inData
:=
range
in
{
// process the data
outData
=
// ...
out
<-
outData
}
}()
return
out
}
func
write
[
T
any
](
in
<-
chan
T
)
<-
chan
struct
{}
{
done
:=
make
(
chan
struct
{})
go
func
()
{
defer
close
(
done
)
for
data
:=
range
in
{
// write the data
}
}()
return
done
}
Output channel
A goroutine can signal other goroutines that it has finished its work using an
output channel
:
func
generate
(
start
,
stop
int
)
<-
chan
int
{
out
:=
make
(
chan
int
)
go
func
()
{
defer
close
(
out
)
for
i
:=
start
;
i
<
stop
;
i
++
{
out
<-
i
}
}()
return
out
}
func
main
()
{
nums
:=
generate
(
5
,
10
)
for
n
:=
range
nums
{
fmt
.
Print
(
n
,
" "
)
}
}
5 6 7 8 9
Done channel
If a goroutine doesn't need to return results, it can signal completion using a
done channel
:
func
work
()
<-
chan
struct
{}
{
done
:=
make
(
chan
struct
{})
go
func
()
{
defer
close
(
done
)
fmt
.
Println
(
"work done"
)
}()
return
done
}
func
main
()
{
done
:=
work
()
<-
done
}
work done
Cancel channel
To terminate a goroutine early, a calling goroutine can use a
cancel channel
:
func
generate
(
cancel
chan
struct
{},
n
int
)
<-
chan
int
{
out
:=
make
(
chan
int
)
go
func
()
{
defer
close
(
out
)
for
i
:=
1
;
i
<=
n
;
i
++
{
select
{
case
out
<-
i
:
case
<-
cancel
:
return
}
}
}()
return
out
}
func
main
()
{
cancel
:=
make
(
chan
struct
{})
defer
close
(
cancel
)
nums
:=
generate
(
cancel
,
10
)
fmt
.
Println
(
<-
nums
)
fmt
.
Println
(
<-
nums
)
fmt
.
Println
(
<-
nums
)
}
1
2
3
Error handling
There are three approaches to error handling in concurrent pipelines.
➊ Return on the first error:
// calculate produces answers for the given numbers.
func
process
(
in
<-
chan
int
)
(
<-
chan
int
,
<-
chan
error
)
{
out
:=
make
(
chan
Answer
)
errc
:=
make
(
chan
error
,
1
)
go
func
()
{
defer
close
(
out
)
for
n
:=
range
in
{
ans
,
err
:=
fetchAnswer
(
n
)
if
err
!=
nil
{
errc
<-
err
// return with error
return
}
out
<-
ans
}
errc
<-
nil
// return with nil
}()
return
out
,
errc
}
➋ Use a result type:
// Result contains an answer or an error.
type
Result
struct
{
answer
int
err
error
}
// calculate produces answers for the given numbers.
func
calculate
(
in
<-
chan
int
)
<-
chan
Result
{
out
:=
make
(
chan
Result
)
go
func
()
{
defer
close
(
out
)
for
n
:=
range
in
{
ans
,
err
:=
fetchAnswer
(
n
)
out
<-
Result
{
ans
,
err
}
// return answer + error
}
}()
return
out
}
➌ Collect errors separately:
// calculate produces answers for the given numbers.
func
calculate
(
in
<-
chan
int
,
errc
chan
<-
error
)
<-
chan
int
{
out
:=
make
(
chan
Answer
)
go
func
()
{
defer
close
(
out
)
for
n
:=
range
in
{
ans
,
err
:=
fetchAnswer
(
n
)
if
err
==
nil
{
out
<-
ans
// send answer
}
else
{
errc
<-
err
// or error
}
}
}()
return
out
}
#
Time
Besides handling date and time, the
time
package offers tools for managing time-sensitive operations in concurrent programs.
After
time.After()
returns a channel that is initially empty, but receives a value after the timeout period. It's useful for timing out operations:
// withTimeout executes a function with a given timeout.
func
withTimeout
(
timeout
time
.
Duration
,
fn
func
())
error
{
done
:=
make
(
chan
struct
{})
go
func
()
{
defer
close
(
done
)
fn
()
}()
// blocks until fn completes or the timer expires,
// whichever happens first
select
{
case
<-
done
:
return
nil
case
<-
time
.
After
(
timeout
):
return
errors
.
New
(
"timeout"
)
}
}
withTimeout()
waits for
fn()
to complete, but thanks to
time.After()
, it won't wait longer than the
timeout
duration:
func
main
()
{
var
err
error
// completes in time
err
=
withTimeout
(
50
*
time
.
Millisecond
,
func
()
{
fmt
.
Println
(
"work done"
)
},
)
fmt
.
Println
(
"err ="
,
err
)
// gets canceled on timeout
err
=
withTimeout
(
50
*
time
.
Millisecond
,
func
()
{
time
.
Sleep
(
100
*
time
.
Millisecond
)
fmt
.
Println
(
"work done"
)
},
)
fmt
.
Println
(
"err ="
,
err
)
}
work done
err = <nil>
err = timeout
Timer
A
timer
(
time.Timer
) is a structure with a
C
channel to which it sends the current time when it triggers (expires). Timers are useful for planning future executions:
done
:=
make
(
chan
struct
{})
timer
:=
time
.
NewTimer
(
50
*
time
.
Millisecond
)
go
func
()
{
eventTime
:=
<-
timer
.
C
// blocks for 50ms
fmt
.
Println
(
"work done at"
,
eventTime
)
close
(
done
)
}()
<-
done
work done at 2009-11-10 23:00:00.05
Stop()
stops the timer and returns
true
if it hasn't expired yet, and
false
otherwise:
// timer expires after 50ms
timer
:=
time
.
NewTimer
(
50
*
time
.
Millisecond
)
go
func
()
{
eventTime
:=
<-
timer
.
C
fmt
.
Println
(
"work done at"
,
eventTime
)
}()
// after 10ms, the timer hasn't expired yet
time
.
Sleep
(
10
*
time
.
Millisecond
)
if
timer
.
Stop
()
{
fmt
.
Println
(
"execution canceled"
)
}
else
{
fmt
.
Println
(
"too late to cancel"
)
}
execution canceled
It's often more convenient to use the
time.AfterFunc()
wrapper function. It waits for duration
d
and then executes function
f
:
done
:=
make
(
chan
struct
{})
work
:=
func
()
{
fmt
.
Println
(
"work done"
)
close
(
done
)
}
// executes work after 50ms
time
.
AfterFunc
(
50
*
time
.
Millisecond
,
work
)
<-
done
work done
time.AfterFunc()
returns a timer that you can cancel before execution starts:
// executes the function after 50ms
timer
:=
time
.
AfterFunc
(
50
*
time
.
Millisecond
,
func
()
{})
// after 10ms, the timer hasn't expired yet
time
.
Sleep
(
10
*
time
.
Millisecond
)
if
timer
.
Stop
()
{
fmt
.
Println
(
"execution canceled"
)
}
execution canceled
If a timer is used in a loop, it's better to create a single timer and
reset
it instead of creating a new instance on each iteration:
// consumer reads tokens from the input channel and alerts
// if a value does not appear in a channel after an hour.
func
consumer
(
in
<-
chan
token
)
{
const
timeout
=
time
.
Hour
timer
:=
time
.
NewTimer
(
timeout
)
for
{
timer
.
Reset
(
timeout
)
select
{
case
<-
in
:
// do stuff
case
<-
timer
.
C
:
// log warning
}
}
}
// Suppose we send 10,000 values to the in channel
// and measure memory usage.
Memory used: 4 KB, # allocations: 6
Ticker
A
ticker
is like a timer, but it keeps firing until you stop it. Tickers are useful for executing periodic tasks:
// fires every 50ms
ticker
:=
time
.
NewTicker
(
50
*
time
.
Millisecond
)
defer
ticker
.
Stop
()
go
func
()
{
for
{
// waits for ticker to fire on each iteration
at
:=
<-
ticker
.
C
fmt
.
Println
(
"work done at"
,
at
)
}
}()
// enough time for the ticker to fire 3 times
time
.
Sleep
(
160
*
time
.
Millisecond
)
ticker
.
Stop
()
work done at 2009-11-10 23:00:00.05
work done at 2009-11-10 23:00:00.10
work done at 2009-11-10 23:00:00.15
NewTicker(d)
creates a ticker that sends the current time to the channel
C
at interval
d
. You must stop the ticker eventually with
Stop()
to free up resources.
If the channel reader can't keep up with the ticker, the ticker will skip ticks.
#
Context
The main purpose of
context
is to cancel operations, either manually or by timeout/deadline.
The function accepts a context and uses its
Done()
channel to listen for cancellation:
// work performs a task for 50 ms unless canceled.
// Returns an error when canceled.
func
work
(
ctx
context
.
Context
)
error
{
done
:=
make
(
chan
struct
{})
go
func
()
{
time
.
Sleep
(
50
*
time
.
Millisecond
)
fmt
.
Println
(
"work done"
)
close
(
done
)
}()
select
{
case
<-
done
:
return
nil
case
<-
ctx
.
Done
():
return
ctx
.
Err
()
}
}
Cancel manually (
context.Canceled
error):
func
main
()
{
// empty context
ctx
:=
context
.
Background
()
// manual canellation context
ctx
,
cancel
:=
context
.
WithCancel
(
ctx
)
defer
cancel
()
done
:=
make
(
chan
struct
{})
go
func
()
{
// takes 50 ms unless canceled
err
:=
work
(
ctx
)
fmt
.
Println
(
"err ="
,
err
)
close
(
done
)
}()
// cancels after 10 ms
time
.
Sleep
(
10
*
time
.
Millisecond
)
cancel
()
<-
done
}
err = context canceled
Cancel by timeout (
context.DeadlineExceeded
error):
func
main
()
{
ctx
:=
context
.
Background
()
// cancels after 10 ms
ctx
,
cancel
:=
context
.
WithTimeout
(
ctx
,
10
*
time
.
Millisecond
)
defer
cancel
()
done
:=
make
(
chan
struct
{})
go
func
()
{
// takes 50 ms unless canceled
err
:=
work
(
ctx
)
fmt
.
Println
(
"err ="
,
err
)
close
(
done
)
}()
<-
done
}
err = context deadline exceeded
Cancel by deadline (
context.DeadlineExceeded
error):
func
main
()
{
ctx
:=
context
.
Background
()
// cancels at now + 10 ms
deadline
:=
time
.
Now
().
Add
(
10
*
time
.
Millisecond
)
ctx
,
cancel
:=
context
.
WithDeadline
(
ctx
,
deadline
)
defer
cancel
()
done
:=
make
(
chan
struct
{})
go
func
()
{
// takes 50 ms unless canceled
err
:=
work
(
ctx
)
fmt
.
Println
(
"err ="
,
err
)
close
(
done
)
}()
<-
done
}
err = context deadline exceeded
Context is layered. A context object is immutable. To add new properties to a context, a new (child) context is created based on the old (parent) context. The shorter timeout between the parent and child contexts always wins. The child context can only shorten the parent's timeout, not extend it:
func
main
()
{
// parent context with a 100 ms timeout
const
dur100ms
=
100
*
time
.
Millisecond
parentCtx
,
cancel
:=
context
.
WithTimeout
(
context
.
Background
(),
dur100ms
)
defer
cancel
()
// child context with a 10 ms timeout
const
dur10ms
=
10
*
time
.
Millisecond
childCtx
,
cancel
:=
context
.
WithTimeout
(
parentCtx
,
dur10ms
)
defer
cancel
()
// now the work gets canceled
err
:=
work
(
childCtx
)
fmt
.
Println
(
"err ="
,
err
)
}
err = context deadline exceeded
Multiple cancels are safe. You can call
cancel()
on the context as many times as you want. The first cancel will work, and the rest will be ignored.
You can specify a custom cancellation cause using
context.WithCancelCause()
,
context.WithTimeoutCause()
and
context.WithDeadlineCause()
. This cause is accessible through
context.Cause()
:
ctx
,
cancel
:=
context
.
WithCancelCause
(
context
.
Background
())
cancel
(
errors
.
New
(
"the night is dark"
))
fmt
.
Println
(
context
.
Cause
(
ctx
))
the night is dark
You can register a function to execute when the context is canceled with
context.AfterFunc()
:
ctx
,
cancel
:=
context
.
WithCancel
(
context
.
Background
())
cleanup
:=
func
()
{
fmt
.
Println
(
"cleanup"
)
}
context
.
AfterFunc
(
ctx
,
cleanup
)
cancel
()
time
.
Sleep
(
10
*
time
.
Millisecond
)
cleanup
Context can pass additional information about a call using
context.WithValue()
, which creates a context with a value for a specific key. But it's generally better to avoid passing values in context. It's better to use explicit parameters or custom structs instead.
#
Wait groups
The
sync.WaitGroup
type lets you wait for one or more goroutines to finish:
const
n
=
10
var
wg
sync
.
WaitGroup
wg
.
Add
(
n
)
for
range
n
{
go
func
()
{
defer
wg
.
Done
()
fmt
.
Print
(
"."
)
}()
}
wg
.
Wait
()
..........
A
WaitGroup
doesn't know anything about the goroutines it manages. It works with an internal counter. Calling
wg.Add(1)
increments the counter by one, while
wg.Done()
decrements it.
wg.Wait()
blocks the calling goroutine until the counter reaches zero.
The
Go
method combines
Add
, starting a goroutine, and
Done
:
var
wg
sync
.
WaitGroup
for
range
10
{
wg
.
Go
(
func
()
{
fmt
.
Print
(
"."
)
})
}
wg
.
Wait
()
..........
All methods are safe to use from multiple goroutines.
Normally, all
Add
calls happen before
Wait
. But technically, there's nothing stopping you from doing some of the
Add
calls before
Wait
and some after (from another goroutine).
You can call
Wait
from multiple goroutines. They will all block until the group's counter reaches zero.
#
Data races
A data race happens when multiple goroutines access shared data, and at least one of them modifies it. We need to protect the data from this kind of concurrent access.
A data race doesn't always cause a runtime panic. That's why Go provides a special tool called the race detector. You can turn it on with the
race
flag, which works with the
test
,
run
,
build
, and
install
commands.
var
total
int
// There's a data race on total.
var
wg
sync
.
WaitGroup
wg
.
Go
(
func
()
{
total
++
})
wg
.
Go
(
func
()
{
total
++
})
wg
.
Wait
()
fmt
.
Println
(
"total:"
,
total
)
total: 2
go run -race main.go
==================
WARNING: DATA RACE
...
2
Found 1 data race(s)
Channels are safe for concurrent reading and writing, and they don't cause data races.
Ways to prevent data races:
Avoid concurrent data modification (typically by using channels).
Synchronize access with mutexes.
Use only atomic operations.
Race conditions
A race condition happens when an unpredictable order of operations from multiple goroutines leads to an incorrect system state:
// There's a race condition when working with balance.
withdraw
:=
func
(
amount
int
)
{
if
getBalance
()
<
amount
{
return
}
time
.
Sleep
(
time
.
Millisecond
)
setBalance
(
getBalance
()
-
amount
)
}
setBalance
(
50
)
var
wg
sync
.
WaitGroup
wg
.
Go
(
func
()
{
withdraw
(
40
)
})
wg
.
Go
(
func
()
{
withdraw
(
40
)
})
wg
.
Wait
()
fmt
.
Println
(
"balance:"
,
getBalance
())
balance: -30
If individual operations are concurrent-safe, Go's race detector won't find any issues. Because of this, it doesn't catch race conditions:
go run -race main.go
balance: -30
You can't fully eliminate uncertainty in a concurrent environment. Events will happen in an unpredictable order — that's just how concurrency works. However, you can prevent a race condition — often by protecting a composite operation with a mutex:
var
mu
sync
.
Mutex
withdraw
:=
func
(
amount
int
)
{
mu
.
Lock
()
defer
mu
.
Unlock
()
if
getBalance
()
<
amount
{
return
}
time
.
Sleep
(
time
.
Millisecond
)
setBalance
(
getBalance
()
-
amount
)
}
setBalance
(
50
)
var
wg
sync
.
WaitGroup
wg
.
Go
(
func
()
{
withdraw
(
40
)
})
wg
.
Go
(
func
()
{
withdraw
(
40
)
})
wg
.
Wait
()
fmt
.
Println
(
"balance:"
,
getBalance
())
balance: 10
Compare-and-set
Sometimes you can prevent a race condition without using mutexes by applying an atomic compare-and-set operation or one of its flavors:
// CompareAndSet changes the value to new if the current value equals old.
// Returns true if the value was changed.
CompareAndSet
(
old
,
new
any
)
bool
// CompareAndSwap changes the value to new if the current value equals old.
// Returns the old value.
CompareAndSwap
(
old
,
new
any
)
any
// CompareAndDelete deletes the value if the current value equals old.
// Returns true if the value was deleted.
CompareAndDelete
(
old
any
)
bool
// etc
The idea is always the same:
Check if the assumed (old) state matches reality.
If it does, change the state to new.
If not, do nothing.
#
Mutexes
The
sync.Mutex
type protects shared data and parts of your code from being accessed concurrently:
var
total
int
var
mu
sync
.
Mutex
var
wg
sync
.
WaitGroup
for
range
100
{
wg
.
Go
(
func
()
{
mu
.
Lock
()
time
.
Sleep
(
time
.
Millisecond
)
total
++
mu
.
Unlock
()
})
}
wg
.
Wait
()
total: 100
The mutex guarantees that only one goroutine can run the code between
Lock()
and
Unlock()
at a time.
A mutex is used in these situations:
When multiple goroutines are modifying the same data.
When one goroutine is modifying the data and others are reading it.
If all goroutines are only reading the data, you don't need a mutex.
TryLock
The
TryLock
method tries to lock the mutex, just like a regular
Lock
. But if it can't, it returns
false
right away instead of blocking the goroutine:
var
total
int
var
mu
sync
.
Mutex
var
wg
sync
.
WaitGroup
for
range
100
{
wg
.
Go
(
func
()
{
if
!
mu
.
TryLock
()
{
return
}
defer
mu
.
Unlock
()
time
.
Sleep
(
time
.
Millisecond
)
total
++
})
}
wg
.
Wait
()
total: 1
RWMutex
The
sync.RWMutex
type distinguishes between readers and writers. It provides two sets of methods:
Lock
/
Unlock
lock and unlock the mutex for both reading and writing.
RLock
/
RUnlock
lock and unlock the mutex for reading only.
var
total
int
var
mu
sync
.
RWM

## Metadata
- **Source**: [Original Article](https://antonz.org/go-concurrency-distilled/)
