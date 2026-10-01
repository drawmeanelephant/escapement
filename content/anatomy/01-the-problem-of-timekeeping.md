---
title: "Anatomy 1: The Problem of Timekeeping"
description: "Why keeping time with a machine is hard at all: you need a repeating oscillator, a way to count it, and a way to pay for the counting."
date: "2026-09-23"
author: "Buffy"
categories: ["anatomy"]
tags: ["series-anatomy", "guide", "escapement", "balance", "physics"]
---

*Part 1 of 8 in the [Anatomy series](../start-here/read-me-first.md#path-1--the-machinist-8-parts-90-minutes).*

Before any wheels, before any jewels: what does it mean for a *machine* to keep
time? Strip the problem down and there are exactly three requirements — and every
part in a watch exists to serve one of them.

## 1. Something must repeat, perfectly

Timekeeping is counting repetitions. A sundial counts the sun's motion; a
water clock counts drips; a mechanical watch counts *oscillations*. The quality
of the timekeeping is the quality of the repetition: if every swing takes exactly
the same duration, counting is trivial. If the swings drift, no amount of clever
gearwork can rescue the result.

Pendulums are superb repeators — the length of a pendulum largely fixes its
period, which is why the [pendulum clock](../history/1656-huygens-and-the-pendulum.md)
dominated for 300 years. But a pendulum needs gravity and stillness; it fails on
a moving ship. The wrist solution is the
[balance and spring](../anatomy/05-the-balance-assembly.md): a wheel that rocks
on a hairspring instead of swinging on a rod.

The hard truth this series keeps returning to: the oscillator's repetition is
*almost* perfect but never exactly so. It shifts with
[position](../physics/positions-and-rate.md), [temperature](../physics/isochronism.md),
[magnetism](../maintenance/magnetism.md), and [amplitude](../physics/amplitude.md).
Modern horology is mostly the art of shrinking those shifts.

## 2. Something must count, without interfering

You cannot simply attach a counter to a spinning oscillator — friction would stop
it. The count must be taken *gently*, a tiny sample per swing, without dragging
on the oscillator's rhythm.

That is the [escapement's](../anatomy/04-the-escapement.md) whole job: to let the
power train advance one discrete step per oscillation, and to deliver each step as
a small push that replaces exactly the energy friction stole. The tick-tock is
the sound of that transaction.

## 3. Something must pay for it all

Counting and oscillating both cost energy. The energy comes from your wrist (an
automatic) or your fingers (a manual wind), stored in a
[mainspring](../anatomy/03-the-mainspring-and-barrel.md). A spring is a flawed
battery: it delivers its hardest shove when full and its gentlest when nearly
spent — so the machine must behave identically at both extremes, or the watch
would run fast at 9 p.m. and slow at 9 a.m. The engineering name for this
requirement is *constant torque*, and meeting it occupies several pages of this
site.

## The shape of the solution

The mechanical watch answers all three requirements with four subsystems:

1. The [gear train](../anatomy/02-the-gear-train.md) — transports and scales energy.
2. The [mainspring and barrel](../anatomy/03-the-mainspring-and-barrel.md) — stores it.
3. The [escapement](../anatomy/04-the-escapement.md) — referees the exchange.
4. The [balance assembly](../anatomy/05-the-balance-assembly.md) — keeps the rhythm.

Plus two quiet support casts: the [keyless works](../anatomy/06-the-keyless-works.md)
for winding and setting, and the [motion works](../anatomy/07-the-motion-works-and-dial.md)
for turning gear rotations into hand positions. Next: the train.
