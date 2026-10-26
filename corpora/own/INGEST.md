# Ingest report

Written by `uv run p2 ingest`.
It lists every document in this corpus that ingest added, with what the cleaning pass did and anything that looks wrong.
Running ingest again adds to the table and replaces the "last run" section, and `uv run p2 ingest --report` rewrites it for the documents in docs/ now, after you removed some.

## Summary

- Documents: 526 (the final check needs at least 200)
- Words: 514,833
- Estimated tokens (words times 1.4): 720,766 (`p2 check` warns above 800,000 and fails above 1,000,000)
- Flagged documents: 3

## Documents

| docid | words | characters per page | flags | cleaning |
|---|---:|---:|---|---|
| `100-minutes` | 370 | - | - | - |
| `3-a.m` | 659 | - | - | - |
| `3-way-rats` | 219 | - | - | - |
| `4-seasons` | 179 | - | - | - |
| `7-deadly-sins` | 264 | - | - | - |
| `8-pack` | 3,250 | - | - | - |
| `aces` | 410 | - | - | - |
| `adorkables` | 272 | - | - | - |
| `ai-chip-install` | 91 | - | - | - |
| `ainsley` | 169 | - | - | - |
| `america-s-care-package` | 830 | - | - | - |
| `america-s-eviction-vote` | 158 | - | - | - |
| `america-s-field-trip` | 124 | - | - | - |
| `america-s-nominee` | 681 | - | - | - |
| `america-s-player` | 848 | - | - | - |
| `america-s-winner` | 517 | - | - | - |
| `americory` | 609 | - | - | - |
| `an-offer-you-can-t-refuse` | 101 | - | - | - |
| `area-51-alliance` | 2,240 | - | - | - |
| `as-close-as-you-can` | 192 | - | - | - |
| `ask-the-evictee` | 626 | - | - | - |
| `austwins` | 1,827 | - | - | - |
| `ball-roll` | 193 | - | - | - |
| `bash` | 151 | - | - | - |
| `battle-back-competition` | 1,159 | - | - | - |
| `battle-of-the-block` | 1,256 | - | - | - |
| `bb-app-store` | 1,049 | - | - | - |
| `bb-besties` | 140 | - | - | - |
| `bb-comics` | 2,597 | - | - | - |
| `bb-flix-chill` | 76 | - | - | - |
| `bb-guns` | 152 | - | - | - |
| `bb-power-of-invincibility` | 77 | - | - | - |
| `bb-rewind` | 851 | - | - | - |
| `bb-storm-watch` | 68 | - | - | - |
| `bb-takeover` | 384 | - | - | - |
| `before-or-after` | 1,356 | - | - | - |
| `bermuda-triangle` | 177 | - | - | - |
| `berry-balanced` | 151 | - | - | - |
| `big-brother` | 68 | - | - | - |
| `big-brother-1-us` | 6,542 | - | - | - |
| `big-brother-10-us` | 4,953 | - | - | - |
| `big-brother-11-us` | 4,975 | - | - | - |
| `big-brother-12-us` | 5,648 | - | - | - |
| `big-brother-13-gallery` | 10 | - | very short (10 words) | - |
| `big-brother-13-us` | 5,876 | - | - | - |
| `big-brother-14-us` | 8,520 | - | - | - |
| `big-brother-15-us` | 9,024 | - | - | - |
| `big-brother-16-us` | 9,948 | - | - | - |
| `big-brother-17-us` | 8,664 | - | - | - |
| `big-brother-18-us` | 10,532 | - | - | - |
| `big-brother-19-us` | 9,367 | - | - | - |
| `big-brother-2-us` | 4,581 | - | - | - |
| `big-brother-20-us` | 10,273 | - | - | - |
| `big-brother-21-us` | 8,587 | - | - | - |
| `big-brother-22-us` | 9,035 | - | - | - |
| `big-brother-23-us` | 8,676 | - | - | - |
| `big-brother-24-us` | 7,420 | - | - | - |
| `big-brother-25-us` | 9,004 | - | - | - |
| `big-brother-25th-anniversary-celebration` | 902 | - | - | - |
| `big-brother-26-us` | 7,168 | - | - | - |
| `big-brother-27-us` | 6,941 | - | - | - |
| `big-brother-28-us` | 12,000 | - | - | - |
| `big-brother-29-us` | 2,088 | - | - | - |
| `big-brother-3-us` | 5,060 | - | - | - |
| `big-brother-30-us` | 2,088 | - | - | - |
| `big-brother-4-us` | 5,354 | - | - | - |
| `big-brother-5-us` | 5,075 | - | - | - |
| `big-brother-6-us` | 5,549 | - | - | - |
| `big-brother-7-us` | 5,706 | - | - | - |
| `big-brother-8-us` | 5,516 | - | - | - |
| `big-brother-9-us` | 5,709 | - | - | - |
| `big-brother-after-dark` | 1,531 | - | - | - |
| `big-brother-all-stars-us` | 82 | - | - | - |
| `big-brother-house` | 714 | - | - | - |
| `big-brother-house-australia` | 440 | - | - | - |
| `big-brother-house-brazil` | 129 | - | - | - |
| `big-brother-house-canada` | 758 | - | - | - |
| `big-brother-house-israel` | 59 | - | - | - |
| `big-brother-house-nigeria` | 46 | - | very short (46 words) | - |
| `big-brother-house-philippines` | 2,970 | - | - | - |
| `big-brother-house-portugal` | 418 | - | - | - |
| `big-brother-house-united-kingdom` | 457 | - | - | - |
| `big-brother-house-united-states` | 653 | - | - | - |
| `big-brother-live-chat` | 1,177 | - | - | - |
| `big-brother-rule-book` | 6,158 | - | - | - |
| `big-brother-swap` | 308 | - | - | - |
| `big-brother-unlocked` | 1,085 | - | - | - |
| `big-brother-unlocked-season-1` | 1,375 | - | - | - |
| `big-brother-unlocked-season-2` | 1,120 | - | - | - |
| `big-sister` | 208 | - | - | - |
| `big-sister-alliance` | 220 | - | - | - |
| `big-top-drop` | 162 | - | - | - |
| `binary-bridge` | 75 | - | - | - |
| `black-girl-magic-bb22` | 122 | - | - | - |
| `block-and-roll` | 181 | - | - | - |
| `blockbusters` | 101 | - | - | - |
| `bomb-squad` | 487 | - | - | - |
| `bond-girls` | 145 | - | - | - |
| `boomerang-power-of-veto` | 441 | - | - | - |
| `bowlerina` | 527 | - | - | - |
| `brad-chad` | 135 | - | - | - |
| `break-the-ice` | 120 | - | - | - |
| `brenchel` | 191 | - | - | - |
| `brenchie` | 286 | - | - | - |
| `bros` | 149 | - | - | - |
| `brown-sugar-babes` | 223 | - | - | - |
| `build-the-bridge` | 616 | - | - | - |
| `burger-boys` | 403 | - | - | - |
| `bye-bye-bitches` | 695 | - | - | - |
| `caf-con-leche` | 174 | - | - | - |
| `caged-eggs` | 631 | - | - | - |
| `camp-comeback` | 269 | - | - | - |
| `camp-director` | 100 | - | - | - |
| `carnival-quick-shot` | 719 | - | - | - |
| `cartel` | 538 | - | - | - |
| `category-four` | 265 | - | - | - |
| `cbs` | 818 | - | - | - |
| `chilltown` | 2,198 | - | - | - |
| `chrenchie` | 328 | - | - | - |
| `chrisalyss` | 428 | - | - | - |
| `clelli` | 338 | - | - | - |
| `cliff-s-angels` | 223 | - | - | - |
| `clique` | 725 | - | - | - |
| `close-to-20` | 60 | - | - | - |
| `coach` | 199 | - | - | - |
| `coaches-competition` | 360 | - | - | - |
| `coast2coast` | 281 | - | - | - |
| `coup-d-etat` | 1,072 | - | - | - |
| `cover-your-days` | 527 | - | - | - |
| `crazy-8s` | 276 | - | - | - |
| `croquet` | 621 | - | - | - |
| `crowd-control` | 215 | - | - | - |
| `crowd-control-bb26` | 130 | - | - | - |
| `dark-moon` | 81 | - | - | - |
| `defected-newbie-alliance` | 612 | - | - | - |
| `den-of-temptation` | 782 | - | - | - |
| `derstian` | 324 | - | - | - |
| `diamond-power-of-veto` | 1,019 | - | - | - |
| `digital-decryption` | 603 | - | - | - |
| `dizzy-discs` | 272 | - | - | - |
| `domino-effect` | 105 | - | - | - |
| `don-t-miss-a-beat` | 533 | - | - | - |
| `double-d-s` | 237 | - | - | - |
| `double-eviction` | 13,138 | - | - | - |
| `double-power-of-veto` | 1,176 | - | - | - |
| `double-the-fun` | 203 | - | - | - |
| `downlowmance` | 131 | - | - | - |
| `drenchie` | 283 | - | - | - |
| `drinks-on-us` | 108 | - | - | - |
| `dynamic-duos` | 572 | - | - | - |
| `el-cuatro` | 319 | - | - | - |
| `eliminator` | 252 | - | - | - |
| `elite-eight` | 671 | - | - | - |
| `eternal-immunity` | 485 | - | - | - |
| `eviction` | 1,480 | - | - | - |
| `f.a.p` | 2,068 | - | - | - |
| `facial-recognition` | 634 | - | - | - |
| `fam-five` | 149 | - | - | - |
| `family-style` | 414 | - | - | - |
| `faster-than-a-speeding-veto` | 98 | - | - | - |
| `fatal-five` | 448 | - | - | - |
| `feel-the-burn` | 223 | - | - | - |
| `final-four-bb11` | 109 | - | - | - |
| `final-four-bb18` | 352 | - | - | - |
| `final-three-bb26` | 1,394 | - | - | - |
| `finger-guns-alliance` | 192 | - | - | - |
| `fitting-in` | 255 | - | - | - |
| `five-pointz` | 187 | - | - | - |
| `flaming-five` | 214 | - | - | - |
| `flower-power` | 388 | - | - | - |
| `foam-party` | 599 | - | - | - |
| `food-competition` | 266 | - | - | - |
| `for-real-for-real` | 213 | - | - | - |
| `four-horsemen` | 469 | - | - | - |
| `four-prime` | 286 | - | - | - |
| `foutte` | 1,513 | - | - | - |
| `freakazoids` | 262 | - | - | - |
| `french-kisses` | 190 | - | - | - |
| `gear-puzzle` | 48 | - | very short (48 words) | - |
| `get-a-grip` | 161 | - | - | - |
| `getting-loopy` | 102 | - | - | - |
| `giddy-up` | 61 | - | - | - |
| `giggle-girls` | 189 | - | - | - |
| `girl-power` | 375 | - | - | - |
| `girls-girls` | 730 | - | - | - |
| `girls-girls-bb27` | 529 | - | - | - |
| `golden-girlies` | 184 | - | - | - |
| `golden-key` | 588 | - | - | - |
| `golf-invitational` | 148 | - | - | - |
| `gr8ful` | 2,032 | - | - | - |
| `hacker-competition` | 696 | - | - | - |
| `have-have-not-competition` | 229 | - | - | - |
| `head-of-household` | 3,987 | - | - | - |
| `heavy-hitters` | 293 | - | - | - |
| `hide-and-go-veto` | 745 | - | - | - |
| `hide-and-seek` | 135 | - | - | - |
| `hit-the-road` | 745 | - | - | - |
| `hourglass` | 370 | - | - | - |
| `house-calls-the-big-brother-talk-show` | 147 | - | - | - |
| `house-currency` | 108 | - | - | - |
| `houseguest-description` | 117 | - | - | - |
| `houseguestsonly.com` | 438 | - | - | - |
| `housemates` | 1,211 | - | - | - |
| `how-bad-do-you-want-it` | 144 | - | - | - |
| `immunity-competition` | 792 | - | - | - |
| `in-the-balance` | 622 | - | - | - |
| `invisible-hoh` | 2,053 | - | - | - |
| `it-s-time-to-reflect` | 81 | - | - | - |
| `item-catching` | 600 | - | - | - |
| `item-maze` | 322 | - | - | - |
| `jackpot` | 461 | - | - | - |
| `jankie` | 448 | - | - | - |
| `jatalie` | 190 | - | - | - |
| `jaylor` | 513 | - | - | - |
| `jaysar` | 321 | - | - | - |
| `jecky` | 2,661 | - | - | - |
| `jessie-s-alliance` | 110 | - | - | - |
| `jetpack-attack` | 215 | - | - | - |
| `jody` | 735 | - | - | - |
| `jokers` | 562 | - | - | - |
| `jury-removal` | 62 | - | - | - |
| `jury-statements` | 1,622 | - | - | - |
| `kaitlyn-s-puzzle` | 139 | - | - | - |
| `kings` | 608 | - | - | - |
| `knight-moves` | 410 | - | - | - |
| `knockout` | 573 | - | - | - |
| `kyrah` | 535 | - | - | - |
| `laser-maze` | 370 | - | - | - |
| `last-one-standing` | 239 | - | - | - |
| `late-night-crew` | 739 | - | - | - |
| `legend-25` | 209 | - | - | - |
| `level-six` | 1,147 | - | - | - |
| `list-of-head-of-household-competitions` | 2,948 | - | - | - |
| `list-of-power-of-veto-competitions` | 1,570 | - | - | - |
| `list-of-recurring-competitions` | 1,935 | - | - | - |
| `living-art` | 255 | - | - | - |
| `log-roll` | 69 | - | - | - |
| `los-tres-amigos` | 163 | - | - | - |
| `lots-of-love` | 431 | - | - | - |
| `majority-rules` | 300 | - | - | - |
| `mama-s-angels` | 172 | - | - | - |
| `marlena` | 104 | - | - | - |
| `match-it` | 71 | - | - | - |
| `melodrew` | 2,182 | - | - | - |
| `memory-dip` | 60 | - | - | - |
| `microbrews` | 309 | - | - | - |
| `microchip-mayhem` | 119 | - | - | - |
| `million-club` | 245 | - | - | - |
| `morph-o-matic` | 586 | - | - | - |
| `mosh-pit` | 622 | - | - | - |
| `most-valuable-player` | 343 | - | - | - |
| `mr.and-mrs.smith-alliance` | 118 | - | - | - |
| `mrs.robinson-alliance` | 794 | - | - | - |
| `new-rule` | 59 | - | - | - |
| `newbies` | 547 | - | - | - |
| `niagara-balls` | 384 | - | - | - |
| `nicorey` | 247 | - | - | - |
| `no-names` | 611 | - | - | - |
| `nomination-competition` | 1,415 | - | - | - |
| `nominations` | 5,649 | - | - | - |
| `oasis` | 358 | - | - | - |
| `off-the-block` | 1,025 | - | - | - |
| `old-skool` | 415 | - | - | - |
| `only-one-path` | 127 | - | - | - |
| `otev` | 1,461 | - | - | - |
| `pandora-s-box` | 924 | - | - | - |
| `peach-cobbler` | 167 | - | - | - |
| `perfect-game` | 1,454 | - | - | - |
| `perfect-shot` | 1,086 | - | - | - |
| `phalanx-5` | 490 | - | - | - |
| `pinky-swear-alliance` | 601 | - | - | - |
| `pipeline` | 90 | - | - | - |
| `po-s-pack` | 450 | - | - | - |
| `pose-in-ivy` | 108 | - | - | - |
| `power-couple` | 226 | - | - | - |
| `power-of-veto` | 4,086 | - | - | - |
| `premiere-night-eviction` | 853 | - | - | - |
| `pressure-cooker` | 753 | - | - | - |
| `previously-evicted-contestant` | 4,667 | - | - | - |
| `project-dna` | 1,506 | - | - | - |
| `pull-some-strings` | 249 | - | - | - |
| `punch-slap-kick` | 626 | - | - | - |
| `pyramid` | 191 | - | - | - |
| `queens` | 466 | - | - | - |
| `re-entry-competition` | 439 | - | - | - |
| `ready-set-woah` | 634 | - | - | - |
| `reclaim-the-relic` | 126 | - | - | - |
| `records-statistics` | 12,662 | - | - | - |
| `repeat-after-me` | 624 | - | - | - |
| `repetitive-task-punishment` | 599 | - | - | - |
| `returning-players` | 4,389 | - | - | - |
| `rewind-button` | 136 | - | - | - |
| `ride-the-rocket` | 162 | - | - | - |
| `rivals` | 110 | - | - | - |
| `roadkill-competition` | 448 | - | - | - |
| `rockstars` | 1,218 | - | - | - |
| `rogue-rats` | 682 | - | - | - |
| `roll-it-down` | 341 | - | - | - |
| `rollerball` | 140 | - | - | - |
| `rollin-in-the-dough` | 220 | - | - | - |
| `rookies` | 166 | - | - | - |
| `round-trip-ticket` | 320 | - | - | - |
| `rush-hour` | 135 | - | - | - |
| `safety-suite-competition` | 472 | - | - | - |
| `sam-s-boys` | 164 | - | - | - |
| `scamper-squad` | 3,244 | - | - | - |
| `scorpio-sisters` | 282 | - | - | - |
| `scyler` | 139 | - | - | - |
| `second-chance-challenge` | 2,829 | - | - | - |
| `secret-power-competition` | 660 | - | - | - |
| `secret-room` | 1,958 | - | - | - |
| `seesaw` | 341 | - | - | - |
| `sequence-explosion` | 255 | - | - | - |
| `shackles` | 441 | - | - | - |
| `shelltown` | 174 | - | - | - |
| `shootout` | 607 | - | - | - |
| `silent-six` | 464 | - | - | - |
| `sirens` | 179 | - | - | - |
| `six-shooters` | 383 | - | - | - |
| `sixth-avenue` | 187 | - | - | - |
| `sky-high-memory` | 90 | - | - | - |
| `slapshot` | 619 | - | - | - |
| `sleeper-cell` | 161 | - | - | - |
| `slick-six` | 190 | - | - | - |
| `slingshot-aim` | 138 | - | - | - |
| `slippery-slope` | 1,437 | - | - | - |
| `slop` | 386 | - | - | - |
| `snake-eyes` | 622 | - | - | - |
| `snapshot-shuffle` | 78 | - | - | - |
| `solitary-confinement` | 79 | - | - | - |
| `somewhere-over-the-veto` | 370 | - | - | - |
| `soulmates` | 339 | - | - | - |
| `sovereign-six` | 936 | - | - | - |
| `spelling-search` | 611 | - | - | - |
| `spy-girls` | 1,246 | - | - | - |
| `stage-five` | 308 | - | - | - |
| `starting-lineup` | 609 | - | - | - |
| `staten-island` | 177 | - | - | - |
| `stay-or-fold` | 602 | - | - | - |
| `strong-side` | 171 | - | - | - |
| `students-of-sound` | 140 | - | - | - |
| `swayleigh` | 259 | - | - | - |
| `swing-slam-dunk` | 118 | - | - | - |
| `take-it-off` | 181 | - | - | - |
| `tangela` | 726 | - | - | - |
| `tea-party` | 1,660 | - | - | - |
| `team-america` | 1,060 | - | - | - |
| `team-boogie` | 185 | - | - | - |
| `team-britney` | 135 | - | - | - |
| `team-christ` | 119 | - | - | - |
| `team-dan` | 209 | - | - | - |
| `team-freeze` | 185 | - | - | - |
| `team-janelle` | 268 | - | - | - |
| `team-jesus` | 143 | - | - | - |
| `team-jj` | 128 | - | - | - |
| `team-pp` | 168 | - | - | - |
| `team-touch` | 231 | - | - | - |
| `team-unicorn` | 186 | - | - | - |
| `teams` | 1,232 | - | - | - |
| `temptation-competition` | 841 | - | - | - |
| `tenexas` | 293 | - | - | - |
| `terek` | 292 | - | - | - |
| `the-afterparty` | 473 | - | - | - |
| `the-amazons` | 198 | - | - | - |
| `the-andersons` | 202 | - | - | - |
| `the-athletes` | 152 | - | - | - |
| `the-barbershop` | 372 | - | - | - |
| `the-black-box` | 822 | - | - | - |
| `the-black-ops` | 174 | - | - | - |
| `the-blonde-tourage` | 519 | - | - | - |
| `the-board` | 197 | - | - | - |
| `the-bond` | 266 | - | - | - |
| `the-bookends` | 583 | - | - | - |
| `the-brains` | 195 | - | - | - |
| `the-brigade` | 1,288 | - | - | - |
| `the-butchers` | 378 | - | - | - |
| `the-carolinas` | 210 | - | - | - |
| `the-ceasefire` | 226 | - | - | - |
| `the-chenbots` | 737 | - | - | - |
| `the-chillers` | 297 | - | - | - |
| `the-collective` | 175 | - | - | - |
| `the-commission` | 134 | - | - | - |
| `the-committee` | 1,177 | - | - | - |
| `the-connect` | 231 | - | - | - |
| `the-connect-bb23` | 179 | - | - | - |
| `the-cookout` | 1,202 | - | - | - |
| `the-core` | 220 | - | - | - |
| `the-core-four` | 150 | - | - | - |
| `the-court-jesters` | 186 | - | - | - |
| `the-coven` | 256 | - | - | - |
| `the-covenant` | 179 | - | - | - |
| `the-critics` | 137 | - | - | - |
| `the-crossovers` | 1,993 | - | - | - |
| `the-crossroads` | 184 | - | - | - |
| `the-crow-boys` | 146 | - | - | - |
| `the-culture` | 246 | - | - | - |
| `the-dapper-dans` | 201 | - | - | - |
| `the-detectives` | 147 | - | - | - |
| `the-detonators` | 916 | - | - | - |
| `the-executives` | 439 | - | - | - |
| `the-exterminators` | 540 | - | - | - |
| `the-fatal-spies` | 163 | - | - | - |
| `the-fellowship-of-the-zing` | 220 | - | - | - |
| `the-fields` | 641 | - | - | - |
| `the-five-swatters` | 367 | - | - | - |
| `the-flop` | 180 | - | - | - |
| `the-frenemies` | 163 | - | - | - |
| `the-friendship` | 308 | - | - | - |
| `the-fugitives` | 372 | - | - | - |
| `the-goblins` | 517 | - | - | - |
| `the-goof-troupe` | 470 | - | - | - |
| `the-handful` | 475 | - | - | - |
| `the-handymen` | 174 | - | - | - |
| `the-haunting` | 86 | - | - | - |
| `the-hitmen` | 625 | - | - | - |
| `the-hive` | 299 | - | - | - |
| `the-honor-society` | 189 | - | - | - |
| `the-icons` | 1,398 | - | - | - |
| `the-judges` | 1,008 | - | - | - |
| `the-jugglers` | 1,842 | - | - | - |
| `the-kingslayers` | 178 | - | - | - |
| `the-leftovers` | 1,237 | - | - | - |
| `the-legion-of-doom` | 431 | - | - | - |
| `the-lorraines` | 136 | - | - | - |
| `the-love-triangle` | 1,097 | - | - | - |
| `the-mafia-bb23` | 181 | - | - | - |
| `the-mafia-bb25` | 589 | - | - | - |
| `the-mastermind` | 561 | - | - | - |
| `the-maze` | 82 | - | - | - |
| `the-melting-pot` | 189 | - | - | - |
| `the-minutemen` | 348 | - | - | - |
| `the-misfits` | 152 | - | - | - |
| `the-mom-squad-bb15` | 1,293 | - | - | - |
| `the-mom-squad-bb27` | 345 | - | - | - |
| `the-moving-company` | 544 | - | - | - |
| `the-night-owls` | 1,079 | - | - | - |
| `the-night-shift` | 384 | - | - | - |
| `the-oddballs` | 142 | - | - | - |
| `the-off-beats` | 118 | - | - | - |
| `the-original-six` | 145 | - | - | - |
| `the-other-people` | 612 | - | - | - |
| `the-pentagon` | 171 | - | - | - |
| `the-populars` | 168 | - | - | - |
| `the-pound` | 519 | - | - | - |
| `the-primaries` | 185 | - | - | - |
| `the-professors` | 352 | - | - | - |
| `the-quack-pack` | 683 | - | - | - |
| `the-radicals` | 177 | - | - | - |
| `the-rationale` | 141 | - | - | - |
| `the-real-fields` | 184 | - | - | - |
| `the-red-corner` | 260 | - | - | - |
| `the-regulators` | 294 | - | - | - |
| `the-renegades` | 1,314 | - | - | - |
| `the-returners` | 546 | - | - | - |
| `the-revolution` | 185 | - | - | - |
| `the-root` | 125 | - | - | - |
| `the-royal-flush` | 180 | - | - | - |
| `the-saboteur` | 993 | - | - | - |
| `the-sacred-six` | 195 | - | - | - |
| `the-secret-alliance` | 1,073 | - | - | - |
| `the-sirens` | 362 | - | - | - |
| `the-sitting-ducks` | 153 | - | - | - |
| `the-sixth-sense` | 2,127 | - | - | - |
| `the-slaughterhouse` | 552 | - | - | - |
| `the-slitherpuffs` | 174 | - | - | - |
| `the-snoots` | 134 | - | - | - |
| `the-team` | 2,562 | - | - | - |
| `the-toolshed` | 734 | - | - | - |
| `the-trio` | 1,407 | - | - | - |
| `the-unexpendables` | 175 | - | - | - |
| `the-unreliables` | 473 | - | - | - |
| `the-untouchables` | 347 | - | - | - |
| `the-vendetta` | 170 | - | - | - |
| `the-visionaries` | 311 | - | - | - |
| `the-vixens` | 276 | - | - | - |
| `the-walking-dead` | 113 | - | - | - |
| `the-wall` | 1,813 | - | - | - |
| `the-weirdos` | 299 | - | - | - |
| `the-wingmen` | 127 | - | - | - |
| `the-wise-guys` | 209 | - | - | - |
| `the-wolfpack` | 189 | - | - | - |
| `the-writers-room` | 398 | - | - | - |
| `the-zingbot` | 1,160 | - | - | - |
| `three-s-company` | 132 | - | - | - |
| `three-stooges` | 625 | - | - | - |
| `threemance` | 179 | - | - | - |
| `tiffney` | 225 | - | - | - |
| `time-flies` | 142 | - | - | - |
| `time-highway` | 85 | - | - | - |
| `to-drink-or-to-bluff` | 99 | - | - | - |
| `tower-of-hanoi` | 157 | - | - | - |
| `tree-of-temptation` | 214 | - | - | - |
| `triple-eviction` | 1,092 | - | - | - |
| `triple-threat-bb22` | 176 | - | - | - |
| `triple-threat-bb27` | 895 | - | - | - |
| `triplets` | 146 | - | - | - |
| `tubina` | 144 | - | - | - |
| `tumblin-dice` | 130 | - | - | - |
| `two-sweet` | 161 | - | - | - |
| `unde9able` | 772 | - | - | - |
| `unitard` | 1,544 | - | - | - |
| `unpopular-alliance` | 112 | - | - | - |
| `veterans` | 727 | - | - | - |
| `veto-replacement` | 135 | - | - | - |
| `watch-your-step` | 75 | - | - | - |
| `weight-gain` | 67 | - | - | - |
| `whacktivity-competition` | 544 | - | - | - |
| `what-competition-was-that` | 598 | - | - | - |
| `what-did-they-just-do` | 1,015 | - | - | - |
| `what-s-the-hold-up` | 403 | - | - | - |
| `what-the-bleep` | 560 | - | - | - |
| `wheel-of-first-impressions` | 422 | - | - | - |
| `whenchie` | 149 | - | - | - |
| `where-were-you` | 636 | - | - | - |
| `whistlenut-ole` | 155 | - | - | - |
| `who-did-what` | 997 | - | - | - |
| `who-said-it` | 241 | - | - | - |
| `wildcard-competition` | 440 | - | - | - |
| `will-s-daughters` | 141 | - | - | - |
| `winners-us` | 1,266 | - | - | - |
| `x-factor` | 212 | - | - | - |
| `yankee-swap` | 1,022 | - | - | - |
| `young-grasshoppers` | 350 | - | - | - |
| `zankie` | 321 | - | - | - |
| `zaulie` | 133 | - | - | - |
| `zingbot-competition` | 845 | - | - | - |

