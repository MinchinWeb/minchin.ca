title: Buying FBOs
modified: March 4, 2025
slug: fse/worksheets/buying-fbos
status: hidden

Does it make sense to buy an FBO?

Buy it for pride, for vanity, or because you want to fly a route in or out of it.
Rather hard to make money off of landing fees (i.e. "passively") alone.

There are XX FBO's in the game, and XX active players last month. Not all FBO's
are built out, so you can build one up, or buy an existing one. The prices on
existing FBOs are kind of all over the map. 1-lots can start as low as $50k,
2-lots often start about $200k, and 3-lots start in ~$3.5 million.

I think many of the discount ones struggle because they don't show up in the
simulator (e.g. the airport has closed since FSE started) or are labeled
different between FSE and the simulator[^1].

Assuming building materials at $4/kg[^2] and supplies at $6.75/kg (the current
computer provided price), to build up an FBO, including passenger terminal[^3],
costs:

| Size  | Gates | Building Materials | BM Cost  | Monthly Supply Cost[^4] |
| ----- | ----- | ------------------ | -------- | ----------------------- |
| 1 lot | 1     | 12,000 kg          | $48,000  | $2,052                  |
| 2 lot | 4     | 42,000 kg          | $126,000 | $8,208                  |
| 3 lot | 9     | 92,000 kg          | $276,000 | $18,468                 |

May want to consider building a repair shop at the same time (extra 2,000 kg of
building material).

If you tare down a FBO, you get 60% of the material back. So it may be
worthwhile to buy single lot FBOs under $28,800 just for material.

**XX** What plane to use to move that material?

Per the developers, the idea is you can pay for the upkeep for a FBO buy flying
the jobs it produces three times. It's pretty hard to make a FBO pay for itself
just on other people flying through. Let's do some math: let's assume each
passenger pays $700, and you keep 95% if you fly to passengers, and 5% ground
fees if someone else flies your passengers (this effectively assumes that you
don't own the FBO at the other end of the trip):

| Size  | Gates | Monthly Supply Cost | You Fly | Ground Fees Only |
| ----- | ----- | ------------------- | ------: | ---------------: |
| 1 lot | 1     | $2,052              | 3.1     | 58.6             |
| 2 lot | 4     | $8,208              | 12.3    | 234.5            |
| 3 lot | 9     | $18,468             | 27.8    | 527.7            |

Considering that each gate will only generate 3 passengers at a time, flying
that may passenger (3.1 / gate) seems doable in a month, but getting buy on
ground fees only seems tough. If you can point your trips to another FBO that
you own, you will get the ground fees on both sides, but you also now have two
FBOs to keep up. Rough math, if you could fly perfectly with a Cessna 208 (13
passengers) between two FBOs, you'd need 18 round trips for a pair of 2-lot
FBOs and 41 round trips for a pair of 3-lot FBOs.

**XX** Number of FBOs that get more than 41 aircraft movements per month, and a
list of them

[^1]: for a very long time, the FSE FBO database has been frozen, not even
    allowing corrections like incorrect states. They recently announced an
    intention to allow updates going forward, the first of these has yet to
    role out.
[^2]: 25% discount after 20,000 kg
[^3]: 10,000 kg per gate, and 2,000 kg for the passenger terminal. A repair
    shop would cost an additional 2,000 kg of building materials. --
    <https://sites.google.com/site/fseoperationsguide/fbos/creating-buying-and-selling-fbos?authuser=0>
[^4]: 10 kg/day/lot; assuming 30.4 days/month
