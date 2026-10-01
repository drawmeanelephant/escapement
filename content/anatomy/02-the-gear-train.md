---
title: "Anatomy 2: The Gear Train"
description: "Barrel to escape wheel: how a train of wheels turns one rotation an hour into one a minute, and why every ratio is a compromise with friction."
date: "2026-09-24"
author: "Buffy"
categories: ["anatomy"]
tags: ["series-anatomy", "gear-train", "mainspring", "escapement"]
---

*Part 2 of 8 in the [Anatomy series](../start-here/read-me-first.md#path-1--the-machinist-8-parts-90-minutes).*

A watch gear train is not a gearbox. A gearbox trades speed for torque to move a
load; a watch train mostly exists to *slow down* a spring's unwinding into
useful, countable speeds — while losing as little energy as possible along the
way.

## The canonical layout

![The going train from barrel to escape wheel, with turning speeds](/assets/img/gear-train.svg "The going train: energy flows left to right, rotation slows as torque is diluted")

In a classic movement the wheels run:

**barrel → center wheel → third wheel → fourth wheel → escape wheel**

- The **barrel** turns once every 6–8 hours or so (it holds the
  [mainspring](../anatomy/03-the-mainspring-and-barrel.md)).
- The **center wheel** turns exactly once per hour — the minute hand mounts on
  its arbor, poking through the dial.
- The **third wheel** is pure ratio, an idler with attitude.
- The **fourth wheel** turns exactly once per minute — the seconds hand. Small
  seconds at 6 o'clock is literally the fourth wheel's extended pivot.
- The **escape wheel** hands energy to the
  [escapement](../anatomy/04-the-escapement.md) one tooth at a time.

Every wheel meshes with a *pinion*: a small, hardened steel leaf-gear on the
next wheel's arbor. A wheel driving a pinion is a reduction; the train's
counting is done by ratios (typically 72:1 from barrel to center in a manual
movement) chosen so the hands turn at the right speeds.

## Why not fewer, bigger wheels?

Friction. Every mesh and every pivot is a leak. The design goal is the *fewest
meshes that achieve the ratio*, with the least sliding friction — which is why
watch teeth are shaped like a cycloidal-ish rounded stub rather than the
involute teeth of industrial gearing, and why pivots run in
[jeweled bearings](../physics/friction-and-lubrication.md).

## The center-seconds problem

A fourth-wheel seconds hand lives at 6 o'clock. If you want seconds in the
*center*, where a hand would pass over the cannon pinion, you need extra work:
an indirect center seconds (an extra wheel driven off the fourth) or a direct
drive (train redesigned so the fourth wheel is central). Both are compromises —
indirect seconds can stutter when the hands are set, direct drive adds height.
This is the sort of "trivial" detail that keeps watchmakers employed.

## The cannon pinion: the train's one intentional slip

The [motion works](../anatomy/07-the-motion-works-and-dial.md) must let you set
the hands without forcing the whole train to spin against the
[escapement](../anatomy/04-the-escapement.md). The center wheel's arbor therefore
carries a *cannon pinion* mounted on a friction fit: tight enough to drive the
hands, loose enough to slip when you turn the crown to set. That single
controlled slip is why setting a watch feels like it has a detent, and why
worn cannon pinions make watches "lose" their set time.

Next: where the energy comes from —
[The Mainspring and Barrel](../anatomy/03-the-mainspring-and-barrel.md).
