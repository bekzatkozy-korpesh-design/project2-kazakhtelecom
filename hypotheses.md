# Pre-registered plan (written 2026-11-25, before any speed data was downloaded)

**Company:** Kazakhtelecom JSC, the largest fixed-line operator in Kazakhstan (listed on KASE and AIX; about 66% of fixed broadband).

**Problem (what hurts):**
- Kazakhstan's median fixed broadband speed is 88.1 Mbps against a global 118.8 Mbps (Speedtest Global Index, Feb 2026).
- Users filed 67,544 complaints about home internet quality in 2025.

**Bottleneck (where it gets stuck):** the last mile in villages. Old copper (ADSL, up to ~12 Mbps) is still in place where fibre (GPON) has not arrived. The backbone and the cities are not the constraint: in a city, the same operator sells 500 Mbps on fibre.

**Evidence (public):**
1. ranking.kz: Kazakhstan's fixed internet is slower than the global median; 66% of fixed broadband is held by one operator, Kazakhtelecom. https://ranking.kz/en/reviews-en/world-en/internet-in-kazakhstan-is-slower-than-in-guatemala-and-nicaragua.html
2. zakon.kz (2026): the first village in North Kazakhstan region moved fully to fibre; before, copper gave up to 12 Mbps; speed rose more than 40×. https://www.zakon.kz/obshestvo/6531045-kazakhtelekom-polnostyu-perevel-otdalennoe-selo-v-sko-na-optiku.html
3. inform.kz: the agreement with Kazakhtelecom (June 2025) targets 3,000+ villages by the end of 2027; so far 12 have fibre and 340 use satellite. Complaints: 67,544 in 2025. https://www.inform.kz/ru/5g-sputniki-i-optika-kak-rasshiryayut-internet-dostup-v-kazahstane-8f275d77
4. Azattyq Ruhy: user complaints about Kazakhtelecom service quality. https://rus.azattyq-ruhy.kz/avtory/111465-stabilno-rabotaet-tolko-vystavlenie-schetov-kazakhstantsy-pishut-o-problemakh-s-kazakhtelekom
5. digitalbusiness.kz (2025): "Internet in villages will soon be as fast as in the city", the rural program. https://digitalbusiness.kz/2025-06-09/internet-v-selah-kazahstana-skoro-stanet-takim-zhe-bistrim-kak-v-gorode/amp/

**Data (real):** Ookla Speedtest Open Data, fixed network performance tiles (zoom-16, about 610 m), Q3 2025 and Q3 2026, licence CC BY-NC-SA 4.0. Kazakh reference data:
- Kazakhstan border and regions: geoBoundaries ADM1, CC BY 4.0.
- Settlements with population: GeoNames KZ, CC BY 4.0.

One row = one map tile in one quarter.

**Settlement class (fixed before the data is seen):** each tile gets the nearest GeoNames populated place.
- **City:** the nearest place with ≥ 100,000 people is within 15 km.
- **Village:** no place with ≥ 10,000 people within 15 km.
- **Town:** everything else.

## Hypotheses (fixed before seeing data)

**Pair 1: is there a rural gap?**
- H1: fixed download speed in villages is lower than in cities.
- H0: mean tile download speed is the same in cities and villages (Q3 2026).
- Test: Welch t-test on log speed, plus Mann–Whitney U.

**Pair 2: is it the last mile (copper), not the whole network?**
- H1: villages have a much larger share of tiles below 25 Mbps, the copper/ADSL zone.
- H0: the share of tiles below 25 Mbps is the same in cities and villages (Q3 2026).
- Test: chi-square.

**Pair 3: is the fix working yet?**
- H1: village speeds rose from Q3 2025 to Q3 2026.
- H0: mean village tile download speed is the same in Q3 2025 and Q3 2026.
- Test: Welch t-test on log speed (all village tiles), plus a paired test on tiles present in both quarters.

Significance level: 0.05. Results are reported as "H0 rejected" or "H0 not rejected", including the ones that go against my guess.

---

# Addendum: sharper hypotheses (written 2026-11-25, before mobile data was downloaded and before any distance analysis)

Pairs 1–3 were tested and all three H0 were rejected. They confirm what everyone already knows: villages are slower. That does not tell Kazakhtelecom where to spend money. Pairs 1–3 stay in the analysis as **"the problem exists"**. The two pairs below are the main hypotheses and can change an investment decision.

**Refined bottleneck question:** fibre-to-the-home in villages (the 2025–2027 programme) is the right fix *only if* (a) the village line is the constraint, not the trunk line to the village, and (b) mobile 4G is not already beating the fixed line there. If mobile is already faster, the scarce resource is not fibre but the reason to buy fixed internet at all.

**Pair 4: is the trunk line to the village (backhaul) the constraint?**
- H1: villages far from a big city have slower fixed internet than villages near one, which points to weak backhaul, not only the copper inside the village.
- H0: mean fixed download speed (log) is the same for village tiles **near** a city (≤ 50 km to a place with ≥ 100k people) and **far** from one (> 150 km). Q3 2026.
- Test: Welch t-test on log speed, plus Mann–Whitney U. Secondary: Spearman correlation between distance and speed for all village tiles.

**Pair 5: does mobile beat home internet in villages but not in cities?**
- H1: in villages, mobile internet is faster than fixed on a larger share of places than in cities.
- H0: the share of tiles where mobile download > fixed download is the same in cities and villages. Q3 2026, tiles that have both a fixed and a mobile measurement.
- Test: chi-square. Secondary: paired t-test on log(mobile) − log(fixed) for village tiles.
- Data: Ookla mobile performance tiles, Q3 2026, same licence. Tiles are matched on quadkey.
- Fallback rule (fixed now): if fewer than 300 village tiles have both measurements, I compare at the level of the nearest town cluster (median per `nearest_town` × settlement class) instead of single tiles.
