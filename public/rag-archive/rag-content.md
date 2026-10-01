<file path="content/about.md">
<content>
---
title: "About & Colophon"
description: "Who writes Escapement, how it is built, and why every claim on this site is meant to be checkable."
date: "2026-09-30"
author: "Buffy"
categories: ["orientation"]
tags: ["colophon", "guide"]
---

**Escapement** is an independent explainer site about mechanical horology: how
watches work, why they work *that* way, and what the last four hundred years of
timekeeping got right and wrong.

## Who writes this

Every page was written by **Buffy**, an AI coding agent, as part of an exercise in
building a real, self-contained publication with
[La Famille](https://github.com/drawmeanelephant/la-famille), a Go static site
generator. No page is placeholder text. Where a claim is contested in horology —
the [balance-spring priority dispute](history/1675-the-balance-spring-race.md),
for instance, or whether a [tourbillon](complications/tourbillon.md) helps a
wristwatch at all — the page says so instead of picking a winner silently.

## How it is built

- **Generator:** La Famille, from source or a release binary. The whole site is
  markdown, a config file, and hand-drawn SVG diagrams — no external fonts, no
  CDNs, no trackers,no runtime JavaScript dependencies beyond the self-contained
[graph explorer](/graph/) page the build emits.
- **Diagrams:** every illustration is an SVG drawn for this site, stored in
  `assets/img/`, and rebuildable by editing the file with a text editor.
- **Portability:** the built `public/` directory is a complete static artifact.
  Drop it on any static host. Serve it from a domain root (image paths are
  root-absolute `/assets/...`); from a subpath, adjust those few references.
- **Machine-readable corpus:** each build publishes a `rag-archive/` whose
  `rag-content.md` is the entire site flattened into one coherent document,
  designed to be pasted into a prompt.

## Corrections

Horology writing is full of confident myths (Breguet invented everything,
the Swiss invented the lever, quartz killed mechanical forever). This site tries
to date and attribute its claims; if you find one that is wrong, the fix is a
markdown edit away.

Continue with [Read Me First](start-here/read-me-first.md) for the guided tour,
or [The Five-Minute Watch](start-here/the-five-minute-watch.md) for the whole
machine in one page.

</content>
</file>

<file path="content/anatomy/01-the-problem-of-timekeeping.md">
<content>
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

</content>
</file>

<file path="content/anatomy/02-the-gear-train.md">
<content>
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

</content>
</file>

<file path="content/anatomy/03-the-mainspring-and-barrel.md">
<content>
---
title: "Anatomy 3: The Mainspring and Barrel"
description: "The engine: a coiled steel ribbon whose torque falls as it unwinds — and the tricks (barrel, fusee, remontoir) that keep a watch honest about it."
date: "2026-09-25"
author: "Buffy"
categories: ["anatomy"]
tags: ["series-anatomy", "mainspring", "gear-train", "power-reserve", "physics"]
---

*Part 3 of 8 in the [Anatomy series](../start-here/read-me-first.md#path-1--the-machinist-8-parts-90-minutes).*

The mainspring is a flat ribbon of special steel, a meter or so long, coiled
inside a drum called the **barrel**. Wind the crown and you coil it tighter;
the stored torque then drives the [gear train](../anatomy/02-the-gear-train.md)
as it uncoils. Simple. The problem is in the torque curve.

## The dishonest battery

A coiled spring's torque is highest fully wound and lowest nearly spent —
easily a 30–40% difference across the power reserve. If that difference reached
the escapement directly, the watch's [amplitude](../physics/amplitude.md) would
collapse overnight and its rate would wander with the hour of day.

## Constant-force tricks

Watchmakers fight back with dilution and cleverness:

1. **The going barrel.** In most watches the barrel *is* the first wheel, and
   the spring is sized so the watch runs on the *middle* of the torque curve.
   The mainspring's hooked inner end (the bridle) slips along the barrel wall
   when fully wound — an automatic clutch, so over-winding is impossible. This
   is why an automatic watch is always "slipping" near full wind.
2. **The fusee.** The historical answer: the spring drives a cone-shaped
   pulley via a chain or gut, so that as torque falls, leverage rises. A fusee
   chronometer keeps nearly constant torque across its entire reserve — it is
   also tall, fragile, and expensive, which is why it vanished from wristwatches
   but remains the textbook constant-force device.
3. **The remontoir.** A tiny secondary spring (or weight) re-wound at fixed
   intervals delivers constant force to the escapement regardless of the main
   spring's mood. Beautiful, rare, and covered where it belongs — with the
   [detent escapements](../escapements/detent.md) that love it.

## Power reserve

The useful wind is a countable resource, so of course we display it: a
[power-reserve indicator](../complications/power-reserve.md) is a differential
mechanism measuring the difference between how far the barrel has unwound and
how far you have wound it. Calibrating one by hand during assembly is one of
the least envious jobs in the workshop.

## Materials science in one paragraph

Mainsprings are alloys (Nivaflex and kin) designed for high yield strength,
minimal set (they must spring back to shape for decades), and corrosion
resistance. Before the 1950s, springs broke — literally snapped — as a routine
service item; the "unbreakable" mainspring was a genuine marketing revolution.
Modern springs in modern barrels deliver 48–70+ hours of
[power reserve](../complications/power-reserve.md), and the arms race for longer
reserves is mostly a barrel-and-efficiency contest, not some new energy source.

Next: the machine's conscience —
[The Escapement](../anatomy/04-the-escapement.md).

</content>
</file>

<file path="content/anatomy/04-the-escapement.md">
<content>
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

</content>
</file>

<file path="content/anatomy/05-the-balance-assembly.md">
<content>
---
title: "Anatomy 5: The Balance Assembly"
description: "The oscillator that actually keeps time: balance wheel, hairspring, jewels, and the adjustment screws that let a watchmaker negotiate with physics."
date: "2026-09-27"
author: "Buffy"
categories: ["anatomy"]
tags: ["series-anatomy", "balance", "balance-spring", "physics", "shock-protection"]
---

*Part 5 of 8 in the [Anatomy series](../start-here/read-me-first.md#path-1--the-machinist-8-parts-90-minutes).*

If you could keep only one assembly from the whole watch, keep this one. The
balance assembly is the timekeeper; everything else is support.

## The balance wheel

![The balance assembly from above: wheel, hairspring, regulator and stud](/assets/img/balance-spring.svg "The balance assembly from above — the timekeeper itself")

A weighted wheel on a staff, mounted between two jeweled bearings, free to
rotate back and forth. Its period depends on three things:

- **Moment of inertia** (mass distributed around the rim),
- **Spring strength** (the hairspring's torque per degree),
- **Geometry luck** (the wheel must oscillate, not wander).

Adding weight to the rim slows it down; moving weight inward speeds it up.
**Timing screws** (or small weights on free-sprung balances) let the watchmaker
adjust the wheel's inertia precisely — that is what "adjusting in positions"
ultimately manipulates.

## The hairspring

The [balance spring](../physics/the-balance-spring.md) is the flat spiral of
exotic alloy above the wheel. It is the second-most important invention in
horology after the pendulum: without it the balance would oscillate at a rate
that depends on how hard it was pushed (a property called *isochronism failure*,
discussed [here](../physics/isochronism.md)) — with it, the period is governed
mainly by the spring itself.

The spring's outer end is pinned to the stud; the inner end coils around the
collet on the balance staff. Between them sits the **regulator** — an index with
curb pins that changes the spring's effective length to speed the watch up or
slower it down. Free-sprung watches omit the index entirely and adjust by
timing weights alone: fewer moving parts, better stability, harder to service.

## Shock protection

The balance staff pivots are absurdly thin — thinner than a hair — and a drop
would snap them instantly. **Shock settings** (Incabloc, KIF, Paraflex,
Diashock) mount the jewel bearings in spring-loaded cups: a shock lets the
jewel move a fraction of a millimeter and return. Introduced in the 1930s and
one of the quiet reasons the wristwatch became survivable. See
[Shock protection](../physics/friction-and-lubrication.md#shock-settings) for
the details and limits.

## The roller and impulse jewel

Under the balance sits the **roller table** carrying the **impulse jewel** —
the little ruby tongue that engages the [pallet fork](../anatomy/04-the-escapement.md)
once per swing. Its height, depth, and the roller's **safety action** (roller
dart and fork's safety pin) guarantee that the fork can only be thrown when the
balance is actually coming to give it impulse — a knocked wrist otherwise
couldn't double-unlock the escapement.

## The whole, in one sentence

A mass on a spring, isolated from the world on jeweled pivots, exchanging a
pinch of energy with the [escapement](../escapements/swiss-lever.md) twice per
period, counting 86,400 beats a day to within a few seconds.

That last number — the [rate](../physics/positions-and-rate.md) — is where
watchmaking stops being assembly and starts being adjustment. Next, though:
[The Keyless Works](../anatomy/06-the-keyless-works.md).

</content>
</file>

<file path="content/anatomy/06-the-keyless-works.md">
<content>
---
title: "Anatomy 6: The Keyless Works"
description: "One crown, two jobs: how a sliding pinion and a setting lever let you both wind the mainspring and set the hands without a key."
date: "2026-09-28"
author: "Buffy"
categories: ["anatomy"]
tags: ["series-anatomy", "keyless-works", "gear-train", "mainspring"]
---

*Part 6 of 8 in the [Anatomy series](../start-here/read-me-first.md#path-1--the-machinist-8-parts-90-minutes).*

Before 1842 you wound a watch with a key. The **keyless works** — the
mechanism that lets a single crown both wind and set — was the everyday
revolution of the 19th century, and it is still the part of a watch most likely
to be gritty, worn, or badly reassembled.

## The cast

Mounted along the stem inside the case:

- The **winding stem** with its square section and the crown outside the case.
- The **clutch wheel (crown wheel)**: teeth that mesh with the winding train in
  one position.
- The **sliding pinion** (clutch pinion): splined to the stem so it rotates with
  it but can slide along it.
- The **setting lever** and its spring (yoke in many designs): hold the pinion
  in position, and give the crown its two-pull click feel.
- The **winding pinion and crown wheel** (first wheel of the winding train)
  feeding the [barrel](../anatomy/03-the-mainspring-and-barrel.md).

## The two positions

**Winding position (crown in):** the sliding pinion engages the winding pinion;
turning the crown winds the [mainspring](../anatomy/03-the-mainspring-and-barrel.md)
through a ratchet and click. The ratchet's click spring is why winding makes
noise and why the spring can't unwind back through the crown.

**Setting position (crown pulled):** the setting lever shoves the sliding
pinion into mesh with the **minute wheel** of the [motion works](../anatomy/07-the-motion-works-and-dial.md);
now the crown turns the hands, and the cannon pinion's friction clutch slips so
the [gear train](../anatomy/02-the-gear-train.md) isn't force-fed.

Pulling feels like a click because a detent spring drops into a notch on the
setting lever. The quality of that click — crisp, indexed, one confident
position — is pure case-and-lever engineering.

## Variations worth knowing

- **Screw-down crowns** (dive watches) thread the whole crown against a gasket
  for [water resistance](../maintenance/water-resistance.md); they add a tube
  and a decoupling clutch so winding pressure doesn't fight the threads.
- **Push-button adjusters** and **quick-set date** mechanisms add cam paths so
  the crown's second position sets the date without moving the hands.
- **Hidden crowns** and **recessed pushers** serve
  [perpetual calendars](../complications/perpetual-calendar.md), which must
  never be set "backwards" through a forbidden zone — the classic way to bend a
  QP's month lever.

Next: turning rotations into hours —
[The Motion Works and Dial](../anatomy/07-the-motion-works-and-dial.md).

</content>
</file>

<file path="content/anatomy/07-the-motion-works-and-dial.md">
<content>
---
title: "Anatomy 7: The Motion Works and Dial"
description: "How the hands are geared to disagree by exactly 12:1, why the cannon pinion slips, and what dial feet have to do with all of it."
date: "2026-09-29"
author: "Buffy"
categories: ["anatomy"]
tags: ["series-anatomy", "dial-train", "gear-train", "keyless-works"]
---

*Part 7 of 8 in the [Anatomy series](../start-here/read-me-first.md#path-1--the-machinist-8-parts-90-minutes).*

The [gear train](../anatomy/02-the-gear-train.md) turns at the right speeds; the
motion works is the small, exact gear cluster that turns those speeds into *hand
positions* — and reconciles the one ratio that matters to humans: 12 hours per
revolution of the minute hand.

## The three wheels

- **Cannon pinion** — on the center wheel's arbor; turns once per hour. The
  minute hand presses onto it.
- **Minute wheel** — an idler between cannon and hour wheel, which is why the
  hands move opposite to the train's rotation direction.
- **Hour wheel** — turns once per 12 hours; the hour hand presses onto it.

The cannon-to-hour ratio is 12:1 exactly. The idler's tooth count doesn't change
the ratio, only the direction and spacing — designers pick it to fit the dial
real estate.

## The cannon pinion is a clutch

We met it in [part 2](../anatomy/02-the-gear-train.md#the-cannon-pinion-the-trains-one-intentional-slip):
the cannon pinion is pressed onto the center arbor with controlled friction.
Winding never touches it; setting the hands forces it to slip around the arbor.
Its friction must be:

- High enough that the motion works never slips during normal running (or the
  watch would "lose time" while the seconds kept ticking),
- Low enough that setting feels smooth and doesn't strain the
  [keyless works](../anatomy/06-the-keyless-works.md) or the
  [escapement](../anatomy/04-the-escapement.md).

Watchmakers tune it by feel with a staking tool. When it wears loose, a watch
keeps perfect time and yet the *hands* drift — one of the great diagnostic
puzzles for beginners.

## Hands, dial, and motion

Hands are calibrated press-fits: hour, minute, and (seconds on the
[fourth wheel](../anatomy/02-the-gear-train.md) or a center-seconds runner).
The dial is held by **dial feet** — two or three posts soldered to the dial's
back, locked under the movement by dial-foot screws or a locking plate. Dial
feet positions define dial variants: the same calibre can be dressed in
different dial layouts (sub-seconds at 6, 9, or center) by moving feet and
hands.

Lume, printing, and finishing live here too — but the mechanical point is
simple: between the fourth wheel and the tip of a hand there is nothing but
exact ratios and controlled friction. Next, the finale:
[Putting It Together](../anatomy/08-putting-it-together.md).

</content>
</file>

<file path="content/anatomy/08-putting-it-together.md">
<content>
---
title: "Anatomy 8: Putting It Together"
description: "A full watch teardown in service order — what comes apart first, what gets cleaned, what gets oiled, and how the subsystems reunite."
date: "2026-09-30"
author: "Buffy"
categories: ["anatomy"]
tags: ["series-anatomy", "service", "gear-train", "escapement", "balance", "lubrication"]
---

*Part 8 of 8 in the [Anatomy series](../start-here/read-me-first.md#path-1--the-machinist-8-parts-90-minutes).*

Theory is finished; now the bench. This is a movement teardown in the order a
watchmaker actually works — because order is the difference between a service
and an incident.

## The service order, annotated

1. **Case out.** Hands off (with protector film), dial off (dial feet screws),
   movement out of the case. Note the [keyless works](../anatomy/06-the-keyless-works.md)
   state before touching anything.
2. **Let down the power.** Hold the click open and let the
   [mainspring](../anatomy/03-the-mainspring-and-barrel.md) down in a controlled
   way. Working on a wound movement is how screwdrivers become projectiles.
3. **Motion works and calendar** (if any): cannon pinion, minute wheel, hour
   wheel, then calendar plates and their springs — photograph springs before
   removal; they photograph their own revenge later.
4. **Balance out first among the train.** The
   [balance assembly](../anatomy/05-the-balance-assembly.md) is the most
   fragile part; removing it early removes the risk. It goes straight into a
   labeled basket, hairspring up.
5. **Pallet fork and bridge**, then the escape wheel. The
   [escapement](../anatomy/04-the-escapement.md) stones and pivots are
   inspected for chips and wear under magnification.
6. **Train wheels and bridges** down to the barrel. Check endshake and
   sideshake at each wheel as it comes out.
7. **Barrel:** open, inspect the mainspring (set? rust? cracked bridle?), clean,
   re-grease the barrel wall with braking grease, reassemble with correct
   [lubrication](../physics/friction-and-lubrication.md).

## Cleaning and lubrication

Baskets into an ultrasonic cleaning cycle (clean, rinse, rinse, dry), then
selective oiling: light oil on fast, light pivots (escape, pallet), heavier oil
on slow, loaded ones (center, barrel arbor), epilame on the
[impulse surfaces](../escapements/swiss-lever/drop-lock-and-lift.md) where oil
must *not* creep. A well-oiled watch runs for years; a badly-oiled one runs
fast, then stops.

## Reassembly and the four tests

Reverse the order; fit the balance last so it never bears load. Then:

1. **Amplitude and rate** on a timegrapher — see
   [Amplitude](../physics/amplitude.md) for what healthy looks like.
2. **Positions** — dial up, dial down, crown down, crown left… the spread
   should be single-digit seconds, per [positions and rate](../physics/positions-and-rate.md).
3. **Functions** — winding feel, setting feel, hand alignment at 12:00, date
   changeover if any.
4. **Case tests** — gaskets, [water resistance](../maintenance/water-resistance.md)
   pressure test, and a 24-hour rest before final rate check.

## Where to go next

You now know the whole machine. The deep dives await: the geometry of
[drop, lock, and lift](../escapements/swiss-lever/drop-lock-and-lift.md), the
philosophy of the [co-axial](../escapements/co-axial.md), the science of
[isochronism](../physics/isochronism.md), or the [timeline](../history/index.md)
that produced every idea above.

</content>
</file>

<file path="content/complications/chronograph.md">
<content>
---
title: "The Chronograph"
description: "A stopwatch on a wrist: column wheel vs cam, lateral clutch vs vertical, the heart-piece reset — how a chronograph counts without a computer."
date: "2026-09-28"
author: "Buffy"
categories: ["complications"]
tags: ["chronograph", "complications", "guide", "frequency"]
---

A **chronograph** (Greek: *time writer*) is a watch that can start, stop, and
reset an independent elapsed-seconds count while the timekeeping train keeps
running. It is the most popular complication in the world and the one with the
most engineering folklore. Here is the whole machine.

## The three subsystems

1. **The coupling** — connects the timekeeping train to the chronograph runner
   when you press start.
2. **The drive** — wheels that turn the chronograph seconds (center), the
   30-minute and 12-hour counters.
3. **The control** — the start/stop/reset logic, levers and cams or column
   wheel, plus the reset heart pieces.

## Column wheel vs cam

The **column wheel** is a rotating turret with pillars; levers ride its
columns, so each press is a crisp sequence of lifts and drops. Feel: smooth,
precise, expensive to make.

The **cam** replaces the turret with a shaped cam and jumper springs; modern
cams (the [Valjoux 7750](../movements/valjoux-7750.md) lineage) can feel
excellent, and the industry's snobbery about column wheels outruns the physics
— but the column wheel remains the traditional mark of a considered design.

## Lateral clutch vs vertical clutch

- **Lateral (horizontal) clutch** — the chronograph runner swings into mesh
  with the running seconds wheel. Traditional, thin, visible in action; can
  shudder on start ("stuttering seconds hand") because it engages a moving
  wheel.
- **Vertical clutch** — a friction clutch stacked on the center; engagement
  is invisible and jerk-free, like a car's clutch. Rolex's 4130 (2000) made it
  famous; most modern integrated chronographs use it. Also allows the seconds
  hand to run continuously without wear.

The [Zenith El Primero](../movements/zenith-el-primero.md) famously uses an
**oscillating pinion** — a pinion that tilts into mesh — a wonderfully compact
lateral variant with near-vertical engagement feel.

## Reset: the heart piece

Each counter hand's arbor carries a **heart cam**. Press reset and a hammer
drops on the heart; the cam's geometry forces the hand to *its zero* whatever
its position — a mechanical "return to zero" solved with pure shape. The
column wheel or cam ensures reset can only fire when stopped (or, in
flybacks, whenever).

## Buying sense

- **Integrated** chronograph (built as a chronograph, e.g. El Primero,
  4130-family) vs **module** (added on a base calibre): thinner and more
  coherent vs cheaper and taller.
- Higher beat rates ([5 Hz](../physics/frequency.md)) allow 1/10-second
  displays — El Primero's party trick since 1969.
- Service cost scales with levers, not prestige: a column-wheel split-seconds
  is the deep end.

</content>
</file>

<file path="content/complications/gmt-and-world-time.md">
<content>
---
title: "GMT and World Time"
description: "Second time zones without a second watch: the extra hour hand, the 24-hour bezel, and Louis Cottier's world-time mechanism."
date: "2026-09-29"
author: "Buffy"
categories: ["complications"]
tags: ["complications", "guide", "history"]
---

Time zones are a political-geographic mess, so of course watches built
mechanisms to hold several at once. Two families dominate: the **GMT watch**
(one extra hour hand) and the **world timer** (all 24 zones at a glance).

## The GMT watch

A fourth hand — the **GMT hand** — geared to the [motion works](../anatomy/07-the-motion-works-and-dial.md)
makes one revolution per 24 hours. Read it against a 24-hour bezel or an inner
24-hour track: it points at the home zone's hour while the normal hands show
local time.

The archetype: the **Rolex GMT-Master (1955)**, designed with Pan Am for
transatlantic crews who needed home and destination time simultaneously. Its
24-hour bezel (two-color Bakelite originally) isn't a toy — it distinguishes
day from night in the home zone, which matters when you call the office.

Mechanically, the GMT hand is almost free: one extra wheel ratio off the hour
wheel. Modern "true" or "flyer" GMTs (local-hour-jumping) add a mechanism to
jump the local hour hand in whole hours when crossing zones — the traveler's
GMT — while "caller" GMTs move the GMT hand instead. Purks argue; both are
gear trains.

## World time

The **world timer** shows all 24 zones at once: a city ring, a 24-hour ring
rotating once per day, and the local city at 12 o'clock. The design is due to
**Louis Cottier** (1930s Geneva watchmaker), whose mechanism is delightfully
simple — the 24-hour disc is driven off the hour wheel; the city ring is set
by a pusher or bezel.

Reading it: find your city on the ring; the hour it aligns with on the
rotating 24-hour disc is the current hour there. Daylight saving is the one
thing it can't know — world timers assume standard offsets, so the display is
a *political* snapshot, not a live database. (Everything is a trade-off; see
[What Counts as a Complication](index.md).)

## Complications that count zones

Both designs are, at heart, [counting](index.md) mechanisms: GMT counts a
24:1 ratio; world timers map 24 hours onto 24 labels. The
[perpetual calendar](perpetual-calendar.md) counts months; the same gear-train
honesty applies. And all of them go wrong only where politics does: borders,
half-hour zones (India, Newfoundland), and daylight saving.

</content>
</file>

<file path="content/complications/index.md">
<content>
---
title: "What Counts as a Complication"
description: "Anything that isn't just hours, minutes, and seconds — a taxonomy of watch complications and the one insight that explains almost all of them."
date: "2026-09-27"
author: "Buffy"
categories: ["complications"]
tags: ["guide", "chronograph", "perpetual-calendar", "tourbillon", "repeater", "moonphase"]
---

In horology a **complication** is any function beyond simple hours, minutes,
and (usually) seconds. The word is a translation of the French
*complication* — and the honest truth is that most complications are variations
on a single idea: **count something else cleverly**.

## The taxonomy

**Counting elapsed time** (the stopwatch family):
- [Chronograph](chronograph.md) — seconds, minutes, sometimes hours, on demand.
- Flyback, rattrapante (split-seconds) — counting tricks on top of counting.

**Counting calendar time** (the computer family):
- Date, day, month — wheels and pins.
- [Perpetual calendar](perpetual-calendar.md) — remembers leap years with a
  4-year cam.
- [Moonphase](moonphase.md) — a 59-tooth (or better) simulation of the lunar
  month.
- Annual calendar — the honest middle: knows 30 vs 31, asks for help in March.

**Counting sounds** (the music family):
- [Minute repeater](minute-repeater.md) — strikes hours, quarters, minutes.
- Grande/petite sonnerie — striking on autopilot; alarm — striking on purpose.

**Fighting position errors** (the physics family):
- [Tourbillon](tourbillon.md) — rotates the escapement to average gravity.
- [GMT / world time](gmt-and-world-time.md) — counts a second (and third)
  time zone.

**Counting the spring's mood:**
- [Power reserve](power-reserve.md) — shows how much counting is left.

## The insight

Each complication is a *mechanical memory plus a display*. The perpetual
calendar's memory is a 48-month cam; the chronograph's is its coupling lever;
the repeater's is a rack-and-snail that physically *measures* how far the
minute hand has passed. There is no software, no sensor — only geometry that
remembers. When you press a pusher and a tiny lever falls into a notch, that
notch *is* the data structure.

## What makes one good

Watchmakers judge complications by: thinness of the added module, robustness
of the memory (what happens if you set it backwards?), service burden (how
many extra springs fly away at disassembly), and whether the complication
earns its friction budget. The pages in this section score each candidate on
those terms — including the parts of the story the marketing omits.

</content>
</file>

<file path="content/complications/minute-repeater.md">
<content>
---
title: "The Minute Repeater"
description: "A watch that speaks the time: racks, snails, gongs, and the acoustics of striking hours, quarters, and minutes on demand."
date: "2026-09-29"
author: "Buffy"
categories: ["complications"]
tags: ["repeater", "complications", "guide", "history"]
---

A **minute repeater** does not display the time when asked — it *sounds* it.
Push the slide and the watch strikes: low tones for hours, a high-low pair for
each quarter, high tones for the minutes past the quarter. Before electric
light, it was how you read the time in the dark. Today it is the summit of
mechanical virtuosity, because sound is unforgiving.

## The mechanism: measure, then strike

Two trains, both separate from the timekeeping [gear train](../anatomy/02-the-gear-train.md):

1. **The measuring train.** Winding the slide tensions a dedicated spring. A
   set of **snails** (cams shaped like spirals, one per unit) and **racks**
   (toothed arms that fall onto the snails) physically *measure* the current
   hours, quarters, and minutes-past-quarter. The racks' fall distances are
   the data; no memory, just immediate geometry.
2. **The striking train.** A governor (fan fly) meters the speed; a hammer
   (or two) strikes **gongs** — hardened steel or gold wires circling the
   movement. The racks' positions control how many strikes sound.

The famous "minutes repeat" complexity: the last minutes sound one at a time,
deliberately, up to 14 tones after the quarters.

## Acoustics: why repeaters differ wildly

The case is the instrument. Tone depends on:

- **Gong geometry** — length, cross-section, attachment; "cathedral gongs"
  wrap nearly twice around the movement for longer, deeper resonance.
- **Case metal and volume** — gold vs platinum vs titanium changes damping;
  hollowed "soundbox" cases (Richard Mille, Audemars Piguet's RD# work) treat
  the case as a resonant chamber.
- **Regulation** — the governor's speed sets strike tempo; a good repeater
  has even, unhurried rhythm.

Chiming trains come in grades: **quarter repeater** (quarters + hours),
**minute repeater** (adds minutes), **grande sonnerie** (strikes quarters
automatically), **petite sonnerie** (hours automatically, quarters on demand),
and **grande sonnerie + minute repeater + Westminster chimes** (the stratosphere).

## Owning one

Prices start where sensible cars stop and rise without limit. But the honest
reviewer's note: a repeater's value is *acoustic* — listen before buying, and
know that servicing one is a specialty (the racks-and-snails adjustment is a
craft by itself). For pure mechanical romance, nothing else in horology
argues this hard. See [Tourbillon](tourbillon.md) for the visual equivalent
of the same argument.

</content>
</file>

<file path="content/complications/moonphase.md">
<content>
---
title: "The Moonphase"
description: "A 59-tooth disc pretending to be the moon: how moonphase displays work, their real error rate, and the high-precision versions that chase a century of accuracy."
date: "2026-09-30"
author: "Buffy"
categories: ["complications"]
tags: ["moonphase", "complications", "guide"]
---

The **moonphase** display is the most romantic useless thing on a watch: a
little disc with two moons peeking through a shaped aperture, tracking the
synodic month — new moon, first quarter, full, last quarter — in metal.

## The mechanism

The lunar month (new moon to new moon) averages **29.53059 days**. The classic
display is a disc with 59 teeth and two moons, advanced one tooth every 24
hours by a pin on the 24-hour wheel. Two moons × 29.5 days = 59 days per
revolution.

But 2 × 29.5 = 59.0, while the real month is 29.53059 — so the classic
moonphase gains about **one day every 2.7 years** (the error accumulates:
59/2 = 29.5 vs 29.53059). Owner's reality: reset it whenever you notice; no
moonphase displays the actual lunar phase with astronomical accuracy anyway
(the moon's face as seen from Earth varies with latitude and orbit
eccentrics).

## The precision chase

Watchmakers can't leave a rounding error alone:

- **135-tooth discs** (and similar high-count trains) shrink error to roughly
  one day per 122 years or better.
- **Astronomical moonphases** (e.g. Patek Philippe's with 135 teeth, Arnold &
  Son's perpetual moon, Ochs und Jahre's modular moon) are driven by precise
  ratios geared off the date train.
- **Ulysse Nardin's moonphase** modules track the moon with startling accuracy
  using differential gearing.

A "one-day-in-122-years" moonphase is, mechanically, a very slow argument
between 29.5 and 29.53059 — the same fight the [perpetual calendar](perpetual-calendar.md)
has with 2100.

## Why bother

Because it is the only complication that points *out* of the watch. Everything
else on the dial is a human convention — seconds, dates, zones. The moonphase
tracks an actual object in the sky, imperfectly, forever. Set it to the last
new moon and it will be slightly wrong for decades while still telling a truth
about the machine inside.

See [What Counts as a Complication](index.md) for the family it belongs to.

</content>
</file>

<file path="content/complications/perpetual-calendar.md">
<content>
---
title: "The Perpetual Calendar"
description: "A watch that knows leap years: 48-month cams, the QP memory, the setting forbidden zones — and why most of them will be wrong on March 1, 2100."
date: "2026-09-28"
author: "Buffy"
categories: ["complications"]
tags: ["perpetual-calendar", "complications", "guide", "history"]
---

A **perpetual calendar** (QP — *quantième perpétuel*) displays day, date,
month, and usually moonphase and leap year, and — the whole point — knows that
February has 28 days except in leap years. It is a mechanical calendar
computer with a four-year memory.

## The memory is a cam

The core is the **48-month cam**: a snail-like wheel with 48 steps encoding
four years of month lengths. A feeler rides its edge; at year end, the cam's
step drops the date mechanism from Dec 31 straight to Jan 1 regardless of
month length. The **leap-year indicator** (1/2/3/4 or a simple 4-year disc)
is a small wheel geared to the same train.

Wheels stacked on wheels carry the display: day, date, month, moonphase —
each with its own corrector pusher, and each with its own spring waiting to
betray a careless watchmaker.

## The forbidden zones

A QP is a one-way state machine. Setting it backward through a date change can
bend levers or skip states, so manufacturers specify "do not set between 8 pm
and 3 am" (or similar) and place corrector recesses in the case. The modern
convenience arms race — safe-set mechanisms, crown-set QPs (IWC Portugieser
Perpetual, Ulysse Nardin Perpetual Ludwig) — is entirely about removing those
forbidden zones without adding failure modes.

## The 2100 problem

The Gregorian calendar skips leap years on century years not divisible by 400:
2100 is **not** a leap year. A typical mechanical QP assumes the simple 4-year
cycle, so on **March 1, 2100** it will show March 2 — and need a watchmaker.
A handful of designs (the rare "secular" perpetuals) add a 400-year wheel or
programmed cam to handle it. When someone sells you a watch "your
grandchildren won't need to adjust," ask them about 2100.

## History in one breath

Pocket QPs date to the 18th century (Mudge and others; Breguet refined).
The first perpetual calendar *wristwatch* is generally credited to Patek
Philippe's **1526** (1941); Audemars Piguet's 5516 (1955) added a leap-year
indicator display. The modern era treats the QP as the gateway to high
complication — paired with chronographs ([the "QP chrono" archetype](chronograph.md))
and, at the summit, [repeaters](minute-repeater.md) and [tourbillons](tourbillon.md).

More mechanics in [What Counts as a Complication](index.md).

</content>
</file>

<file path="content/complications/power-reserve.md">
<content>
---
title: "Power Reserve"
description: "A gauge for the mainspring: differentials, indicator scales, and why a power-reserve display is harder to build than it looks."
date: "2026-09-30"
author: "Buffy"
categories: ["complications"]
tags: ["power-reserve", "complications", "mainspring", "guide"]
---

A **power-reserve indicator** (réserve de marche) shows how much energy
remains in the [mainspring](../anatomy/03-the-mainspring-and-barrel.md) —
typically 40 to 70+ hours on a small arc. It is the watch's fuel gauge, and
mechanically it is a subtraction problem.

## The differential

The barrel winds in one direction (via the crown or an automatic rotor) and
unwinds in another (running the [gear train](../anatomy/02-the-gear-train.md)).
A needle that merely followed the barrel would swing wildly during winding.

The solution is a **differential**: a planetary gear that outputs the
*difference* between how far the barrel has unwound and how far it has been
wound. The hand shows remaining travel — going to zero as the reserve dies.
Assembly requires hand-calibrating the zero point against the actual stop:
the least envious job on the bench (as [noted earlier](../anatomy/03-the-mainspring-and-barrel.md)).

## Design shapes

- **Linear scales** (F.P. Journe's Réserve de Marche, A. Lange & Söhne's
  outsize date family) — an arc or straight scale sweeping 0 to max.
- **Sub-dial gauges** — vintage instrument style.
- **Retrograde** hands that snap back to zero when rewound.

Automatic movements complicate the picture: the rotor is always topping up, so
the display oscillates in daily wear rather than sweeping monotonically down.
Owners learn to read the *trend*.

## Why it matters beyond romance

[Amplitude](../physics/amplitude.md) falls as the reserve empties, and with it
(rate-wise) goes [isochronism](../physics/isochronism.md). A power reserve
display is therefore the only complication that tells you *when your watch's
accuracy will change*. Long reserves (70h+, 120h, 8 days) are the modern
luxury arms race — often won by twin or series-coupled barrels
([constant-force thinking](../anatomy/03-the-mainspring-and-barrel.md#constant-force-tricks))
rather than magic.

More in [What Counts as a Complication](index.md).

</content>
</file>

<file path="content/complications/tourbillon.md">
<content>
---
title: "The Tourbillon"
description: "Breguet's 1801 patent: a rotating cage that averages gravity's mischief — what it really does, why wristwatches arguably don't need it, and why we love it anyway."
date: "2026-09-29"
author: "Buffy"
categories: ["complications"]
tags: ["tourbillon", "complications", "history", "physics", "timeline"]
---

The **tourbillon** (French: *whirlwind*) is a cage carrying the entire
escapement and [balance assembly](../anatomy/05-the-balance-assembly.md),
rotating once per minute (typically), so that positional errors average out
over each revolution. Patented by **Abraham-Louis Breguet on 26 June 1801**
(7 Messidor, Year IX) — and argued about ever since.

![A tourbillon cage: balance and escape wheel rotating inside the carriage](/assets/img/tourbillon-cage.svg "The tourbillon cage — the escapement rotates once per minute")

## The physics it attacks

A watch hanging in a pocket holds its balance in one orientation for hours;
gravity then pulls the balance's center of mass consistently off-axis,
producing a steady positional rate error ([details](../physics/positions-and-rate.md)).
Breguet's insight: if the escapement rotates through all vertical positions
each minute, the errors average to nearly zero.

It is a genuinely clever, purely mechanical averaging algorithm.

## Does it help a wristwatch?

The honest debate:

- **The case for:** wristwatches *do* move through positions, and fine
  tourbillons have won chronometer competitions into the modern era (e.g.
  observatory trials and modern certifications). A one-minute tourbillon in a
  wristwatch still averages the vertical positions it spends time in.
- **The case against:** the wrist already randomizes position; the
  [lever escapement](../escapements/swiss-lever.md) is already detached; and
  adding a cage costs energy ([amplitude](../physics/amplitude.md)) and adds
  mass and fragility. Some tests show wrist tourbillons improving averages
  barely or not at all.
- **The verdict of the market:** irrelevant. The tourbillon is the visible
  soul of the craft — a spinning heart you can watch — and it has become the
  canvas where watchmakers show what they can do (multi-axis cages, flying
  tourbillons without an upper bridge, tourbillons inside tourbillons).

## Cousins and variants

- **Carrousel (Bonniksen, 1892):** same averaging goal, but the cage is driven
  by the train rather than carrying the escapement on its own axis; cheaper to
  make historically, Danish-British origin.
- **Flying tourbillon:** cantilevered cage, no upper pivot — the full
  spectacle.
- **Multi-axis tourbillons:** average in all planes; beautiful, energy-hungry,
  rare (Greubel Forsey, Jaeger-LeCoultre Gyrotourbillon).

If you want accuracy per dollar, buy [certification](../physics/positions-and-rate.md).
If you want to see the 1801 patent still spinning, nothing else will do.

</content>
</file>

<file path="content/escapements/co-axial.md">
<content>
---
title: "The Co-axial Escapement"
description: "George Daniels' answer to sliding friction: separate locking from impulse so the escapement pushes instead of rubs — history, mechanics, and the trade-offs."
date: "2026-09-28"
author: "Buffy"
categories: ["escapements"]
tags: ["escapement", "physics", "lubrication", "timeline"]
---

George Daniels — the greatest independent watchmaker of the 20th century, and
the man who hand-made watches from raw metal — patented the **co-axial
escapement** in 1974 (patent granted 1980) as "the last great escapement." Its
claim: eliminate sliding friction from the impulse phase, so an escapement can
run for years without oil degrading its rate.

## The complaint it answers

In the [Swiss lever](swiss-lever.md), impulse happens *while the pallet stone
slides along the tooth face* — rubbing, by design. Lubricant cushions the rub,
but lubricant decays, migrates, and thickens. A lever watch's rate is therefore
a slow negotiation with its own oil.

## The mechanism

The co-axial escapement stacks two functions on one staff:

- **Locking** happens on nearly radial faces — the wheel pushes the pallet
  stone directly, like a detent, with barely any sliding.
- **Impulse** happens on separate, dedicated impulse surfaces in the same
  brief event.

Three wheels share one axis (hence "co-axial"): the co-axial wheel drives two
pallet stones — one impulse, one locking-and-impulse — through a lever that
looks like a conventional fork. The balance keeps its detached rhythm; the
wheels deliver energy by *pushing* rather than *scraping*.

## What it actually changed

- Sliding friction per impulse drops dramatically; escape-wheel tooth wear
  falls; oil on the critical surfaces becomes far less load-bearing.
- Omega commercialized it in the Calibre 2500 (1999, based on the ETA 2892),
  after buying Daniels' rights; later 8xxx and 9xxx families (Si14 silicon
  springs, coaxial architecture) made it mainstream.
- Servicing got *different*, not easier: the geometry demands precision, and
  early calibres had their own adjustment lessons (beat error, amplitude
  sensitivity) before the design matured.

## The honest trade-offs

The co-axial is not friction-free — impulses still involve contact, and the
lever still slides at unlock. Detachment quality equals a lever; raw
chronometric ceiling arguably still belongs to the [detent](detent.md). What
the co-axial buys is *stability over the service interval*: the rate it keeps
on day 100 is closer to the rate it kept on day 1.

Daniels wanted a mechanical watch that could be a lifetime companion without
annual ritual. Whether the co-axial is "better" than a well-made Swiss lever
is horology's most productive argument — but that it is *different in kind* is
undeniable. See [Drop, Lock, and Lift](swiss-lever/drop-lock-and-lift.md) for
the friction it escaped from.

</content>
</file>

<file path="content/escapements/compared.md">
<content>
---
title: "Escapements, Compared"
description: "An open scorecard: accuracy ceiling, robustness, self-starting, service tolerance, and cost across the escapement family."
date: "2026-09-29"
author: "Buffy"
categories: ["escapements"]
tags: ["escapement", "guide", "accuracy", "history"]
---

Every escapement page on this site makes a case. This page makes the case
against each one, in one table, scored 1–5 (5 = best). Scores are engineering
judgments, not gospel — argue with them via the factors below.

| Design | Accuracy ceiling | Robustness | Self-start | Service tolerance | Cost to make | Where |
| --- | --- | --- | --- | --- | --- | --- |
| [Verge](verge-and-foliot.md) | 1 | 3 | 5 | 2 | 5 | tower clocks (historic) |
| Cylinder | 2 | 2 | 5 | 2 | 4 | cheap pocket watches (historic) |
| Duplex | 3 | 2 | 2 | 2 | 3 | slender pocket watches (historic) |
| [Swiss lever](swiss-lever.md) | 4 | 5 | 5 | 4 | 5 | nearly all wristwatches |
| [Co-axial](co-axial.md) | 4 | 5 | 5 | 3 | 3 | Omega and licensees |
| [Detent](detent.md) | 5 | 1 | 1 | 2 | 2 | chronometers, regulators |

## How to read the scores

- **Accuracy ceiling** — best achievable rate when perfectly made and
  adjusted, independent of case. The detent wins because the oscillator is
  freest ([isochronism](../physics/isochronism.md) losses minimized).
- **Robustness** — tolerance to shocks, positional change, and neglect. The
  lever's safety action and forgiveness dominate; the detent is fragile.
- **Self-start** — will it tick again after dying without special handling?
  Detents famously won't.
- **Service tolerance** — how long between services before rate degrades,
  driven mostly by [lubrication](../physics/friction-and-lubrication.md)
  sensitivity. The co-axial's whole pitch lives here.
- **Cost to make** — manufacturing and finishing burden at equal quality.

## The verdicts people actually make

- **You want a watch you can wear anywhere, service anywhere:** Swiss lever.
  It is the QWERTY of horology — good enough everywhere, unbeatable on total
  cost of ownership.
- **You want the longest stable interval between services:** co-axial (with
  modern materials), accepting a smaller service network and fussier geometry.
- **You want the last word in rate, in a box, on a ship:** detent, plus a
  [remontoir](../anatomy/03-the-mainspring-and-barrel.md#constant-force-tricks).
- **You want history on your wrist:** cylinder or duplex, and a patient
  watchmaker.

The deeper lesson from the whole table: escapements improve by *removing
friction from the oscillator's life*. Everything else — safety, starting,
manufacturing — is the price paid for that removal.

</content>
</file>

<file path="content/escapements/cylinder-and-duplex.md">
<content>
---
title: "Cylinder and Duplex"
description: "The watch escapements between the verge and the lever: the deadbeat cylinder, the clever duplex, and why both were displaced by the detached lever."
date: "2026-09-26"
author: "Buffy"
categories: ["escapements"]
tags: ["escapement", "history", "timeline"]
---

Between the crude [verge](verge-and-foliot.md) and the modern
[lever](swiss-lever.md) sit two clever compromises that powered the pocket-watch
century: the **cylinder** and the **duplex**.

## The cylinder escapement

Patented in refined form by Thomas Tompion and others around 1700 (the idea is
credited to Graham, c. 1720s), the cylinder escapement replaces pallets with a
hollow, notched **cylinder** on the balance staff. Escape wheel teeth pass
*inside* the cylinder wall, giving impulse through the cylinder's lip.

- **Virtue:** flat — perfect for the slim pocket watches the 18th century
  adored. Cheap enough for mass production.
- **Vice:** the balance staff is a wearing part (it *is* the escapement surface),
  so it wears out; and the balance is never detached — the tooth rests against
  the cylinder between beats, so rate depends on driving torque.

A well-made cylinder watch keeps a few minutes a week; a worn one owns your
patience. Breguet and the observatory makers never loved it.

## The duplex

The duplex separates the two jobs: a tall tooth locks the balance's ruby roller
directly (frictionless-ish *lock*), while a second set of teeth gives *impulse*
through a single impulse pin on the balance.

- **Virtue:** near-detached locking, so it can be very accurate — duplex pocket
  watches won prizes.
- **Vice:** fragile under shocks ("trip" failures), tricky to start after
  stopping, and it cannot tolerate a slipping seconds hand.

## Why the lever won

The [Swiss lever](swiss-lever.md) offered almost the duplex's detachment with
the cylinder's robustness — and, crucially, it tolerates the modern
[shock setting](../physics/friction-and-lubrication.md#shock-settings) era:
a knocked wrist doesn't double-unlock it, thanks to the safety action. By the
late 1800s the lever had won the wrist; the cylinder survived only in cheap
mass production into the early 20th century.

The escapee's-eye view of progress: each design pushed friction into a smaller
window until the window became the [co-axial](co-axial.md) and
[detent](detent.md) debates of today.

</content>
</file>

<file path="content/escapements/detent.md">
<content>
---
title: "The Detent Escapement"
description: "The chronometer escapement: impulse with virtually no friction, absolute detachment — and why it rules the sea but never the wrist."
date: "2026-09-29"
author: "Buffy"
categories: ["escapements"]
tags: ["escapement", "history", "physics", "power-reserve"]
---

The **detent escapement** (spring detent, chronometer escapement) is the
purest answer to the escapement problem: the oscillator receives impulse
directly from the escape wheel through a single frictionless-ish push, and is
otherwise completely detached. It is the most accurate mechanical escapement
ever devised — and it cannot survive a wrist.

## How it works

- A **detent** — a tiny spring-loaded arm with a locking stone — holds the
  escape wheel until the balance unlocks it.
- The impulse is delivered by the **escape wheel tooth directly onto the
  balance's impulse jewel** (or an impulse roller). No lever in the path.
- A **second roller and safety action** ensure the detent can only be unlocked
  during a real impulse; after unlocking, the detent is re-caught ("trapped")
  so the wheel cannot escape twice.

Because the impulse path is direct and short, sliding friction is minimal and
the oscillator's free arc is nearly ideal. A spring detent chronometer in a
gimbaled box could hold rates of fractions of a second per day.

## The catch

Two properties kill it for portable use:

1. **It is not shock-proof.** A jar can bounce the detent; the escapement
   double-unlocks or stops. Marine chronometers lived in gimbals for exactly
   this reason. (Modern *free* detent designs with improved safety exist but
   remain delicate.)
2. **It is not reliably self-starting.** Let the amplitude die and the watch
   may sit there, fully wound, politely refusing to tick.

## Where it belongs

Marine chronometers, some astronomical regulators, and the wrists of
exhibitionists (a few modern firms make detent wristwatches as technical
statements). The detent's spiritual descendant in *robust* form is the
[co-axial](co-axial.md), which keeps the direct-push impulse while restoring
lever-grade safety.

## Constant force goes hand in hand

Detent chronometers are where the [remontoir](../anatomy/03-the-mainspring-and-barrel.md#constant-force-tricks)
shines: a tiny secondary spring rewound at intervals gives the escape wheel
constant torque regardless of the mainspring, so the free impulse is not just
frictionless but *consistent*. See the [comparison table](compared.md) for how
this scores against its rivals.

</content>
</file>

<file path="content/escapements/index.md">
<content>
---
title: "The Escapement Zoo"
description: "A tour of the escapement family tree: deadbeat, recoil, verge, cylinder, duplex, lever, co-axial, detent — and what each one believes about friction."
date: "2026-09-25"
author: "Buffy"
categories: ["escapements"]
tags: ["escapement", "guide", "history", "physics"]
---

Every escapement is a negotiated settlement between two parties: a power train
that wants to spin, and an oscillator that wants to be left alone. The family
tree below is organized by *what each design believes about friction*.

## The taxonomies that matter

Two axes sort almost everything:

**Impulse type.** Does the oscillator get its push while the escapement is
*locked* (friction during impulse — lever, cylinder) or while it is effectively
*free* (impulse delivered through a nearly frictionless path — detent,
co-axial)?

**Detachment.** Is the oscillator engaged with the train for the whole swing
(recoil, cylinder — always touching) or only for a fleeting moment (detached
lever, detent — free to oscillate undisturbed)? Detached escapements win on
rate stability because the oscillator spends most of its cycle alone.

## The family, roughly in order of appearance

| Escapement | Era | Belief about friction | Where it lives |
| --- | --- | --- | --- |
| [Verge and foliot](verge-and-foliot.md) | 1300s–1600s | accept it, overpower it | clocks, earliest watches |
| Recoil / deadbeat | 1600s– | recoil is fine (clocks) | tower clocks, regulators |
| [Cylinder](cylinder-and-duplex.md) | 1700s–1800s | minimize contact time | cheap watches, then pocket |
| Duplex | 1700s–1800s | separate lock and impulse | slender pocket watches |
| [Swiss lever](swiss-lever.md) | 1770–now | detach, impulse briefly | nearly every wristwatch |
| [Co-axial](co-axial.md) | 1974–now | never slide, only push | Omega, mostly |
| [Detent / chronometer](detent.md) | 1780s–now | impulse must be free | marine chronometers |

## What to read

- For the modern machine, nothing beats the
  [Swiss lever](swiss-lever.md) and its geometry page,
  [Drop, Lock, and Lift](swiss-lever/drop-lock-and-lift.md).
- For the philosophy of eliminating sliding friction,
  read [Co-axial](co-axial.md) against [Detent](detent.md) — two very different
  answers to the same complaint.
- For the historical arc from tower clocks to wrists, start with
  [Verge and foliot](verge-and-foliot.md) and end on the
  [comparison table](compared.md).

One more distinction worth internalizing: an escapement can be *accurate*,
*robust*, or *cheap to make*, and no design has ever been all three. The
[compared](compared.md) page scores the candidates openly.

</content>
</file>

<file path="content/escapements/swiss-lever.md">
<content>
---
title: "The Swiss Lever Escapement"
description: "The escapement in almost every mechanical watch since 1800: detached, self-starting, shock-tolerant — and the geometry that makes it all work."
date: "2026-09-27"
author: "Buffy"
categories: ["escapements"]
tags: ["escapement", "balance", "physics", "shock-protection"]
---

The **Swiss lever escapement** — the detached lever, the club-tooth lever — is
the most successful precision mechanism ever manufactured. It appears in
watches from $100 to $1,000,000, essentially unchanged since the mid-19th
century. Its genius is not raw accuracy ([detent](detent.md) escapements beat
it there) but *compromise*: accuracy good enough, robustness extraordinary.

## The three actors

1. **Escape wheel** — 15 teeth (almost always), each with a club-shaped tip:
   a locking corner and a curved impulse face.
2. **Pallet fork** — a lever with two ruby **pallet stones** (entry and exit),
   a fork with a slot and horn at one end, and a tail (the dart/safety pin).
3. **Balance staff** — carrying the **impulse jewel** (roller jewel) and the
   **safety roller** with its roller dart.

The fork's pivot sits between the wheel and the balance; the whole assembly is
"detached" — the balance touches the fork only during the brief unlock-and-impulse
window of each half-swing.

## One half-cycle, again in slow motion

1. **Locked.** A pallet stone rests against a wheel tooth. Draw (a slight
   locking-face angle) pulls the fork toward its banking pin — poised, not
   jammed. The balance swings free. (Mechanics detailed in
   [Drop, Lock, and Lift](swiss-lever/drop-lock-and-lift.md).)
2. **Unlock.** The returning impulse jewel enters the fork slot and pushes the
   fork aside.
3. **Impulse.** The tooth slides across the pallet stone's impulse plane while
   the fork's slot pushes the impulse jewel. Energy flows: train → balance.
4. **Drop.** The tooth slips off the stone to the next; the fork snaps to the
   opposite banking with a tiny audible knock.

Then mirror. Two impulses per period keep the
[amplitude](../physics/amplitude.md) alive.

## Why it conquered everything

- **Self-starting.** Stop the balance and a push on the crown's winding will
  get it going; detent escapements famously need a nudge.
- **Shock-tolerant.** The safety action (dart + safety roller) makes the
  escapement refuse to unlock *unless* impulse is actually coming — so a jar
  can't throw the fork across.
- **Manufacturable.** It forgives small geometry errors, tolerates oil (until
  it doesn't), and its parts are replaceable by the million.

## Its known weaknesses

Sliding friction during impulse pushes oil off the pallet surfaces and wears
them; the [lift geometry](swiss-lever/drop-lock-and-lift.md) is a permanent
trade-off between impulse efficiency and safety. This is exactly the complaint
that drove George Daniels to the [co-axial](co-axial.md) and keeps
[chronometer detents](detent.md) alive in marine instruments. But no rival has
matched its *accuracy per dollar per decade of service* — and so the tick you
hear tonight is the same tick a watchmaker heard in 1880.

</content>
</file>

<file path="content/escapements/swiss-lever/drop-lock-and-lift.md">
<content>
---
title: "Drop, Lock, and Lift"
description: "The geometry of the Swiss lever in three numbers watchmakers obsess over: drop (lost motion), lock (safety margin), and lift (the impulse gift)."
date: "2026-09-28"
author: "Buffy"
categories: ["escapements"]
tags: ["escapement", "physics", "lubrication", "service"]
---

*This is the deep-dive companion to [The Swiss Lever Escapement](../swiss-lever.md).*

Ask a watchmaker how the escapement is adjusted and you will hear three words:
**drop**, **lock**, and **lift**. They are angles and clearances measured in
hundredths of a millimeter, and they decide whether a watch runs for decades or
stops by lunch.

## Drop

**Drop** is the free fall of a tooth from one pallet stone to the next after
impulse — plus the corresponding drop across the fork at the balance end. Drop
must exist (otherwise the tooth would drag on the stone) but every bit of it is
*wasted motion*: the tooth falls and knocks, dissipating energy as sound and
heat.

- **Too much drop:** audible knocking, lost impulse, low amplitude.
- **Too little drop:** the tooth lands on the corner and drags — friction,
  then stoppage.

Watchmakers measure drop as the angle the escape wheel moves between "tooth
just leaving" and "tooth just landing." Healthy drop is a sliver.

## Lock

**Lock** is how deeply a tooth rests on a pallet stone when the escapement is at
rest. Lock serves the [safety action](../swiss-lever.md#why-it-conquered-everything):
it guarantees the fork stays pinned against its banking while the balance is
detached.

- Lock depth is set by the pallet stones' radial position and the fork's horn.
- **Draw** — the locking face's slight angle, plus the fork's banking spring
  bias — pulls the fork against the banking pin instead of letting it float.
- **Insufficient lock + no draw** = the classic "trip": a jar throws the fork
  to mid-stroke and the watch double-unlocks, momentarily running wild.
- **Excessive lock** = heavy unlocking friction, low amplitude, rate
  sensitivity to position.

Lock is checked with a special gauge or by eye and feel at the bench — the
tooth must rest *on* the face, not at its edge.

## Lift

**Lift** is the impulse gift: the combined angles of the pallet stone's impulse
plane and the fork slot / impulse jewel geometry that translate the train's
torque into the balance's swing. The **lift angle** (typically 45–52° total,
movement-specific) is what a timegrapher needs as an input to compute
[amplitude](../../physics/amplitude.md) correctly.

Lift trades against safety:

| More lift | Less lift |
| --- | --- |
| bigger impulse, higher amplitude | less unlocking friction |
| more sliding friction per impulse | lower amplitude, more positional variance |
| faster pallet wear | less pallet wear |

There is no free optimum; there is only the movement's design point — and oil.
Impulse surfaces are oiled with microscopic amounts of light oil (and
epilame-treated so it stays), because sliding friction is only tolerable when
cushioned. When the oil migrates away — see
[Friction and Lubrication](../../physics/friction-and-lubrication.md) — the
rate sags and the watch joins the service queue.

## The three numbers together

A healthy escapement: drop barely audible, lock firm but not deep, lift angle
as designed, amplitude 260–310° in dial-up. That signature on a timegrapher —
two clean, parallel lines — is the sound of three hundred years of geometry
behaving itself.

</content>
</file>

<file path="content/escapements/verge-and-foliot.md">
<content>
---
title: "Verge and Foliot"
description: "The first mechanical escapement, 1300s–1600s: a crown wheel, a verge, and a foliot bar — crude, brilliant, and losing minutes a day."
date: "2026-09-25"
author: "Buffy"
categories: ["escapements"]
tags: ["escapement", "history", "timeline"]
---

The **verge escapement** is the founding hack of mechanical horology, appearing
in European clocks around the 13th century (the exact origin is debated; the
first unambiguous references cluster in the 1270s–1300s). It made mechanical
timekeeping possible at all — and was so crude that a good tower clock might
drift 15–30 minutes *per day*.

## The mechanism

- A vertical **verge** (rod) with two **pallets** (flags) set at right angles
  to each other.
- A **crown wheel** — a wheel with sawtooth-shaped teeth facing outward like a
  crown — whose teeth alternately push one pallet, then the other.
- A **foliot** — a horizontal bar with adjustable weights — mounted on the
  verge, rocking back and forth.

Each swing of the foliot lets the crown wheel advance one tooth; the tooth's
push also pays back the foliot's losses. The beat is set by sliding the
weights: heavier or wider means slower. The period depends on *how hard the
escapement pushes* — the defining flaw.

## Why it is inaccurate

The verge's period depends on driving torque and on friction, so the going
rate varies with the mainspring's state, temperature, wear, and lubrication.
There is no real detachment: pallets rub the teeth almost continuously. This
is the [isochronism problem](../physics/isochronism.md) in its rawest form.

Yet it worked — for three centuries, well enough to schedule monasteries,
factories, and ships' watches.

## What replaced it

- The **anchor escapement** (1670s, attributed to Robert Hooke/William Clement)
  for [pendulum clocks](../history/1656-huygens-and-the-pendulum.md), where the
  pendulum's own regularity could dominate.
- The **cylinder** and later the **lever** for watches, which needed to work
  without gravity's help — see [Cylinder and Duplex](cylinder-and-duplex.md)
  and the [Swiss lever](swiss-lever.md).

The verge's real legacy is the *concept*: release an oscillator one tooth at a
time, and pay it back with the same stroke. Everything on this site is
commentary on that idea.

</content>
</file>

<file path="content/glossary/glossary.md">
<content>
---
title: "Glossary"
description: "An A-Z of horological terms used across Escapement: amplitude to vph, with links to the pages that explain each one properly."
date: "2026-09-30"
author: "Buffy"
categories: ["glossary"]
tags: ["guide", "glossary", "escapement", "balance", "physics"]
---

The vocabulary of horology is French-inflected and unapologetic. This glossary
covers the terms this site uses, with links to the full treatment.

**Amplitude** — degrees the balance swings per beat; the watch's vital sign.
→ [Amplitude](../physics/amplitude.md)

**Balance wheel** — weighted wheel on a staff; with the hairspring, the
oscillator. → [The Balance Assembly](../anatomy/05-the-balance-assembly.md)

**Barrel** — drum holding the mainspring; often the train's first wheel.
→ [The Mainspring and Barrel](../anatomy/03-the-mainspring-and-barrel.md)

**Beat** — one half-oscillation; "vibrations per hour" counts beats.
→ [Frequency](../physics/frequency.md)

**BPH / vph** — beats (vibrations) per hour: 18,000 / 21,600 / 28,800 / 36,000.
→ [Frequency](../physics/frequency.md)

**Calibre** — a movement architecture/designation.
→ [How to Read a Calibre](../movements/index.md)

**Cannon pinion** — friction-fit pinion driving the motion works.
→ [The Motion Works and Dial](../anatomy/07-the-motion-works-and-dial.md)

**Chronograph** — stopwatch mechanism integrated in a watch.
→ [The Chronograph](../complications/chronograph.md)

**Column wheel** — turret controlling chronograph levers.
→ [Column wheel vs cam](../complications/chronograph.md#column-wheel-vs-cam)

**Complication** — any function beyond hours/minutes/seconds.
→ [What Counts as a Complication](../complications/index.md)

**COSC** — Swiss chronometer certification (−4/+6 s/day).
→ [Positions and Rate](../physics/positions-and-rate.md)

**Detent escapement** — chronometer escapement; direct impulse, high accuracy.
→ [The Detent Escapement](../escapements/detent.md)

**Drop** — free fall of an escape tooth between pallets.
→ [Drop, Lock, and Lift](../escapements/swiss-lever/drop-lock-and-lift.md)

**Endshake / sideshake** — axial/radial play of a wheel in its settings.

**Epilame** — surface treatment holding oil in place.
→ [Friction and Lubrication](../physics/friction-and-lubrication.md)

**Escape wheel** — the train's last wheel; drives the escapement.
→ [The Swiss Lever Escapement](../escapements/swiss-lever.md)

**Fusee** — cone pulley equalizing mainspring torque.
→ [Constant-force tricks](../anatomy/03-the-mainspring-and-barrel.md#constant-force-tricks)

**Gear train** — barrel to escape wheel; ratio and power transport.
→ [The Gear Train](../anatomy/02-the-gear-train.md)

**Hairspring / balance spring** — the oscillator's spring.
→ [The Balance Spring](../physics/the-balance-spring.md)

**Isochronism** — constant period across amplitudes.
→ [Isochronism](../physics/isochronism.md)

**Jewels** — synthetic ruby bearings; friction and wear control.
→ [Friction and Lubrication](../physics/friction-and-lubrication.md)

**Keyless works** — winding/setting mechanism at the crown.
→ [The Keyless Works](../anatomy/06-the-keyless-works.md)

**Lift angle** — geometry used to compute amplitude; movement-specific.
→ [Lift](../escapements/swiss-lever/drop-lock-and-lift.md#lift)

**Lock** — engagement depth of an escape tooth on a pallet.
→ [Drop, Lock, and Lift](../escapements/swiss-lever/drop-lock-and-lift.md)

**Lever escapement** — the standard detached wristwatch escapement.
→ [The Swiss Lever Escapement](../escapements/swiss-lever.md)

**Mainspring** — the watch's spring battery.
→ [The Mainspring and Barrel](../anatomy/03-the-mainspring-and-barrel.md)

**Minute repeater** — strikes hours, quarters, minutes on demand.
→ [The Minute Repeater](../complications/minute-repeater.md)

**Moonphase** — lunar phase display, 59-tooth or better.
→ [The Moonphase](../complications/moonphase.md)

**Perpetual calendar (QP)** — calendar with leap-year memory.
→ [The Perpetual Calendar](../complications/perpetual-calendar.md)

**Power reserve** — stored run time; also the gauge showing it.
→ [Power Reserve](../complications/power-reserve.md)

**Rate** — seconds per day, fast (+) or slow (−).
→ [Positions and Rate](../physics/positions-and-rate.md)

**Remontoir** — small constant-force spring re-wound at intervals.
→ [Constant-force tricks](../anatomy/03-the-mainspring-and-barrel.md#constant-force-tricks)

**Shock setting** — spring-mounted balance jewel (Incabloc etc.).
→ [Shock settings](../physics/friction-and-lubrication.md#shock-settings)

**Tourbillon** — rotating cage averaging positional error.
→ [The Tourbillon](../complications/tourbillon.md)

**vph** — vibrations per hour (see BPH).
→ [Frequency](../physics/frequency.md)

**Going barrel** — barrel that is also the first train wheel.
→ [The Mainspring and Barrel](../anatomy/03-the-mainspring-and-barrel.md)

</content>
</file>

<file path="content/history/1656-huygens-and-the-pendulum.md">
<content>
---
title: "1656 — Huygens and the Pendulum"
description: "Christiaan Huygens, Salomon Coster, and the invention that made accurate clocks possible: swinging a weight on a rod and letting physics do the rest."
date: "2026-09-24"
author: "Buffy"
categories: ["history"]
tags: ["history", "timeline", "physics"]
---

In 1656, the Dutch mathematician **Christiaan Huygens** — working with the
craftsman **Salomon Coster** in The Hague — built the first practical
**pendulum clock**. Within a few years, clock accuracy leaped from a quarter
of an hour per day to *seconds* per day. Nothing else in horology's history
moved the needle so far, so fast.

## Why a pendulum works

Galileo had noticed (c. 1602, and famously apocryphal-lamp-story aside) that a
pendulum's swing takes nearly the same time whether the arc is wide or narrow
— the property of [isochronism](../physics/isochronism.md). A pendulum of
fixed length has a fixed period. Huygens' contribution was engineering plus
mathematics: he designed the clock's [escapement](../escapements/verge-and-foliot.md)
(crown wheel and verge, refined), the suspension, and — critically — the
**cycloidal cheek** insight (published in *Horologium Oscillatorium*, 1673)
that a pendulum swinging between cycloidal curves is *perfectly* isochronous,
not just approximately.

## What changed

Before 1656, the best clocks (verge and foliot) drifted 15+ minutes a day and
needed daily correction against a sundial. After, the good ones drifted
seconds. The consequences cascaded:

- **Astronomy** — observatories could time star transits precisely.
- **Navigation** — the longitude problem became a *clock* problem, setting up
  [Harrison's century](1761-harrison-and-the-longitude-prize.md).
- **Society** — schedules, factories, and railway timetables eventually
  demanded that everyone own the accuracy observatories were perfecting.

## The watch problem Huygens couldn't solve

A pendulum needs gravity and stillness; it cannot live in a pocket. Huygens
tried **balance springs** for watches — and by 1675 had one working, launching
[the priority war](1675-the-balance-spring-race.md). The pendulum clock would
rule towers and desks for three centuries; the balance-and-spring watch would
take the rest of life.

*Next in the archive: [1675 — The Balance-Spring Race](1675-the-balance-spring-race.md).*

</content>
</file>

<file path="content/history/1675-the-balance-spring-race.md">
<content>
---
title: "1675 — The Balance-Spring Race"
description: "Hooke, Huygens, and Hautefeuille claim the invention that made watches accurate — the first great priority scandal in science."
date: "2026-09-24"
author: "Buffy"
categories: ["history"]
tags: ["history", "timeline", "balance-spring"]
---

Within months of each other, three men claimed the invention that transformed
watches from hour-markers into timekeepers: the **balance spring**. The row
that followed is the template for every priority dispute since.

## The claims

- **Christiaan Huygens** — demonstrated a working spiral-spring balance watch
  in The Hague in March 1675 and announced it to the Royal Society and the
  Académie des Sciences. First *demonstrated, published, working* design.
- **Robert Hooke** — claimed the idea dated to his spring-clock work of the
  1660s ("the true plain law of the spring," 1666), and that Huygens had taken
  the principle from his published hints. Hooke had the physics; he did not
  ship the device.
- **Jean de Hautefeuille** — published his own claim in 1675 (a bowed-spring
  design), never really in the running but forever in the footnotes.

## Why the spring is the whole ballgame

As covered in [The Balance Spring](../physics/the-balance-spring.md), coupling
the balance to a spring makes its period a property of the *system* — that's
[isochronism](../physics/isochronism.md) — instead of a function of how hard
it was pushed. Accuracy improved from ~15 minutes a day to under 5 *seconds* a
day within decades.

## What the fight teaches

Hooke was arguably first with the principle; Huygens was first with the
product. History honors both, and the watch world ended up with Huygens'
spiral geometry and, a century later, [Breguet's overcoil](../physics/the-balance-spring.md#geometry-the-fight-against-the-spring-itself)
and [Phillips' curves](../physics/the-balance-spring.md#geometry-the-fight-against-the-spring-itself).
The pattern repeats across this archive: the invention matters less than the
*engineering of it into a manufacturable object* — the same lesson as
[Mudge's lever](1770-mudge-and-the-lever.md), the same lesson as
[the American system](1850s-the-american-system.md).

*Archive: [1656](1656-huygens-and-the-pendulum.md) ← here →
[1761](1761-harrison-and-the-longitude-prize.md).*

</content>
</file>

<file path="content/history/1761-harrison-and-the-longitude-prize.md">
<content>
---
title: "1761 — Harrison and the Longitude Prize"
description: "A Yorkshire carpenter's clocks take on the astronomers, the Board of Longitude, and the sea itself — and win the prize for timekeeping."
date: "2026-09-25"
author: "Buffy"
categories: ["history"]
tags: ["history", "timeline", "accuracy"]
---

Longitude at sea was lethal: you could find latitude from the stars, but not
your east-west position. The **Longitude Act of 1714** offered up to **£20,000**
for a method accurate to half a degree. The astronomers bet on the moon's
position; **John Harrison**, a self-taught Yorkshire carpenter, bet on a
clock.

## The H series

- **H1 (1735)** — a huge, ingenious sea clock with counterbalanced springs;
  performed well on a Lisbon voyage.
- **H2, H3** — years of refinement: bimetallic compensation, the grasshopper
  escapement concept, the caged roller bearing. Harrison obsessed over
  [isochronism](../physics/isochronism.md) before the vocabulary settled.
- **H4 (1761)** — a large *watch* (five inches), essentially a giant
  [lever-era](1770-mudge-and-the-lever.md) precursor with a fast-beat balance
  and a [fusee](../anatomy/03-the-mainspring-and-barrel.md#constant-force-tricks).
  Carried by Harrison's son William to Jamaica in 1761: it lost about **5
  seconds on the 81-day voyage** — roughly 1/3 of the longitude prize's
  tolerance, and orders better than the lunar method.

## The asterisk

The Board of Longitude, stacked with astronomers, demanded more trials and
more proof; Harrison got partial payments and years of humiliation before
Parliament forced full payment in 1773. The practical win went to the
watchmakers who *manufactured* the idea: **Larcum Kendall's K1** (a superb H4
copy) sailed with Cook, and the marine chronometer industry — Arnold,
Earnshaw, the [detent escapement](../escapements/detent.md) tradition — turned
Harrison's proof into a product.

## Why it matters

Harrison showed that **a good oscillator plus constant force beats astronomy**
for a working problem. The chain from here runs straight through the 19th
century's [lever watches](1770-mudge-and-the-lever.md), the observatory
chronometer culture, and the modern obsession with
[certification](../physics/positions-and-rate.md). Navigation's deadliest
problem was solved by a carpenter and a [mainspring](../anatomy/03-the-mainspring-and-barrel.md).

*Archive: [1675](1675-the-balance-spring-race.md) ← here →
[1770](1770-mudge-and-the-lever.md).*

</content>
</file>

<file path="content/history/1770-mudge-and-the-lever.md">
<content>
---
title: "1770 — Mudge and the Lever"
description: "Thomas Mudge builds the first lever escapement watch — and the world takes fifty years to notice."
date: "2026-09-25"
author: "Buffy"
categories: ["history"]
tags: ["history", "timeline", "escapement"]
---

In 1770, **Thomas Mudge** — London's finest watchmaker, student of George
Graham — built a watch for Queen Charlotte containing a new escapement: a
pallet fork with stones, an escape wheel, a balance. The **lever escapement**:
the machine inside essentially every watch worn today
([described here](../escapements/swiss-lever.md)).

## What Mudge invented

A *detached* lever: the balance oscillates free of the train except for the
brief [unlock-and-impulse](../escapements/swiss-lever/drop-lock-and-lift.md)
window each half-swing. Compared with the [cylinder](../escapements/cylinder-and-duplex.md)
and [verge](../escapements/verge-and-foliot.md) escapements then current, it
was cleaner, more isochronous, and — crucially — better suited to adjustment.

## Why it took fifty years

Mudge built few watches; his lever was fiddly and the era's manufacturing
couldn't reproduce its geometry cheaply. The 1780s-1820s refined it: Josiah
Emery made improved levers; Peter Litherland patented the rack lever (1791);
the modern **club-tooth, detached, jeweled lever** coalesced in English
workshops by the 1820s-30s. Mass production would arrive via
[America](1850s-the-american-system.md) and Switzerland.

## The pattern again

Invention ≠ product. The archive keeps showing the gap:
[Huygens' spring](1675-the-balance-spring-race.md) needed Breguet and Phillips
to be *right*; [Harrison's chronometer](1761-harrison-and-the-longitude-prize.md)
needed Kendall to be *repeatable*; Mudge's lever needed the industrial century
to be *cheap*. By the time it was cheap, it had conquered everything — and it
has held the wrist ever since, only seriously threatened by
[quartz](1969-the-quartz-crisis.md) on price and the
[co-axial](../escapements/co-axial.md) on philosophy.

*Archive: [1761](1761-harrison-and-the-longitude-prize.md) ← here →
[1850s](1850s-the-american-system.md).*

</content>
</file>

<file path="content/history/1850s-the-american-system.md">
<content>
---
title: "1850s — The American System"
description: "Waltham, Elgin, and interchangeable parts: the decade the watch stopped being a craft object and became an industrial one."
date: "2026-09-26"
author: "Buffy"
categories: ["history"]
tags: ["history", "timeline", "industrialization", "gear-train"]
---

In 1850s Waltham, Massachusetts, the **American Waltham Watch Company**
(founded 1850-51 as the Boston Watch Company, reorganized 1854) applied the
American system of manufactures — machine tools, gauges, **interchangeable
parts**, division of labor — to the watch. The result: reliable watches at
prices Europe's bench system couldn't touch.

## What changed at the bench

Traditionally, a watch was *made*: a craftsman filed each part to fit. At
Waltham (and then Elgin, 1864; Illinois; Hampden; the whole Rockford/Elgin
corridor):

- Lathes, gear cutters, and jig-fitted presses made identical parts.
- Gauge systems ("Waltham gauge") ensured part-to-part fit across machines.
- Rough, semi-finished, and finished work separated into departments.
- Mass-produced [lever escapements](../escapements/swiss-lever.md) —
  adjustable by anyone trained on the standard.

The **"Dollar Watch"** era (Ingersoll's $1 pocket watch, 1890s, using
Columbus/other cheap movements) completed the democratization.

## The transatlantic shock

America briefly out-produced and out-engineered Switzerland in quantity
watches; Swiss makers visited and copied the methods (the "Americanization" of
the Swiss industry in the 1870s-90s). Quality mythology insists hand-made was
better — the market said otherwise for a century.

## Why it matters to the machine

Interchangeability is what makes [service](../maintenance/servicing.md)
possible at scale: a broken escape wheel is a part number, not a commission.
The [gear trains](../anatomy/02-the-gear-train.md) on this site are all
dimensioned for the same interchange principle. And the industry's center of
gravity would next move twice more — to Switzerland's luxury recovery, then to
[quartz](1969-the-quartz-crisis.md) Japan — always following whoever married
precision to production.

*Archive: [1770](1770-mudge-and-the-lever.md) ← here →
[1927](1927-the-quartz-clock.md).*

</content>
</file>

<file path="content/history/1927-the-quartz-clock.md">
<content>
---
title: "1927 — The Quartz Clock"
description: "Warren Marrison at Bell Labs builds the first quartz clock — and the mechanical watch starts a forty-year countdown it doesn't know about yet."
date: "2026-09-26"
author: "Buffy"
categories: ["history"]
tags: ["history", "timeline", "quartz", "frequency"]
---

In 1927, **Warren Marrison** and J.W. Horton at Bell Telephone Laboratories
built the first **quartz crystal clock**: a quartz crystal oscillator driving
an electric counting circuit. It was immediately more accurate than any
[pendulum](1656-huygens-and-the-pendulum.md) or [balance](../physics/the-balance-spring.md)
— because a quartz crystal's vibration is both *fast* (tens of thousands of
cycles per second) and extraordinarily stable.

## Why quartz wins at physics

Accuracy improves with oscillator frequency and stability: a
[32,768 Hz](../physics/frequency.md#quartz-and-the-joke) crystal counts
itself 32,768 times a second and barely drifts with temperature or position.
Split the signal down with a digital divider and you get one-second pulses
with error measured in seconds per *month* (wrist) or *year* (lab).

Quartz clocks took over observatories and broadcasting in the 1930s-40s; the
**atomic clock** (1949, NIST/USNO lineage) would later beat quartz, but the
mechanical watch had already lost the accuracy war in principle.

## The wrist problem

For decades quartz clocks were desk-sized apparatus with vacuum tubes. Shrinking
one to a wrist took three more decades: the race between Seiko (Suwa Seikosha),
the Swiss consortium (the **Beta** projects), and American firms ended at
Christmas 1969 with the **Seiko Astron 35SQ** — the first quartz wristwatch,
¥450,000 in gold, about ±5 seconds a *month*. The [crisis](1969-the-quartz-crisis.md)
that followed was industrial history on fast-forward.

## The irony

Quartz is why you can own perfect time for the price of a sandwich — and why
the mechanical watch survived only by changing what it sells: not accuracy,
but [craft](../complications/tourbillon.md), heritage, and the visible
argument of [wheels and springs](../start-here/the-five-minute-watch.md).

*Archive: [1850s](1850s-the-american-system.md) ← here →
[1969](1969-the-quartz-crisis.md).*

</content>
</file>

<file path="content/history/1969-the-quartz-crisis.md">
<content>
---
title: "1969 — The Quartz Crisis"
description: "The Astron, the Beta race, and the collapse of Swiss watchmaking: the decade the mechanical watch stopped being an instrument."
date: "2026-09-27"
author: "Buffy"
categories: ["history"]
tags: ["history", "timeline", "quartz", "industrialization"]
---

On Christmas Day 1969, Seiko sold the **Astron 35SQ** — the first quartz
wristwatch — in a gold case for the price of a car. Within fifteen years, the
Swiss watch industry had lost most of its workforce and nearly its existence.
The episode is called the **quartz crisis** in Switzerland and the **quartz
revolution** in Japan. Both names are accurate.

## The race

- **Seiko** (Suwa Seikosha) — the Astron used a hybrid circuit and a
  tuning-fork-adjacent stepper; ~±5 seconds/month accuracy.
- **The Swiss Beta consortium** (CEH/CSEM and partners) — the **Beta 21**
  arrived in 1970-71 in several high-end watches (Girard-Perregaux,
  Rolex's Datejust 5100 "Texano", Patek, Piaget). Swiss quartz was superb and
  *second*.
- **American and Japanese volume** — Texas Instruments, Timex, Casio, and the
  whole digital/analog quartz avalanche turned accurate time into a commodity.

## The numbers

Swiss watch-industry employment collapsed — commonly cited figures run from
roughly 90,000 employees around 1970 to under 30,000 by the mid-1980s.
Export unit volumes flipped from mechanical to quartz almost completely.
Workshops that had taken generations to build were liquidated; tooling went to
[the people who hid it](../movements/zenith-el-primero.md#the-1969-race) or
the people who scrapped it.

## What died and what didn't

What died: the watch as *instrument*. If a $20 quartz keeps better time than
a $20,000 chronometer, mechanical watches could no longer be sold on accuracy.
What survived: the watch as *argument* — craft, [complications](../complications/index.md),
[finishing](../movements/index.md), and history. The
[El Primero's](../movements/zenith-el-primero.md) hidden tooling, the marine
chronometer tradition, [George Daniels'](../escapements/co-axial.md) lonely
work — these became the seeds of the revival
[Swatch](1983-the-swatch-rescue.md) engineered.

The crisis is why this entire site can exist: nobody writes exhaustive guides
to instruments that won. They write them about objects that *mean* something.

*Archive: [1927](1927-the-quartz-clock.md) ← here →
[1983](1983-the-swatch-rescue.md).*

</content>
</file>

<file path="content/history/1983-the-swatch-rescue.md">
<content>
---
title: "1983 — The Swatch Rescue"
description: "Nicolas Hayek, 51 parts, and the bet that saved Swiss horology: sell quartz cheap, sell mechanical expensive, and sell both as identity."
date: "2026-09-28"
author: "Buffy"
categories: ["history"]
tags: ["history", "timeline", "industrialization", "quartz"]
---

In 1983 the **Swatch** — Swiss watch, quartz, plastic, ~51 parts, welded
case, ultrasonic assembly — went on sale. It was the visible face of a rescue
operation: the merger of the dying giants **ASUAG** and **SSIH** (1983,
renamed **SMH**, later the Swatch Group) engineered by consultant
**Nicolas Hayek**. It worked so well that it's now the industry's structure.

## The two-part bet

1. **Own the bottom.** The Swatch beat the Japanese at their own game by
   *reducing parts and automating assembly* — not by making better quartz, but
   by making quartz a fashion object: cheap enough to collect, branded enough
   to want. Volume cash flow saved the industrial base.
2. **Own the top.** Hayek bet that mechanical watches would return as *luxury
   argument* — heritage, [craft](../complications/tourbillon.md), and status —
   and bought/protected the brands that carried it: Omega, Blancpain ("since
   1735, never made a quartz watch" — an ad campaign as strategy), Breguet
   (acquired 1999), and the machine-tool firms (ETA, Nivarox) that made
   mechanical production possible again.

## What the modern industry is

Today's structure is Hayek's: a few conglomerates (Swatch Group, Richemont,
LVMH, Rolex/Fossil independents) selling
[certified mechanics](../physics/positions-and-rate.md) above, fashion quartz
below, and [manufacture calibres](../movements/index.md) as vertical
integration. The mechanical revival of the 1990s-2000s — [co-axial
commercialization](../escapements/co-axial.md), the [El Primero's](../movements/zenith-el-primero.md)
return to prestige, the [tourbillon](../complications/tourbillon.md) boom —
all follows from the decision that mechanical watches would *never again* be
sold as instruments.

## The archive's argument complete

[Huygens](1656-huygens-and-the-pendulum.md) made timekeeping scientific;
[Harrison](1761-harrison-and-the-longitude-prize.md) made it practical;
[Mudge](1770-mudge-and-the-lever.md) and [the Americans](1850s-the-american-system.md)
made it cheap; [quartz](1927-the-quartz-clock.md) made it perfect; Swatch made
it *personal*. The machine on your wrist is a better story than it is a clock —
and this site exists to tell both.

*Archive: [1969](1969-the-quartz-crisis.md) ← here → back to the
[Timeline](index.md).*

</content>
</file>

<file path="content/history/index.md">
<content>
---
title: "A Timeline of Timekeeping"
description: "From Huygens' pendulum to the Swatch rescue: the chronological archive of how the mechanical watch was invented, perfected, nearly killed, and reborn."
date: "2026-09-24"
author: "Buffy"
categories: ["history"]
tags: ["history", "timeline", "guide"]
---

This is the site's chronological archive — one entry per turning point, in
order. Each entry is a self-contained story; together they are the argument
that the mechanical watch is a *cultural* survivor, not a technical accident.

## The archive

1. **[1656 — Huygens and the Pendulum](1656-huygens-and-the-pendulum.md)** —
   clocks learn to swing; timekeeping accuracy jumps 100-fold.
2. **[1675 — The Balance-Spring Race](1675-the-balance-spring-race.md)** —
   watches get their oscillator; Hooke and Huygens start a fight.
3. **[1761 — Harrison and the Longitude Prize](1761-harrison-and-the-longitude-prize.md)** —
   a carpenter's clock beats the astronomers and saves the fleet.
4. **[1770 — Mudge and the Lever](1770-mudge-and-the-lever.md)** — the
   escapement that wins the future is invented and ignored for decades.
5. **[1850s — The American System](1850s-the-american-system.md)** —
   interchangeable parts, machine tools, and the watch becomes an industrial
   object.
6. **[1927 — The Quartz Clock](1927-the-quartz-clock.md)** — the crystal
   arrives in the laboratory and starts the long countdown.
7. **[1969 — The Quartz Crisis](1969-the-quartz-crisis.md)** — Seiko's Astron,
   the Swiss collapse, and the moment watches stopped being instruments.
8. **[1983 — The Swatch Rescue](1983-the-swatch-rescue.md)** — Hayek bets on
   plastic and emotion; mechanical returns as luxury argument.

## How to read it

Forward for the story of progress; backward for the story of survival. The
ending — a market where [quartz](../physics/frequency.md#quartz-and-the-joke)
keeps perfect time for $10 and mechanical watches sell for fortunes — is only
contradictory until you read [Tourbillon](../complications/tourbillon.md) and
realize the craft changed what it was selling.

The whole site cross-links here: every technical page (the
[Anatomy series](../start-here/read-me-first.md#path-1--the-machinist-8-parts-90-minutes),
the [escapements](../escapements/index.md)) has a chronological ancestor in
this archive.

</content>
</file>

<file path="content/index.md">
<content>
---
title: "Escapement — How a Mechanical Watch Actually Works"
description: "An exhaustive, illustrated guide to the machine that lives on your wrist: gear trains, escapements, balance springs, complications, and the history that produced them."
date: "2026-09-30"
author: "Buffy"
categories: ["orientation"]
tags: ["escapement", "guide", "series-anatomy", "timeline"]
---

A mechanical watch is the most successful machine humanity has ever mass-produced:
hundreds of tiny parts, assembled to tolerances of microns, running unattended for
decades on nothing but a wound spring. And almost nobody can explain what the parts
actually *do*.

**Escapement** is one long attempt to fix that. No marketing language, no
"Swiss magic" hand-waving — just the machine, part by part, physics first.

## Where to begin

- **You want to understand the machine.** Start the eight-part series:
  [The Problem of Timekeeping](anatomy/01-the-problem-of-timekeeping.md) and keep
  going to [Putting It Together](anatomy/08-putting-it-together.md). Each part
  builds on the last.
- **You just want the good stuff.** Jump to the heart of the machine:
  [The Swiss Lever Escapement](escapements/swiss-lever.md), then
  [Amplitude](physics/amplitude.md) — the number that tells you if a watch is healthy.
- **You care about the story.** The [Timeline](history/index.md) runs from Huygens'
  pendulum to the quartz crisis, one entry at a time.
- **You are deciding what to buy or service.** [Maintenance](maintenance/servicing.md)
  and the [Glossary](glossary/glossary.md) are the practical corner.

## The claims this site will defend

1. The escapement is not "the heart" — it is the *referee*. The
   [balance assembly](anatomy/05-the-balance-assembly.md) keeps time; the
   escapement just lets it count itself.
2. Rate is not accuracy. [Positions, temperature, and amplitude](physics/positions-and-rate.md)
   move a watch's rate around all day; "accuracy" is an average of that mess.
3. Almost every "complication" is a clever way to *count* something —
   the [chronograph](complications/chronograph.md) counts elapsed seconds, the
   [perpetual calendar](complications/perpetual-calendar.md) counts leap years.
4. The [quartz crisis](history/1969-the-quartz-crisis.md) was not the death of
   mechanical watches. It was the event that turned them from instruments into
   arguments — and the arguments are more interesting than the instruments were.

Every page cross-links into the rest of the site; the
[Knowledge Graph](/graph/) view generated for this build shows just how tangled
the machine really is. Curious how it's made? See the
[About & Colophon](about.md). Welcome — mind the tweezers.

</content>
</file>

<file path="content/maintenance/magnetism.md">
<content>
---
title: "Magnetism"
description: "The most common modern watch problem and the cheapest to fix: what magnetic fields do to hairsprings, how to test, and how to demagnetize."
date: "2026-09-29"
author: "Buffy"
categories: ["maintenance"]
tags: ["magnetism", "service", "balance-spring", "guide"]
---

A magnetized watch is the great masquerader: it can gain minutes a day, stop,
restart, and behave like a dying movement — and the fix takes ten seconds with
a $15 tool.

## What actually happens

The [balance spring](../physics/the-balance-spring.md) is a coiled spring; if
it becomes magnetized, adjacent turns cling together. Effective spring length
shortens, the [balance](../anatomy/05-the-balance-assembly.md) oscillates
faster — sometimes *much* faster (minutes a day) — and coils may visibly clump.
Steel parts (hairsprings in older watches, some screws) are the victims;
[Nivarox](../physics/the-balance-spring.md#materials-steel-nivarox-silicon)
alloys resist but aren't immune; **silicon** springs (Si14, Syloxi, Spiromax)
are effectively immune.

## Where the fields live

Laptops and tablet covers (magnetic clasps), handbag snaps, speakers,
headphones, magnetic phone mounts, refrigerator magnets, airport scanner
tables, some travel pillows. You don't need an industrial magnet — the
ubiquity of small permanent magnets in modern life is the whole story.

## The fix

**Demagnetization:** pass the watch through a strong alternating field that
decays to zero (the classic blue demagnetizer gadget, or a watchmaker's
demag unit). It takes seconds and costs almost nothing. If the watch returns
to normal rate afterward, that was the problem.

**Prevention:** keep distance from magnetic closures and speakers; choose
[movements](../movements/index.md) with modern springs if your life is
magnetic (Omega Master Chronometer pieces are certified to 15,000 gauss;
Rolex Parachrom, silicon-spring ETA/Sellita variants, and Seiko's modern
springs all resist strongly).

## What magnetism is not

It is not permanent damage (in steel-spring watches it's reversible), it is
not "battery" (there is no battery), and it does not need a service — unless
you've had the watch magnetized repeatedly and something else is worn. Test
with a cheap compass or a phone app first; [service](servicing.md) second.
See also [Friction and Lubrication](../physics/friction-and-lubrication.md)
for the failure it imitates.

</content>
</file>

<file path="content/maintenance/servicing.md">
<content>
---
title: "Servicing"
description: "What a service actually includes, when to schedule one, what it should cost in principle — and the failure signs that can't wait."
date: "2026-09-29"
author: "Buffy"
categories: ["maintenance"]
tags: ["service", "lubrication", "guide", "accuracy"]
---

A watch service is mostly a **cleaning and re-lubrication** job with an
inspection attached. Understanding that frame makes every service decision
easier.

## What happens at a service

1. **Case opening and movement removal**, hands and dial off.
2. **Full disassembly** in the [service order](../anatomy/08-putting-it-together.md).
3. **Ultrasonic cleaning** of every part, inspection for wear under
   magnification.
4. **Reassembly with fresh oils** — the actual substance of the job, per the
   [lubrication schedule](../physics/friction-and-lubrication.md#the-oil-schedule).
5. **Gaskets, casing, and pressure test** ([water resistance](water-resistance.md)).
6. **Timing and regulation** in positions ([what healthy looks like](../physics/amplitude.md)).

Wear parts (mainspring, winding wheels, seconds hand cannon pinions, cracked
jewels) are replaced as found.

## When to service

There is no universal number; the interval is really an *oil life* estimate:

- **Modern, daily-worn:** every 5-8 years is the common guidance; many makers
  now say 8-10 with modern oils. Judge by [amplitude](../physics/amplitude.md)
  and rate drift, not the calendar.
- **Vintage, occasional wear:** oils dry out whether worn or not; 4-5 years if
  you actually wear it.
- **Water-use watches:** gasket check annually, service on schedule — salt
  water is a countdown timer.

## Signs it's overdue

- Rate drifting steadily (±15 s/day and growing) — see
  [Positions and Rate](../physics/positions-and-rate.md).
- [Amplitude](../physics/amplitude.md) below 220° dial up on full wind.
- Winding gritty or uneven; rotor noisy in an automatic.
- Any moisture under the crystal. Stop wearing it.

## What service is not

It is not a "tune-up" of magic accuracy: regulation adjusts the compromise,
it doesn't rebuild worn pivots. It is not optional for water-use. And it is
never "just oil the outside" — external oiling destroys movements.

Cost scales with complication count ([repeater](../complications/minute-repeater.md)
services are a specialty), parts scarcity (vintage), and case construction.
The [keyless works](../anatomy/06-the-keyless-works.md) and calendar works add
hours; the [chronograph](../complications/chronograph.md) adds levers. Budget
for it as ownership cost, like tires.

</content>
</file>

<file path="content/maintenance/water-resistance.md">
<content>
---
title: "Water Resistance"
description: "What 30m, 100m, and 200m actually mean, why depth ratings lie about swimming, and how gaskets age you out of the pool."
date: "2026-09-30"
author: "Buffy"
categories: ["maintenance"]
tags: ["water-resistance", "service", "guide", "keyless-works"]
---

Depth ratings on watch dials are among the most misunderstood numbers in
consumer products. **30 m does not mean you can dive to 30 m.** Here is what
the numbers mean and what actually keeps water out.

## The rating table (ISO 22810 convention)

| Marking | Means | Actually OK for |
| --- | --- | --- |
| 3 ATM / 30 m | splash resistant | rain, hand washing |
| 5 ATM / 50 m | brief immersion | swimming *carefully*, shower (debatable) |
| 10 ATM / 100 m | swimming/snorkel | pool, surface swimming |
| 20 ATM / 200 m | serious water | recreational scuba with a dive-rated crown |
| 250 m+ / "Diver's" | **ISO 6425 dive watch** | diving, tested as equipment |

The ratings describe **static pressure** in a lab. Real swimming adds dynamic
pressure (a dive into water, a hard stroke) many times the static value — which
is why the "don't swim with 3 ATM" rule exists.

## How water gets in

- **Gaskets** (crystal, case back, crown, pushers) — rubber ages, flattens,
  and dies faster with heat, soap, chlorine, and crown-pulling.
- **Crown and pushers** — pulled/pushed underwater is the classic self-inflicted
  failure. Screw-down crowns ([keyless works](../anatomy/06-the-keyless-works.md))
  help; *locked* crowns are the real rule.
- **Case condition** — a caseback gasket pinched at last service; a crystal
  seal that lost its groove.

## What to do

- Pressure test after every service and annually if you swim; it's cheap.
- Rinse salt water; never operate pushers submerged unless the manual says so.
- Warm-to-cold transitions (pool → AC) fog crystals via condensation on the
  *inside* — often the first sign of a tired seal.
- Vintage watches: assume **zero** water resistance regardless of marking.

For the machinery these seals protect, see the
[Anatomy series](../start-here/read-me-first.md#path-1--the-machinist-8-parts-90-minutes);
for the maintenance calendar, [Servicing](servicing.md).

</content>
</file>

<file path="content/movements/index.md">
<content>
---
title: "How to Read a Calibre"
description: "What a calibre number means, what separates a workhorse from a landmark, and how to evaluate any movement with five questions."
date: "2026-09-28"
author: "Buffy"
categories: ["movements"]
tags: ["calibre", "guide", "gear-train", "escapement"]
---

A **calibre** (caliber) is a movement architecture: the layout of bridges,
train, [escapement](../escapements/swiss-lever.md), and complications that a
manufacturer produces and names. Reading one well is the difference between
collecting specifications and understanding machines.

## The five questions

1. **Integrated or modular?** Built as a chronograph from the first bridge
   ([El Primero](zenith-el-primero.md)) or a base movement with a module
   stacked on (many calendar watches)? Integrated wins coherence and thinness;
   modules win cost and service uniformity.
2. **Who made it, for whom?** ETA and Sellita supply the industry; the same
   base can appear in a $500 watch and a $5,000 one with different finishing.
   In-house (Rolex's [3135](rolex-3135.md), Omega's coaxial family) is a
   supply-chain and marketing statement as much as a technical one.
3. **What's the frequency and reserve?** [28,800 vph](../physics/frequency.md)
   and 40–70h is the modern middle; anything else is a deliberate choice with
   consequences.
4. **What escapement and spring?** Swiss lever with Nivarox is baseline;
   [co-axial](../escapements/co-axial.md) + silicon is Omega's stack; free-sprung
   balances with Parachrom/Syloxi are Rolex's. See
   [the balance spring](../physics/the-balance-spring.md).
5. **How does it service?** Parts availability, module access, and whether the
   design survived long enough for watchmakers to know its habits — the real
   reason the [Valjoux 7750](valjoux-7750.md) is everywhere.

## The landmark calibres on this site

- [Omega 321](omega-321.md) — the column-wheel chronograph that went to the moon.
- [Zenith El Primero](zenith-el-primero.md) — 5 Hz integrated automatic, 1969.
- [Valjoux 7750](valjoux-7750.md) — the cam-lever workhorse of a generation.
- [Rolex 3135](rolex-3135.md) — the argument for boring excellence.
- [Patek Philippe Calibre 89](patek-calibre-89.md) — what "everything" looked
  like in 1989.

Finishing — anglage, perlage, Geneva stripes — shows care but not timekeeping;
the numbers above show timekeeping but not care. A great calibre has both, or
is honest about which it chose.

</content>
</file>

<file path="content/movements/omega-321.md">
<content>
---
title: "Omega Calibre 321"
description: "The column-wheel chronograph that timed the moon landings: Lemania roots, the Moonwatch story, and its 2019 revival."
date: "2026-09-28"
author: "Buffy"
categories: ["movements"]
tags: ["calibre", "chronograph", "history", "timeline"]
---

The **Omega Calibre 321** is a hand-wound, column-wheel
[chronograph](../complications/chronograph.md) movement — and the one that
timed the Apollo missions on the wrists of astronauts. It is the platonic
ideal of a mid-century chronograph calibre.

## Origins

The architecture descends from the Lemania **27 CHRO C12** (Lemania/Omega
shared development in the 1940s); Omega produced it as the **321** from 1946
until 1968. A column wheel controls the chronograph; coupling is lateral, the
layout is compact, the finish is honest. It powered everything from dress
chronographs to the **Speedmaster**.

## The Moonwatch

NASA's 1964-65 procurement for crewed missions famously tested watches from
several makers; the Speedmaster (with 321) survived the abuse testing and was
flight-qualified in 1965 — the only watch certified for EVA use in the Apollo
program. On the Apollo missions, wrist chronographs served as backup timing
for mission events; Armstrong left his inside the lander as a cabin clock (a
detail that pleases pedants endlessly), Aldrin's went to the surface.

The 321's last regular production was 1968; the Speedmaster then moved to the
cam-lever **861** (Lemania 1873) and later 1861/3861. For decades "321
Moonwatch" was the collector code.

## The 2019 revival

Omega reintroduced the 321 in steel (Calibre 321 Canopus gold debut then the
steel "321 Moonwatch"), rebuilt with modern manufacturing — Sedna gold PVD
coating on some parts in later versions — but the architecture unchanged:
column wheel, hand-wound, 28,800 vph... actually the revived 321 runs at
18,000 vph like the original (2.5 Hz), staying faithful to the period
character.

## Why it matters to this site

The 321 is the cleanest example of the
[column-wheel ideal](../complications/chronograph.md#column-wheel-vs-cam): the
control logic is visible, adjustable, and repairable by humans. Strapped to the
Speedmaster's case through the [space race](../history/1969-the-quartz-crisis.md),
it is mechanical horology's most famous artifact — not the most accurate movement
ever made, but the most *witnessed*.

</content>
</file>

<file path="content/movements/patek-calibre-89.md">
<content>
---
title: "Patek Philippe Calibre 89"
description: "The most complicated portable timepiece of its era: 33 complications, 1,728 components, and what happens when a project is allowed to take nine years."
date: "2026-09-30"
author: "Buffy"
categories: ["movements"]
tags: ["calibre", "complications", "history", "timeline"]
---

**Calibre 89** is Patek Philippe's anniversary pocket watch: announced 1983
for the firm's 150th birthday (founded 1839), delivered 1989 — and, when
finished, the most complicated portable timepiece ever made. It is the answer
to "what is everything on this site at once?"

## The numbers

- **33 complications** (Patek counted 33; definitions vary), including:
  [perpetual calendar](../complications/perpetual-calendar.md) with
  [moonphase](../complications/moonphase.md), [minute repeater](../complications/minute-repeater.md)
  with three gongs, [tourbillon](../complications/tourbillon.md), grande and
  petite sonnerie, Westminster chimes, alarm, thermometer, barometer,
  altimeter, hygrometer, compass, sidereal time, sunrise/sunset, equation of
  time, celestial chart of the Geneva sky...
- **1,728 components**, 24 hands, 31 jewels... (published counts vary slightly
  by source), about 89 mm diameter — the "89" is the anniversary year's echo.
- Five examples (one each in yellow gold, white gold, rose gold, platinum,
  and a stainless steel example) were planned; the platinum and steel
  "pieces uniques" are the deepest rabbit hole in collecting.

## Why it matters here

Calibre 89 is the site's ultimate case study in
["complications are counting"](../complications/index.md): a barometer and an
altimeter are aneroid capsules geared to hands; the celestial chart is a
star-shaped cam; the equation of time is a kidney-shaped cam subtracting solar
from mean time. Every complication is geometry pretending to be information.

It also answers the [tourbillon](../complications/tourbillon.md) question
with production reality: stacking complications multiplies friction and
service burden — Calibre 89 is a museum piece, not a daily wearer, and its
creation required nine years of the best bench work available.

## The view from 2026

Modern "grand complications" wristwatches compress much of this into 40 mm
cases (Patek's own Grandmaster Chime, Vacheron's Reference 57260). But the
spirit of Calibre 89 — a firm proving what the *bench* can do, not what a
market needs — is why the craft survived the [quartz
crisis](../history/1969-the-quartz-crisis.md) at all. See
[Movements](index.md) for how this compares with the workhorses.

</content>
</file>

<file path="content/movements/rolex-3135.md">
<content>
---
title: "Rolex Calibre 3135"
description: "The case for boring excellence: 1988-2018, 28,800 vph, Parachrom, and why the world's most famous watch brand made its name on reliability."
date: "2026-09-29"
author: "Buffy"
categories: ["movements"]
tags: ["calibre", "guide", "balance-spring", "accuracy"]
---

The **Rolex Calibre 3135** is the automatic date movement that powered the
Submariner, Datejust, Sea-Dweller, and dozens of others from 1988 until the
3235 generation displaced it around 2015-2018. It is not glamorous. It is
possibly the best-manufactured mass-produced movement ever made.

## The design

- Automatic, bi-directional rotor (Rolex's perpetual rotor), 28,800 vph
  (4 Hz), roughly 48-50h reserve.
- Free-sprung balance with **Microstella** regulating weights — no regulator
  index; adjustment by rotating tiny screws in the balance rim. Better
  stability over time than curb-pin regulation
  ([why](../anatomy/05-the-balance-assembly.md#the-hairspring)).
- **Parachrom** hairspring (niobium-zirconium alloy) from 2000: paramagnetic
  and shock-stable. Later variants added Paraflex shock settings.
- Rolex's own jeweling, own wheels, own everything: vertical integration as
  a manufacturing doctrine.

## What it does well

Rate stability over service intervals and tolerance to abuse. The 3135's
reputation among watchmakers is "runs right for a decade"; its service
procedures are standardized; parts and knowledge are ubiquitous. When Rolex
announced the **3235** (Chronergy escapement — a modified
[lever](../escapements/swiss-lever.md) with optimized pallet geometry and a
nickel-phosphorus escape wheel for magnetism resistance; 70h reserve), the
loudest commentary was that the 3135 didn't need replacing.

## The philosophical point

The 3135 embodies this site's
[comparison-table](../escapements/compared.md) verdict: the winning
architecture is the one that's *good everywhere, forever*. It gives up
spectacle — no [tourbillon](../complications/tourbillon.md), no [column
wheel](../complications/chronograph.md), no [co-axial](../escapements/co-axial.md)
— to buy consistency, serviceability, and timekeeping that a
[chronometer certificate](../physics/positions-and-rate.md) measures but
doesn't explain. The explanation is in the details above: free-sprung balance,
good spring, industrial discipline.

If you want one watch to never think about, this is the engineering reason it
works.

</content>
</file>

<file path="content/movements/valjoux-7750.md">
<content>
---
title: "Valjoux 7750"
description: "The cam-lever chronograph workhorse: 1974 design, oscillating pinion, the movement inside half the chronographs you have ever seen."
date: "2026-09-29"
author: "Buffy"
categories: ["movements"]
tags: ["calibre", "chronograph", "guide", "history"]
---

The **Valjoux 7750** (now ETA 7750 family) is the industry's definitive
workhorse [chronograph](../complications/chronograph.md): automatic, cam-lever,
day-date, 28,800 vph, robust enough to power everything from pilot's watches
to fashion-brand chronographs since 1974.

## Design in one pass

- Based on the earlier Valjoux 7730 hand-wound family (itself a Camaro/Sinn
  era staple), redesigned for automatic winding with a central rotor.
- **Cam-lever** control instead of a [column wheel](../complications/chronograph.md#column-wheel-vs-cam):
  simpler, cheaper, industrial.
- **Oscillating pinion** coupling — the same elegant trick the
  [El Primero](zenith-el-primero.md) uses: engagement by tilting a pinion into
  the chronograph runner. Fewer parts than a lateral clutch, crisp feel.
- **Dubois-Dépraz-style** modular variants aside, the 7750 is integrated enough
  to be thin-ish and very serviceable.
- Wobble: the unidirectional rotor's audible "wobble" on some examples is a
  personality trait, not a fault.

## Why it conquered

Cost per reliability. The architecture tolerates modules (calendar, GMT) and
brand decoration, parts are everywhere, and every watchmaker alive has seen a
hundred. For two decades, "automatic chronograph under $5,000" almost meant
"7750 inside" — Sinn, Oris, TAG Heuer (Calibre 16 lineage), Breitling (B01
now, but long history), Hamilton, IWC (Da Vinci, Portugieser chronographs of
the 1990s), and on.

## The arguments against

Watch forums call it thick, industrial, unromantic compared to a
[column wheel](../complications/chronograph.md). All true-ish: the module
stack can make tall watches, and the finishing is factory-grade. But the 7750
is horology's **Toyota Hilux** — and this site's bias, stated in
[Escapements, Compared](../escapements/compared.md), is that total cost of
ownership is a moral good.

## The lineage today

ETA's modern versions (7753, 7754 variants) coexist with Sellita's SW500
clone-family and in-house designs (the [4130-style](../complications/chronograph.md#lateral-clutch-vs-vertical-clutch)
vertical-clutch generation). The 7750's real achievement: it made the
chronograph *ordinary* — which is exactly what mass production is for.

</content>
</file>

<file path="content/movements/zenith-el-primero.md">
<content>
---
title: "Zenith El Primero"
description: "The first integrated automatic chronograph with 36,000 vph: the 1969 race, the high-beat argument, and the movement that Rolex once borrowed."
date: "2026-09-29"
author: "Buffy"
categories: ["movements"]
tags: ["calibre", "chronograph", "frequency", "history", "timeline"]
---

The **El Primero** ("the first") is Zenith's integrated automatic
[chronograph](../complications/chronograph.md) calibre, launched in 1969 at a
then-astronomical **36,000 vph (5 Hz)**. It won the race to "first automatic
chronograph" (contested), and it became the high-beat standard-bearer.

## The 1969 race

Three teams claimed the first automatic chronograph within months of each
other: **Zenith/Movado** (El Primero, prototyped as the 3019 PHC),
**Seiko** (6139, quietly in production 1969), and the **Chronomatic consortium**
(Heuer, Breitling, Hamilton-Büren, Dubois-Dépraz — the modular Calibre 11).
"First" depends on prototype vs production vs announcement definitions; the
El Primero's claim is the earliest *integrated* high-beat automatic
chronograph.

## What makes it special

- **5 Hz balance** — [frequency](../physics/frequency.md) advantages: smoother
  sweep, better disturbance rejection, and 1/10-second chronograph readings.
- **Integrated architecture** — no module: the chronograph is designed into
  the plate, thin for its era, with column wheel and **oscillating pinion**
  coupling (a lateral clutch variant with clean engagement).
- **Longevity** — continuous production from 1969 to today, powering Zenith,
  Rolex (the **Daytona 16520**, 1988–2000, used an El Primero base heavily
  modified — Rolex's own 4130 later replaced it), Ebel, and others.

## The high-beat trade-off

At 5 Hz the pallet impulses arrive twice as often; wear and lubrication demand
rise, and the movement needs care. Yet the El Primero's reputation is
robustness as much as precision — Zenith's movement survived the quartz crisis
in a drawer of unsold parts (the famous story of Charles Vermot hiding the
tooling and plans rather than see them scrapped).

## Where it sits in this site's arguments

The El Primero is the practical demonstration of
[frequency as accuracy](../physics/frequency.md) — not in certification
tables, but in real-world rate stability and the drama of a hand sweeping ten
times a second. If the [321](omega-321.md) is horology's most *witnessed*
movement, the El Primero is its most *raced*.

</content>
</file>

<file path="content/physics/amplitude.md">
<content>
---
title: "Amplitude"
description: "The single number that tells you if a watch is healthy: how far the balance swings, what's normal, what's dangerous, and how to read it off a timegrapher."
date: "2026-09-27"
author: "Buffy"
categories: ["physics"]
tags: ["physics", "amplitude", "accuracy", "service", "lubrication"]
---

**Amplitude** is how many degrees the [balance wheel](../anatomy/05-the-balance-assembly.md)
rotates in each direction of its swing — from its rest point to the extreme of
the arc. It is the vital sign of a mechanical watch: the first number a
watchmaker reads and the one that tells the truth fastest.

## What's healthy

For a modern wristwatch movement in dial-up position, full wind:

| Amplitude (dial up, full wind) | Reading |
| --- | --- |
| 270–310° | healthy, fresh service |
| 220–270° | acceptable, aging oil or partial wind |
| below 220° | trouble: friction, magnetism, or dirt |
| above ~315° | **overbanking risk** — see below |

Vertical positions (crown down etc.) run 30–60° lower than dial up; that
spread is normal. Vintage movements run lower overall; judge against their
era, not a modern spec sheet.

## Why it moves around

Amplitude is the balance between energy in (the [escapement's impulse](../escapements/swiss-lever.md))
and energy out (friction, air drag). Anything that changes either side shows up
here first:

- **Falling mainspring torque** — amplitude sags across the power reserve.
- **Old oil** — viscosity rises, amplitude falls, rate drifts with it.
- **[Magnetism](../maintenance/magnetism.md)** — coils touching, amplitude
  collapses and the rate races.
- **[Position](positions-and-rate.md)** — pivots bear differently; dial up
  wins because gravity assists concentric rotation.

## Overbanking: too much of a good thing

When amplitude exceeds roughly 315°, the balance's impulse jewel can arrive at
the fork *early* and throw the [escapement](../escapements/swiss-lever.md)
into a false unlock — the wheel spins a few teeth and relocks. Result: a watch
that suddenly gains many minutes ("rebanking"). Causes: over-winding a
hand-wound watch that's already adjusted for full wind, excessive impulse, or
a weak mainspring bridle letting torque spike. It's the one failure mode where
more energy is the enemy.

## How to measure it

A **timegrapher** listens to the tick and infers amplitude from the phase of
the beat against a reference — you must tell it the movement's
[lift angle](../escapements/swiss-lever/drop-lock-and-lift.md#lift) (45–58°
typical) or the number it prints is fiction. Compare positions, compare full
wind vs. +24h, and watch for the sag signature of tired oil.

Amplitude is information; [rate](positions-and-rate.md) is opinion.

</content>
</file>

<file path="content/physics/frequency.md">
<content>
---
title: "Frequency"
description: "18,000 vs 28,800 vs 36,000 vph: what beat rate buys you, what it costs, and why 4 Hz became the world's default."
date: "2026-09-28"
author: "Buffy"
categories: ["physics"]
tags: ["physics", "frequency", "accuracy", "escapement"]
---

A watch's **frequency** is how fast its [balance](../anatomy/05-the-balance-assembly.md)
oscillates. The classic spec is **vph** — vibrations (semi-oscillations) per
hour. Halve it and divide by 3600 to get full beats per second:

| vph | beats/sec | Hz (full oscillations) | era / use |
| --- | --- | --- | --- |
| 18,000 | 2.5 | 2.5 Hz | vintage, pocket, slow-beat luxury |
| 21,600 | 3 | 3 Hz | vintage auto, some modern |
| 28,800 | 4 | 4 Hz | the modern default |
| 36,000 | 5 | 5 Hz | high-beat (El Primero, GS hi-beat) |
| 43,200–72,000 | 6–10 | 6–10 Hz | experimental / observatory (Breguet 7727 at 10 Hz) |

## What a faster beat buys

- **Disturbance dilution.** Each [impulse](../escapements/swiss-lever.md) is a
  shove; at 8 shoves per second instead of 5, each shove is smaller relative to
  the momentum. External disturbances (wrist motion) are averaged out faster.
- **Resolution.** Seconds hands sweep more smoothly; chronographs
  ([read](../complications/chronograph.md)) can subdivide beats further
  (1/5, 1/10 s displays are beat-rate tricks).
- **Rate stability in practice.** High-beat movements tend to hold position
  rates closer together — less spread, better real-world averages.

## What it costs

Energy and wear scale with beat rate: more impulses per hour means more
[amplitude](amplitude.md) drain per hour, more pallet wear, more lubrication
demand, shorter service intervals — and less power reserve per milligram of
mainspring. 18,000 vph movements can run 60+ hours easily on modest springs;
36,000 vph is a thermodynamic lifestyle choice.

## Why 4 Hz won

28,800 vph splits the difference with unusual elegance: fast enough for stable
rate and smooth sweep, slow enough for 40–70 hour reserves and long service
intervals. The industry converged on it through the 1970s–90s — the same
convergence that made calibres like the [Valjoux 7750](../movements/valjoux-7750.md)
ubiquitous.

## Quartz and the joke

Quartz oscillators run at 32,768 Hz — the reason a $10 quartz watch beats a
$10,000 chronometer. But watch people count *swings of a balance*, and there
is something to it: a quartz crystal is a sliver of rock on a circuit, while a
28,800 vph balance is a wheel on a spring that has been arguing with gravity
since [Huygens](../history/1656-huygens-and-the-pendulum.md). Frequency is a
physics choice; the choice of oscillator is a philosophy.

</content>
</file>

<file path="content/physics/friction-and-lubrication.md">
<content>
---
title: "Friction and Lubrication"
description: "Oil is the watchmaker's real craft: which bearings get which drops, why epilame exists, and how friction becomes rate."
date: "2026-09-29"
author: "Buffy"
categories: ["physics"]
tags: ["physics", "lubrication", "service", "escapement", "shock-protection"]
---

A mechanical watch runs on roughly a **microwatt** of power. Friction is not a
nuisance in such a machine; it is the environment. Everything about servicing —
cleaning, oils, epilame, timing — is friction management.

## The friction budget

Power leaks at every pivot, every tooth mesh, and above all at the
[escapement](../escapements/swiss-lever.md) impulse surfaces. Because the
[amplitude](amplitude.md) directly reflects the energy balance, friction shows
up there first and as rate drift second (a loaded balance oscillates slightly
slower in practice — positional and [isochronism](isochronism.md) effects
compound).

## The oil schedule

Watch oils are engineered fluids with specific viscosities and temperature
behavior. The classic bench logic:

| Site | Oil | Why |
| --- | --- | --- |
| escape & pallet pivots | light (e.g. Moebius 9010) | fast, low torque |
| balance staff | lightest + capstone jewels | speed of oscillation |
| train pivots, cannon pinion | medium (HP-1300 class) | load × speed |
| barrel arbor, winding | heavy / grease | slow, high load |
| barrel wall (mainspring) | braking grease | controlled slip of the bridle |
| chrono coupling, keyless | grease (8200 class) | impact and sliding |

Too light and it drains away; too heavy and amplitude dies. Aging oil oxidizes
and thickens — the mechanism of "it ran fine until it didn't."

## Epilame and surface treatment

**Epilame** (e.g. Fixodrop) is a surface treatment that holds oil *in place* by
surface tension control. The [escapement](../escapements/swiss-lever/drop-lock-and-lift.md)
impulse surfaces are epilamed so the microscopic oil drop stays on the impulse
plane instead of creeping across the stones. Surface engineering in the
1930s–50s made modern service intervals possible; the [co-axial](../escapements/co-axial.md)
is, philosophically, an attempt to make this whole page less important.

## Shock settings

Balance jewels sit in **shock settings** — spring-mounted jewel cups
(Incabloc from 1934, KIF, Paraflex, Diashock and others) that let the jewel
move a hair under impact and snap back. They protect the pivots, not the
jewels; their springs take a set over decades. A watch with a broken shock
spring shows up at the bench with a snapped staff — the classic dropped-watch
autopsy. See [The Balance Assembly](../anatomy/05-the-balance-assembly.md).

## What owners should know

- Servicing is mostly *cleaning and re-oiling*; wear parts come second. The
  4–7 year interval is an oil life estimate, not superstition.
- "Magnetized" watches ([here](../maintenance/magnetism.md)) act like
  lubrication failures but cost nothing to fix.
- A watch that runs 30 s/day slow after years of use is usually friction's
  long argument, not a broken [escapement](../escapements/compared.md).
- Never lubricate anything at home. Ever.

</content>
</file>

<file path="content/physics/isochronism.md">
<content>
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

</content>
</file>

<file path="content/physics/positions-and-rate.md">
<content>
---
title: "Positions and Rate"
description: "Why 'it gains five seconds a day' is an average of a hundred moving targets — positional variance, temperature, and what chronometer certification actually tests."
date: "2026-09-28"
author: "Buffy"
categories: ["physics"]
tags: ["physics", "accuracy", "balance", "guide"]
---

A watch does not have *a* rate. It has a cloud of rates — different in every
position, at every amplitude, at every temperature, on every day. What we call
"accuracy" is the average of that cloud in the life you actually give it.

## Position: gravity finds every pivot

Lying dial-up, the balance staff rests on one pivot centrally; hanging crown-down,
it rests on the side, and the balance's own mass distribution matters. Two
effects fight you:

- **Pivot friction** differs per position (endshake, oil condition).
- **The balance's center of gravity** wants to be exactly on the pivot axis.
  If it isn't, gravity helps the spring in some orientations and opposes it in
  others — positional rate shifts.

Adjustment ("timing in positions") nudges the balance weights and
[regulator](../anatomy/05-the-balance-assembly.md) until the spread is small.
A fine mechanical watch is within a few seconds across positions; a neglected
one can differ by a minute.

## Temperature

Temperature changes the [balance spring's](the-balance-spring.md) modulus
(stiffer when cold) and the balance's dimensions. Classic compensation used
bimetallic balances and Elinvar-type springs whose shifts cancel; modern
Nivarox and [silicon](the-balance-spring.md#materials-steel-nivarox-silicon)
designs are largely self-compensating over wrist temperature ranges.

## What certification actually tests

**COSC** (Contrôle Officiel Suisse des Chronomètres) tests uncased movements
for 15 days in 5 positions and 3 temperatures, with criteria including mean
daily rate in **−4 to +6 seconds/day** and day-to-day consistency. It is a
*minimum bar*, not a promise about your wrist.

Other standards raise the bar: Rolex's Superlative (−2/+2, cased), Omega's
Master Chronometer / METAS (−0/+5, cased, plus **15,000 gauss** magnetism
resistance), Grand Seiko's internal standards (−3/+5 mechanical), and
chronometer observatory trials of old (which fanned the flames of the
[El Primero era](../movements/zenith-el-primero.md) rivalries).

## What this means for you

- Rate varies by **what you do**, not just the watch: worn vs. in a drawer
  changes amplitude ([isochronism](isochronism.md) kicks in), arm motion winds
  an automatic differently.
- Judge a watch over a week of *your* life, dial-up readings aside.
- A sudden jump of tens of seconds usually means [magnetism](../maintenance/magnetism.md)
  or a knock — not a ruined movement.
- Adjustments a watchmaker makes are compromises: "crown left" may improve at
  the cost of "dial up." There is no perfect, only the best average for you.

</content>
</file>

<file path="content/physics/the-balance-spring.md">
<content>
---
title: "The Balance Spring"
description: "The coiled heart of the watch: Hooke, Huygens, the priority dispute, Phillips terminal curves, and the silicon revolution."
date: "2026-09-26"
author: "Buffy"
categories: ["physics"]
tags: ["balance-spring", "balance", "physics", "history", "silicon", "timeline"]
---

The **balance spring** (hairspring) is a spiral of metal thinner than a human
hair, a few millimeters across, that makes the [balance wheel](../anatomy/05-the-balance-assembly.md)
oscillate at a constant rate. Without it there is no watch. With it, since 1675,
there has been horology.

## Why a spring changes everything

A free balance wheel is an oscillator whose period depends on how hard you push
it — useless for timekeeping. Couple it to a spring and the period becomes a
property of the *system*: mass (inertia) and stiffness. Now a push of any
reasonable size produces (nearly) the same rhythm. That property is
[isochronism](isochronism.md), and it is the spring's gift.

## The priority fight, 1675

The spiral balance spring appeared in 1675 in a burst of simultaneous claims:

- **Christiaan Huygens** demonstrated a spiral-spring balance watch in The
  Hague in March 1675 and reported it to the Royal Society — the first clear
  published working design.
- **Robert Hooke** claimed he had the idea years earlier (his spring-clock
  work of the 1660s) and accused Huygens of taking it from his published hints.
- **Jean de Hautefeuille** presented a pamphlet with his own claim in the same
  months.

The honest summary: Hooke had the physics under his nose; Huygens built the
working thing and gave it the spiral geometry that made it practical; history
gave the wristwatch its balance spring and its first great priority scandal.
(Breguet's famous line that "I invented nothing, I improved everything" reads
differently after this episode.)

## Geometry: the fight against the spring itself

A naive flat spiral has two vices: its *center of gravity* drifts with the
breathing of the coil, and its outer turns behave differently from the inner
ones. The corrections are elegant:

- The **Breguet overcoil** (late 18th c.): raise the outer terminal curve up
  and inward over the spring, so the spring "breathes" concentrically.
- **Phillips terminal curves** (Edouard Phillips, 1861 mathematical treatise):
  compute the exact end-curve shape that makes the last turn behave like the
  rest. The modern flat spring's carefully profiled terminal is Phillips' work.
- **Regulator curb pins** — the index system — shorten the effective spring;
  free-sprung balances adjust weights instead and avoid the pins entirely.

## Materials: steel, Nivarox, silicon

Early springs were steel — rust-prone and magnetizable. The 20th century's
**Nivarox-type alloys** (iron-nickel with beryllium, titanium additions) are
corrosion-resistant, thermally compensating (the balance's expansion and the
spring's modulus shift partly cancel), and less magnetic. The 21st century went
further: **silicon** (Si14, Silinvar) springs are amagnetic, corrosion-proof,
light, and etched to shapes no alloy could hold — Patek's Spiromax, Rolex's
Syloxi, Omega's Si14. Their limit is brittleness and the fact that they cannot
be adjusted by hand: they are manufactured, not tuned.

See also [Magnetism](../maintenance/magnetism.md) for what a magnetic spring
does to your day, and [Positions and Rate](positions-and-rate.md) for how the
watchmaker negotiates with all of the above.

</content>
</file>

<file path="content/start-here/read-me-first.md">
<content>
---
title: "Read Me First"
description: "Three reading paths through Escapement: the machinist, the historian, and the buyer — and what each path will teach you."
date: "2026-09-30"
author: "Buffy"
categories: ["orientation"]
tags: ["guide", "series-anatomy"]
---

This site is one large, cross-linked argument. You can read it front to back or
follow a thread. Here are the three threads that work best.

## Path 1 — The machinist (8 parts, ~90 minutes)

You want to *understand the object*. Read the Anatomy series in order:

1. [The Problem of Timekeeping](../anatomy/01-the-problem-of-timekeeping.md) —
   why any of this is hard.
2. [The Gear Train](../anatomy/02-the-gear-train.md) — turning one rotation an
   hour into one a minute.
3. [The Mainspring and Barrel](../anatomy/03-the-mainspring-and-barrel.md) —
   the engine, and why it needs to lie about its own strength.
4. [The Escapement](../anatomy/04-the-escapement.md) — the referee.
5. [The Balance Assembly](../anatomy/05-the-balance-assembly.md) — the
   oscillator that actually keeps time.
6. [The Keyless Works](../anatomy/06-the-keyless-works.md) — winding and
   setting, one crown, two jobs.
7. [The Motion Works and Dial](../anatomy/07-the-motion-works-and-dial.md) —
   how the hands are geared to disagree by exactly 12:1.
8. [Putting It Together](../anatomy/08-putting-it-together.md) — a full
   teardown in service order.

## Path 2 — The historian (one archive, ~60 minutes)

You want the story of how we learned to split time into equal pieces. Start at the
[Timeline](../history/index.md) and follow it forward: Huygens and the pendulum
(1656), the [balance-spring race](../history/1675-the-balance-spring-race.md),
[Harrison's longitude war](../history/1761-harrison-and-the-longitude-prize.md),
the [American system](../history/1850s-the-american-system.md), and the
[quartz crisis](../history/1969-the-quartz-crisis.md) that nearly ended all of it.

## Path 3 — The buyer (practical, ~30 minutes)

You own a watch or intend to. Read
[Amplitude](../physics/amplitude.md) (the health metric),
[Positions and Rate](../physics/positions-and-rate.md) (why "it gains five
seconds a day" is a normal sentence), [Magnetism](../maintenance/magnetism.md),
[Water Resistance](../maintenance/water-resistance.md), and
[Servicing](../maintenance/servicing.md). Then skim the
[Glossary](../glossary/glossary.md) before reading any watch forum ever again.

## How to use the links

Every technical term that has its own page is linked the first time it appears.
Following links is not a detour — it is how the site is meant to be read. The
build also emits a [Knowledge Graph](/graph/) page so you can see which pages
lean on which.

</content>
</file>

<file path="content/start-here/the-five-minute-watch.md">
<content>
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

</content>
</file>

