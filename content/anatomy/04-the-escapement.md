---
title: "Anatomy 4: The Escapement"
description: "The referee between the train and the balance: lock, impulse, drop — the two milliseconds that make the tick, and the geometry that makes it work."
date: "2026-09-26"
author: "Buffy"
categories: ["anatomy"]
tags: ["series-anatomy", "escapement", "balance", "physics"]
---

*Part 4 of 8 in the [Anatomy series](../start-here/read-me-first.md#path-1--the-machinist-8-parts-90-minutes).*

Everything before this point was plumbing. The escapement is where the watch
decides what time it is. It has two duties, and they conflict:

1. **Lock** the power train completely between ticks (or friction would drag
   the oscillator).
2. **Impulse** the oscillator once per tick, delivering exactly the energy it
   lost — no more (it would over-bank), no less (it would stop).

The standard solution in nearly every mechanical watch is the
[Swiss lever escapement](../escapements/swiss-lever.md), in service since the
18th century in concept and the 19th in practice. It has three actors: the
**escape wheel** (the train's last wheel, with distinctive club-shaped teeth),
the **pallet fork** (a lever with two ruby stones), and the **balance staff**
carrying the impulse jewel.

## One tick, four events

![Lock, unlock, impulse, drop: the four events of one tick](/assets/img/escapement-cycle.svg "One tick, four events — the geometry of a single tick")

Watchmakers decompose a tick into events, and the vocabulary is worth learning:

1. **Lock.** The escape wheel rests against a pallet stone, held by the train's
   torque. The balance swings freely, "detached" — hence *detached lever*. This
   is most of the tick's duration.
2. **Unlock.** The returning impulse jewel nudges the fork; the fork's horn
   unlocks the wheel. The unlocking consumes a little energy — geometry
   ([draw](../escapements/swiss-lever/drop-lock-and-lift.md)) keeps the fork
   poised against its banking pin throughout.
3. **Impulse.** The escape wheel tooth slides across the pallet stone's impulse
   face, then the fork's slot pushes the impulse jewel. This is the gift of
   energy — the *only* energy the oscillator ever receives.
4. **Drop.** The tooth falls off the stone's locking corner to the next stone:
   a small shock, the "tock" in tick-tock, and the fork crosses to the opposite
   banking.

Then the balance swings out, returns, and the whole sequence mirrors on the other
pallet. Two events per oscillation; 8 per second in a
[4 Hz](../physics/frequency.md) watch.

## Why the geometry matters

The angles are hair-raisingly small — pallet stones span a few degrees of the
escape wheel, impulse faces are inclined by *lift angle* degrees (typically
45–52° of lock-to-lift action summed), and manufacturing tolerances are counted
in hundredths of a millimeter. Get the geometry wrong and you get friction
without impulse (a watch that stops), or impulse without lock (a watch that
runs 20 minutes fast), or banking knocks (a fork hammering its pins).

That is why [drop, lock, and lift](../escapements/swiss-lever/drop-lock-and-lift.md)
get their own page, and why [co-axial](../escapements/co-axial.md) and
[detent](../escapements/detent.md) escapements exist at all: each is a
different philosophical answer to "how do we give the oscillator energy without
stealing accuracy?"

Next: the timekeeper itself —
[The Balance Assembly](../anatomy/05-the-balance-assembly.md).

---

**Anatomy 4 of 8** · ← [Anatomy 3: The Mainspring and Barrel](03-the-mainspring-and-barrel.md) · [Anatomy 5: The Balance Assembly](05-the-balance-assembly.md) →