## Not added in the last run

- `100-minutes.html`: The text is the same as `100-minutes`, which is already in the corpus.
- `3-a.m..html`: The text is the same as `3-a.m`, which is already in the corpus.
- `3-way-rats.html`: The text is the same as `3-way-rats`, which is already in the corpus.
- `4-seasons.html`: The text is the same as `4-seasons`, which is already in the corpus.
- `7-deadly-sins.html`: The text is the same as `7-deadly-sins`, which is already in the corpus.
- `8-pack.html`: The text is the same as `8-pack`, which is already in the corpus.
- `aces.html`: The text is the same as `aces`, which is already in the corpus.
- `adorkables.html`: The text is the same as `adorkables`, which is already in the corpus.
- `ai-chip-install.html`: The text is the same as `ai-chip-install`, which is already in the corpus.
- `ainsley.html`: The text is the same as `ainsley`, which is already in the corpus.
- `america-s-care-package.html`: The text is the same as `america-s-care-package`, which is already in the corpus.
- `america-s-eviction-vote.html`: The text is the same as `america-s-eviction-vote`, which is already in the corpus.
- `america-s-field-trip.html`: The text is the same as `america-s-field-trip`, which is already in the corpus.
- `america-s-nominee.html`: The text is the same as `america-s-nominee`, which is already in the corpus.
- `america-s-player.html`: The text is the same as `america-s-player`, which is already in the corpus.
- `america-s-winner.html`: The text is the same as `america-s-winner`, which is already in the corpus.
- `americory.html`: The text is the same as `americory`, which is already in the corpus.
- `an-offer-you-can-t-refuse.html`: The text is the same as `an-offer-you-can-t-refuse`, which is already in the corpus.
- `area-51-alliance.html`: The text is the same as `area-51-alliance`, which is already in the corpus.
- `as-close-as-you-can.html`: The text is the same as `as-close-as-you-can`, which is already in the corpus.
- `ask-the-evictee.html`: The text is the same as `ask-the-evictee`, which is already in the corpus.
- `austwins.html`: The text is the same as `austwins`, which is already in the corpus.
- `ball-roll.html`: The text is the same as `ball-roll`, which is already in the corpus.
- `bash.html`: The text is the same as `bash`, which is already in the corpus.
- `battle-back-competition.html`: The text is the same as `battle-back-competition`, which is already in the corpus.
- `battle-of-the-block.html`: The text is the same as `battle-of-the-block`, which is already in the corpus.
- `bb-app-store.html`: The text is the same as `bb-app-store`, which is already in the corpus.
- `bb-besties.html`: The text is the same as `bb-besties`, which is already in the corpus.
- `bb-comics.html`: The text is the same as `bb-comics`, which is already in the corpus.
- `bb-flix-chill.html`: The text is the same as `bb-flix-chill`, which is already in the corpus.
- `bb-guns.html`: The text is the same as `bb-guns`, which is already in the corpus.
- `bb-power-of-invincibility.html`: The text is the same as `bb-power-of-invincibility`, which is already in the corpus.
- `bb-rewind.html`: The text is the same as `bb-rewind`, which is already in the corpus.
- `bb-storm-watch.html`: The text is the same as `bb-storm-watch`, which is already in the corpus.
- `bb-takeover.html`: The text is the same as `bb-takeover`, which is already in the corpus.
- `before-or-after.html`: The text is the same as `before-or-after`, which is already in the corpus.
- `bermuda-triangle.html`: The text is the same as `bermuda-triangle`, which is already in the corpus.
- `berry-balanced.html`: The text is the same as `berry-balanced`, which is already in the corpus.
- `big-brother-1-us.html`: The text is the same as `big-brother-1-us`, which is already in the corpus.
- `big-brother-10-us.html`: The text is the same as `big-brother-10-us`, which is already in the corpus.
- `big-brother-11-us.html`: The text is the same as `big-brother-11-us`, which is already in the corpus.
- `big-brother-12-us.html`: The text is the same as `big-brother-12-us`, which is already in the corpus.
- `big-brother-13-gallery.html`: The text is the same as `big-brother-13-gallery`, which is already in the corpus.
- `big-brother-13-us.html`: The text is the same as `big-brother-13-us`, which is already in the corpus.
- `big-brother-14-us.html`: The text is the same as `big-brother-14-us`, which is already in the corpus.
- `big-brother-15-us.html`: The text is the same as `big-brother-15-us`, which is already in the corpus.
- `big-brother-16-us.html`: The text is the same as `big-brother-16-us`, which is already in the corpus.
- `big-brother-17-us.html`: The text is the same as `big-brother-17-us`, which is already in the corpus.
- `big-brother-18-us.html`: The text is the same as `big-brother-18-us`, which is already in the corpus.
- `big-brother-19-us.html`: The text is the same as `big-brother-19-us`, which is already in the corpus.
- `big-brother-2-us.html`: The text is the same as `big-brother-2-us`, which is already in the corpus.
- `big-brother-20-us.html`: The text is the same as `big-brother-20-us`, which is already in the corpus.
- `big-brother-21-us.html`: The text is the same as `big-brother-21-us`, which is already in the corpus.
- `big-brother-22-us.html`: The text is the same as `big-brother-22-us`, which is already in the corpus.
- `big-brother-23-us.html`: The text is the same as `big-brother-23-us`, which is already in the corpus.
- `big-brother-24-us.html`: The text is the same as `big-brother-24-us`, which is already in the corpus.
- `big-brother-25-us.html`: The text is the same as `big-brother-25-us`, which is already in the corpus.
- `big-brother-25th-anniversary-celebration.html`: The text is the same as `big-brother-25th-anniversary-celebration`, which is already in the corpus.
- `big-brother-26-us.html`: The text is the same as `big-brother-26-us`, which is already in the corpus.
- `big-brother-27-us.html`: The text is the same as `big-brother-27-us`, which is already in the corpus.
- `big-brother-28-us.html`: The text is the same as `big-brother-28-us`, which is already in the corpus.
- `big-brother-29-us.html`: The text is the same as `big-brother-29-us`, which is already in the corpus.
- `big-brother-3-us.html`: The text is the same as `big-brother-3-us`, which is already in the corpus.
- `big-brother-30-us.html`: The text is the same as `big-brother-30-us`, which is already in the corpus.
- `big-brother-4-us.html`: The text is the same as `big-brother-4-us`, which is already in the corpus.
- `big-brother-5-us.html`: The text is the same as `big-brother-5-us`, which is already in the corpus.
- `big-brother-6-us.html`: The text is the same as `big-brother-6-us`, which is already in the corpus.
- `big-brother-7-us.html`: The text is the same as `big-brother-7-us`, which is already in the corpus.
- `big-brother-8-us.html`: The text is the same as `big-brother-8-us`, which is already in the corpus.
- `big-brother-9-us.html`: The text is the same as `big-brother-9-us`, which is already in the corpus.
- `big-brother-after-dark.html`: The text is the same as `big-brother-after-dark`, which is already in the corpus.
- `big-brother-all-stars-us.html`: The text is the same as `big-brother-all-stars-us`, which is already in the corpus.
- `big-brother-house-australia.html`: The text is the same as `big-brother-house-australia`, which is already in the corpus.
- `big-brother-house-brazil.html`: The text is the same as `big-brother-house-brazil`, which is already in the corpus.
- `big-brother-house-canada.html`: The text is the same as `big-brother-house-canada`, which is already in the corpus.
- `big-brother-house-israel.html`: The text is the same as `big-brother-house-israel`, which is already in the corpus.
- `big-brother-house-nigeria.html`: The text is the same as `big-brother-house-nigeria`, which is already in the corpus.
- `big-brother-house-philippines.html`: The text is the same as `big-brother-house-philippines`, which is already in the corpus.
- `big-brother-house-portugal.html`: The text is the same as `big-brother-house-portugal`, which is already in the corpus.
- `big-brother-house-united-kingdom.html`: The text is the same as `big-brother-house-united-kingdom`, which is already in the corpus.
- `big-brother-house-united-states.html`: The text is the same as `big-brother-house-united-states`, which is already in the corpus.
- `big-brother-house.html`: The text is the same as `big-brother-house`, which is already in the corpus.
- `big-brother-live-chat.html`: The text is the same as `big-brother-live-chat`, which is already in the corpus.
- `big-brother-rule-book.html`: The text is the same as `big-brother-rule-book`, which is already in the corpus.
- `big-brother-swap.html`: The text is the same as `big-brother-swap`, which is already in the corpus.
- `big-brother-unlocked-season-1.html`: The text is the same as `big-brother-unlocked-season-1`, which is already in the corpus.
- `big-brother-unlocked-season-2.html`: The text is the same as `big-brother-unlocked-season-2`, which is already in the corpus.
- `big-brother-unlocked.html`: The text is the same as `big-brother-unlocked`, which is already in the corpus.
- `big-brother.html`: The text is the same as `big-brother`, which is already in the corpus.
- `big-sister-alliance.html`: The text is the same as `big-sister-alliance`, which is already in the corpus.
- `big-sister.html`: The text is the same as `big-sister`, which is already in the corpus.
- `big-top-drop.html`: The text is the same as `big-top-drop`, which is already in the corpus.
- `binary-bridge.html`: The text is the same as `binary-bridge`, which is already in the corpus.
- `black-girl-magic-bb22.html`: The text is the same as `black-girl-magic-bb22`, which is already in the corpus.
- `block-and-roll.html`: The text is the same as `block-and-roll`, which is already in the corpus.
- `blockbusters.html`: The text is the same as `blockbusters`, which is already in the corpus.
- `bomb-squad.html`: The text is the same as `bomb-squad`, which is already in the corpus.
- `bond-girls.html`: The text is the same as `bond-girls`, which is already in the corpus.
- `boomerang-power-of-veto.html`: The text is the same as `boomerang-power-of-veto`, which is already in the corpus.
- `bowlerina.html`: The text is the same as `bowlerina`, which is already in the corpus.
- `brad-chad.html`: The text is the same as `brad-chad`, which is already in the corpus.
- `break-the-ice.html`: The text is the same as `break-the-ice`, which is already in the corpus.
- `brenchel.html`: The text is the same as `brenchel`, which is already in the corpus.
- `brenchie.html`: The text is the same as `brenchie`, which is already in the corpus.
- `bros.html`: The text is the same as `bros`, which is already in the corpus.
- `brown-sugar-babes.html`: The text is the same as `brown-sugar-babes`, which is already in the corpus.
- `build-the-bridge.html`: The text is the same as `build-the-bridge`, which is already in the corpus.
- `burger-boys.html`: The text is the same as `burger-boys`, which is already in the corpus.
- `bye-bye-bitches.html`: The text is the same as `bye-bye-bitches`, which is already in the corpus.
- `caf-con-leche.html`: The text is the same as `caf-con-leche`, which is already in the corpus.
- `caged-eggs.html`: The text is the same as `caged-eggs`, which is already in the corpus.
- `camp-comeback.html`: The text is the same as `camp-comeback`, which is already in the corpus.
- `camp-director.html`: The text is the same as `camp-director`, which is already in the corpus.
- `carnival-quick-shot.html`: The text is the same as `carnival-quick-shot`, which is already in the corpus.
- `cartel.html`: The text is the same as `cartel`, which is already in the corpus.
- `category-four.html`: The text is the same as `category-four`, which is already in the corpus.
- `cbs.html`: The text is the same as `cbs`, which is already in the corpus.
- `chilltown.html`: The text is the same as `chilltown`, which is already in the corpus.
- `chrenchie.html`: The text is the same as `chrenchie`, which is already in the corpus.
- `chrisalyss.html`: The text is the same as `chrisalyss`, which is already in the corpus.
- `clelli.html`: The text is the same as `clelli`, which is already in the corpus.
- `cliff-s-angels.html`: The text is the same as `cliff-s-angels`, which is already in the corpus.
- `clique.html`: The text is the same as `clique`, which is already in the corpus.
- `close-to-20.html`: The text is the same as `close-to-20`, which is already in the corpus.
- `coach.html`: The text is the same as `coach`, which is already in the corpus.
- `coaches-competition.html`: The text is the same as `coaches-competition`, which is already in the corpus.
- `coast2coast.html`: The text is the same as `coast2coast`, which is already in the corpus.
- `coup-d-etat.html`: The text is the same as `coup-d-etat`, which is already in the corpus.
- `cover-your-days.html`: The text is the same as `cover-your-days`, which is already in the corpus.
- `crazy-8s.html`: The text is the same as `crazy-8s`, which is already in the corpus.
- `croquet.html`: The text is the same as `croquet`, which is already in the corpus.
- `crowd-control-bb26.html`: The text is the same as `crowd-control-bb26`, which is already in the corpus.
- `crowd-control.html`: The text is the same as `crowd-control`, which is already in the corpus.
- `dark-moon.html`: The text is the same as `dark-moon`, which is already in the corpus.
- `defected-newbie-alliance.html`: The text is the same as `defected-newbie-alliance`, which is already in the corpus.
- `den-of-temptation.html`: The text is the same as `den-of-temptation`, which is already in the corpus.
- `derstian.html`: The text is the same as `derstian`, which is already in the corpus.
- `diamond-power-of-veto.html`: The text is the same as `diamond-power-of-veto`, which is already in the corpus.
- `digital-decryption.html`: The text is the same as `digital-decryption`, which is already in the corpus.
- `dizzy-discs.html`: The text is the same as `dizzy-discs`, which is already in the corpus.
- `domino-effect.html`: The text is the same as `domino-effect`, which is already in the corpus.
- `don-t-miss-a-beat.html`: The text is the same as `don-t-miss-a-beat`, which is already in the corpus.
- `double-d-s.html`: The text is the same as `double-d-s`, which is already in the corpus.
- `double-eviction.html`: The text is the same as `double-eviction`, which is already in the corpus.
- `double-power-of-veto.html`: The text is the same as `double-power-of-veto`, which is already in the corpus.
- `double-the-fun.html`: The text is the same as `double-the-fun`, which is already in the corpus.
- `downlowmance.html`: The text is the same as `downlowmance`, which is already in the corpus.
- `drenchie.html`: The text is the same as `drenchie`, which is already in the corpus.
- `drinks-on-us.html`: The text is the same as `drinks-on-us`, which is already in the corpus.
- `dynamic-duos.html`: The text is the same as `dynamic-duos`, which is already in the corpus.
- `el-cuatro.html`: The text is the same as `el-cuatro`, which is already in the corpus.
- `eliminator.html`: The text is the same as `eliminator`, which is already in the corpus.
- `elite-eight.html`: The text is the same as `elite-eight`, which is already in the corpus.
- `eternal-immunity.html`: The text is the same as `eternal-immunity`, which is already in the corpus.
- `eviction.html`: The text is the same as `eviction`, which is already in the corpus.
- `f.a.p..html`: The text is the same as `f.a.p`, which is already in the corpus.
- `facial-recognition.html`: The text is the same as `facial-recognition`, which is already in the corpus.
- `fam-five.html`: The text is the same as `fam-five`, which is already in the corpus.
- `family-style.html`: The text is the same as `family-style`, which is already in the corpus.
- `faster-than-a-speeding-veto.html`: The text is the same as `faster-than-a-speeding-veto`, which is already in the corpus.
- `fatal-five.html`: The text is the same as `fatal-five`, which is already in the corpus.
- `feel-the-burn.html`: The text is the same as `feel-the-burn`, which is already in the corpus.
- `feeling-knotty.html`: The text is the same as `don-t-miss-a-beat`, which is already in the corpus.
- `final-four-bb11.html`: The text is the same as `final-four-bb11`, which is already in the corpus.
- `final-four-bb18.html`: The text is the same as `final-four-bb18`, which is already in the corpus.
- `final-three-bb26.html`: The text is the same as `final-three-bb26`, which is already in the corpus.
- `finger-guns-alliance.html`: The text is the same as `finger-guns-alliance`, which is already in the corpus.
- `fitting-in.html`: The text is the same as `fitting-in`, which is already in the corpus.
- `five-pointz.html`: The text is the same as `five-pointz`, which is already in the corpus.
- `flaming-five.html`: The text is the same as `flaming-five`, which is already in the corpus.
- `flower-power.html`: The text is the same as `flower-power`, which is already in the corpus.
- `foam-party.html`: The text is the same as `foam-party`, which is already in the corpus.
- `food-competition.html`: The text is the same as `food-competition`, which is already in the corpus.
- `for-real-for-real.html`: The text is the same as `for-real-for-real`, which is already in the corpus.
- `four-horsemen.html`: The text is the same as `four-horsemen`, which is already in the corpus.
- `four-prime.html`: The text is the same as `four-prime`, which is already in the corpus.
- `foutte.html`: The text is the same as `foutte`, which is already in the corpus.
- `freakazoids.html`: The text is the same as `freakazoids`, which is already in the corpus.
- `french-kisses.html`: The text is the same as `french-kisses`, which is already in the corpus.
- `gear-puzzle.html`: The text is the same as `gear-puzzle`, which is already in the corpus.
- `get-a-grip.html`: The text is the same as `get-a-grip`, which is already in the corpus.
- `getting-loopy.html`: The text is the same as `getting-loopy`, which is already in the corpus.
- `giddy-up.html`: The text is the same as `giddy-up`, which is already in the corpus.
- `giggle-girls.html`: The text is the same as `giggle-girls`, which is already in the corpus.
- `girl-power.html`: The text is the same as `girl-power`, which is already in the corpus.
- `girls-girls-bb27.html`: The text is the same as `girls-girls-bb27`, which is already in the corpus.
- `girls-girls.html`: The text is the same as `girls-girls`, which is already in the corpus.
- `golden-girlies.html`: The text is the same as `golden-girlies`, which is already in the corpus.
- `golden-key.html`: The text is the same as `golden-key`, which is already in the corpus.
- `golf-invitational.html`: The text is the same as `golf-invitational`, which is already in the corpus.
- `gr8ful.html`: The text is the same as `gr8ful`, which is already in the corpus.
- `hacker-competition.html`: The text is the same as `hacker-competition`, which is already in the corpus.
- `have-have-not-competition.html`: The text is the same as `have-have-not-competition`, which is already in the corpus.
- `head-of-household.html`: The text is the same as `head-of-household`, which is already in the corpus.
- `heavy-hitters.html`: The text is the same as `heavy-hitters`, which is already in the corpus.
- `hide-and-go-veto.html`: The text is the same as `hide-and-go-veto`, which is already in the corpus.
- `hide-and-seek.html`: The text is the same as `hide-and-seek`, which is already in the corpus.
- `hit-the-road.html`: The text is the same as `hit-the-road`, which is already in the corpus.
- `hourglass.html`: The text is the same as `hourglass`, which is already in the corpus.
- `house-calls-the-big-brother-talk-show.html`: The text is the same as `house-calls-the-big-brother-talk-show`, which is already in the corpus.
- `house-currency.html`: The text is the same as `house-currency`, which is already in the corpus.
- `houseguest-description.html`: The text is the same as `houseguest-description`, which is already in the corpus.
- `houseguestsonly.com.html`: The text is the same as `houseguestsonly.com`, which is already in the corpus.
- `housemates.html`: The text is the same as `housemates`, which is already in the corpus.
- `how-bad-do-you-want-it.html`: The text is the same as `how-bad-do-you-want-it`, which is already in the corpus.
- `immunity-competition.html`: The text is the same as `immunity-competition`, which is already in the corpus.
- `in-the-balance.html`: The text is the same as `in-the-balance`, which is already in the corpus.
- `invisible-hoh.html`: The text is the same as `invisible-hoh`, which is already in the corpus.
- `it-s-time-to-reflect.html`: The text is the same as `it-s-time-to-reflect`, which is already in the corpus.
- `item-catching.html`: The text is the same as `item-catching`, which is already in the corpus.
- `item-maze.html`: The text is the same as `item-maze`, which is already in the corpus.
- `jackpot.html`: The text is the same as `jackpot`, which is already in the corpus.
- `jankie.html`: The text is the same as `jankie`, which is already in the corpus.
- `jatalie.html`: The text is the same as `jatalie`, which is already in the corpus.
- `jaylor.html`: The text is the same as `jaylor`, which is already in the corpus.
- `jaysar.html`: The text is the same as `jaysar`, which is already in the corpus.
- `jecky.html`: The text is the same as `jecky`, which is already in the corpus.
- `jessie-s-alliance.html`: The text is the same as `jessie-s-alliance`, which is already in the corpus.
- `jetpack-attack.html`: The text is the same as `jetpack-attack`, which is already in the corpus.
- `jody.html`: The text is the same as `jody`, which is already in the corpus.
- `jokers.html`: The text is the same as `jokers`, which is already in the corpus.
- `jury-removal.html`: The text is the same as `jury-removal`, which is already in the corpus.
- `jury-statements.html`: The text is the same as `jury-statements`, which is already in the corpus.
- `kaitlyn-s-puzzle.html`: The text is the same as `kaitlyn-s-puzzle`, which is already in the corpus.
- `kings.html`: The text is the same as `kings`, which is already in the corpus.
- `knight-moves.html`: The text is the same as `knight-moves`, which is already in the corpus.
- `knockout.html`: The text is the same as `knockout`, which is already in the corpus.
- `kyrah.html`: The text is the same as `kyrah`, which is already in the corpus.
- `laser-maze.html`: The text is the same as `laser-maze`, which is already in the corpus.
- `last-one-standing.html`: The text is the same as `last-one-standing`, which is already in the corpus.
- `late-night-crew.html`: The text is the same as `late-night-crew`, which is already in the corpus.
- `legend-25.html`: The text is the same as `legend-25`, which is already in the corpus.
- `level-six.html`: The text is the same as `level-six`, which is already in the corpus.
- `list-of-head-of-household-competitions.html`: The text is the same as `list-of-head-of-household-competitions`, which is already in the corpus.
- `list-of-power-of-veto-competitions.html`: The text is the same as `list-of-power-of-veto-competitions`, which is already in the corpus.
- `list-of-recurring-competitions.html`: The text is the same as `list-of-recurring-competitions`, which is already in the corpus.
- `living-art.html`: The text is the same as `living-art`, which is already in the corpus.
- `log-roll.html`: The text is the same as `log-roll`, which is already in the corpus.
- `los-tres-amigos.html`: The text is the same as `los-tres-amigos`, which is already in the corpus.
- `lots-of-love.html`: The text is the same as `lots-of-love`, which is already in the corpus.
- `majority-rules.html`: The text is the same as `majority-rules`, which is already in the corpus.
- `mama-s-angels.html`: The text is the same as `mama-s-angels`, which is already in the corpus.
- `marlena.html`: The text is the same as `marlena`, which is already in the corpus.
- `match-it.html`: The text is the same as `match-it`, which is already in the corpus.
- `melodrew.html`: The text is the same as `melodrew`, which is already in the corpus.
- `memory-dip.html`: The text is the same as `memory-dip`, which is already in the corpus.
- `microbrews.html`: The text is the same as `microbrews`, which is already in the corpus.
- `microchip-mayhem.html`: The text is the same as `microchip-mayhem`, which is already in the corpus.
- `million-club.html`: The text is the same as `million-club`, which is already in the corpus.
- `morph-o-matic.html`: The text is the same as `morph-o-matic`, which is already in the corpus.
- `mosh-pit.html`: The text is the same as `mosh-pit`, which is already in the corpus.
- `most-valuable-player.html`: The text is the same as `most-valuable-player`, which is already in the corpus.
- `mr.-and-mrs.-smith-alliance.html`: The text is the same as `mr.and-mrs.smith-alliance`, which is already in the corpus.
- `mrs.-robinson-alliance.html`: The text is the same as `mrs.robinson-alliance`, which is already in the corpus.
- `new-rule.html`: The text is the same as `new-rule`, which is already in the corpus.
- `newbies.html`: The text is the same as `newbies`, which is already in the corpus.
- `niagara-balls.html`: The text is the same as `niagara-balls`, which is already in the corpus.
- `nicorey.html`: The text is the same as `nicorey`, which is already in the corpus.
- `no-names.html`: The text is the same as `no-names`, which is already in the corpus.
- `nomination-competition.html`: The text is the same as `nomination-competition`, which is already in the corpus.
- `nominations.html`: The text is the same as `nominations`, which is already in the corpus.
- `oasis.html`: The text is the same as `oasis`, which is already in the corpus.
- `off-the-block.html`: The text is the same as `off-the-block`, which is already in the corpus.
- `old-skool.html`: The text is the same as `old-skool`, which is already in the corpus.
- `only-one-path.html`: The text is the same as `only-one-path`, which is already in the corpus.
- `otev.html`: The text is the same as `otev`, which is already in the corpus.
- `pandora-s-box.html`: The text is the same as `pandora-s-box`, which is already in the corpus.
- `peach-cobbler.html`: The text is the same as `peach-cobbler`, which is already in the corpus.
- `perfect-game.html`: The text is the same as `perfect-game`, which is already in the corpus.
- `perfect-shot.html`: The text is the same as `perfect-shot`, which is already in the corpus.
- `phalanx-5.html`: The text is the same as `phalanx-5`, which is already in the corpus.
- `pinky-swear-alliance.html`: The text is the same as `pinky-swear-alliance`, which is already in the corpus.
- `pipeline.html`: The text is the same as `pipeline`, which is already in the corpus.
- `po-s-pack.html`: The text is the same as `po-s-pack`, which is already in the corpus.
- `pose-in-ivy.html`: The text is the same as `pose-in-ivy`, which is already in the corpus.
- `power-couple.html`: The text is the same as `power-couple`, which is already in the corpus.
- `power-of-veto.html`: The text is the same as `power-of-veto`, which is already in the corpus.
- `premiere-night-eviction.html`: The text is the same as `premiere-night-eviction`, which is already in the corpus.
- `pressure-cooker.html`: The text is the same as `pressure-cooker`, which is already in the corpus.
- `previously-evicted-contestant.html`: The text is the same as `previously-evicted-contestant`, which is already in the corpus.
- `project-dna.html`: The text is the same as `project-dna`, which is already in the corpus.
- `pull-some-strings.html`: The text is the same as `pull-some-strings`, which is already in the corpus.
- `punch-slap-kick.html`: The text is the same as `punch-slap-kick`, which is already in the corpus.
- `pyramid.html`: The text is the same as `pyramid`, which is already in the corpus.
- `queens.html`: The text is the same as `queens`, which is already in the corpus.
- `re-entry-competition.html`: The text is the same as `re-entry-competition`, which is already in the corpus.
- `ready-set-woah.html`: The text is the same as `ready-set-woah`, which is already in the corpus.
- `reclaim-the-relic.html`: The text is the same as `reclaim-the-relic`, which is already in the corpus.
- `records-statistics.html`: The text is the same as `records-statistics`, which is already in the corpus.
- `repeat-after-me.html`: The text is the same as `repeat-after-me`, which is already in the corpus.
- `repetitive-task-punishment.html`: The text is the same as `repetitive-task-punishment`, which is already in the corpus.
- `returning-players.html`: The text is the same as `returning-players`, which is already in the corpus.
- `rewind-button.html`: The text is the same as `rewind-button`, which is already in the corpus.
- `ride-the-rocket.html`: The text is the same as `ride-the-rocket`, which is already in the corpus.
- `rivals.html`: The text is the same as `rivals`, which is already in the corpus.
- `roadkill-competition.html`: The text is the same as `roadkill-competition`, which is already in the corpus.
- `rockstars.html`: The text is the same as `rockstars`, which is already in the corpus.
- `rogue-rats.html`: The text is the same as `rogue-rats`, which is already in the corpus.
- `roll-it-down.html`: The text is the same as `roll-it-down`, which is already in the corpus.
- `rollerball.html`: The text is the same as `rollerball`, which is already in the corpus.
- `rollin-in-the-dough.html`: The text is the same as `rollin-in-the-dough`, which is already in the corpus.
- `rookies.html`: The text is the same as `rookies`, which is already in the corpus.
- `round-trip-ticket.html`: The text is the same as `round-trip-ticket`, which is already in the corpus.
- `rush-hour.html`: The text is the same as `rush-hour`, which is already in the corpus.
- `safety-suite-competition.html`: The text is the same as `safety-suite-competition`, which is already in the corpus.
- `sam-s-boys.html`: The text is the same as `sam-s-boys`, which is already in the corpus.
- `scamper-squad.html`: The text is the same as `scamper-squad`, which is already in the corpus.
- `scorpio-sisters.html`: The text is the same as `scorpio-sisters`, which is already in the corpus.
- `scyler.html`: The text is the same as `scyler`, which is already in the corpus.
- `second-chance-challenge.html`: The text is the same as `second-chance-challenge`, which is already in the corpus.
- `secret-power-competition.html`: The text is the same as `secret-power-competition`, which is already in the corpus.
- `secret-room.html`: The text is the same as `secret-room`, which is already in the corpus.
- `seesaw.html`: The text is the same as `seesaw`, which is already in the corpus.
- `sequence-explosion.html`: The text is the same as `sequence-explosion`, which is already in the corpus.
- `shackles.html`: The text is the same as `shackles`, which is already in the corpus.
- `shelltown.html`: The text is the same as `shelltown`, which is already in the corpus.
- `shootout.html`: The text is the same as `shootout`, which is already in the corpus.
- `silent-six.html`: The text is the same as `silent-six`, which is already in the corpus.
- `sirens.html`: The text is the same as `sirens`, which is already in the corpus.
- `six-shooters.html`: The text is the same as `six-shooters`, which is already in the corpus.
- `sixth-avenue.html`: The text is the same as `sixth-avenue`, which is already in the corpus.
- `sky-high-memory.html`: The text is the same as `sky-high-memory`, which is already in the corpus.
- `slapshot.html`: The text is the same as `slapshot`, which is already in the corpus.
- `sleeper-cell.html`: The text is the same as `sleeper-cell`, which is already in the corpus.
- `slick-six.html`: The text is the same as `slick-six`, which is already in the corpus.
- `slingshot-aim.html`: The text is the same as `slingshot-aim`, which is already in the corpus.
- `slippery-slope.html`: The text is the same as `slippery-slope`, which is already in the corpus.
- `slop.html`: The text is the same as `slop`, which is already in the corpus.
- `snake-eyes.html`: The text is the same as `snake-eyes`, which is already in the corpus.
- `snapshot-shuffle.html`: The text is the same as `snapshot-shuffle`, which is already in the corpus.
- `solitary-confinement.html`: The text is the same as `solitary-confinement`, which is already in the corpus.
- `somewhere-over-the-veto.html`: The text is the same as `somewhere-over-the-veto`, which is already in the corpus.
- `soulmates.html`: The text is the same as `soulmates`, which is already in the corpus.
- `sovereign-six.html`: The text is the same as `sovereign-six`, which is already in the corpus.
- `spelling-search.html`: The text is the same as `spelling-search`, which is already in the corpus.
- `spy-girls.html`: The text is the same as `spy-girls`, which is already in the corpus.
- `stage-five.html`: The text is the same as `stage-five`, which is already in the corpus.
- `starting-lineup.html`: The text is the same as `starting-lineup`, which is already in the corpus.
- `staten-island.html`: The text is the same as `staten-island`, which is already in the corpus.
- `stay-or-fold.html`: The text is the same as `stay-or-fold`, which is already in the corpus.
- `strong-side.html`: The text is the same as `strong-side`, which is already in the corpus.
- `students-of-sound.html`: The text is the same as `students-of-sound`, which is already in the corpus.
- `swayleigh.html`: The text is the same as `swayleigh`, which is already in the corpus.
- `swing-slam-dunk.html`: The text is the same as `swing-slam-dunk`, which is already in the corpus.
- `take-it-off.html`: The text is the same as `take-it-off`, which is already in the corpus.
- `tangela.html`: The text is the same as `tangela`, which is already in the corpus.
- `tea-party.html`: The text is the same as `tea-party`, which is already in the corpus.
- `team-america.html`: The text is the same as `team-america`, which is already in the corpus.
- `team-boogie.html`: The text is the same as `team-boogie`, which is already in the corpus.
- `team-britney.html`: The text is the same as `team-britney`, which is already in the corpus.
- `team-christ.html`: The text is the same as `team-christ`, which is already in the corpus.
- `team-dan.html`: The text is the same as `team-dan`, which is already in the corpus.
- `team-freeze.html`: The text is the same as `team-freeze`, which is already in the corpus.
- `team-janelle.html`: The text is the same as `team-janelle`, which is already in the corpus.
- `team-jesus.html`: The text is the same as `team-jesus`, which is already in the corpus.
- `team-jj.html`: The text is the same as `team-jj`, which is already in the corpus.
- `team-pp.html`: The text is the same as `team-pp`, which is already in the corpus.
- `team-touch.html`: The text is the same as `team-touch`, which is already in the corpus.
- `team-unicorn.html`: The text is the same as `team-unicorn`, which is already in the corpus.
- `teams.html`: The text is the same as `teams`, which is already in the corpus.
- `temptation-competition.html`: The text is the same as `temptation-competition`, which is already in the corpus.
- `tenexas.html`: The text is the same as `tenexas`, which is already in the corpus.
- `terek.html`: The text is the same as `terek`, which is already in the corpus.
- `the-afterparty.html`: The text is the same as `the-afterparty`, which is already in the corpus.
- `the-amazons.html`: The text is the same as `the-amazons`, which is already in the corpus.
- `the-andersons.html`: The text is the same as `the-andersons`, which is already in the corpus.
- `the-athletes.html`: The text is the same as `the-athletes`, which is already in the corpus.
- `the-barbershop.html`: The text is the same as `the-barbershop`, which is already in the corpus.
- `the-black-box.html`: The text is the same as `the-black-box`, which is already in the corpus.
- `the-black-ops.html`: The text is the same as `the-black-ops`, which is already in the corpus.
- `the-blonde-tourage.html`: The text is the same as `the-blonde-tourage`, which is already in the corpus.
- `the-board.html`: The text is the same as `the-board`, which is already in the corpus.
- `the-bond.html`: The text is the same as `the-bond`, which is already in the corpus.
- `the-bookends.html`: The text is the same as `the-bookends`, which is already in the corpus.
- `the-brains.html`: The text is the same as `the-brains`, which is already in the corpus.
- `the-brigade.html`: The text is the same as `the-brigade`, which is already in the corpus.
- `the-butchers.html`: The text is the same as `the-butchers`, which is already in the corpus.
- `the-carolinas.html`: The text is the same as `the-carolinas`, which is already in the corpus.
- `the-ceasefire.html`: The text is the same as `the-ceasefire`, which is already in the corpus.
- `the-chenbots.html`: The text is the same as `the-chenbots`, which is already in the corpus.
- `the-chillers.html`: The text is the same as `the-chillers`, which is already in the corpus.
- `the-collective.html`: The text is the same as `the-collective`, which is already in the corpus.
- `the-commission.html`: The text is the same as `the-commission`, which is already in the corpus.
- `the-committee.html`: The text is the same as `the-committee`, which is already in the corpus.
- `the-connect-bb23.html`: The text is the same as `the-connect-bb23`, which is already in the corpus.
- `the-connect.html`: The text is the same as `the-connect`, which is already in the corpus.
- `the-cookout.html`: The text is the same as `the-cookout`, which is already in the corpus.
- `the-core-four.html`: The text is the same as `the-core-four`, which is already in the corpus.
- `the-core.html`: The text is the same as `the-core`, which is already in the corpus.
- `the-court-jesters.html`: The text is the same as `the-court-jesters`, which is already in the corpus.
- `the-coven.html`: The text is the same as `the-coven`, which is already in the corpus.
- `the-covenant.html`: The text is the same as `the-covenant`, which is already in the corpus.
- `the-critics.html`: The text is the same as `the-critics`, which is already in the corpus.
- `the-crossovers.html`: The text is the same as `the-crossovers`, which is already in the corpus.
- `the-crossroads.html`: The text is the same as `the-crossroads`, which is already in the corpus.
- `the-crow-boys.html`: The text is the same as `the-crow-boys`, which is already in the corpus.
- `the-culture.html`: The text is the same as `the-culture`, which is already in the corpus.
- `the-dapper-dans.html`: The text is the same as `the-dapper-dans`, which is already in the corpus.
- `the-detectives.html`: The text is the same as `the-detectives`, which is already in the corpus.
- `the-detonators.html`: The text is the same as `the-detonators`, which is already in the corpus.
- `the-executives.html`: The text is the same as `the-executives`, which is already in the corpus.
- `the-exterminators.html`: The text is the same as `the-exterminators`, which is already in the corpus.
- `the-fatal-spies.html`: The text is the same as `the-fatal-spies`, which is already in the corpus.
- `the-fellowship-of-the-zing.html`: The text is the same as `the-fellowship-of-the-zing`, which is already in the corpus.
- `the-fields.html`: The text is the same as `the-fields`, which is already in the corpus.
- `the-five-swatters.html`: The text is the same as `the-five-swatters`, which is already in the corpus.
- `the-flop.html`: The text is the same as `the-flop`, which is already in the corpus.
- `the-frenemies.html`: The text is the same as `the-frenemies`, which is already in the corpus.
- `the-friendship.html`: The text is the same as `the-friendship`, which is already in the corpus.
- `the-fugitives.html`: The text is the same as `the-fugitives`, which is already in the corpus.
- `the-goblins.html`: The text is the same as `the-goblins`, which is already in the corpus.
- `the-goof-troupe.html`: The text is the same as `the-goof-troupe`, which is already in the corpus.
- `the-handful.html`: The text is the same as `the-handful`, which is already in the corpus.
- `the-handymen.html`: The text is the same as `the-handymen`, which is already in the corpus.
- `the-haunting.html`: The text is the same as `the-haunting`, which is already in the corpus.
- `the-hitmen.html`: The text is the same as `the-hitmen`, which is already in the corpus.
- `the-hive.html`: The text is the same as `the-hive`, which is already in the corpus.
- `the-honor-society.html`: The text is the same as `the-honor-society`, which is already in the corpus.
- `the-icons.html`: The text is the same as `the-icons`, which is already in the corpus.
- `the-judges.html`: The text is the same as `the-judges`, which is already in the corpus.
- `the-jugglers.html`: The text is the same as `the-jugglers`, which is already in the corpus.
- `the-kingslayers.html`: The text is the same as `the-kingslayers`, which is already in the corpus.
- `the-leftovers.html`: The text is the same as `the-leftovers`, which is already in the corpus.
- `the-legion-of-doom.html`: The text is the same as `the-legion-of-doom`, which is already in the corpus.
- `the-lorraines.html`: The text is the same as `the-lorraines`, which is already in the corpus.
- `the-love-triangle.html`: The text is the same as `the-love-triangle`, which is already in the corpus.
- `the-mafia-bb23.html`: The text is the same as `the-mafia-bb23`, which is already in the corpus.
- `the-mafia-bb25.html`: The text is the same as `the-mafia-bb25`, which is already in the corpus.
- `the-mastermind.html`: The text is the same as `the-mastermind`, which is already in the corpus.
- `the-maze.html`: The text is the same as `the-maze`, which is already in the corpus.
- `the-melting-pot.html`: The text is the same as `the-melting-pot`, which is already in the corpus.
- `the-minutemen.html`: The text is the same as `the-minutemen`, which is already in the corpus.
- `the-misfits.html`: The text is the same as `the-misfits`, which is already in the corpus.
- `the-mom-squad-bb15.html`: The text is the same as `the-mom-squad-bb15`, which is already in the corpus.
- `the-mom-squad-bb27.html`: The text is the same as `the-mom-squad-bb27`, which is already in the corpus.
- `the-moving-company.html`: The text is the same as `the-moving-company`, which is already in the corpus.
- `the-night-owls.html`: The text is the same as `the-night-owls`, which is already in the corpus.
- `the-night-shift.html`: The text is the same as `the-night-shift`, which is already in the corpus.
- `the-oddballs.html`: The text is the same as `the-oddballs`, which is already in the corpus.
- `the-off-beats.html`: The text is the same as `the-off-beats`, which is already in the corpus.
- `the-original-six.html`: The text is the same as `the-original-six`, which is already in the corpus.
- `the-other-people.html`: The text is the same as `the-other-people`, which is already in the corpus.
- `the-pentagon.html`: The text is the same as `the-pentagon`, which is already in the corpus.
- `the-populars.html`: The text is the same as `the-populars`, which is already in the corpus.
- `the-pound.html`: The text is the same as `the-pound`, which is already in the corpus.
- `the-primaries.html`: The text is the same as `the-primaries`, which is already in the corpus.
- `the-professors.html`: The text is the same as `the-professors`, which is already in the corpus.
- `the-quack-pack.html`: The text is the same as `the-quack-pack`, which is already in the corpus.
- `the-radicals.html`: The text is the same as `the-radicals`, which is already in the corpus.
- `the-rationale.html`: The text is the same as `the-rationale`, which is already in the corpus.
- `the-real-fields.html`: The text is the same as `the-real-fields`, which is already in the corpus.
- `the-red-corner.html`: The text is the same as `the-red-corner`, which is already in the corpus.
- `the-regulators.html`: The text is the same as `the-regulators`, which is already in the corpus.
- `the-renegades.html`: The text is the same as `the-renegades`, which is already in the corpus.
- `the-returners.html`: The text is the same as `the-returners`, which is already in the corpus.
- `the-revolution.html`: The text is the same as `the-revolution`, which is already in the corpus.
- `the-root.html`: The text is the same as `the-root`, which is already in the corpus.
- `the-royal-flush.html`: The text is the same as `the-royal-flush`, which is already in the corpus.
- `the-saboteur.html`: The text is the same as `the-saboteur`, which is already in the corpus.
- `the-sacred-six.html`: The text is the same as `the-sacred-six`, which is already in the corpus.
- `the-secret-alliance.html`: The text is the same as `the-secret-alliance`, which is already in the corpus.
- `the-sirens.html`: The text is the same as `the-sirens`, which is already in the corpus.
- `the-sitting-ducks.html`: The text is the same as `the-sitting-ducks`, which is already in the corpus.
- `the-sixth-sense.html`: The text is the same as `the-sixth-sense`, which is already in the corpus.
- `the-slaughterhouse.html`: The text is the same as `the-slaughterhouse`, which is already in the corpus.
- `the-slitherpuffs.html`: The text is the same as `the-slitherpuffs`, which is already in the corpus.
- `the-snoots.html`: The text is the same as `the-snoots`, which is already in the corpus.
- `the-team.html`: The text is the same as `the-team`, which is already in the corpus.
- `the-toolshed.html`: The text is the same as `the-toolshed`, which is already in the corpus.
- `the-trio.html`: The text is the same as `the-trio`, which is already in the corpus.
- `the-unexpendables.html`: The text is the same as `the-unexpendables`, which is already in the corpus.
- `the-unreliables.html`: The text is the same as `the-unreliables`, which is already in the corpus.
- `the-untouchables.html`: The text is the same as `the-untouchables`, which is already in the corpus.
- `the-vendetta.html`: The text is the same as `the-vendetta`, which is already in the corpus.
- `the-visionaries.html`: The text is the same as `the-visionaries`, which is already in the corpus.
- `the-vixens.html`: The text is the same as `the-vixens`, which is already in the corpus.
- `the-walking-dead.html`: The text is the same as `the-walking-dead`, which is already in the corpus.
- `the-wall.html`: The text is the same as `the-wall`, which is already in the corpus.
- `the-weirdos.html`: The text is the same as `the-weirdos`, which is already in the corpus.
- `the-wingmen.html`: The text is the same as `the-wingmen`, which is already in the corpus.
- `the-wise-guys.html`: The text is the same as `the-wise-guys`, which is already in the corpus.
- `the-wolfpack.html`: The text is the same as `the-wolfpack`, which is already in the corpus.
- `the-writers-room.html`: The text is the same as `the-writers-room`, which is already in the corpus.
- `the-zingbot.html`: The text is the same as `the-zingbot`, which is already in the corpus.
- `three-s-company.html`: The text is the same as `three-s-company`, which is already in the corpus.
- `three-stooges.html`: The text is the same as `three-stooges`, which is already in the corpus.
- `threemance.html`: The text is the same as `threemance`, which is already in the corpus.
- `tiffney.html`: The text is the same as `tiffney`, which is already in the corpus.
- `time-flies.html`: The text is the same as `time-flies`, which is already in the corpus.
- `time-highway.html`: The text is the same as `time-highway`, which is already in the corpus.
- `to-drink-or-to-bluff.html`: The text is the same as `to-drink-or-to-bluff`, which is already in the corpus.
- `tower-of-hanoi.html`: The text is the same as `tower-of-hanoi`, which is already in the corpus.
- `tree-of-temptation.html`: The text is the same as `tree-of-temptation`, which is already in the corpus.
- `triple-eviction.html`: The text is the same as `triple-eviction`, which is already in the corpus.
- `triple-threat-bb22.html`: The text is the same as `triple-threat-bb22`, which is already in the corpus.
- `triple-threat-bb27.html`: The text is the same as `triple-threat-bb27`, which is already in the corpus.
- `triplets.html`: The text is the same as `triplets`, which is already in the corpus.
- `tubina.html`: The text is the same as `tubina`, which is already in the corpus.
- `tumblin-dice.html`: The text is the same as `tumblin-dice`, which is already in the corpus.
- `two-sweet.html`: The text is the same as `two-sweet`, which is already in the corpus.
- `unde9able.html`: The text is the same as `unde9able`, which is already in the corpus.
- `unitard.html`: The text is the same as `unitard`, which is already in the corpus.
- `unpopular-alliance.html`: The text is the same as `unpopular-alliance`, which is already in the corpus.
- `veterans.html`: The text is the same as `veterans`, which is already in the corpus.
- `veto-replacement.html`: The text is the same as `veto-replacement`, which is already in the corpus.
- `watch-your-step.html`: The text is the same as `watch-your-step`, which is already in the corpus.
- `weight-gain.html`: The text is the same as `weight-gain`, which is already in the corpus.
- `whacktivity-competition.html`: The text is the same as `whacktivity-competition`, which is already in the corpus.
- `what-competition-was-that.html`: The text is the same as `what-competition-was-that`, which is already in the corpus.
- `what-did-they-just-do.html`: The text is the same as `what-did-they-just-do`, which is already in the corpus.
- `what-s-the-hold-up.html`: The text is the same as `what-s-the-hold-up`, which is already in the corpus.
- `what-the-bleep.html`: The text is the same as `what-the-bleep`, which is already in the corpus.
- `wheel-of-first-impressions.html`: The text is the same as `wheel-of-first-impressions`, which is already in the corpus.
- `whenchie.html`: The text is the same as `whenchie`, which is already in the corpus.
- `where-were-you.html`: The text is the same as `where-were-you`, which is already in the corpus.
- `whistlenut-ole.html`: The text is the same as `whistlenut-ole`, which is already in the corpus.
- `who-did-what.html`: The text is the same as `who-did-what`, which is already in the corpus.
- `who-said-it.html`: The text is the same as `who-said-it`, which is already in the corpus.
- `wildcard-competition.html`: The text is the same as `wildcard-competition`, which is already in the corpus.
- `will-s-daughters.html`: The text is the same as `will-s-daughters`, which is already in the corpus.
- `winners-us.html`: The text is the same as `winners-us`, which is already in the corpus.
- `x-factor.html`: The text is the same as `x-factor`, which is already in the corpus.
- `yankee-swap.html`: The text is the same as `yankee-swap`, which is already in the corpus.
- `young-grasshoppers.html`: The text is the same as `young-grasshoppers`, which is already in the corpus.
- `zankie.html`: The text is the same as `zankie`, which is already in the corpus.
- `zaulie.html`: The text is the same as `zaulie`, which is already in the corpus.
- `zingbot-competition.html`: The text is the same as `zingbot-competition`, which is already in the corpus.

