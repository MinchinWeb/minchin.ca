title: Buying FBOs
modified: March 16, 2026
slug: fse/worksheets/buying-fbos
status: hidden
at: FSEconomy
at_link: fse/
at_2: Worksheets
at_2_link: fse/worksheets/

**Basic Question**: Does it make sense to buy an FBO?

**Simple Answer**: Buy it for pride, for vanity, or because you want to fly a
route in or out of it. It is rather hard to make money off of landing fees
(i.e. "passively") alone.

**More Details**:

There are ~20,000 FBO's in the game (of which ~50% have FBO's on them), and
1,000 active players last month. Not all FBO's are built out, so you can build
one up, or buy an existing one. The prices on existing FBO's are kind of all
over the map. 1-lots can start as low as $50k, 2-lots often start about $200k,
and 3-lots start at ~$3.5 million.

I think many of the discount ones struggle because they don't show up in the
simulator (e.g. the airport has closed since FSE started) or are labeled
different between FSE and the simulator[^1]. One of the oddities of the
FSEconomy database (and perhaps general aviation generally) is that it is very
heavily American, with lots of American airports and the rest of the world not
as well represented. As a consequence, FBO's outside the US (and in northern
Europe in particular) can be priced at a premium and there are many fewer (if
any) open spots are available. On the flip side, if you want to build a network
*de neuvo*, the US (or Africa?) might give you more options.

There is a complicating issue that even if you have the cash on hand, many
FBO's just never come up for sale; it's not unheard of for an owner to hold on
to an FBO for 10 years or more, and many major hubs seem to be picked up by
groups running larger networks.

If you are considering building: assuming building materials at $4/kg[^2] and
supplies at $6.75/kg (the current computer provided price), to build up an FBO,
including passenger terminal[^3], costs:

| Size  | Gates | Building Materials | BM Cost   | Monthly Supply Cost[^4] |
| ----- | ----- | ------------------ | --------- | ----------------------- |
| 1 lot | 1     | 12,000 kg          | v$48,000  | v$2,052                 |
| 2 lot | 4     | 42,000 kg          | v$126,000 | v$8,208                 |
| 3 lot | 9     | 92,000 kg          | v$276,000 | v$18,468                |

For medium and large FBO's, you're not required to build out all lots initially,
and thus save on your initial investment, at the risk that someone else
might show up and build on the open lot(s) at "your" airport.

May want to consider building a repair shop at the same time (extra 2,000 kg of
building material). Additional costs come up if you want to bring in
[fuel][fuel-costs] (which you probably do); count another ~v$15k.

If you tare down an FBO, you get 60% of the material back. So it may be
worthwhile to buy single lot FBOs under v$28,800 just for material.

<!-- **XX** --> *I still don't have an answer to, What plane to use to move that material?*
I'm still trying to figure out what plane to use to bring in building
materials. I've had luck with the [DeHavilland Dash 8 100/200][es30] and
[DC-3][dc3], with both carrying ~3,500 kg of materials at a time.


The third way to acquire an FBO is through the Lottery[^6]. FBO's enter the
lottery when the owner has failed to supply them long enough[^5], and then they
are put up for sale (through lottery tickets) to all. If you're interested in
an FBO, you can buy a ticket against it. Pricing is set by FBO size, multiplied
by the number of lots occupied by the FBO:

| FBO Size         | per lot ticket price |
| ---------------- | -------------------- |
| Small ("1 lot")  | v$50,000             |
| Medium ("2 lot") | v$100,000            |
| Large ("3 lot")  | v$150,000            |

Most medium and large FBO's are built on all available lots, so you're likely
to need v$200k to bid on a medium FBO and v$450k to bid on a large FBO.

Being a lottery (or draw), it's not a given that simply buying a ticket will be
enough to win, but you can see if anyone else has bought a ticket yet. The
lottery is open for a week for each round; any FBO's not sold this way are torn
down and become available for anyone to come in and build an FBO anew.

Per the developers, the idea is you can pay for the upkeep for an FBO by flying
the jobs it produces three times. It's pretty hard to make an FBO pay for
itself just on other people flying through. Let's do some math: let's assume
each passenger job pays v$700, and you keep 95% if you fly the passengers
(convienantly ignoring any plane rental/maintenance or fuel costs, which could
cut this in half...), and 5% ground fees if someone else flies your passengers
(this effectively assumes that you don't own the FBO at the other end of the
trip):

| Size  | Gates | Monthly Supply Cost | You Fly (assignments) | Ground Fees Only (assignments flown) |
| ----- | ----- | ------------------- | --------------------: | -----------------------------------: |
| 1 lot | 1     | $2,052              |                   3.1 |                                 58.6 |
| 2 lot | 4     | $8,208              |                  12.3 |                                234.5 |
| 3 lot | 9     | $18,468             |                  27.8 |                                527.7 |

Considering that each gate will only generate 3 passengers at a time, flying
that many passenger (3.1 / gate) seems doable in a month, but getting by on
ground fees only seems tough. If you can point your trips to another FBO that
you own, you will get the ground fees on both sides, but you also now have two
FBO's to keep up. Rough math, if you could fly perfectly with a Cessna 208 (13
passengers, and ignoring booking fees) between two FBO's, you'd need 18 round
trips for a pair of 2-lot FBO's and 41 round trips for a pair of 3-lot FBO's.

One final thing to consider is, How are you going to fly this network? (As we
just determined that hoping on others to fly it probably isn't a good business
plan.) One option would be to rely on rental planes, but there is the risk of
someone else taking off with the plane in question, or it breaking down without
a way for you to repair it. So of you're going to need a plane, just make sure
it figures into your budget, or [go plane
shopping]({filename}/pages/fse/planes/index-planes.md) before you start
building out your FBO empire.

<!-- **XX** Number of FBOs that get more than 41 aircraft movements per month, and a
list of them -->

[^1]: for a very long time, the FSE FBO database has been frozen, not even
    allowing corrections like incorrect states. They recently announced an
    intention to allow updates going forward, ~~the first of these has yet to
    role out~~ and the first of these updates rolled out in December of 2025.
[^2]: 25% discount after 20,000 kg
[^3]: 10,000 kg per gate, and 2,000 kg for the passenger terminal. A repair
    shop would cost an additional 2,000 kg of building materials. --
    <https://sites.google.com/site/fseoperationsguide/fbos/creating-buying-and-selling-fbos?authuser=0>
[^4]: 10 kg/day/lot; assuming 30.4 days/month
[^5]: 45 days, continuously
[^6]: see <https://sites.google.com/site/fseoperationsguide/fbos/fbo-lottery>

[dc3]: {filename}/pages/fse/planes/dc3.md
[es30]: {filename}/pages/fse/planes/es30.md

[fuel-costs]: {filename}fbo-fuel-costs.md
