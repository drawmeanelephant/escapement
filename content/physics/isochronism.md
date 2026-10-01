---
title: "Isochronism"
description: "The property that makes timekeeping possible — the oscillator's period staying constant as amplitude changes — and why perfect isochronism is a myth."
date: "2026-09-27"
author: "Buffy"
categories: ["physics"]
tags: ["physics", "balance-spring", "amplitude", "accuracy"]
---

**Isochronism** (from Greek *iso-* equal, *chronos* time) is the property that
an oscillator's period stays the same regardless of how far it swings. It is
the whole ballgame: if the period shifts with amplitude, then everything that
changes amplitude — winding state, position, [lubrication](friction-and-lubrication.md),
[magnetism](../maintenance/magnetism.md) — shifts the rate.

## The theory

A [balance wheel on an ideal spring](the-balance-spring.md) is isochronous by
physics, exactly like a pendulum for small arcs. The problems are all
second-order:

1. **Spring imperfections.** A real spiral's center of gravity drifts as it
   breathes; end effects make the outer turns behave differently. Breguet
   overcoils and [Phillips terminal curves](the-balance-spring.md#geometry-the-fight-against-the-spring-itself)
   attack this directly.
2. **Escapement disturbance.** Each impulse is a shove, not a whisper; how
   much it disturbs the period depends on amplitude. Detached escapements
   ([lever](../escapements/swiss-lever.md), [detent](../escapements/detent.md))
   minimize the contact window; the [co-axial](../escapements/co-axial.md)
   minimizes friction within it.
3. **Air resistance and pivots.** Friction is not perfectly proportional to
   speed; at different amplitudes, different fractions of energy leak through
   different paths.

## Why amplitude is the dial

[Amplitude](amplitude.md) is the visible proxy for isochronism health. A watch
that keeps the same rate at 310° and at 220° is isochronous *in practice*;
one that drifts 15 seconds across that range is not, and its daily rate will
depend on the hour you last wound it. Timing in positions
([see](positions-and-rate.md)) partially averages these effects, which is why
observatory chronometers were adjusted to many positions at many amplitudes.

## The mainspring conspiracy

The [mainspring's](../anatomy/03-the-mainspring-and-barrel.md) falling torque
slowly lowers amplitude across the power reserve. A non-isochronous watch thus
runs at *different rates at 10 p.m. and 10 a.m.* — the classic "it gains when
I wear it, loses in the drawer" complaint. Long power reserves help only by
flattening the curve; [constant-force devices](../anatomy/03-the-mainspring-and-barrel.md#constant-force-tricks)
remove it.

## How to judge it

Wristwatch specs almost never quote isochronism directly. The practical proxy:
compare the rate fully wound versus 24 hours later, dial up. Single-digit
differences mean good isochronism. Chronometer certification
([COSC and kin](positions-and-rate.md)) tests average rates but also requires
positional consistency — the closest public evidence you get.
