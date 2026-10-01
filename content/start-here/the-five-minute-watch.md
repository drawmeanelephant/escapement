---
title: "The Five-Minute Watch"
description: "The entire mechanical watch in one page: a spring, a train of wheels, an oscillator, and a mechanism that refuses to let either run free."
date: "2026-09-30"
author: "Buffy"
categories: ["orientation"]
tags: ["guide", "gear-train", "escapement", "balance", "mainspring"]
---

Strip a mechanical watch to its ideas and there are only four. Everything else —
every [complication](../complications/index.md), every decorated bridge — is
variation on this theme.

## 1. A spring that lies about its strength

The [mainspring](../anatomy/03-the-mainspring-and-barrel.md) is a coiled ribbon of
steel in a drum called the barrel. Wound tight it pulls hard; nearly spent it
pulls gently. Left alone it would empty in hours and at wildly uneven speed.
So the barrel drives a [gear train](../anatomy/02-the-gear-train.md), and the
watch's designers arrange for the spring's dishonesty to be diluted at every
wheel — plus, in quality movements, a [fusee or similar constant-force device](../anatomy/03-the-mainspring-and-barrel.md#constant-force-tricks).

## 2. A train of wheels that exists to be interrupted

The gear train does two jobs: turn the [motion works](../anatomy/07-the-motion-works-and-dial.md)
at the right speed for the hands, and deliver the spring's power to the
[escapement](../anatomy/04-the-escapement.md) in usable form. The fourth wheel
turns once a minute (seconds), the center wheel once an hour (minutes); the
escapement's wheel is the last wheel in line, and it is never allowed to simply
spin.

## 3. An oscillator that keeps its own time

A weighted wheel on a spring — the [balance assembly](../anatomy/05-the-balance-assembly.md)
— rocks back and forth at a fixed rate: 28,800 vibrations per hour in a typical
modern watch. This is the timekeeper. Not the gears, not the spring: the
*oscillator*. Everything else just counts its swings.

## 4. A referee

The [escapement](../escapements/swiss-lever.md) sits between the eager gear train
and the serene oscillator. Each swing of the balance, the escapement unlocks and
lets the train advance *one tooth* — delivering a tiny push that pays back the
energy the oscillator loses to friction. Between swings: locked, silent, ticking.

That push-and-release is the tick you hear. (An old watchmaker's joke: a watch is
a machine for counting to 86,400 a day.)

## Why the details matter

Each of the four ideas has a failure mode that the rest of the machine exists to
manage:

| Idea | Failure mode | Managed by |
| --- | --- | --- |
| Spring | torque falls as it unwinds | [barrel and train ratios](../anatomy/03-the-mainspring-and-barrel.md), [remontoirs](../escapements/detent.md) |
| Train | friction, side-shake, oil decay | [jewels, lubrication](../physics/friction-and-lubrication.md) |
| Oscillator | position, temperature, magnetism | [regulation](../physics/positions-and-rate.md), [materials](../physics/the-balance-spring.md) |
| Escapement | friction steals accuracy | [geometry](../escapements/swiss-lever/drop-lock-and-lift.md), [materials](../escapements/co-axial.md) |

Ready for detail? Begin [The Problem of Timekeeping](../anatomy/01-the-problem-of-timekeeping.md).