## What to check by eye

Ingest cleans text by rules, and rules miss things.
Take five minutes to open the shortest, a middle one and the longest document next to its original and read one page of each.

- Search the documents for `þ`, `¼`, `(cid:` and the replacement character.
  A hit usually means the PDF's font map is wrong, which no tool can repair, so treat it as a defect and leave that document out.
- Look at the end of a few papers.
  Ingest drops a trailing reference list when it finds a References heading or a run of numbered entries.
  A paper whose list has neither can keep it, and then every author and journal name matches queries it should not.
- Open the first lines of a few documents.
  Author lists, copyright pages and tables of contents are not removed automatically, and you may want to cut them.
- Compare one table with the PDF.
  A PDF prints footnote marks as small raised digits, and the converter glues them onto the word or number next to them: `ALUMINUM1` is the heading ALUMINUM with footnote 1, and `11210,000` can be 210,000 with footnote 11.
  Quotes still match the stored text, but a number read from it can be wrong, so check before you trust a figure in a query, a judgment or an answer.
- Fix the `license` column in the manifest for every document, then run `uv run p2 license`.
  It is `unknown` until you do, and `unknown` does not pass.

## If a document is flagged as scanned

A scan is a picture of a page, so there is no text for ingest to read.
This template does not install an OCR tool, because it is large and most students never need it.
If you do need one, the opt-in route is pymupdf4llm with rapidocr, run on its own outside the template's environment:

```
uv run --no-project --with pymupdf4llm --with rapidocr python -c "import pymupdf4llm, sys, pathlib; pathlib.Path(sys.argv[2]).write_text(pymupdf4llm.to_markdown(sys.argv[1], use_ocr=True, force_ocr=True), encoding='utf-8')" scan.pdf scan.md
```

Put the resulting `.md` file in your folder and ingest the folder again.
It costs about 2 seconds a page, and OCR text needs a second look: it misreads ligatures, hyphens and numbers.
pymupdf4llm is AGPL-3.0 software, so use it only as a tool on your own machine, and do not add it to this repo's dependencies or copy its code into the repo.
