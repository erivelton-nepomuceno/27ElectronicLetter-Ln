[CAS *Lab*Sustainable Circuits and Systems Lab](https://www.maynoothuniversity.ie/caslab)

# Logical Chaos

Core idea: build every chaotic system from nothing but two-input AND, OR, XOR and NOT gates in n-bit fixed point, then rank the implementations by how little they cost, gates per iteration L(n) and energy per output bit, while checking that the digital version is still chaotic and faithful to the original. The simplest digital chaos is the one at the top of that ranking. Flows appear twice: Euler at the original step and RK4 at a 4× larger step. pJ/bit is the estimated typical energy per output bit at 32 and 64 bits. Click any column heading to sort, and any system name to open its profile.

**Baseline:** 64-bit floating point (float64). Comparisons are made with the 64-bit fixed-point logic circuit, both running the same scheme with the same step.


| # | System | ID | Type | Class | Scheme | L(n) | L(64) | L(16) | L(32) | L(128) | L(256) | pJ/bit 32 | pJ/bit 64 | 1-step err | λ err | Density err |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Gingerbreadman](#gingerbreadman__map) | 14 | map | L | map iteration | 7n + 2 | 450 | 114 | 226 | 898 | 1,794 | 0.063 | 0.063 | 0 | 0.282 | 0.034 |
| 2 | [Arnold's cat](#arnold_s_cat__map) | 07 | map | L | map iteration | 10n − 32 | 608 | 128 | 288 | 1,248 | 2,528 | 0.070 | 0.063 | 0 | 2.03×10⁻⁸ | 0.003✓ |
| 3 | [Lozi (a = 1.75)](#lozi_a_1_75__map) | 10 | map | L | map iteration | 12n − 14 | 754 | 178 | 370 | 1,522 | 3,058 | 0.084 | 0.088 | 0 | 0.002 | 0.003✓ |
| 4 | [Tent (μ = 2 − 2⁻⁷)](#tent_2_2__map) | 06 | map | L | map iteration | 14n − 17 | 879 | 207 | 431 | 1,775 | 3,567 | 0.133 | 0.140 | 0 | 1.10×10⁻⁸ | 0.004✓ |
| 5 | [MDCS (Nepomuceno et al., 2019)](#mdcs_nepomuceno_et_al_2019__map) | 71 | map | P | map iteration | ≈ 1.50n² + 4.7n − 26 | 6,432 | 434 | 1,662 | 25,186 | 99,552 | 0.704 | 1.353 | 1.47×10⁻¹⁹ | 5.83×10⁻⁵ | 0.003✓ |
| 6 | [Sprott jerk circuit](#sprott_jerk_circuit__euler) | 53-E | flow | P | Euler, dt = 2⁻⁶ | ≈ 1.57n² + 86n − 1258 | 10,524 | 850 | 3,018 | 20,636‡ | 40,860‡ | 0.286 | 0.537 | 2.22×10⁻¹⁷ | 0.049 | 0.014 |
| 7 | [Sprott jerk circuit](#sprott_jerk_circuit__rk4) | 53-R | flow | P | RK4, dt = 2⁻⁴ | ≈ 22.1n² + 1.25e+03n + … | 149,588 | 11,005 | 43,117 | 505,746ᵉ | 1,754,107ᵉ | 4.013 | 7.509 | 1.06×10⁻¹⁶ | 4.82×10⁻⁶✓ | 1.04×10⁻¹⁰✓ |
| 8 | [Chua](#chua__euler) | 05-E | flow | P | Euler, dt = 2⁻⁷ | ≈ 1.44n² + 354n − 5528 | 22,647 | 1,993 | 6,891 | 44,343‡ | 87,735‡ | 0.599 | 1.107 | 4.14×10⁻¹⁶ | 0.016✓ | 0.124 |
| 9 | [Chua](#chua__rk4) | 05-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 28.4n² + 1.69e+03n + … | 197,858 | 14,080 | 57,208 | 659,590ᵉ | 2,274,075ᵉ | 5.162 | 9.684 | 5.98×10⁻¹⁶ | 0.026✓ | 0.015✓ |
| 10 | [Pomeau-Manneville type I (x+x^2 mod 1)](#pomeau_manneville_type_i_x_x_2_mod_1__map) | 20 | map | P | map iteration | 5.75n² − 11.5n − 37 | 22,779 | 1,251 | 5,483 | 92,699 | 373,851 | 1.083 | 2.991 | 2.06×10⁻¹⁹ | 1.289 | 0.493 |
| 11 | [Logistic (r = 3.9375)](#logistic_r_3_9375__map) | 01 | map | P | map iteration | 5.75n² + 2.5n − 7 | 23,705 | 1,505 | 5,961 | 94,521 | 377,465 | 1.705 | 3.467 | 4.99×10⁻¹⁹ | 0.009 | 0.004 |
| 12 | [Sprott-Linz R ◊](#sprott_linz_r__euler) | 51-E | flow | P | Euler, dt = 2⁻⁷ | 5.75n² + 5.09n − 53 | 23,821 | 1,500 | 5,997 | 94,461 | 377,021 | 0.468 | 1.086 | 7.45×10⁻¹⁶ | 0.008✓ | 0.007✓ |
| 13 | [Sprott-Linz R](#sprott_linz_r__rk4) | 51-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 50.5n² − 5.78n + … | 202,238 | 9,634 | 47,602 | 822,828ᵉ | 3,303,350ᵉ | 3.967 | 9.425 | 1.64×10⁻¹⁵ | 0.056 | 0.009✓ |
| 14 | [Sprott-Linz N](#sprott_linz_n__euler) | 48-E | flow | P | Euler, dt = 2⁻⁷ | 5.75n² + 7n + 17 | 24,017 | 1,601 | 6,129 | 95,121 | 378,641 | 0.520 | 1.135 | 3.33×10⁻¹⁶ | 0.037✓ | 0.015✓ |
| 15 | [Sprott-Linz N](#sprott_linz_n__rk4) | 48-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 48.6n² + 163n + … | 203,496 | 10,569 | 49,305 | 812,725ᵉ | 3,224,302ᵉ | 4.289 | 9.629 | 9.73×10⁻¹⁶ | 0.081✓ | 0.012✓ |
| 16 | [Sprott-Linz J](#sprott_linz_j__euler) | 44-E | flow | P | Euler, dt = 2⁻⁷ | 5.75n² + 9.5n + 1 | 24,161 | 1,625 | 6,193 | 95,425 | 379,265 | 0.512 | 1.116 | 7.77×10⁻¹⁶ | 0.002✓ | 0.013✓ |
| 17 | [Sprott-Linz J](#sprott_linz_j__rk4) | 44-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 48.6n² + 191n + … | 205,199 | 10,926 | 50,110 | 816,235ᵉ | 3,231,471ᵉ | 4.300 | 9.570 | 1.08×10⁻¹⁵ | 0.055✓ | 0.004✓ |
| 18 | [Sprott-Linz S ◊](#sprott_linz_s__euler) | 52-E | flow | P | Euler, dt = 2⁻⁹ | 5.75n² + 13n + 26 | 24,410 | 1,706 | 6,330 | 95,898 | 380,186 | 0.502 | 1.135 | 3.48×10⁻¹⁶ | 0.051✓ | 0.023 |
| 19 | [Sprott-Linz S](#sprott_linz_s__rk4) | 52-R | flow | P | RK4, dt = 2⁻⁷ | ≈ 48.7n² + 178n + … | 205,027 | 10,925 | 50,013 | 816,531ᵉ | 3,235,435ᵉ | 4.205 | 9.681 | 8.72×10⁻¹⁶ | 0.154 | 0.011✓ |
| 20 | [Sprott-Linz F](#sprott_linz_f__euler) | 40-E | flow | P | Euler, dt = 2⁻⁷ | 5.75n² + 14.5n + 12 | 24,492 | 1,716 | 6,364 | 96,076 | 380,556 | 0.509 | 1.155 | 1.75×10⁻¹⁶ | 0.130✓ | 0.078✓ |
| 21 | [Sprott-Linz F](#sprott_linz_f__rk4) | 40-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 46.8n² + 347n + … | 205,404 | 11,622 | 51,318 | 803,720ᵉ | 3,146,219ᵉ | 4.079 | 9.392 | 4.12×10⁻¹⁶ | 0.015✓ | 0.012✓ |
| 22 | [Sprott-Linz H](#sprott_linz_h__euler) | 42-E | flow | P | Euler, dt = 2⁻⁷ | 5.75n² + 14.5n + 12 | 24,492 | 1,716 | 6,364 | 96,076 | 380,556 | 0.491 | 1.112 | 1.81×10⁻¹⁶ | 0.195 | 0.022✓ |
| 23 | [Sprott-Linz H](#sprott_linz_h__rk4) | 42-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 46.8n² + 347n + … | 205,404 | 11,622 | 51,318 | 803,720ᵉ | 3,146,219ᵉ | 4.328 | 9.574 | 4.22×10⁻¹⁶ | 0.138 | 0.056 |
| 24 | [Delayed logistic (a=2.27)](#delayed_logistic_a_2_27__map) | 18 | map | P | map iteration | ≈ 6.07n² + 77.5n − 977 | 28,702 | 1,954 | 7,508 | 104,318 | 396,862 | 1.060 | 2.133 | 1.28×10⁻¹⁸ | 0.003✓ | 0.004 |
| 25 | [Hyper-Rössler (4D) ◊](#hyper_r_ssler_4d__euler) | 30-E | flow | P | Euler, dt = 2⁻⁸ | ≈ 8.15n² − 22.3n − 392 | 31,566 | 1,311* | 7,246 | 112,554 | 413,162 | 0.342 | 0.997 | 2.55×10⁻¹⁴ | 90.151✗ | 7.666✗ |
| 26 | [Hyper-Rössler (4D)](#hyper_r_ssler_4d__rk4) | 30-R | flow | P | RK4, dt = 2⁻⁶ | ≈ 71.2n² − 382n + … | 260,606 | 4,922 | 54,078 | 1,110,578ᵉ | 4,560,326ᵉ | 2.485 | 7.866 | 1.46×10⁻¹⁴ | 0.148✓ | 0.314 |
| 27 | [Rössler](#r_ssler__euler) | 04-E | flow | P | Euler, dt = 2⁻⁸ | 8.25n² − 27n − 169 | 31,925 | 1,483* | 7,426 | 111,867‡ | 411,707‡ | 0.524 | 1.427 | 5.79×10⁻¹⁵ | 0.036✓ | 0.002✓ |
| 28 | [Rössler](#r_ssler__rk4) | 04-R | flow | P | RK4, dt = 2⁻⁶ | ≈ 56.8n² + 213n + … | 237,294 | 11,429 | 56,693 | 950,180ᵉ | 3,768,024ᵉ | 4.388 | 10.873 | 3.47×10⁻¹⁵ | 0.093 | 0.028 |
| 29 | [Sprott-Linz M ◊](#sprott_linz_m__euler) | 47-E | flow | P | Euler, dt = 2⁻⁹ | 8.25n² − 8.68n − 97 | 33,147 | 1,877 | 8,075 | 112,861 | 413,597 | 0.601 | 1.482 | 6.66×10⁻¹⁶ | 0.005✓ | 0.001✓ |
| 30 | [Sprott-Linz M](#sprott_linz_m__rk4) | 47-R | flow | P | RK4, dt = 2⁻⁷ | ≈ 52.4n² + 619n + … | 241,056 | 13,777 | 61,089 | 926,573ᵉ | 3,580,158ᵉ | 5.077 | 11.236 | 8.82×10⁻¹⁶ | 9.24×10⁻⁵✓ | 9.65×10⁻⁷✓ |
| 31 | [Sprott-Linz K ◊](#sprott_linz_k__euler) | 45-E | flow | P | Euler, dt = 2⁻⁷ | ≈ 7.94n² + 19.9n − 347 | 33,365 | 2,043 | 8,371 | 113,429 | 414,869 | 0.682 | 1.533 | 8.56×10⁻¹⁷ | 5.87×10⁻⁵✓ | 8.18×10⁻¹⁴✓ |
| 32 | [Sprott-Linz K](#sprott_linz_k__rk4) | 45-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 49.9n² + 817n + … | 240,368 | 14,485 | 62,213 | 909,385ᵉ | 3,467,431ᵉ | 5.402 | 11.414 | 2.30×10⁻¹⁶ | 2.76×10⁻⁵✓ | 9.23×10⁻⁹✓ |
| 33 | [Sprott-Linz G ◊](#sprott_linz_g__euler) | 41-E | flow | P | Euler, dt = 2⁻⁷ | ≈ 7.94n² + 21n − 347 | 33,429 | 2,061 | 8,405 | 113,557 | 415,125 | 0.654 | 1.520 | 8.88×10⁻¹⁷ | 0.003✓ | 2.36×10⁻⁴✓ |
| 34 | [Sprott-Linz G](#sprott_linz_g__rk4) | 41-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 48.7n² + 929n + … | 241,576 | 15,117 | 63,485 | 902,262ᵉ | 3,413,131ᵉ | 5.510 | 11.519 | 2.23×10⁻¹⁶ | 4.70×10⁻⁶✓ | 3.82×10⁻⁸✓ |
| 35 | [Sprott-Linz O](#sprott_linz_o__euler) | 49-E | flow | P | Euler, dt = 2⁻⁷ | ≈ 7.31n² + 73.4n − 885 | 33,531 | 2,281 | 8,809 | 113,755 | 415,515 | 0.685 | 1.522 | 4.91×10⁻¹⁷ | 0.007✓ | 2.61×10⁻⁴✓ |
| 36 | [Sprott-Linz O](#sprott_linz_o__rk4) | 49-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 44.4n² + 1.25e+03n + … | 240,853 | 16,193 | 65,489 | 869,669ᵉ | 3,211,547ᵉ | 5.784 | 11.547 | 1.06×10⁻¹⁶ | 0.001✓ | 1.11×10⁻⁴✓ |
| 37 | [Sprott-Linz P](#sprott_linz_p__euler) | 50-E | flow | P | Euler, dt = 2⁻⁷ | ≈ 7.31n² + 73.4n − 884 | 33,532 | 2,282 | 8,810 | 113,756 | 415,516 | 0.719 | 1.555 | 5.55×10⁻¹⁷ | 0.095✓ | 0.010✓ |
| 38 | [Sprott-Linz P](#sprott_linz_p__rk4) | 50-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 44.3n² + 1.26e+03n + … | 241,296 | 16,278 | 65,734 | 869,863ᵉ | 3,208,397ᵉ | 5.752 | 11.736 | 1.32×10⁻¹⁶ | 0.076✓ | 0.017✓ |
| 39 | [Sprott-Linz I ◊](#sprott_linz_i__euler) | 43-E | flow | P | Euler, dt = 2⁻⁷ | ≈ 7.63n² + 50.4n − 609 | 33,695 | 2,229 | 8,717 | 114,079 | 416,159 | 0.737 | 1.589 | 2.22×10⁻¹⁷ | 9.75×10⁻⁷✓ | 2.75×10⁻¹¹✓ |
| 40 | [Sprott-Linz I](#sprott_linz_i__rk4) | 43-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 44.9n² + 1.24e+03n + … | 242,164 | 16,453 | 65,909 | 877,979ᵉ | 3,245,487ᵉ | 5.424 | 11.444 | 5.48×10⁻¹⁷ | 1.06×10⁻⁶✓ | 2.25×10⁻¹³✓ |
| 41 | [Genesio-Tesi](#genesio_tesi__euler) | 54-E | flow | P | Euler, dt = 2⁻⁷ | ≈ 8.58n² + 80.7n − 1130 | 38,792 | 2,534 | 9,978 | 124,040 | 435,848 | 0.752 | 1.771 | 2.79×10⁻¹⁷ | 0.056✓ | 0.015✓ |
| 42 | [Genesio-Tesi](#genesio_tesi__rk4) | 54-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 44.9n² + 1.65e+03n + … | 262,578 | 18,433 | 72,985 | 924,131ᵉ | 3,340,516ᵉ | 6.094 | 12.387 | 5.40×10⁻¹⁷ | 0.032✓ | 0.009✓ |
| 43 | [Sprott-Linz L](#sprott_linz_l__euler) | 46-E | flow | P | Euler, dt = 2⁻⁷ | 10.8n² − 51.1n − 223 | 40,543 | 1,712* | 9,151 | 128,109 | 443,885 | 0.741 | 1.861 | 2.11×10⁻¹⁵ | 0.009✓ | 2.03×10⁻⁴✓ |
| 44 | [Sprott-Linz L](#sprott_linz_l__rk4) | 46-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 61.8n² + 480n + … | 268,792 | 12,765 | 64,749 | 1,061,681ᵉ | 4,160,271ᵉ | 5.620 | 12.748 | 3.52×10⁻¹⁵ | 0.058✓ | 0.001✓ |
| 45 | [Hopalong (a=7.17,b=8.44,c=2.56)](#hopalong_a_7_17_b_8_44_c_2_56__map) | 67 | map | D | map iteration | ≈ 10.6n² − 32.8n − 539 | 40,739 | 1,779* | 9,114 | 169,516ᵉ | 688,065ᵉ | 1.132 | 2.471 | 2.88×10⁻¹⁶ | 0.599 | 0.718✓ |
| 46 | [Hénon](#h_non__map) | 03 | map | P | map iteration | ≈ 5.47n² + 394n − 6449 | 40,846 | 2,914 | 11,394 | 128,078‡ | 443,854‡ | 1.768 | 3.219 | 3.79×10⁻¹⁷ | 0.005 | 0.002✓ |
| 47 | [Lü](#l__euler) | 25-E | flow | P | Euler, dt = 2⁻⁹ | 11.5n² − 16n − 145 | 45,935 | 520* | 11,119 | 186,223 | 749,423 | 0.828 | 2.036 | 4.49×10⁻¹⁴ | 12.702 | 0.005 |
| 48 | [Lü](#l__rk4) | 25-R | flow | P | RK4, dt = 2⁻⁷ | ≈ 73.5n² − 192n + … | 281,364 | 7,273 | 61,492 | 1,172,335ᵉ | 4,762,091ᵉ | 4.960 | 12.874 | 1.38×10⁻¹⁴ | 0.012✓ | 0.008✓ |
| 49 | [Sprott-Linz A (Nose-Hoover) ◊](#sprott_linz_a_nose_hoover__euler) | 36-E | flow | P | Euler, dt = 2⁻⁹ | 11.5n² − 16n − 20 | 46,060 | 2,668 | 11,244 | 186,348 | 749,548 | 0.750 | 1.973 | 1.44×10⁻¹⁵ | 5.71×10⁻⁴ | 8.29×10⁻¹³✓ |
| 50 | [Sprott-Linz A (Nose-Hoover)](#sprott_linz_a_nose_hoover__rk4) | 36-R | flow | P | RK4, dt = 2⁻⁷ | ≈ 73.6n² − 114n + … | 290,209 | 13,827 | 67,891 | 1,188,332ᵉ | 4,792,946ᵉ | 4.874 | 12.753 | 3.24×10⁻¹⁵ | 6.72×10⁻⁵✓ | 4.16×10⁻⁹✓ |
| 51 | [Sprott-Linz B](#sprott_linz_b__euler) | 37-E | flow | P | Euler, dt = 2⁻⁷ | 11.5n² − 12n − 8 | 46,328 | 2,744 | 11,384 | 186,872 | 750,584 | 0.791 | 2.007 | 1.73×10⁻¹⁶ | 8.02×10⁻⁴✓ | 0.059✓ |
| 52 | [Sprott-Linz B](#sprott_linz_b__rk4) | 37-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 69.8n² + 241n + … | 292,828 | 15,814 | 71,478 | 1,166,984ᵉ | 4,626,411ᵉ | 6.036 | 13.826 | 4.29×10⁻¹⁶ | 0.041 | 0.070✓ |
| 53 | [Sprott-Linz C](#sprott_linz_c__euler) | 38-E | flow | P | Euler, dt = 2⁻⁷ | 11.5n² − 11n − 12 | 46,388 | 2,756 | 11,412 | 186,996 | 750,836 | 0.936 | 2.137 | 1.78×10⁻¹⁶ | 0.030✓ | 0.084 |
| 54 | [Sprott-Linz C](#sprott_linz_c__rk4) | 38-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 71.6n² + 71.1n + … | 291,736 | 14,905 | 69,833 | 1,177,701ᵉ | 4,707,998ᵉ | 4.029 | 10.942 | 8.55×10⁻¹⁶ | 0.056✓ | 0.040✓ |
| 55 | [Chen](#chen__euler) | 24-E | flow | P | Euler, dt = 2⁻⁹ | 11.5n² − 5n − 143 | 46,641 | 636* | 11,473 | 187,633 | 752,241 | 0.916 | 2.143 | 8.88×10⁻¹⁴ | 0.021 | 0.024 |
| 56 | [Chen](#chen__rk4) | 24-R | flow | P | RK4, dt = 2⁻⁷ | ≈ 66.9n² + 446n + … | 281,869 | —* | 61,549 | 1,131,608ᵉ | 4,478,168ᵉ | 5.010 | 12.952 | 2.95×10⁻¹⁴ | 0.037 | 0.023 |
| 57 | [Sprott-Linz E](#sprott_linz_e__euler) | 39-E | flow | P | Euler, dt = 2⁻⁷ | 11.5n² − 7n + 5 | 46,661 | 2,837 | 11,557 | 187,525 | 751,877 | 0.916 | 2.138 | 8.38×10⁻¹⁷ | 0.087 | 0.011✓ |
| 58 | [Sprott-Linz E](#sprott_linz_e__rk4) | 39-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 67.9n² + 412n + … | 294,152 | 16,733 | 73,197 | 1,156,973ᵉ | 4,547,180ᵉ | 6.132 | 13.916 | 2.33×10⁻¹⁶ | 0.007✓ | 1.79×10⁻⁴✓ |
| 59 | [2D Lorenz map (a=1.25,b=0.75)](#2d_lorenz_map_a_1_25_b_0_75__map) | 65 | map | P | map iteration | 11.5n² + 1n − 4 | 47,164 | 2,956 | 11,804 | 188,540 | 753,916 | 1.626 | 3.347 | 1.08×10⁻¹⁸ | 0.007 | 0.009 |
| 60 | [Arneodo](#arneodo__euler) | 27-E | flow | P | Euler, dt = 2⁻⁸ | 11.5n² + n + 9 | 47,177 | 2,969* | 11,817 | 188,553 | 753,929 | 0.952 | 2.165 | 1.47×10⁻¹⁵ | 0.095 | 0.044✓ |
| 61 | [Arneodo](#arneodo__rk4) | 27-R | flow | P | RK4, dt = 2⁻⁶ | ≈ 73.7n² − 70.3n + … | 293,400 | 14,509 | 69,373 | 1,195,517ᵉ | 4,810,663ᵉ | 5.608 | 13.341 | 3.45×10⁻¹⁵ | 0.031✓ | 0.030✓ |
| 62 | [Moore-Spiegel (T=6,R=20)](#moore_spiegel_t_6_r_20__euler) | 29-E | flow | P | Euler, dt = 2⁻⁹ | 11.5n² + 4n + 16 | 47,376 | 3,024 | 11,920 | 188,944 | 754,704 | 0.923 | 2.163 | 2.91×10⁻¹⁵ | 0.162 | 0.002✓ |
| 63 | [Moore-Spiegel (T=6,R=20)](#moore_spiegel_t_6_r_20__rk4) | 29-R | flow | P | RK4, dt = 2⁻⁷ | ≈ 76n² − 398n + … | 283,241 | 10,536 | 62,537 | 1,191,492ᵉ | 4,875,386ᵉ | 4.726 | 12.588 | 7.70×10⁻¹⁵ | 0.042✓ | 4.88×10⁻⁴✓ |
| 64 | [Burke-Shaw](#burke_shaw__euler) | 56-E | flow | P | Euler, dt = 2⁻⁹ | ≈ 11.5n² + 26.6n + 74 | 48,856 | 3,441 | 12,698 | 191,704 | 760,024 | 1.048 | 2.245 | 2.30×10⁻¹⁶ | 0.062✓ | 0.011 |
| 65 | [Burke-Shaw](#burke_shaw__rk4) | 56-R | flow | P | RK4, dt = 2⁻⁷ | ≈ 73.5n² − 13.1n + … | 295,492 | 14,829 | 70,389 | 1,198,518ᵉ | 4,809,725ᵉ | 5.808 | 13.539 | 3.34×10⁻¹⁵ | 0.010 | 0.009✓ |
| 66 | [Lorenz](#lorenz__euler) | 02-E | flow | P | Euler, dt = 2⁻⁷ | 14.0n² − 51n − 281 | 53,799 | 2,487* | 12,423 | 202,231‡ | 781,047‡ | 0.987 | 2.448 | 3.59×10⁻¹⁴ | 0.016✓ | 0.093 |
| 67 | [Lorenz](#lorenz__rk4) | 02-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 82.3n² − 137n + … | 321,325 | 13,501 | 73,421 | 1,324,205ᵉ | 5,349,421ᵉ | 6.565 | 15.427 | 2.97×10⁻¹⁵ | 0.003✓ | 0.067 |
| 68 | [Hyper-Lu (4D)](#hyper_lu_4d__euler) | 60-E | flow | P | Euler, dt = 2⁻⁹ | ≈ 12.1n² + 144n − 4272 | 54,668 | 636* | 12,860 | 205,304 | 787,192 | 0.706 | 1.829 | 1.16×10⁻¹³ | 0.026✓ | 0.016✓ |
| 69 | [Hyper-Lu (4D)](#hyper_lu_4d__rk4) | 60-R | flow | P | RK4, dt = 2⁻⁷ | ≈ 84.6n² + 445n + … | 349,680 | —* | 75,120 | 1,416,922ᵉ | 5,632,886ᵉ | 4.651 | 12.241 | 3.20×10⁻¹⁴ | 0.078 | 0.044 |
| 70 | [Rucklidge](#rucklidge__euler) | 33-E | flow | P | Euler, dt = 2⁻⁷ | ≈ 13.7n² − 13n − 418 | 54,734 | 2,918* | 13,134 | 203,342 | 783,182 | 1.034 | 2.508 | 1.47×10⁻¹⁵ | 0.038✓ | 0.052✓ |
| 71 | [Rucklidge](#rucklidge__rk4) | 33-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 78.6n² + 204n + … | 324,625 | 15,693 | 77,277 | 1,305,863ᵉ | 5,197,169ᵉ | 5.855 | 14.408 | 3.31×10⁻¹⁵ | 0.015✓ | 0.020✓ |
| 72 | [Duffing map](#duffing_map__map) | 11 | map | P | map iteration | ≈ 12.1n² + 130n − 2474 | 55,299 | 3,383 | 13,967 | 204,419‡ | 785,283‡ | 1.937 | 4.035 | 1.26×10⁻¹⁷ | 0.003 | 0.001✓ |
| 73 | [Shimizu–Morioka](#shimizu_morioka__euler) | 28-E | flow | P | Euler, dt = 2⁻⁷ | ≈ 13.5n² + 25n − 658 | 56,288 | 3,366 | 13,950 | 206,368‡ | 789,152‡ | 1.162 | 2.614 | 4.89×10⁻¹⁷ | 0.032✓ | 0.027✓ |
| 74 | [Shimizu–Morioka](#shimizu_morioka__rk4) | 28-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 69.9n² + 1.02e+03n + … | 332,533 | 20,801 | 86,449 | 1,260,508ᵉ | 4,826,980ᵉ | 7.221 | 15.540 | 1.09×10⁻¹⁶ | 0.016✓ | 0.017✓ |
| 75 | [Finance (a=0.001,b=0.2,c=1.1)](#finance_a_0_001_b_0_2_c_1_1__euler) | 62-E | flow | P | Euler, dt = 2⁻⁷ | ≈ 16.2n² − 31.2n − 447 | 63,795 | 3,238 | 15,088 | 221,038 | 818,158 | 1.056 | 2.769 | 3.71×10⁻¹⁶ | 0.480 | 0.011✓ |
| 76 | [Finance (a=0.001,b=0.2,c=1.1)](#finance_a_0_001_b_0_2_c_1_1__rk4) | 62-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 81.7n² + 721n + … | 362,948 | 19,729 | 90,129 | 1,415,838ᵉ | 5,522,091ᵉ | 7.185 | 16.524 | 8.31×10⁻¹⁶ | 0.091✓ | 0.017✓ |
| 77 | [Rikitake](#rikitake__euler) | 26-E | flow | P | Euler, dt = 2⁻⁸ | 17.25n² − 36n − 59 | 68,325 | 3,789* | 16,469 | 278,021 | 1,121,349 | 1.313 | 3.125 | 1.42×10⁻¹⁵ | 0.002✓ | 0.026 |
| 78 | [Rikitake](#rikitake__rk4) | 26-R | flow | P | RK4, dt = 2⁻⁶ | ≈ 96.5n² − 113n + … | 383,666 | 19,490 | 91,090 | 1,562,866ᵉ | 6,291,570ᵉ | 7.416 | 17.649 | 1.68×10⁻¹⁵ | 0.023✓ | 0.017✓ |
| 79 | [Complex quadratic (c=-2)](#complex_quadratic_c_2__map) | 15 | map | P | map iteration | 17.3n² − 35n − 2 | 68,414 | 3,854 | 16,542 | 278,142 | 1,121,534 | 0.798 | 1.676 | 4.59×10⁻¹⁹ | 4.86×10⁻⁶✓ | 0.002 |
| 80 | [Hyperchaotic Chen (4D) ◊](#hyperchaotic_chen_4d__euler) | 59-E | flow | P | Euler, dt = 2⁻¹⁰ | ≈ 14.1n² + 283n − 6611 | 69,789 | 741* | 17,165 | 281,021 | 1,127,421 | 0.947 | 2.337 | 9.58×10⁻¹⁴ | 0.027✓ | 0.020 |
| 81 | [Hyperchaotic Chen (4D)](#hyperchaotic_chen_4d__rk4) | 59-R | flow | P | RK4, dt = 2⁻⁸ | ≈ 95.3n² + 713n + … | 405,516 | —* | 89,164 | 1,620,766ᵉ | 6,397,550ᵉ | 5.205 | 13.610 | 2.94×10⁻¹⁴ | 0.006✓ | 0.006✓ |
| 82 | [Hyper-Lorenz (4D)](#hyper_lorenz_4d__euler) | 58-E | flow | P | Euler, dt = 2⁻⁹ | ≈ 16.8n² + 213n − 6335 | 76,644 | 635* | 17,940 | 295,716 | 1,156,452 | 1.048 | 2.600 | 1.38×10⁻¹³ | 0.084 | 0.009 |
| 83 | [Hyper-Lorenz (4D)](#hyper_lorenz_4d__rk4) | 58-R | flow | P | RK4, dt = 2⁻⁷ | ≈ 112n² − 29.5n + … | 439,084 | 11,990 | 97,532 | 1,808,162ᵉ | 7,286,748ᵉ | 6.083 | 15.320 | 1.52×10⁻¹⁴ | 0.047✓ | 0.007 |
| 84 | [Chen-Lee ◊](#chen_lee__euler) | 61-E | flow | P | Euler, dt = 2⁻¹⁰ | ≈ 18.5n² + 134n − 6082 | 78,442 | 169* | 17,334 | 302,514 | 1,169,906 | 1.097 | 3.289 | 1.49×10⁻¹³ | 0.024✓ | 0.008✓ |
| 85 | [Chen-Lee](#chen_lee__rk4) | 61-R | flow | P | RK4, dt = 2⁻⁸ | ≈ 99.8n² + 664n + … | 419,333 | —* | 91,189 | 1,686,773ᵉ | 6,676,455ᵉ | 5.213 | 17.201 | 2.70×10⁻¹⁴ | 0.089✓ | 0.003✓ |
| 86 | [Sakarya](#sakarya__euler) | 64-E | flow | P | Euler, dt = 2⁻⁸ | ≈ 22.2n² − 105n − 400 | 84,001 | 3,616* | 19,025 | 311,357 | 1,187,325 | 1.370 | 3.678 | 7.58×10⁻¹⁵ | 1.320✗ | 2.424✗ |
| 87 | [Sakarya](#sakarya__rk4) | 64-R | flow | P | RK4, dt = 2⁻⁶ | ≈ 114n² − 206n + … | 445,265 | 19,249 | 102,113 | 1,834,374ᵉ | 7,412,068ᵉ | 8.425 | 20.723 | 1.75×10⁻¹⁵ | 0.172✓ | 0.035✓ |
| 88 | [Tinkerbell](#tinkerbell__map) | 22 | map | P | map iteration | ≈ 16.9n² + 343n − 5848 | 84,866 | 5,490 | 21,930 | 310,434‡ | 1,185,506‡ | 3.190 | 6.320 | 2.70×10⁻¹⁷ | 0.008 | 0.002✓ |
| 89 | [Hadley circulation](#hadley_circulation__euler) | 32-E | flow | P | Euler, dt = 2⁻⁹ | 23n² − 15.1n + 84 | 93,330 | 5,731 | 23,154 | 374,994 | 1,503,570 | 1.983 | 4.352 | 3.62×10⁻¹⁶ | 0.001✓ | 1.19×10⁻⁶✓ |
| 90 | [Hadley circulation](#hadley_circulation__rk4) | 32-R | flow | P | RK4, dt = 2⁻⁷ | ≈ 120n² − 117n + … | 477,716 | 25,406 | 114,606 | 1,939,328ᵉ | 7,798,243ᵉ | 9.566 | 22.047 | 1.66×10⁻¹⁵ | 0.084✓ | 0.012✓ |
| 91 | [Halvorsen (a = 1.4)](#halvorsen_a_1_4__euler) | 35-E | flow | P | Euler, dt = 2⁻⁹ | 24.75n² − 99n − 381 | 94,659 | 4,371* | 21,795 | 331,533‡ | 1,227,213‡ | 1.675 | 4.237 | 1.20×10⁻¹⁴ | 0.020✓ | 0.016✓ |
| 92 | [Halvorsen (a = 1.4)](#halvorsen_a_1_4__rk4) | 35-R | flow | P | RK4, dt = 2⁻⁷ | ≈ 118n² + 295n + … | 485,118 | 22,986 | 115,002 | 1,954,180ᵉ | 7,781,209ᵉ | 9.387 | 22.406 | 3.56×10⁻¹⁵ | 0.016✓ | 0.008 |
| 93 | [Newton-Leipnik](#newton_leipnik__euler) | 55-E | flow | P | Euler, dt = 2⁻⁸ | ≈ 22.9n² + 119n − 1792 | 99,041 | 6,203 | 25,147 | 338,113 | 1,240,193 | 1.886 | 4.452 | 2.26×10⁻¹⁷ | 0.005✓ | 0.042✓ |
| 94 | [Newton-Leipnik](#newton_leipnik__rk4) | 55-R | flow | P | RK4, dt = 2⁻⁶ | ≈ 97.8n² + 2.11e+03n + … | 501,366 | 33,802 | 134,778 | 1,844,526ᵉ | 6,923,510ᵉ | 11.517 | 23.912 | 1.07×10⁻¹⁶ | 0.066✓ | 0.133✓ |
| 95 | [Lorenz 96 (N=5, F=8)](#lorenz_96_n_5_f_8__euler) | 31-E | flow | P | Euler, dt = 2⁻⁸ | 28.8n² − 57.5n − 155 | 113,925 | 6,285* | 27,445 | 463,525 | 1,869,285 | 1.292 | 3.080 | 6.11×10⁻¹⁵ | 0.012✓ | 0.024 |
| 96 | [Lorenz 96 (N=5, F=8)](#lorenz_96_n_5_f_8__rk4) | 31-R | flow | P | RK4, dt = 2⁻⁶ | ≈ 165n² − 695n + … | 628,095 | 27,855 | 143,455 | 2,611,135ᵉ | 10,632,255ᵉ | 7.129 | 17.373 | 2.03×10⁻¹⁵ | 0.001✓ | 0.020✓ |
| 97 | [Mackey–Glass](#mackey_glass__euler) | 09-E | flow | D | Euler, dt = 2⁻⁶ | ≈ 36n² − 142n − 273 | 138,095 | 6,671 | 32,047 | 571,375ᵉ | 2,322,671ᵉ | 6.813 | 17.432 | 9.09×10⁻¹⁷ | 6.43×10⁻⁴✓ | 1.48×10⁻¹⁰✓ |
| 98 | [Mackey–Glass](#mackey_glass__rk4) | 09-R | flow | D | RK4, dt = 2⁻⁵ | ≈ 113n² + 244n − 8208 | 466,180 | 25,518 | 113,574 | 1,866,319ᵉ | 7,427,477ᵉ | 23.887 | 58.795 | 7.28×10⁻¹⁶ | 9.65×10⁻⁴✓ | 5.09×10⁻¹²✓ |
| 99 | [Gumowski-Mira (mu=-0.7)](#gumowski_mira_mu_0_7__map) | 66 | map | D | map iteration | ≈ 51.3n² − 77.7n − 2878 | 201,611 | 9,307* | 46,801 | 827,300ᵉ | 3,337,716ᵉ | 6.175 | 14.221 | 1.10×10⁻¹⁵ | 0.029 | 0.009 |
| 100 | [Aizawa ◊](#aizawa__euler) | 57-E | flow | P | Euler, dt = 2⁻⁷ | ≈ 58.3n² − 68.5n − 1094 | 233,130 | 12,858 | 56,282 | 888,880 | 3,472,176 | 4.312 | 10.456 | 1.86×10⁻¹⁶ | 0.006✓ | 0.008✓ |
| 101 | [Aizawa](#aizawa__rk4) | 57-R | flow | P | RK4, dt = 2⁻⁵ | ≈ 242n² + 1.24e+03n + … | 1,039,344 | 60,673 | 259,281 | 4,093,823ᵉ | 16,129,913ᵉ | 22.197 | 48.659 | 2.65×10⁻¹⁶ | 0.148 | 0.005✓ |
| 102 | [Zaslavskii (r=3, nu=400/3, eps=0.3)](#zaslavskii_r_3_nu_400_3_eps_0_3__map) | 21 | map | T | map iteration | ≈ 0.333n³ + 69.1n² + … | 270,633 | 3,432* | 36,027 | 1,617,318ᵉ | 9,673,527ᵉ | 4.571 | 18.315 | 9.17×10⁻¹⁵ | 4.79×10⁻⁴✓ | 0.005 |
| 103 | [Sine map (μ = 0.99)](#sine_map_0_99__map) | 16 | map | T | map iteration | ≈ 0.27n³ + 82n² + … | 293,018 | 7,344 | 43,313 | 1,657,288ᵉ | 9,328,421ᵉ | 11.799 | 41.561 | 1.77×10⁻¹⁷ | 0.001 | 0.001✓ |
| 104 | [Standard map (K=5)](#standard_map_k_5__map) | 08 | map | T | map iteration | ≈ 0.264n³ + 82.5n² + … | 294,014 | 7,472 | 43,602 | 1,659,835ᵉ | 9,324,859ᵉ | 6.112 | 21.098 | 3.78×10⁻¹⁷ | 0.020 | 0.012 |
| 105 | [Circle map (K=3, Omega=0.1)](#circle_map_k_3_omega_0_1__map) | 13 | map | T | map iteration | ≈ 0.25n³ + 83.9n² + … | 294,532 | 7,466 | 43,733 | 1,650,676ᵉ | 9,180,328ᵉ | 12.153 | 42.161 | 7.08×10⁻¹⁸ | 9.79×10⁻⁴✓ | 0.001✓ |
| 106 | [Kaplan-Yorke (alpha=0.2) ⚠](#kaplan_yorke_alpha_0_2__map) | 19 | map | T | map iteration | ≈ 0.243n³ + 85.3n² + … | 297,026 | 7,714 | 44,527 | 1,655,945ᵉ | 9,148,593ᵉ | 0.010⚠ | 0.010⚠ | 2.56×10⁻¹⁷ | n/a | n/a |
| 107 | [Ueda oscillator](#ueda_oscillator__euler) | 23-E | flow | T | Euler, dt = 2⁻⁸ | ≈ 0.629n³ + 41.9n² + … | 306,359 | 6,653 | 49,579 | 1,944,343ᵉ | 13,176,065ᵉ | 3.657 | 13.401 | 1.27×10⁻¹⁵ | 0.024✓ | 0.022✓ |
| 108 | [Ueda oscillator](#ueda_oscillator__rk4) | 23-R | flow | T | RK4, dt = 2⁻⁶ | ≈ 1.62n³ + 186n² + … | 1,058,139 | 22,211 | 181,798 | 6,185,062ᵉ | 38,810,984ᵉ | 13.990 | 47.088 | 3.30×10⁻¹⁵ | 0.007✓ | 0.015✓ |
| 109 | [WINDMI (a=0.7,b=2.5)](#windmi_a_0_7_b_2_5__euler) | 63-E | flow | T | Euler, dt = 2⁻⁹ | ≈ 0.314n³ + 109n² + … | 334,429 | 3,746 | 41,830 | 2,024,766ᵉ | 11,529,390ᵉ | 3.774 | 16.195 | 2.91×10⁻¹⁵ | 0.067✓ | 0.021✓ |
| 110 | [WINDMI (a=0.7,b=2.5)](#windmi_a_0_7_b_2_5__rk4) | 63-R | flow | T | RK4, dt = 2⁻⁷ | ≈ 0.831n³ + 509n² + … | 1,442,498 | 19,332 | 192,376 | 8,234,583ᵉ | 43,459,023ᵉ | 16.048 | 68.487 | 6.98×10⁻¹⁵ | 0.139✓ | 0.017✓ |
| 111 | [Gauss (alpha=4.9, beta=-0.5)](#gauss_alpha_4_9_beta_0_5__map) | 17 | map | T | map iteration | ≈ 0.115n³ + 148n² + … | 409,575 | 9,592 | 62,083 | 2,180,169ᵉ | 10,630,853ᵉ | 17.611 | 60.150 | 2.36×10⁻¹⁷ | 0.003✓ | 6.88×10⁻⁴✓ |
| 112 | [Ikeda (u=0.9)](#ikeda_u_0_9__map) | 12 | map | T | map iteration | ≈ 1.93n³ + 63.5n² + … | 756,904 | 21,236 | 127,281 | 5,080,494ᵉ | 36,555,723ᵉ | 16.923 | 52.567 | 9.02×10⁻¹⁷ | 0.002✓ | 0.005 |
| 113 | [Thomas (b=0.208186)](#thomas_b_0_208186__euler) | 34-E | flow | T | Euler, dt = 2⁻⁶ | ≈ 0.782n³ + 272n² + … | 893,994 | 22,581 | 133,350 | 5,169,976ᵉ | 29,008,182ᵉ | 10.642 | 40.584 | 1.86×10⁻¹⁶ | 4.44×10⁻⁴✓ | 1.06×10⁻⁶✓ |
| 114 | [Thomas (b=0.208186)](#thomas_b_0_208186__rk4) | 34-R | flow | T | RK4, dt = 2⁻⁴ | ≈ 2.11n³ + 1.22e+03n² + … | 3,682,854 | 98,889 | 566,301 | 20,356,157ᵉ | 106,930,960ᵉ | 29.789 | 144.762 | 1.28×10⁻¹⁶ | 0.002✓ | 1.92×10⁻⁶✓ |
| 115 | [Fractal-Dream](#fractal_dream__map) | 70 | map | T | map iteration | ≈ 3.7n³ + 64.5n² + … | 1,182,677 | 23,407 | 172,769 | 8,724,610ᵉ | 66,148,957ᵉ | 22.965 | 82.192 | 3.82×10⁻¹⁷ | 0.007✓ | 0.006 |
| 116 | [De Jong](#de_jong__map) | 69 | map | T | map iteration | ≈ 0.869n³ + 380n² + … | 1,191,312 | 30,220 | 178,278 | 6,759,641ᵉ | 36,797,593ᵉ | 24.390 | 84.293 | 2.48×10⁻¹⁷ | 0.003 | 0.003 |
| 117 | [Clifford](#clifford__map) | 68 | map | T | map iteration | ≈ 0.708n³ + 400n² + … | 1,207,509 | 31,547 | 183,319 | 6,700,011ᵉ | 35,313,574ᵉ | 25.433 | 85.831 | 1.33×10⁻¹⁶ | 0.003✓ | 0.005 |


## Columns

#
:   Position in the current order (sort or filter renumbers it; click # for the gate-count ranking).

System
:   Name and main parameters; click it to open the profile. Marks: ⚠ degenerate, ◊ slow divergence at 32 bits.

ID
:   Fixed system number, from the most classical systems (01 logistic, 02 Lorenz, 03 Hénon, …) to the newest; flows add -E for the Euler row and -R for the RK4 row.

Type
:   Map (discrete iteration) or flow (ODE integrated with a fixed step).

Class
:   Cost class: L linear in n, P polynomial (≈ n²), D division or √ (≈ n²), T sin, cos or exp (≈ n³).

Scheme
:   Map iteration, or Euler / RK4 with the step dt (a power of two).

L(n)
:   Fitted law for the gates per iteration as a function of the word width n.

L(64), L(16), L(32), L(128), L(256)
:   Two-input gates per iteration at that word width (ᵉ extrapolated, ‡ 53-bit constants).

pJ/bit 32, pJ/bit 64
:   Estimated energy per output bit per iteration for the 32- and 64-bit circuits (switching model).

1-step err
:   Median error of one 64-bit circuit step against exact arithmetic, over 200 attractor states (÷ dt for flows).

λ err
:   Relative difference between the largest Lyapunov exponent of the 64-bit circuit and of float64.

Density err
:   Wasserstein distance between the distributions of x from the circuit and from float64, ÷ the std of x.

Class: L linear in n (no state products, dyadic constants); P polynomial, about n²; D division or square root, about n²; T sin, cos or exp, about n³.

⚠ degenerate in binary: the state collapses and the circuit stops switching. ◊ chaotic in floating point, but a 2⁻¹² nudge did not saturate within 15,000 steps of the 32-bit circuit. \* at 16 bits too few fractional bits remain to reproduce the attractor. ‡ constants limited to 53-bit precision, so cost is understated. ᵉ extrapolated from the fit over 16 to 64 bits (all RK4 rows at 128 and 256 bits). ≈ approximate fit.

1-step err: median error of one 64-bit circuit step against exact arithmetic (rational, or 200-digit for sin, cos, exp and √), over 200 states on the attractor, divided by dt for flows. λ err: |λcircuit − λfloat64| / |λfloat64| from two-trajectory renormalisation. Density err: Wasserstein distance between the distributions of x, divided by the float64 standard deviation. ✓ at or below the float64 noise floor (float64 against float64 from nearby initial conditions), so indistinguishable. ✗ the 64-bit circuit left the attractor (integer-range overflow). n/a degenerate rows. The profile shows both values and the noise floors.

Energy model: zero-delay switching activity from simulation, 40 fJ per lookup-table output toggle and 10 fJ per flip-flop per cycle; glitches and static power excluded. These are model estimates, not measurements.

Logical Chaos · CAS Lab, Sustainable Circuits and Systems Lab · Maynooth Universitymaynoothuniversity.ie/caslab

## System profiles

<a id="logistic_r_3_9375__map"></a>

### Logistic (01)

**Equations:** x\_k+1 = r x\_k (1 − x\_k)

*Plot (not reproduced in Markdown):* Return map x(k+1) against x(k): 1,500 consecutive iterates after the 10³-step transient.

| Field | Value |
|---|---|
| Parameters | r = 3.9375 = 63/16 (dyadic) |
| Initial condition | x\_0 = 0.3 |
| Type | map |
| Class | Polynomial |
| Scheme | map iteration |
| L(n) | 5.75n² + 2.5n − 7 |
| Gates at 64 bits | 23,705 |
| pJ/bit (32 / 64-bit) | 1.705 / 3.467 |
| Lyapunov exponent | 0.5265 (float64), 0.5216 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 2 integer bits and 62 fractional bits (resolution 2⁻⁶²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 4.99×10⁻¹⁹, max 9.21×10⁻¹⁹; float64: median 2.51×10⁻¹⁷, max 1.27×10⁻¹⁶ |
| Circuit vs float64, one step | median 2.55×10⁻¹⁷, max 1.28×10⁻¹⁶ |
| Netlist check | the 23,705-gate netlist (depth 327) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00927 (noise floor 0.00439) |
| Density of x (relative Wasserstein) | 0.00428 against float64 (noise floor 0.00291) |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

May, R. M. (1976). Simple mathematical models with very complicated dynamics. *Nature*, 261(5560), 459–467. [doi:10.1038/261459a0](https://doi.org/10.1038/261459a0)

Classic review establishing the logistic map as a paradigm of chaos. May studies the full range of r; our r = 3.9375 lies in the chaotic regime he describes.

```bibtex
@article{may1976simple,
  author  = {May, Robert M.},
  title   = {Simple mathematical models with very complicated dynamics},
  journal = {Nature},
  volume  = {261},
  number  = {5560},
  pages   = {459--467},
  year    = {1976},
  doi     = {10.1038/261459a0}
}
```

<a id="lorenz__euler"></a>

### Lorenz (02-E)

**Equations:** ẋ = σ(y − x); ẏ = x(ρ − z) − y; ż = xy − βz

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | σ = 10, ρ = 28, β = 8/3 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | 14.0n² − 51n − 281 |
| Gates at 64 bits | 53,799 |
| pJ/bit (32 / 64-bit) | 0.987 / 2.448 |
| Lyapunov exponent | 1.0004 (float64), 0.9841 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 12 integer bits and 52 fractional bits (resolution 2⁻⁵²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.59×10⁻¹⁴, max 5.86×10⁻¹⁴; float64: median 1.05×10⁻¹³, max 4.55×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 1.14×10⁻¹³, max 4.55×10⁻¹³ |
| Netlist check | the 53,799-gate netlist (depth 363) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0163 (noise floor 0.0167) — indistinguishable |
| Density of x (relative Wasserstein) | 0.093 against float64 (noise floor 0.0728) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Lorenz, E. N. (1963). Deterministic nonperiodic flow. *Journal of the Atmospheric Sciences*, 20(2), 130–141. [doi:10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2](https://doi.org/10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2)

Original paper introducing the three-mode convection model. Ours uses sigma=10, r=28, b=8/3, the values used in the original paper.

```bibtex
@article{Lorenz1963,
  author  = {Lorenz, Edward N.},
  title   = {Deterministic Nonperiodic Flow},
  journal = {Journal of the Atmospheric Sciences},
  year    = {1963},
  volume  = {20},
  number  = {2},
  pages   = {130--141},
  doi     = {10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2}
}
```

<a id="lorenz__rk4"></a>

### Lorenz (02-R)

**Equations:** ẋ = σ(y − x); ẏ = x(ρ − z) − y; ż = xy − βz

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | σ = 10, ρ = 28, β = 8/3 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 82.3n² − 137n + … |
| Gates at 64 bits | 321,325 |
| pJ/bit (32 / 64-bit) | 6.565 / 15.427 |
| Lyapunov exponent | 0.8989 (float64), 0.8966 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 11 integer bits and 53 fractional bits (resolution 2⁻⁵³). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.97×10⁻¹⁵, max 8.45×10⁻¹⁵; float64: median 3.11×10⁻¹⁴, max 1.77×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 3.20×10⁻¹⁴, max 1.78×10⁻¹³ |
| Netlist check | the 321,325-gate netlist (depth 1,090) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00259 (noise floor 0.00723) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0668 against float64 (noise floor 0.032) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Lorenz, E. N. (1963). Deterministic nonperiodic flow. *Journal of the Atmospheric Sciences*, 20(2), 130–141. [doi:10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2](https://doi.org/10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2)

Original paper introducing the three-mode convection model. Ours uses sigma=10, r=28, b=8/3, the values used in the original paper.

```bibtex
@article{Lorenz1963,
  author  = {Lorenz, Edward N.},
  title   = {Deterministic Nonperiodic Flow},
  journal = {Journal of the Atmospheric Sciences},
  year    = {1963},
  volume  = {20},
  number  = {2},
  pages   = {130--141},
  doi     = {10.1175/1520-0469(1963)020<0130:DNF>2.0.CO;2}
}
```

<a id="h_non__map"></a>

### Hénon (03)

**Equations:** x\_k+1 = 1 − ax\_k^2 + y\_k,   y\_k+1 = bx\_k

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | a = 1.4, b = 0.3 |
| Initial condition | x\_0 = 0.1, y\_0 = 0.1 |
| Type | map |
| Class | Polynomial |
| Scheme | map iteration |
| L(n) | ≈ 5.47n² + 394n − 6449 |
| Gates at 64 bits | 40,846 |
| pJ/bit (32 / 64-bit) | 1.768 / 3.219 |
| Lyapunov exponent | 0.4181 (float64), 0.4201 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 3.79×10⁻¹⁷, max 1.44×10⁻¹⁶; float64: median 7.39×10⁻¹⁷, max 4.74×10⁻¹⁶ |
| Circuit vs float64, one step | median 5.79×10⁻¹⁷, max 3.30×10⁻¹⁶ |
| Netlist check | the 40,846-gate netlist (depth 417) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00501 (noise floor 0.00248) |
| Density of x (relative Wasserstein) | 0.00229 against float64 (noise floor 0.00241) — indistinguishable |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Hénon, M. (1976). A two-dimensional mapping with a strange attractor. *Communications in Mathematical Physics*, 50(1), 69–77. [doi:10.1007/BF01608556](https://doi.org/10.1007/BF01608556)

Original paper. Hénon used a = 1.4, b = 0.3; ours match.

```bibtex
@article{henon1976two,
  author  = {H{\'e}non, Michel},
  title   = {A two-dimensional mapping with a strange attractor},
  journal = {Communications in Mathematical Physics},
  volume  = {50},
  number  = {1},
  pages   = {69--77},
  year    = {1976},
  doi     = {10.1007/BF01608556}
}
```

<a id="r_ssler__euler"></a>

### Rössler (04-E)

**Equations:** ẋ = −y − z; ẏ = x + ay; ż = b + z(x − c)

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.2, b = 0.2, c = 5.7 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁸ |
| L(n) | 8.25n² − 27n − 169 |
| Gates at 64 bits | 31,925 |
| pJ/bit (32 / 64-bit) | 0.524 / 1.427 |
| Lyapunov exponent | 0.0654 (float64), 0.0630 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 10 integer bits and 54 fractional bits (resolution 2⁻⁵⁴). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 5.79×10⁻¹⁵, max 9.15×10⁻¹⁵; float64: median 6.09×10⁻¹⁴, max 4.57×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 5.68×10⁻¹⁴, max 4.55×10⁻¹³ |
| Netlist check | the 31,925-gate netlist (depth 321) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0361 (noise floor 0.113) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00187 against float64 (noise floor 0.0111) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Rössler, O. E. (1976). An equation for continuous chaos. *Physics Letters A*, 57(5), 397–398. [doi:10.1016/0375-9601(76)90101-8](https://doi.org/10.1016/0375-9601(76)90101-8)

Original paper. Ours uses a=0.2, b=0.2, c=5.7, the values used in the original paper.

```bibtex
@article{Rossler1976,
  author  = {R{\"o}ssler, Otto E.},
  title   = {An equation for continuous chaos},
  journal = {Physics Letters A},
  year    = {1976},
  volume  = {57},
  number  = {5},
  pages   = {397--398},
  doi     = {10.1016/0375-9601(76)90101-8}
}
```

<a id="r_ssler__rk4"></a>

### Rössler (04-R)

**Equations:** ẋ = −y − z; ẏ = x + ay; ż = b + z(x − c)

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.2, b = 0.2, c = 5.7 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁶ |
| L(n) | ≈ 56.8n² + 213n + … |
| Gates at 64 bits | 237,294 |
| pJ/bit (32 / 64-bit) | 4.388 / 10.873 |
| Lyapunov exponent | 0.0705 (float64), 0.0770 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 8 integer bits and 56 fractional bits (resolution 2⁻⁵⁶). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.47×10⁻¹⁵, max 1.18×10⁻¹⁴; float64: median 1.45×10⁻¹⁴, max 5.90×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 1.60×10⁻¹⁴, max 5.86×10⁻¹⁴ |
| Netlist check | the 237,294-gate netlist (depth 1,014) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0927 (noise floor 0.0831) |
| Density of x (relative Wasserstein) | 0.0277 against float64 (noise floor 0.0124) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Rössler, O. E. (1976). An equation for continuous chaos. *Physics Letters A*, 57(5), 397–398. [doi:10.1016/0375-9601(76)90101-8](https://doi.org/10.1016/0375-9601(76)90101-8)

Original paper. Ours uses a=0.2, b=0.2, c=5.7, the values used in the original paper.

```bibtex
@article{Rossler1976,
  author  = {R{\"o}ssler, Otto E.},
  title   = {An equation for continuous chaos},
  journal = {Physics Letters A},
  year    = {1976},
  volume  = {57},
  number  = {5},
  pages   = {397--398},
  doi     = {10.1016/0375-9601(76)90101-8}
}
```

<a id="chua__euler"></a>

### Chua (05-E)

**Equations:** ẋ = α[y − x − f(x)]; ẏ = x − y + z; ż = −βy; f(x) = m\_1x + ½(m\_0 − m\_1)(\|x + 1\| − \|x − 1\|)

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | α = 15.6, β = 28, m\_0 = −8/7, m\_1 = −5/7 |
| Initial condition | x\_0 = 0.7, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | ≈ 1.44n² + 354n − 5528 |
| Gates at 64 bits | 22,647 |
| pJ/bit (32 / 64-bit) | 0.599 / 1.107 |
| Lyapunov exponent | 0.5787 (float64), 0.5878 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. The diode term ½(\|x + 1\| − \|x − 1\|) is the clamp of x to [−1, 1], done as bit logic. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 4.14×10⁻¹⁶, max 9.06×10⁻¹⁶; float64: median 8.52×10⁻¹⁵, max 2.84×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 8.66×10⁻¹⁵, max 2.83×10⁻¹⁴ |
| Netlist check | the 22,647-gate netlist (depth 256) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0157 (noise floor 0.0256) — indistinguishable |
| Density of x (relative Wasserstein) | 0.124 against float64 (noise floor 0.0396) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Matsumoto, T. (1984). A chaotic attractor from Chua's circuit. *IEEE Transactions on Circuits and Systems*, 31(12), 1055–1058. [doi:10.1109/TCS.1984.1085459](https://doi.org/10.1109/TCS.1984.1085459)

We cite the original Matsumoto (1984) paper, the first report of the attractor. The dimensionless double-scroll form is set out in Chua, Komuro & Matsumoto (1986), The double scroll family, IEEE Trans. Circuits Syst. 33(11), 1072–1118; its DOI could not be confirmed, so it is not used as the main reference. Ours uses alpha=15.6, beta=28, m0=-8/7, m1=-5/7, a widely used later set; Matsumoto (1984) used circuit values and Chua et al. (1986) used alpha=9, beta=100/7, so ours does not match either original.

```bibtex
@article{Matsumoto1984,
  author  = {Matsumoto, Takashi},
  title   = {A chaotic attractor from {Chua}'s circuit},
  journal = {IEEE Transactions on Circuits and Systems},
  year    = {1984},
  volume  = {31},
  number  = {12},
  pages   = {1055--1058},
  doi     = {10.1109/TCS.1984.1085459}
}
```

<a id="chua__rk4"></a>

### Chua (05-R)

**Equations:** ẋ = α[y − x − f(x)]; ẏ = x − y + z; ż = −βy; f(x) = m\_1x + ½(m\_0 − m\_1)(\|x + 1\| − \|x − 1\|)

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | α = 15.6, β = 28, m\_0 = −8/7, m\_1 = −5/7 |
| Initial condition | x\_0 = 0.7, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 28.4n² + 1.69e+03n + … |
| Gates at 64 bits | 197,858 |
| pJ/bit (32 / 64-bit) | 5.162 / 9.684 |
| Lyapunov exponent | 0.4467 (float64), 0.4350 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 6 integer bits and 58 fractional bits (resolution 2⁻⁵⁸). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. The diode term ½(\|x + 1\| − \|x − 1\|) is the clamp of x to [−1, 1], done as bit logic. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 5.98×10⁻¹⁶, max 1.35×10⁻¹⁵; float64: median 2.33×10⁻¹⁵, max 7.68×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 2.33×10⁻¹⁵, max 7.55×10⁻¹⁵ |
| Netlist check | the 197,858-gate netlist (depth 987) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0263 (noise floor 0.0528) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0154 against float64 (noise floor 0.0393) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Matsumoto, T. (1984). A chaotic attractor from Chua's circuit. *IEEE Transactions on Circuits and Systems*, 31(12), 1055–1058. [doi:10.1109/TCS.1984.1085459](https://doi.org/10.1109/TCS.1984.1085459)

We cite the original Matsumoto (1984) paper, the first report of the attractor. The dimensionless double-scroll form is set out in Chua, Komuro & Matsumoto (1986), The double scroll family, IEEE Trans. Circuits Syst. 33(11), 1072–1118; its DOI could not be confirmed, so it is not used as the main reference. Ours uses alpha=15.6, beta=28, m0=-8/7, m1=-5/7, a widely used later set; Matsumoto (1984) used circuit values and Chua et al. (1986) used alpha=9, beta=100/7, so ours does not match either original.

```bibtex
@article{Matsumoto1984,
  author  = {Matsumoto, Takashi},
  title   = {A chaotic attractor from {Chua}'s circuit},
  journal = {IEEE Transactions on Circuits and Systems},
  year    = {1984},
  volume  = {31},
  number  = {12},
  pages   = {1055--1058},
  doi     = {10.1109/TCS.1984.1085459}
}
```

<a id="tent_2_2__map"></a>

### Tent (06)

**Equations:** x\_k+1 = μ · min(x\_k, 1 − x\_k)

*Plot (not reproduced in Markdown):* Return map x(k+1) against x(k): 1,500 consecutive iterates after the 10³-step transient.

| Field | Value |
|---|---|
| Parameters | μ = 2 − 2^−7 = 1.9921875 (dyadic) |
| Initial condition | x\_0 = 0.3 |
| Type | map |
| Class | Linear |
| Scheme | map iteration |
| L(n) | 14n − 17 |
| Gates at 64 bits | 879 |
| pJ/bit (32 / 64-bit) | 0.133 / 0.140 |
| Lyapunov exponent | 0.6892 (float64), 0.6892 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 2 integer bits and 62 fractional bits (resolution 2⁻⁶²). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. \|x\| in one's complement (1 ulp off for negative x). |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 0, max 5.42×10⁻¹⁹; float64: median 1.91×10⁻¹⁷, max 8.13×10⁻¹⁷ |
| Circuit vs float64, one step | median 1.93×10⁻¹⁷, max 8.09×10⁻¹⁷ |
| Netlist check | the 879-gate netlist (depth 263) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 1.10×10⁻⁸ (noise floor 1.94×10⁻¹⁰) |
| Density of x (relative Wasserstein) | 0.00449 against float64 (noise floor 0.00592) — indistinguishable |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Ulam, S. M., & von Neumann, J. (1947). On combination of stochastic and deterministic processes (preliminary report, abstract). *Bulletin of the American Mathematical Society*, 53(11), 1120. <https://www.ams.org/journals/bull/1947-53-11/>

There is no single original paper for the tent map. Ulam and von Neumann's abstract is the earliest standard reference: it studies 4x(1-x), which is topologically conjugate to the full tent map. Only an abstract; no DOI found. Consider also citing May (1976) or a textbook. Ulam and von Neumann treat the slope-2 case; we use slope 1.9921875 (just below 2).

```bibtex
@article{ulam1947combination,
  author  = {Ulam, Stanislaw M. and von Neumann, John},
  title   = {On combination of stochastic and deterministic processes},
  journal = {Bulletin of the American Mathematical Society},
  volume  = {53},
  number  = {11},
  pages   = {1120},
  year    = {1947},
  note    = {Preliminary report (abstract)}
}
```

<a id="arnold_s_cat__map"></a>

### Arnold's cat (07)

**Equations:** x\_k+1 = (x\_k + y\_k) mod 1,   y\_k+1 = (x\_k + 2y\_k) mod 1

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | — |
| Initial condition | x\_0 = 0.3, y\_0 = 0.7 |
| Type | map |
| Class | Linear |
| Scheme | map iteration |
| L(n) | 10n − 32 |
| Gates at 64 bits | 608 |
| pJ/bit (32 / 64-bit) | 0.070 / 0.063 |
| Lyapunov exponent | 0.9624 (float64), 0.9624 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 2 integer bits and 62 fractional bits (resolution 2⁻⁶²). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. mod 1 keeps the fractional bits only (wiring). |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 0, max 0; float64: median 0, max 0 |
| Circuit vs float64, one step | median 0, max 0 |
| Netlist check | the 608-gate netlist (depth 124) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 2.03×10⁻⁸ (noise floor 6.11×10⁻¹¹) |
| Density of x (relative Wasserstein) | 0.00261 against float64 (noise floor 0.00338) — indistinguishable; against the exact uniform on [0,1] density: circuit 0.00242, float64 0.00182 |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Arnold, V. I., & Avez, A. (1968). *Ergodic Problems of Classical Mechanics*. W. A. Benjamin, New York. (French original: *Problèmes ergodiques de la mécanique classique*, Gauthier-Villars, Paris, 1967.) <https://en.wikipedia.org/wiki/Arnold%27s_cat_map>

Book source. Book (no DOI). The cat picture illustrating the torus automorphism (x,y) -> (x+y, x+2y) mod 1 appears in this book, hence the name. Our variant is the standard matrix [[1,1],[1,2]] mod 1; matches.

```bibtex
@book{arnold1968ergodic,
  author    = {Arnold, Vladimir I. and Avez, Andr{\'e}},
  title     = {Ergodic Problems of Classical Mechanics},
  publisher = {W. A. Benjamin},
  address   = {New York},
  series    = {Mathematical Physics Monograph Series},
  year      = {1968}
}
```

<a id="standard_map_k_5__map"></a>

### Standard map (08)

**Equations:** p\_k+1 = [p\_k + (K/2π) sin 2πθ\_k] mod 1,   θ\_k+1 = (θ\_k + p\_k+1) mod 1

*Plot (not reproduced in Markdown):* θ–p attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | K = 5; angle θ and momentum p in turns (unit torus) |
| Initial condition | θ\_0 = 0.1, p\_0 = 0.2 |
| Type | map |
| Class | Transcendental |
| Scheme | map iteration |
| L(n) | ≈ 0.264n³ + 82.5n² − 2.06e+03n + 18259 |
| Gates at 64 bits | 294,014 |
| pJ/bit (32 / 64-bit) | 6.112 / 21.098 |
| Lyapunov exponent | 0.9668 (float64), 0.9858 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. mod 1 keeps the fractional bits only (wiring). |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 3.78×10⁻¹⁷, max 8.54×10⁻¹⁷; float64: median 1.07×10⁻¹⁶, max 5.71×10⁻¹⁶ |
| Circuit vs float64, one step | median 9.50×10⁻¹⁷, max 5.55×10⁻¹⁶ |
| Netlist check | the 294,014-gate netlist (depth 2,680) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0197 (noise floor 0.0129) |
| Density of x (relative Wasserstein) | 0.0118 against float64 (noise floor 0.00781) |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Chirikov, B. V. (1979). A universal instability of many-dimensional oscillator systems. *Physics Reports*, 52(5), 263–379. [doi:10.1016/0370-1573(79)90023-1](https://doi.org/10.1016/0370-1573(79)90023-1)

Standard reference; the map first appeared in Chirikov's 1969 Novosibirsk preprint. Chirikov treats general K (global chaos for K > ~0.97); our K = 5 is strongly chaotic.

```bibtex
@article{chirikov1979universal,
  author  = {Chirikov, Boris V.},
  title   = {A universal instability of many-dimensional oscillator systems},
  journal = {Physics Reports},
  volume  = {52},
  number  = {5},
  pages   = {263--379},
  year    = {1979},
  doi     = {10.1016/0370-1573(79)90023-1}
}
```

<a id="mackey_glass__euler"></a>

### Mackey–Glass (09-E)

**Equations:** dx/dt = β x(t − τ) / [1 + x(t − τ)^n] − γ x(t)

*Plot (not reproduced in Markdown):* x(t) against x(t − τ): 4,000 consecutive points, one per time unit, over 4,000 time units after a 200-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | β = 0.2, γ = 0.1, n = 10, τ = 17 |
| Initial condition | x(t) = 1.2 for −τ ≤ t ≤ 0 |
| Type | flow |
| Class | Division / square root |
| Scheme | Euler, dt = 2⁻⁶ |
| L(n) | ≈ 36n² − 142n − 273 |
| Gates at 64 bits | 138,095 |
| pJ/bit (32 / 64-bit) | 6.813 / 17.432 |
| Lyapunov exponent | 0.0060 (float64), 0.0060 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 7 integer bits and 57 fractional bits (resolution 2⁻⁵⁷). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Division: restoring division of one's-complement magnitudes. Forward Euler; multiplying by dt = 2^−k is wiring. x^10 by repeated squaring (x², x⁴, x⁸, x⁸·x²). The delay line holds 1,088 past values of x in shift registers (no gates). |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 9.09×10⁻¹⁷, max 2.78×10⁻¹⁶; float64: median 2.28×10⁻¹⁵, max 7.03×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 2.22×10⁻¹⁵, max 7.11×10⁻¹⁵ |
| Netlist check | the 138,095-gate netlist (depth 9,010) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 6.43×10⁻⁴ (noise floor 0.124) — indistinguishable |
| Density of x (relative Wasserstein) | 1.48×10⁻¹⁰ against float64 (noise floor 0.00613) — indistinguishable |

_Runs: 2,000 time units after a 200-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). The circuit and float64 trajectories stayed together for the whole run (small exponent, slow divergence), so the λ and density differences reflect rounding, not two independent samples of the attractor. Step-size test (float64, 50,000 time units): reference RK4 with dt = 2⁻⁸, λ = 0.005473 per unit time (noise floor 0.0484; density floor 0.00189). Euler — 2⁻⁴: λ err 0.0559, density 0.00735; 2⁻⁵: λ err 0.979, density 0.0263; 2⁻⁶: λ err 0.00569, density 0.00139 ✓; 2⁻⁷: λ err 0.0268, density 7.93×10⁻⁴ ✓; 2⁻⁸: λ err 0.0355, density 7.35×10⁻⁴ ✓. RK4 — 2⁻¹: λ err 0.0823, density 0.00168; 2⁻²: λ err 0.0996, density 0.00439; 2⁻³: λ err 0.0888, density 0.00231; 2⁻⁴: λ err 0.117, density 0.00158; 2⁻⁵: λ err 0.0359, density 6.74×10⁻⁴ ✓. ✓ = within both floors; the chosen dt is the largest that passes with every finer step also passing. Delay line: 1,088 registers of n bits, 10.88 pJ per output bit per step at 64 bits (10.88 at 32 bits) on top of the pJ/bit column, which counts only the x register. Its state is the whole delay line, so gate and energy figures are not directly comparable with the 3-variable flows._

#### Original reference

Mackey, M. C., & Glass, L. (1977). Oscillation and chaos in physiological control systems. *Science*, 197(4300), 287–289. [doi:10.1126/science.267326](https://doi.org/10.1126/science.267326)

PMID 267326. The delay equation x' = βx(t−τ)/(1+x(t−τ)ⁿ) − γx is their haematopoiesis model.

```bibtex
@article{MackeyGlass1977,
  author  = {Mackey, Michael C. and Glass, Leon},
  title   = {Oscillation and chaos in physiological control systems},
  journal = {Science},
  volume  = {197},
  number  = {4300},
  pages   = {287--289},
  year    = {1977},
  doi     = {10.1126/science.267326}
}
```

<a id="mackey_glass__rk4"></a>

### Mackey–Glass (09-R)

**Equations:** dx/dt = β x(t − τ) / [1 + x(t − τ)^n] − γ x(t)

*Plot (not reproduced in Markdown):* x(t) against x(t − τ): 4,000 consecutive points, one per time unit, over 4,000 time units after a 200-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | β = 0.2, γ = 0.1, n = 10, τ = 17 |
| Initial condition | x(t) = 1.2 for −τ ≤ t ≤ 0 |
| Type | flow |
| Class | Division / square root |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 113n² + 244n − 8208 |
| Gates at 64 bits | 466,180 |
| pJ/bit (32 / 64-bit) | 23.887 / 58.795 |
| Lyapunov exponent | 0.0036 (float64), 0.0036 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 7 integer bits and 57 fractional bits (resolution 2⁻⁵⁷). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Division: restoring division of one's-complement magnitudes. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. x^10 by repeated squaring (x², x⁴, x⁸, x⁸·x²). The delay line holds 544 past values of x in shift registers (no gates); the half-step delayed value for RK4 is the mean of two neighbouring entries (linear interpolation). |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 7.28×10⁻¹⁶, max 9.75×10⁻¹⁶; float64: median 1.07×10⁻¹⁵, max 3.48×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 1.22×10⁻¹⁵, max 4.00×10⁻¹⁵ |
| Netlist check | the 466,180-gate netlist (depth 10,038) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 9.65×10⁻⁴ (noise floor 0.0579) — indistinguishable |
| Density of x (relative Wasserstein) | 5.09×10⁻¹² against float64 (noise floor 0.00169) — indistinguishable |

_Runs: 2,000 time units after a 200-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). The circuit and float64 trajectories stayed together for the whole run (small exponent, slow divergence), so the λ and density differences reflect rounding, not two independent samples of the attractor. Step-size test (float64, 50,000 time units): reference RK4 with dt = 2⁻⁸, λ = 0.005473 per unit time (noise floor 0.0484; density floor 0.00189). Euler — 2⁻⁴: λ err 0.0559, density 0.00735; 2⁻⁵: λ err 0.979, density 0.0263; 2⁻⁶: λ err 0.00569, density 0.00139 ✓; 2⁻⁷: λ err 0.0268, density 7.93×10⁻⁴ ✓; 2⁻⁸: λ err 0.0355, density 7.35×10⁻⁴ ✓. RK4 — 2⁻¹: λ err 0.0823, density 0.00168; 2⁻²: λ err 0.0996, density 0.00439; 2⁻³: λ err 0.0888, density 0.00231; 2⁻⁴: λ err 0.117, density 0.00158; 2⁻⁵: λ err 0.0359, density 6.74×10⁻⁴ ✓. ✓ = within both floors; the chosen dt is the largest that passes with every finer step also passing. Delay line: 544 registers of n bits, 5.44 pJ per output bit per step at 64 bits (5.44 at 32 bits) on top of the pJ/bit column, which counts only the x register. Its state is the whole delay line, so gate and energy figures are not directly comparable with the 3-variable flows._

#### Original reference

Mackey, M. C., & Glass, L. (1977). Oscillation and chaos in physiological control systems. *Science*, 197(4300), 287–289. [doi:10.1126/science.267326](https://doi.org/10.1126/science.267326)

PMID 267326. The delay equation x' = βx(t−τ)/(1+x(t−τ)ⁿ) − γx is their haematopoiesis model.

```bibtex
@article{MackeyGlass1977,
  author  = {Mackey, Michael C. and Glass, Leon},
  title   = {Oscillation and chaos in physiological control systems},
  journal = {Science},
  volume  = {197},
  number  = {4300},
  pages   = {287--289},
  year    = {1977},
  doi     = {10.1126/science.267326}
}
```

<a id="lozi_a_1_75__map"></a>

### Lozi (10)

**Equations:** x\_k+1 = 1 − a\|x\_k\| + y\_k,   y\_k+1 = bx\_k

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | a = 1.75, b = 0.5 |
| Initial condition | x\_0 = 0.1, y\_0 = 0.1 |
| Type | map |
| Class | Linear |
| Scheme | map iteration |
| L(n) | 12n − 14 |
| Gates at 64 bits | 754 |
| pJ/bit (32 / 64-bit) | 0.084 / 0.088 |
| Lyapunov exponent | 0.5140 (float64), 0.5131 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. \|x\| in one's complement (1 ulp off for negative x). |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 0, max 8.67×10⁻¹⁹; float64: median 5.55×10⁻¹⁷, max 2.22×10⁻¹⁶ |
| Circuit vs float64, one step | median 5.55×10⁻¹⁷, max 2.23×10⁻¹⁶ |
| Netlist check | the 754-gate netlist (depth 129) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00172 (noise floor 8.00×10⁻⁴) |
| Density of x (relative Wasserstein) | 0.00331 against float64 (noise floor 0.00404) — indistinguishable |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Lozi, R. (1978). Un attracteur étrange (?) du type attracteur de Hénon. *Journal de Physique Colloques*, 39(C5), C5-9–C5-10. [doi:10.1051/jphyscol:1978505](https://doi.org/10.1051/jphyscol:1978505)

Original paper (in French). Lozi used a = 1.7, b = 0.5; we use a = 1.75, b = 0.5, so a differs slightly.

```bibtex
@article{lozi1978attracteur,
  author  = {Lozi, Ren{\'e}},
  title   = {Un attracteur {\'e}trange (?) du type attracteur de {H}{\'e}non},
  journal = {Journal de Physique Colloques},
  volume  = {39},
  number  = {C5},
  pages   = {C5-9--C5-10},
  year    = {1978},
  doi     = {10.1051/jphyscol:1978505}
}
```

<a id="duffing_map__map"></a>

### Duffing map (11)

**Equations:** x\_k+1 = y\_k,   y\_k+1 = −bx\_k + ay\_k − y\_k^3

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | a = 2.75, b = 0.2 |
| Initial condition | x\_0 = 0.1, y\_0 = 0.1 |
| Type | map |
| Class | Polynomial |
| Scheme | map iteration |
| L(n) | ≈ 12.1n² + 130n − 2474 |
| Gates at 64 bits | 55,299 |
| pJ/bit (32 / 64-bit) | 1.937 / 4.035 |
| Lyapunov exponent | 0.4753 (float64), 0.4766 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 1.26×10⁻¹⁷, max 1.84×10⁻¹⁷; float64: median 1.20×10⁻¹⁶, max 7.35×10⁻¹⁶ |
| Circuit vs float64, one step | median 1.22×10⁻¹⁶, max 7.46×10⁻¹⁶ |
| Netlist check | the 55,299-gate netlist (depth 496) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00282 (noise floor 0.00273) |
| Density of x (relative Wasserstein) | 0.00105 against float64 (noise floor 0.0616) — indistinguishable |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Holmes, P. (1979). A nonlinear oscillator with a strange attractor. *Philosophical Transactions of the Royal Society of London. Series A, Mathematical and Physical Sciences*, 292(1394), 419–448. [doi:10.1098/rsta.1979.0068](https://doi.org/10.1098/rsta.1979.0068)

Origin of the Duffing (Holmes) map x' = y, y' = -bx + ay - y^3. a = 2.75, b = 0.2 are the standard values quoted for this map; ours match (not checked against the original text).

```bibtex
@article{holmes1979nonlinear,
  author  = {Holmes, Philip},
  title   = {A nonlinear oscillator with a strange attractor},
  journal = {Philosophical Transactions of the Royal Society of London. Series A, Mathematical and Physical Sciences},
  volume  = {292},
  number  = {1394},
  pages   = {419--448},
  year    = {1979},
  doi     = {10.1098/rsta.1979.0068}
}
```

<a id="ikeda_u_0_9__map"></a>

### Ikeda (12)

**Equations:** x\_k+1 = 1 + u(x\_k cos t\_k − y\_k sin t\_k),   y\_k+1 = u(x\_k sin t\_k + y\_k cos t\_k); t\_k = 0.4 − 6/(1 + x\_k^2 + y\_k^2)

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | u = 0.9 |
| Initial condition | x\_0 = 0.1, y\_0 = 0.1 |
| Type | map |
| Class | Transcendental |
| Scheme | map iteration |
| L(n) | ≈ 1.93n³ + 63.5n² − 98.3n + 66 |
| Gates at 64 bits | 756,904 |
| pJ/bit (32 / 64-bit) | 16.923 / 52.567 |
| Lyapunov exponent | 0.5093 (float64), 0.5082 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. Division: restoring division of one's-complement magnitudes. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 9.02×10⁻¹⁷, max 1.31×10⁻¹⁶; float64: median 1.44×10⁻¹⁶, max 6.28×10⁻¹⁶ |
| Circuit vs float64, one step | median 1.60×10⁻¹⁶, max 7.37×10⁻¹⁶ |
| Netlist check | the 756,904-gate netlist (depth 11,718) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00221 (noise floor 0.00267) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00455 against float64 (noise floor 0.00344) |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Ikeda, K. (1979). Multiple-valued stationary state and its instability of the transmitted light by a ring cavity system. *Optics Communications*, 30(2), 257–261. [doi:10.1016/0030-4018(79)90090-7](https://doi.org/10.1016/0030-4018(79)90090-7)

Original physical model (ring cavity). The real 2D form x' = 1 + u(x cos t - y sin t), t = 0.4 - 6/(1+x^2+y^2) is from Hammel, Jones & Moloney (1985), J. Opt. Soc. Am. B 2(4), 552-564 (DOI not verified). u = 0.9 is the standard chaotic value of the Hammel-Jones-Moloney form; ours matches.

```bibtex
@article{ikeda1979multiple,
  author  = {Ikeda, Kensuke},
  title   = {Multiple-valued stationary state and its instability of the transmitted light by a ring cavity system},
  journal = {Optics Communications},
  volume  = {30},
  number  = {2},
  pages   = {257--261},
  year    = {1979},
  doi     = {10.1016/0030-4018(79)90090-7}
}
```

<a id="circle_map_k_3_omega_0_1__map"></a>

### Circle map (13)

**Equations:** θ\_k+1 = [θ\_k + Ω − (K/2π) sin 2πθ\_k] mod 1

*Plot (not reproduced in Markdown):* Return map x(k+1) against x(k): 1,500 consecutive iterates after the 10³-step transient.

| Field | Value |
|---|---|
| Parameters | K = 3, Ω = 0.1 |
| Initial condition | θ\_0 = 0.3 |
| Type | map |
| Class | Transcendental |
| Scheme | map iteration |
| L(n) | ≈ 0.25n³ + 83.9n² − 2.08e+03n + 18356 |
| Gates at 64 bits | 294,532 |
| pJ/bit (32 / 64-bit) | 12.153 / 42.161 |
| Lyapunov exponent | 0.3467 (float64), 0.3470 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. mod 1 keeps the fractional bits only (wiring). |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 7.08×10⁻¹⁸, max 1.45×10⁻¹⁷; float64: median 3.53×10⁻¹⁷, max 4.34×10⁻¹⁶ |
| Circuit vs float64, one step | median 3.30×10⁻¹⁷, max 4.30×10⁻¹⁶ |
| Netlist check | the 294,532-gate netlist (depth 2,681) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 9.79×10⁻⁴ (noise floor 0.00199) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00142 against float64 (noise floor 0.00345) — indistinguishable |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Arnold, V. I. (1961). Small denominators. I. Mapping the circle onto itself. *Izvestiya Akademii Nauk SSSR, Seriya Matematicheskaya*, 25(1), 21–86. English transl.: *American Mathematical Society Translations, Series 2*, 46 (1965), 213–284. <https://mathnet.ru/eng/im3366>

Original paper (Russian). No DOI verified for either version; Math-Net.ru record given. Arnold's family x + a + (b/2pi) sin(2pi x); our theta + Omega - (K/2pi) sin(2pi theta) is the same family with K's sign flipped. K = 3 > 1 is in the non-invertible chaotic regime.

```bibtex
@article{arnold1961small,
  author  = {Arnold, Vladimir I.},
  title   = {Small denominators. {I}. {M}apping the circle onto itself},
  journal = {Izvestiya Akademii Nauk SSSR, Seriya Matematicheskaya},
  volume  = {25},
  number  = {1},
  pages   = {21--86},
  year    = {1961},
  note    = {English translation: Amer. Math. Soc. Transl. Ser. 2, 46 (1965), 213--284}
}
```

<a id="gingerbreadman__map"></a>

### Gingerbreadman (14)

**Equations:** x\_k+1 = 1 − y\_k + \|x\_k\|,   y\_k+1 = x\_k

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | — |
| Initial condition | x\_0 = −0.1, y\_0 = 0 |
| Type | map |
| Class | Linear |
| Scheme | map iteration |
| L(n) | 7n + 2 |
| Gates at 64 bits | 450 |
| pJ/bit (32 / 64-bit) | 0.063 / 0.063 |
| Lyapunov exponent | 0.0635 (float64), 0.0814 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. \|x\| in one's complement (1 ulp off for negative x). |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 0, max 1.73×10⁻¹⁸; float64: median 0, max 0 |
| Circuit vs float64, one step | median 0, max 1.73×10⁻¹⁸ |
| Netlist check | the 450-gate netlist (depth 128) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.282 (noise floor 0.16) |
| Density of x (relative Wasserstein) | 0.0337 against float64 (noise floor 0.0248) |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Devaney, R. L. (1984). A piecewise linear model for the zones of instability of an area-preserving map. *Physica D: Nonlinear Phenomena*, 10(3), 387–393. [doi:10.1016/0167-2789(84)90187-8](https://doi.org/10.1016/0167-2789(84)90187-8)

Original journal paper; the map was later popularised under the name 'Gingerbreadman' in Devaney's textbooks. Note the DOI check digit is 8 (ScienceDirect PII 0167278984901878). Parameter-free map x' = 1 - y + |x|, y' = x; our variant matches.

```bibtex
@article{devaney1984piecewise,
  author  = {Devaney, Robert L.},
  title   = {A piecewise linear model for the zones of instability of an area-preserving map},
  journal = {Physica D: Nonlinear Phenomena},
  volume  = {10},
  number  = {3},
  pages   = {387--393},
  year    = {1984},
  doi     = {10.1016/0167-2789(84)90187-8}
}
```

<a id="complex_quadratic_c_2__map"></a>

### Complex quadratic (c=-2) (15)

**Equations:** z\_k+1 = z\_k^2 + c,   i.e. x\_k+1 = x\_k^2 − y\_k^2 + c,   y\_k+1 = 2x\_ky\_k

*Plot (not reproduced in Markdown):* Return map x(k+1) against x(k): 1,500 consecutive iterates after the 10³-step transient.

| Field | Value |
|---|---|
| Parameters | c = −2 (real axis: y stays 0, conjugate to the logistic map with r = 4) |
| Initial condition | x\_0 = 0.3, y\_0 = 0 |
| Type | map |
| Class | Polynomial |
| Scheme | map iteration |
| L(n) | 17.3n² − 35n − 2 |
| Gates at 64 bits | 68,414 |
| pJ/bit (32 / 64-bit) | 0.798 / 1.676 |
| Lyapunov exponent | 0.6931 (float64), 0.6931 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 4.59×10⁻¹⁹, max 8.67×10⁻¹⁹; float64: median 6.58×10⁻¹⁷, max 2.18×10⁻¹⁶ |
| Circuit vs float64, one step | median 6.59×10⁻¹⁷, max 2.18×10⁻¹⁶ |
| Netlist check | the 68,414-gate netlist (depth 315) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 4.86×10⁻⁶ (noise floor 6.09×10⁻⁶) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00241 against float64 (noise floor 0.002); against the exact arcsine on [−2,2] density: circuit 0.00368, float64 0.00245 |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Julia, G. (1918). Mémoire sur l'itération des fonctions rationnelles. *Journal de Mathématiques Pures et Appliquées*, 8e série, 1, 47–245. <https://numdam.org/item/JMPA_1918_8_1__47_0/>

Founding paper on iteration of rational maps such as z -> z^2 + c (with Fatou, 1919-1920). No DOI; digitised on Numdam. For the modern parameter-space view see Mandelbrot (1980) and Douady & Hubbard (1982). c = -2 is the Chebyshev case: with real initial value the map stays on [-2, 2] and is conjugate to the logistic map at r = 4.

```bibtex
@article{julia1918memoire,
  author  = {Julia, Gaston},
  title   = {M{\'e}moire sur l'it{\'e}ration des fonctions rationnelles},
  journal = {Journal de Math{\'e}matiques Pures et Appliqu{\'e}es},
  series  = {8},
  volume  = {1},
  pages   = {47--245},
  year    = {1918}
}
```

<a id="sine_map_0_99__map"></a>

### Sine map (16)

**Equations:** x\_k+1 = μ sin(πx\_k)

*Plot (not reproduced in Markdown):* Return map x(k+1) against x(k): 1,500 consecutive iterates after the 10³-step transient.

| Field | Value |
|---|---|
| Parameters | μ = 0.99 |
| Initial condition | x\_0 = 0.3 |
| Type | map |
| Class | Transcendental |
| Scheme | map iteration |
| L(n) | ≈ 0.27n³ + 82n² − … |
| Gates at 64 bits | 293,018 |
| pJ/bit (32 / 64-bit) | 11.799 / 41.561 |
| Lyapunov exponent | 0.5982 (float64), 0.5974 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 1.77×10⁻¹⁷, max 2.74×10⁻¹⁷; float64: median 3.58×10⁻¹⁷, max 3.31×10⁻¹⁶ |
| Circuit vs float64, one step | median 3.53×10⁻¹⁷, max 3.39×10⁻¹⁶ |
| Netlist check | the 293,018-gate netlist (depth 2,687) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00128 (noise floor 4.69×10⁻⁴) |
| Density of x (relative Wasserstein) | 0.00141 against float64 (noise floor 0.00365) — indistinguishable |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Metropolis, N., Stein, M. L., & Stein, P. R. (1973). On finite limit sets for transformations on the unit interval. *Journal of Combinatorial Theory, Series A*, 15(1), 25–44. [doi:10.1016/0097-3165(73)90033-2](https://doi.org/10.1016/0097-3165(73)90033-2)

Earliest standard reference studying x' = lambda sin(pi x) alongside the logistic map (universal MSS sequence). MSS vary lambda over (0, 1]; our mu = 0.99 is within their range.

```bibtex
@article{metropolis1973finite,
  author  = {Metropolis, Nicholas and Stein, Myron L. and Stein, Paul R.},
  title   = {On finite limit sets for transformations on the unit interval},
  journal = {Journal of Combinatorial Theory, Series A},
  volume  = {15},
  number  = {1},
  pages   = {25--44},
  year    = {1973},
  doi     = {10.1016/0097-3165(73)90033-2}
}
```

<a id="gauss_alpha_4_9_beta_0_5__map"></a>

### Gauss (17)

**Equations:** x\_k+1 = exp(−αx\_k^2) + β

*Plot (not reproduced in Markdown):* Return map x(k+1) against x(k): 1,500 consecutive iterates after the 10³-step transient.

| Field | Value |
|---|---|
| Parameters | α = 4.9, β = −0.5 |
| Initial condition | x\_0 = 0.1 |
| Type | map |
| Class | Transcendental |
| Scheme | map iteration |
| L(n) | ≈ 0.115n³ + 148n² − 4.15e+03n + 38563 |
| Gates at 64 bits | 409,575 |
| pJ/bit (32 / 64-bit) | 17.611 / 60.150 |
| Lyapunov exponent | 0.1764 (float64), 0.1770 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. exp: 2^y split into integer and fractional parts, polynomial for 2^f and a barrel shifter. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 2.36×10⁻¹⁷, max 3.19×10⁻¹⁷; float64: median 2.84×10⁻¹⁷, max 8.61×10⁻¹⁷ |
| Circuit vs float64, one step | median 2.23×10⁻¹⁷, max 7.72×10⁻¹⁷ |
| Netlist check | the 409,575-gate netlist (depth 3,734) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00313 (noise floor 0.00375) — indistinguishable |
| Density of x (relative Wasserstein) | 6.88×10⁻⁴ against float64 (noise floor 8.13×10⁻⁴) — indistinguishable |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Hilborn, R. C. (2000). *Chaos and Nonlinear Dynamics: An Introduction for Scientists and Engineers* (2nd ed.). Oxford University Press, Oxford. [doi:10.1093/acprof:oso/9780198507239.001.0001](https://doi.org/10.1093/acprof:oso/9780198507239.001.0001)

Book source. Textbook (section 5.9, 'The Gaussian map'). No original research paper for the Gauss (mouse) map was found; Hilborn is the reference Wikipedia gives. DOI confirmed via library catalogues only. Our alpha = 4.9, beta = -0.5 is a common chaotic setting; not checked against Hilborn.

```bibtex
@book{hilborn2000chaos,
  author    = {Hilborn, Robert C.},
  title     = {Chaos and Nonlinear Dynamics: An Introduction for Scientists and Engineers},
  edition   = {2},
  publisher = {Oxford University Press},
  address   = {Oxford},
  year      = {2000},
  doi       = {10.1093/acprof:oso/9780198507239.001.0001}
}
```

<a id="delayed_logistic_a_2_27__map"></a>

### Delayed logistic (18)

**Equations:** x\_k+1 = a x\_k (1 − y\_k),   y\_k+1 = x\_k

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | a = 2.27 |
| Initial condition | x\_0 = 0.5, y\_0 = 0.4 |
| Type | map |
| Class | Polynomial |
| Scheme | map iteration |
| L(n) | ≈ 6.07n² + 77.5n − 977 |
| Gates at 64 bits | 28,702 |
| pJ/bit (32 / 64-bit) | 1.060 / 2.133 |
| Lyapunov exponent | 0.1828 (float64), 0.1834 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 2 integer bits and 62 fractional bits (resolution 2⁻⁶²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 1.28×10⁻¹⁸, max 7.75×10⁻¹⁸; float64: median 7.88×10⁻¹⁸, max 1.71×10⁻¹⁶ |
| Circuit vs float64, one step | median 7.81×10⁻¹⁸, max 1.74×10⁻¹⁶ |
| Netlist check | the 28,702-gate netlist (depth 420) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00306 (noise floor 0.00504) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00358 against float64 (noise floor 0.00328) |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Maynard Smith, J. (1968). *Mathematical Ideas in Biology*. Cambridge University Press, Cambridge. [doi:10.1017/CBO9780511565144](https://doi.org/10.1017/CBO9780511565144)

Book source. Book. Maynard Smith introduced the delayed logistic equation x' = a x (1 - y), y' = x. Its route to chaos was studied in detail by Aronson, Chory, Hall & McGehee (1982), Commun. Math. Phys. 83, 303-354, doi:10.1007/BF01213607 (verified). a = 2.27 is the value used in Sprott's catalogue, not checked against Maynard Smith.

```bibtex
@book{maynardsmith1968mathematical,
  author    = {Maynard Smith, John},
  title     = {Mathematical Ideas in Biology},
  publisher = {Cambridge University Press},
  address   = {Cambridge},
  year      = {1968},
  doi       = {10.1017/CBO9780511565144}
}
```

<a id="kaplan_yorke_alpha_0_2__map"></a>

### Kaplan-Yorke (19)

**Equations:** x\_k+1 = 2x\_k mod 1,   y\_k+1 = αy\_k + cos 4πx\_k

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | α = 0.2 |
| Initial condition | x\_0 = 0.3, y\_0 = 0.1 |
| Type | map |
| Class | Transcendental |
| Scheme | map iteration |
| L(n) | ≈ 0.243n³ + 85.3n² − 2.11e+03n + 18743 |
| Gates at 64 bits | 297,026 |
| pJ/bit (32 / 64-bit) | 0.010⚠ / 0.010⚠ |
| Lyapunov exponent | Not meaningful: in binary the doubling map shifts the state to 0 within 64 steps (float64 within 53), so both runs end on the unstable fixed point and the measured ln 2 is that point's local stretching. |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. mod 1 keeps the fractional bits only (wiring). |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 2.56×10⁻¹⁷, max 2.56×10⁻¹⁷; float64: median 0, max 0 |
| Circuit vs float64, one step | median 2.56×10⁻¹⁷, max 2.56×10⁻¹⁷ |
| Netlist check | the 297,026-gate netlist (depth 2,635) and the integer model used for the long runs agree bit for bit on all 200 states |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Kaplan, J. L., & Yorke, J. A. (1979). Chaotic behavior of multidimensional difference equations. In H.-O. Peitgen & H.-O. Walther (Eds.), *Functional Differential Equations and Approximation of Fixed Points* (Lecture Notes in Mathematics, Vol. 730, pp. 204–227). Springer, Berlin. [doi:10.1007/BFb0064319](https://doi.org/10.1007/BFb0064319)

Book chapter (conference proceedings); same paper that states the Kaplan-Yorke dimension conjecture. alpha = 0.2 is the commonly quoted value (Sprott); not checked against the original.

```bibtex
@incollection{kaplan1979chaotic,
  author    = {Kaplan, James L. and Yorke, James A.},
  title     = {Chaotic behavior of multidimensional difference equations},
  booktitle = {Functional Differential Equations and Approximation of Fixed Points},
  editor    = {Peitgen, Heinz-Otto and Walther, Hans-Otto},
  series    = {Lecture Notes in Mathematics},
  volume    = {730},
  pages     = {204--227},
  publisher = {Springer},
  address   = {Berlin},
  year      = {1979},
  doi       = {10.1007/BFb0064319}
}
```

<a id="pomeau_manneville_type_i_x_x_2_mod_1__map"></a>

### Pomeau-Manneville type I (x+x^2 mod 1) (20)

**Equations:** x\_k+1 = (x\_k + x\_k^2) mod 1

*Plot (not reproduced in Markdown):* Return map x(k+1) against x(k): 1,500 consecutive iterates after the 10³-step transient.

| Field | Value |
|---|---|
| Parameters | — |
| Initial condition | x\_0 = 0.3 |
| Type | map |
| Class | Polynomial |
| Scheme | map iteration |
| L(n) | 5.75n² − 11.5n − 37 |
| Gates at 64 bits | 22,779 |
| pJ/bit (32 / 64-bit) | 1.083 / 2.991 |
| Lyapunov exponent | 0.0957 (float64), 0.2191 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. mod 1 keeps the fractional bits only (wiring). |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 2.06×10⁻¹⁹, max 4.33×10⁻¹⁹; float64: median 4.43×10⁻²⁰, max 1.39×10⁻¹⁶ |
| Circuit vs float64, one step | median 3.25×10⁻¹⁹, max 1.39×10⁻¹⁶ |
| Netlist check | the 22,779-gate netlist (depth 309) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 1.29 (noise floor 0.851) |
| Density of x (relative Wasserstein) | 0.493 against float64 (noise floor 0.323) |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Pomeau, Y., & Manneville, P. (1980). Intermittent transition to turbulence in dissipative dynamical systems. *Communications in Mathematical Physics*, 74(2), 189–197. [doi:10.1007/BF01197757](https://doi.org/10.1007/BF01197757)

Defines type I intermittency. The specific map x' = x + x^z mod 1 is from Manneville (1980), Intermittency, self-similarity and 1/f spectrum in dissipative dynamical systems, J. Physique 41(11), 1235-1243, doi:10.1051/jphys:0198000410110123500 (also verified); cite both if space allows. Our x' = x + x^2 mod 1 is the Manneville map with z = 2.

```bibtex
@article{pomeau1980intermittent,
  author  = {Pomeau, Yves and Manneville, Paul},
  title   = {Intermittent transition to turbulence in dissipative dynamical systems},
  journal = {Communications in Mathematical Physics},
  volume  = {74},
  number  = {2},
  pages   = {189--197},
  year    = {1980},
  doi     = {10.1007/BF01197757}
}
```

<a id="zaslavskii_r_3_nu_400_3_eps_0_3__map"></a>

### Zaslavskii (21)

**Equations:** x\_k+1 = [x\_k + ν(1 + μy\_k) + εν μ cos 2πx\_k] mod 1; y\_k+1 = e^−r(y\_k + ε cos 2πx\_k),   μ = (1 − e^−r)/r

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | r = 3, ν = 400/3, ε = 0.3 |
| Initial condition | x\_0 = 0.3, y\_0 = 0.1 |
| Type | map |
| Class | Transcendental |
| Scheme | map iteration |
| L(n) | ≈ 0.333n³ + 69.1n² − 1.76e+03n + 12643 |
| Gates at 64 bits | 270,633 |
| pJ/bit (32 / 64-bit) | 4.571 / 18.315 |
| Lyapunov exponent | 3.6911 (float64), 3.6928 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 10 integer bits and 54 fractional bits (resolution 2⁻⁵⁴). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. mod 1 keeps the fractional bits only (wiring). |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 9.17×10⁻¹⁵, max 1.39×10⁻¹⁴; float64: median 1.00×10⁻¹⁴, max 2.94×10⁻¹⁴ |
| Circuit vs float64, one step | median 7.13×10⁻¹⁵, max 2.69×10⁻¹⁴ |
| Netlist check | the 270,633-gate netlist (depth 2,325) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 4.79×10⁻⁴ (noise floor 6.75×10⁻⁴) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00473 against float64 (noise floor 0.00314) |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Zaslavsky, G. M. (1978). The simplest case of a strange attractor. *Physics Letters A*, 69(3), 145–147. [doi:10.1016/0375-9601(78)90195-0](https://doi.org/10.1016/0375-9601(78)90195-0)

Original paper (dissipative kicked rotor). r = 3, nu = 400/3, eps = 0.3 are the values used by Sprott and Wikipedia; not checked against the original.

```bibtex
@article{zaslavsky1978simplest,
  author  = {Zaslavsky, George M.},
  title   = {The simplest case of a strange attractor},
  journal = {Physics Letters A},
  volume  = {69},
  number  = {3},
  pages   = {145--147},
  year    = {1978},
  doi     = {10.1016/0375-9601(78)90195-0}
}
```

<a id="tinkerbell__map"></a>

### Tinkerbell (22)

**Equations:** x\_k+1 = x\_k^2 − y\_k^2 + ax\_k + by\_k,   y\_k+1 = 2x\_ky\_k + cx\_k + dy\_k

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | a = 0.9, b = −0.6013, c = 2, d = 0.5 |
| Initial condition | x\_0 = −0.72, y\_0 = −0.64 |
| Type | map |
| Class | Polynomial |
| Scheme | map iteration |
| L(n) | ≈ 16.9n² + 343n − 5848 |
| Gates at 64 bits | 84,866 |
| pJ/bit (32 / 64-bit) | 3.190 / 6.320 |
| Lyapunov exponent | 0.1989 (float64), 0.2005 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 2.70×10⁻¹⁷, max 8.58×10⁻¹⁷; float64: median 3.64×10⁻¹⁷, max 2.28×10⁻¹⁶ |
| Circuit vs float64, one step | median 2.65×10⁻¹⁷, max 2.11×10⁻¹⁶ |
| Netlist check | the 84,866-gate netlist (depth 408) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00819 (noise floor 0.00312) |
| Density of x (relative Wasserstein) | 0.00162 against float64 (noise floor 0.00251) — indistinguishable |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Nusse, H. E., & Yorke, J. A. (1994). *Dynamics: Numerical Explorations* (Applied Mathematical Sciences, Vol. 101). Springer-Verlag, New York. <https://link.springer.com/book/9780387982649>

Book source. Book. The origin of the Tinkerbell map is uncertain (Wikipedia says so too); it is usually cited to Nusse & Yorke's Dynamics book (2nd edn 1998) and Alligood, Sauer & Yorke (1996). Attribution NOT confirmed from the book text; DOI for the 1994 edition not verified, so left null. a = 0.9, b = -0.6013, c = 2, d = 0.5 are the standard values; ours match.

```bibtex
@book{nusse1994dynamics,
  author    = {Nusse, Helena E. and Yorke, James A.},
  title     = {Dynamics: Numerical Explorations},
  series    = {Applied Mathematical Sciences},
  volume    = {101},
  publisher = {Springer-Verlag},
  address   = {New York},
  year      = {1994}
}
```

<a id="ueda_oscillator__euler"></a>

### Ueda oscillator (23-E)

**Equations:** ẋ = v; v̇ = −kv − x^3 + B cos t

*Plot (not reproduced in Markdown):* x–v projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | k = 0.05, B = 7.5; the phase t is a third state variable (in turns, wrapped mod 1) |
| Initial condition | x\_0 = 2.5, v\_0 = 0, t (turns)\_0 = 0 |
| Type | flow |
| Class | Transcendental |
| Scheme | Euler, dt = 2⁻⁸ |
| L(n) | ≈ 0.629n³ + 41.9n² − 487n + 692 |
| Gates at 64 bits | 306,359 |
| pJ/bit (32 / 64-bit) | 3.657 / 13.401 |
| Lyapunov exponent | 0.1218 (float64), 0.1248 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 8 integer bits and 56 fractional bits (resolution 2⁻⁵⁶). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. mod 1 keeps the fractional bits only (wiring). Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.27×10⁻¹⁵, max 2.71×10⁻¹⁵; float64: median 2.14×10⁻¹⁴, max 1.14×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 2.13×10⁻¹⁴, max 1.14×10⁻¹³ |
| Netlist check | the 306,359-gate netlist (depth 2,284) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0244 (noise floor 0.1) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0217 against float64 (noise floor 0.0472) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Ueda, Y. (1979). Randomly transitional phenomena in the system governed by Duffing's equation. *Journal of Statistical Physics*, 20(2), 181–196. [doi:10.1007/BF01011512](https://doi.org/10.1007/BF01011512)

Ueda's forced Duffing equation x'' + kx' + x³ = B cos t. Ours uses k=0.05, B=7.5, ω=1, the classic Ueda values for the 'Japanese attractor'.

```bibtex
@article{Ueda1979,
  author  = {Ueda, Yoshisuke},
  title   = {Randomly transitional phenomena in the system governed by {Duffing's} equation},
  journal = {Journal of Statistical Physics},
  volume  = {20},
  number  = {2},
  pages   = {181--196},
  year    = {1979},
  doi     = {10.1007/BF01011512}
}
```

<a id="ueda_oscillator__rk4"></a>

### Ueda oscillator (23-R)

**Equations:** ẋ = v; v̇ = −kv − x^3 + B cos t

*Plot (not reproduced in Markdown):* x–v projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | k = 0.05, B = 7.5; the phase t is a third state variable (in turns, wrapped mod 1) |
| Initial condition | x\_0 = 2.5, v\_0 = 0, t (turns)\_0 = 0 |
| Type | flow |
| Class | Transcendental |
| Scheme | RK4, dt = 2⁻⁶ |
| L(n) | ≈ 1.62n³ + 186n² + … |
| Gates at 64 bits | 1,058,139 |
| pJ/bit (32 / 64-bit) | 13.990 / 47.088 |
| Lyapunov exponent | 0.0824 (float64), 0.0818 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 8 integer bits and 56 fractional bits (resolution 2⁻⁵⁶). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. mod 1 keeps the fractional bits only (wiring). Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.30×10⁻¹⁵, max 5.74×10⁻¹⁵; float64: median 5.70×10⁻¹⁵, max 3.07×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 6.22×10⁻¹⁵, max 2.93×10⁻¹⁴ |
| Netlist check | the 1,058,139-gate netlist (depth 2,920) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0067 (noise floor 0.156) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0151 against float64 (noise floor 0.117) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Ueda, Y. (1979). Randomly transitional phenomena in the system governed by Duffing's equation. *Journal of Statistical Physics*, 20(2), 181–196. [doi:10.1007/BF01011512](https://doi.org/10.1007/BF01011512)

Ueda's forced Duffing equation x'' + kx' + x³ = B cos t. Ours uses k=0.05, B=7.5, ω=1, the classic Ueda values for the 'Japanese attractor'.

```bibtex
@article{Ueda1979,
  author  = {Ueda, Yoshisuke},
  title   = {Randomly transitional phenomena in the system governed by {Duffing's} equation},
  journal = {Journal of Statistical Physics},
  volume  = {20},
  number  = {2},
  pages   = {181--196},
  year    = {1979},
  doi     = {10.1007/BF01011512}
}
```

<a id="chen__euler"></a>

### Chen (24-E)

**Equations:** ẋ = a(y − x); ẏ = (c − a)x − xz + cy; ż = xy − bz

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 35, b = 3, c = 28 |
| Initial condition | x\_0 = −10, y\_0 = 0, z\_0 = 37 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁹ |
| L(n) | 11.5n² − 5n − 143 |
| Gates at 64 bits | 46,641 |
| pJ/bit (32 / 64-bit) | 0.916 / 2.143 |
| Lyapunov exponent | 1.9300 (float64), 1.9715 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 13 integer bits and 51 fractional bits (resolution 2⁻⁵¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 8.88×10⁻¹⁴, max 1.37×10⁻¹³; float64: median 4.76×10⁻¹³, max 1.67×10⁻¹² |
| Circuit vs float64, one step ÷ dt | median 4.55×10⁻¹³, max 1.59×10⁻¹² |
| Netlist check | the 46,641-gate netlist (depth 318) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0215 (noise floor 0.0142) |
| Density of x (relative Wasserstein) | 0.0244 against float64 (noise floor 0.0178) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Chen, G., & Ueta, T. (1999). Yet another chaotic attractor. *International Journal of Bifurcation and Chaos*, 9(7), 1465–1466. [doi:10.1142/S0218127499001024](https://doi.org/10.1142/S0218127499001024)

Original two-page letter. Ours uses a=35, b=3, c=28 (y' = (c-a)x - xz + cy), the standard values from the original letter.

```bibtex
@article{ChenUeta1999,
  author  = {Chen, Guanrong and Ueta, Tetsushi},
  title   = {Yet another chaotic attractor},
  journal = {International Journal of Bifurcation and Chaos},
  year    = {1999},
  volume  = {9},
  number  = {7},
  pages   = {1465--1466},
  doi     = {10.1142/S0218127499001024}
}
```

<a id="chen__rk4"></a>

### Chen (24-R)

**Equations:** ẋ = a(y − x); ẏ = (c − a)x − xz + cy; ż = xy − bz

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 35, b = 3, c = 28 |
| Initial condition | x\_0 = −10, y\_0 = 0, z\_0 = 37 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁷ |
| L(n) | ≈ 66.9n² + 446n + … |
| Gates at 64 bits | 281,869 |
| pJ/bit (32 / 64-bit) | 5.010 / 12.952 |
| Lyapunov exponent | 2.0038 (float64), 2.0779 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 13 integer bits and 51 fractional bits (resolution 2⁻⁵¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.95×10⁻¹⁴, max 6.76×10⁻¹⁴; float64: median 1.16×10⁻¹³, max 4.17×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 1.14×10⁻¹³, max 3.98×10⁻¹³ |
| Netlist check | the 281,869-gate netlist (depth 988) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.037 (noise floor 0.0171) |
| Density of x (relative Wasserstein) | 0.023 against float64 (noise floor 0.00825) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Chen, G., & Ueta, T. (1999). Yet another chaotic attractor. *International Journal of Bifurcation and Chaos*, 9(7), 1465–1466. [doi:10.1142/S0218127499001024](https://doi.org/10.1142/S0218127499001024)

Original two-page letter. Ours uses a=35, b=3, c=28 (y' = (c-a)x - xz + cy), the standard values from the original letter.

```bibtex
@article{ChenUeta1999,
  author  = {Chen, Guanrong and Ueta, Tetsushi},
  title   = {Yet another chaotic attractor},
  journal = {International Journal of Bifurcation and Chaos},
  year    = {1999},
  volume  = {9},
  number  = {7},
  pages   = {1465--1466},
  doi     = {10.1142/S0218127499001024}
}
```

<a id="l__euler"></a>

### Lü (25-E)

**Equations:** ẋ = a(y − x); ẏ = −xz + cy; ż = xy − bz

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 36, b = 3, c = 20 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁹ |
| L(n) | 11.5n² − 16n − 145 |
| Gates at 64 bits | 45,935 |
| pJ/bit (32 / 64-bit) | 0.828 / 2.036 |
| Lyapunov exponent | 0.0052 (float64), 0.0708 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 12 integer bits and 52 fractional bits (resolution 2⁻⁵²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 4.49×10⁻¹⁴, max 6.38×10⁻¹⁴; float64: median 4.15×10⁻¹³, max 9.02×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 4.55×10⁻¹³, max 9.09×10⁻¹³ |
| Netlist check | the 45,935-gate netlist (depth 320) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 12.7 (noise floor 5.42) |
| Density of x (relative Wasserstein) | 0.00489 against float64 (noise floor 0.00222) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). The float64 exponent is close to zero, so the orbit at this step may be periodic or quasi-periodic, and the relative λ error is not meaningful._

#### Original reference

Lü, J., & Chen, G. (2002). A new chaotic attractor coined. *International Journal of Bifurcation and Chaos*, 12(3), 659–661. [doi:10.1142/S0218127402004620](https://doi.org/10.1142/S0218127402004620)

Original letter. Ours uses a=36, b=3, c=20, the standard values from the original letter.

```bibtex
@article{LuChen2002,
  author  = {L{\"u}, Jinhu and Chen, Guanrong},
  title   = {A new chaotic attractor coined},
  journal = {International Journal of Bifurcation and Chaos},
  year    = {2002},
  volume  = {12},
  number  = {3},
  pages   = {659--661},
  doi     = {10.1142/S0218127402004620}
}
```

<a id="l__rk4"></a>

### Lü (25-R)

**Equations:** ẋ = a(y − x); ẏ = −xz + cy; ż = xy − bz

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 36, b = 3, c = 20 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁷ |
| L(n) | ≈ 73.5n² − 192n + … |
| Gates at 64 bits | 281,364 |
| pJ/bit (32 / 64-bit) | 4.960 / 12.874 |
| Lyapunov exponent | 1.3414 (float64), 1.3253 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 12 integer bits and 52 fractional bits (resolution 2⁻⁵²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.38×10⁻¹⁴, max 2.91×10⁻¹⁴; float64: median 1.06×10⁻¹³, max 3.01×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 1.14×10⁻¹³, max 3.13×10⁻¹³ |
| Netlist check | the 281,364-gate netlist (depth 997) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.012 (noise floor 0.0234) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00799 against float64 (noise floor 0.00895) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Lü, J., & Chen, G. (2002). A new chaotic attractor coined. *International Journal of Bifurcation and Chaos*, 12(3), 659–661. [doi:10.1142/S0218127402004620](https://doi.org/10.1142/S0218127402004620)

Original letter. Ours uses a=36, b=3, c=20, the standard values from the original letter.

```bibtex
@article{LuChen2002,
  author  = {L{\"u}, Jinhu and Chen, Guanrong},
  title   = {A new chaotic attractor coined},
  journal = {International Journal of Bifurcation and Chaos},
  year    = {2002},
  volume  = {12},
  number  = {3},
  pages   = {659--661},
  doi     = {10.1142/S0218127402004620}
}
```

<a id="rikitake__euler"></a>

### Rikitake (26-E)

**Equations:** ẋ = −μx + yz; ẏ = −μy + (z − a)x; ż = 1 − xy

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | μ = 2, a = 5 |
| Initial condition | x\_0 = 1, y\_0 = 0, z\_0 = 0.5 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁸ |
| L(n) | 17.25n² − 36n − 59 |
| Gates at 64 bits | 68,325 |
| pJ/bit (32 / 64-bit) | 1.313 / 3.125 |
| Lyapunov exponent | 0.1234 (float64), 0.1231 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 8 integer bits and 56 fractional bits (resolution 2⁻⁵⁶). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.42×10⁻¹⁵, max 1.98×10⁻¹⁵; float64: median 5.37×10⁻¹⁴, max 2.25×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 5.33×10⁻¹⁴, max 2.24×10⁻¹³ |
| Netlist check | the 68,325-gate netlist (depth 323) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0018 (noise floor 0.0399) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0264 against float64 (noise floor 0.0248) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Rikitake, T. (1958). Oscillations of a system of disk dynamos. *Mathematical Proceedings of the Cambridge Philosophical Society*, 54(1), 89–105. [doi:10.1017/S0305004100033223](https://doi.org/10.1017/S0305004100033223)

Original two-disc dynamo paper; the scaled form x'=-mu x+yz, y'=-mu y+(z-a)x, z'=1-xy used here is the standard later rescaling. Ours uses mu=2, a=5, common literature values; not checked against the original paper.

```bibtex
@article{Rikitake1958,
  author  = {Rikitake, Tsuneji},
  title   = {Oscillations of a system of disk dynamos},
  journal = {Mathematical Proceedings of the Cambridge Philosophical Society},
  year    = {1958},
  volume  = {54},
  number  = {1},
  pages   = {89--105},
  doi     = {10.1017/S0305004100033223}
}
```

<a id="rikitake__rk4"></a>

### Rikitake (26-R)

**Equations:** ẋ = −μx + yz; ẏ = −μy + (z − a)x; ż = 1 − xy

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | μ = 2, a = 5 |
| Initial condition | x\_0 = 1, y\_0 = 0, z\_0 = 0.5 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁶ |
| L(n) | ≈ 96.5n² − 113n + … |
| Gates at 64 bits | 383,666 |
| pJ/bit (32 / 64-bit) | 7.416 / 17.649 |
| Lyapunov exponent | 0.1317 (float64), 0.1348 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 7 integer bits and 57 fractional bits (resolution 2⁻⁵⁷). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.68×10⁻¹⁵, max 2.05×10⁻¹⁵; float64: median 1.44×10⁻¹⁴, max 5.28×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 1.51×10⁻¹⁴, max 5.42×10⁻¹⁴ |
| Netlist check | the 383,666-gate netlist (depth 1,031) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0232 (noise floor 0.0323) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0165 against float64 (noise floor 0.0309) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Rikitake, T. (1958). Oscillations of a system of disk dynamos. *Mathematical Proceedings of the Cambridge Philosophical Society*, 54(1), 89–105. [doi:10.1017/S0305004100033223](https://doi.org/10.1017/S0305004100033223)

Original two-disc dynamo paper; the scaled form x'=-mu x+yz, y'=-mu y+(z-a)x, z'=1-xy used here is the standard later rescaling. Ours uses mu=2, a=5, common literature values; not checked against the original paper.

```bibtex
@article{Rikitake1958,
  author  = {Rikitake, Tsuneji},
  title   = {Oscillations of a system of disk dynamos},
  journal = {Mathematical Proceedings of the Cambridge Philosophical Society},
  year    = {1958},
  volume  = {54},
  number  = {1},
  pages   = {89--105},
  doi     = {10.1017/S0305004100033223}
}
```

<a id="arneodo__euler"></a>

### Arneodo (27-E)

**Equations:** ẋ = y; ẏ = z; ż = ax − by − z − x^3

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 5.5, b = 3.5 |
| Initial condition | x\_0 = 0.2, y\_0 = 0.2, z\_0 = −0.75 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁸ |
| L(n) | 11.5n² + n + 9 |
| Gates at 64 bits | 47,177 |
| pJ/bit (32 / 64-bit) | 0.952 / 2.165 |
| Lyapunov exponent | 0.2475 (float64), 0.2240 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 8 integer bits and 56 fractional bits (resolution 2⁻⁵⁶). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.47×10⁻¹⁵, max 2.07×10⁻¹⁵; float64: median 3.30×10⁻¹⁴, max 1.87×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 3.20×10⁻¹⁴, max 1.85×10⁻¹³ |
| Netlist check | the 47,177-gate netlist (depth 500) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0951 (noise floor 0.0644) |
| Density of x (relative Wasserstein) | 0.0438 against float64 (noise floor 0.0736) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Arneodo, A., Coullet, P., & Tresser, C. (1981). Possible new strange attractors with spiral structure. *Communications in Mathematical Physics*, 79(4), 573–579. [doi:10.1007/BF01209312](https://doi.org/10.1007/BF01209312)

The cubic jerk form x''' = -x'' - 3.5x' + 5.5x - x^3 is the version listed by Sprott (2003); later papers quote a quadratic example for the 1981 paper, and a cubic family also appears in Arneodo, Coullet & Tresser (1980), Phys. Lett. A 79, 259–263. The exact form in the 1981 paper was not checked. Ours uses a=-5.5, b=3.5, c=1, d=-1 (cubic form); could not confirm these appear in the 1981 paper.

```bibtex
@article{Arneodo1981,
  author  = {Arneodo, A. and Coullet, P. and Tresser, C.},
  title   = {Possible new strange attractors with spiral structure},
  journal = {Communications in Mathematical Physics},
  year    = {1981},
  volume  = {79},
  number  = {4},
  pages   = {573--579},
  doi     = {10.1007/BF01209312}
}
```

<a id="arneodo__rk4"></a>

### Arneodo (27-R)

**Equations:** ẋ = y; ẏ = z; ż = ax − by − z − x^3

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 5.5, b = 3.5 |
| Initial condition | x\_0 = 0.2, y\_0 = 0.2, z\_0 = −0.75 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁶ |
| L(n) | ≈ 73.7n² − 70.3n + … |
| Gates at 64 bits | 293,400 |
| pJ/bit (32 / 64-bit) | 5.608 / 13.341 |
| Lyapunov exponent | 0.2305 (float64), 0.2235 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 8 integer bits and 56 fractional bits (resolution 2⁻⁵⁶). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.45×10⁻¹⁵, max 6.16×10⁻¹⁵; float64: median 7.56×10⁻¹⁵, max 5.26×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 8.88×10⁻¹⁵, max 5.60×10⁻¹⁴ |
| Netlist check | the 293,400-gate netlist (depth 1,011) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0306 (noise floor 0.0963) — indistinguishable |
| Density of x (relative Wasserstein) | 0.03 against float64 (noise floor 0.0385) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Arneodo, A., Coullet, P., & Tresser, C. (1981). Possible new strange attractors with spiral structure. *Communications in Mathematical Physics*, 79(4), 573–579. [doi:10.1007/BF01209312](https://doi.org/10.1007/BF01209312)

The cubic jerk form x''' = -x'' - 3.5x' + 5.5x - x^3 is the version listed by Sprott (2003); later papers quote a quadratic example for the 1981 paper, and a cubic family also appears in Arneodo, Coullet & Tresser (1980), Phys. Lett. A 79, 259–263. The exact form in the 1981 paper was not checked. Ours uses a=-5.5, b=3.5, c=1, d=-1 (cubic form); could not confirm these appear in the 1981 paper.

```bibtex
@article{Arneodo1981,
  author  = {Arneodo, A. and Coullet, P. and Tresser, C.},
  title   = {Possible new strange attractors with spiral structure},
  journal = {Communications in Mathematical Physics},
  year    = {1981},
  volume  = {79},
  number  = {4},
  pages   = {573--579},
  doi     = {10.1007/BF01209312}
}
```

<a id="shimizu_morioka__euler"></a>

### Shimizu–Morioka (28-E)

**Equations:** ẋ = y; ẏ = (1 − z)x − ay; ż = −bz + x^2

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.75, b = 0.45 |
| Initial condition | x\_0 = 0.1, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | ≈ 13.5n² + 25n − 658 |
| Gates at 64 bits | 56,288 |
| pJ/bit (32 / 64-bit) | 1.162 / 2.614 |
| Lyapunov exponent | 0.0572 (float64), 0.0591 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 4.89×10⁻¹⁷, max 7.65×10⁻¹⁷; float64: median 4.89×10⁻¹⁵, max 2.38×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 4.83×10⁻¹⁵, max 2.38×10⁻¹⁴ |
| Netlist check | the 56,288-gate netlist (depth 331) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0321 (noise floor 0.137) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0274 against float64 (noise floor 0.0384) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Shimizu, T., & Morioka, N. (1980). On the bifurcation of a symmetric limit cycle to an asymmetric one in a simple model. *Physics Letters A*, 76(3–4), 201–204. [doi:10.1016/0375-9601(80)90466-1](https://doi.org/10.1016/0375-9601(80)90466-1)

Original paper. Ours uses lambda=0.75, alpha=0.45, the common chaotic values; not checked against the original paper.

```bibtex
@article{ShimizuMorioka1980,
  author  = {Shimizu, Toshihiro and Morioka, Noriyuki},
  title   = {On the bifurcation of a symmetric limit cycle to an asymmetric one in a simple model},
  journal = {Physics Letters A},
  year    = {1980},
  volume  = {76},
  number  = {3--4},
  pages   = {201--204},
  doi     = {10.1016/0375-9601(80)90466-1}
}
```

<a id="shimizu_morioka__rk4"></a>

### Shimizu–Morioka (28-R)

**Equations:** ẋ = y; ẏ = (1 − z)x − ay; ż = −bz + x^2

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.75, b = 0.45 |
| Initial condition | x\_0 = 0.1, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 69.9n² + 1.02e+03n + … |
| Gates at 64 bits | 332,533 |
| pJ/bit (32 / 64-bit) | 7.221 / 15.540 |
| Lyapunov exponent | 0.0646 (float64), 0.0656 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.09×10⁻¹⁶, max 1.76×10⁻¹⁶; float64: median 1.09×10⁻¹⁵, max 5.89×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 1.11×10⁻¹⁵, max 5.77×10⁻¹⁵ |
| Netlist check | the 332,533-gate netlist (depth 893) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0159 (noise floor 0.0471) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0174 against float64 (noise floor 0.111) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Shimizu, T., & Morioka, N. (1980). On the bifurcation of a symmetric limit cycle to an asymmetric one in a simple model. *Physics Letters A*, 76(3–4), 201–204. [doi:10.1016/0375-9601(80)90466-1](https://doi.org/10.1016/0375-9601(80)90466-1)

Original paper. Ours uses lambda=0.75, alpha=0.45, the common chaotic values; not checked against the original paper.

```bibtex
@article{ShimizuMorioka1980,
  author  = {Shimizu, Toshihiro and Morioka, Noriyuki},
  title   = {On the bifurcation of a symmetric limit cycle to an asymmetric one in a simple model},
  journal = {Physics Letters A},
  year    = {1980},
  volume  = {76},
  number  = {3--4},
  pages   = {201--204},
  doi     = {10.1016/0375-9601(80)90466-1}
}
```

<a id="moore_spiegel_t_6_r_20__euler"></a>

### Moore-Spiegel (29-E)

**Equations:** ẋ = y; ẏ = z; ż = −z − (T − R + Rx^2)y − Tx

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | T = 6, R = 20 |
| Initial condition | x\_0 = 0.1, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁹ |
| L(n) | 11.5n² + 4n + 16 |
| Gates at 64 bits | 47,376 |
| pJ/bit (32 / 64-bit) | 0.923 / 2.163 |
| Lyapunov exponent | 0.1119 (float64), 0.0938 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 8 integer bits and 56 fractional bits (resolution 2⁻⁵⁶). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.91×10⁻¹⁵, max 4.83×10⁻¹⁵; float64: median 9.68×10⁻¹⁴, max 1.44×10⁻¹² |
| Circuit vs float64, one step ÷ dt | median 9.59×10⁻¹⁴, max 1.44×10⁻¹² |
| Netlist check | the 47,376-gate netlist (depth 502) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.162 (noise floor 0.0695) |
| Density of x (relative Wasserstein) | 0.0022 against float64 (noise floor 0.00418) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Moore, D. W., & Spiegel, E. A. (1966). A thermally excited non-linear oscillator. *The Astrophysical Journal*, 143, 871–887. [doi:10.1086/148562](https://doi.org/10.1086/148562)

Bibcode 1966ApJ...143..871M. Our jerk form x''' = −x'' − (T−R+Rx²)x' − Tx is the standard statement of the model. Ours uses T=6, R=20, the usual chaotic choice; not checked against the paper.

```bibtex
@article{MooreSpiegel1966,
  author  = {Moore, D. W. and Spiegel, E. A.},
  title   = {A thermally excited non-linear oscillator},
  journal = {The Astrophysical Journal},
  volume  = {143},
  pages   = {871--887},
  year    = {1966},
  doi     = {10.1086/148562}
}
```

<a id="moore_spiegel_t_6_r_20__rk4"></a>

### Moore-Spiegel (29-R)

**Equations:** ẋ = y; ẏ = z; ż = −z − (T − R + Rx^2)y − Tx

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | T = 6, R = 20 |
| Initial condition | x\_0 = 0.1, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁷ |
| L(n) | ≈ 76n² − 398n + … |
| Gates at 64 bits | 283,241 |
| pJ/bit (32 / 64-bit) | 4.726 / 12.588 |
| Lyapunov exponent | 0.1065 (float64), 0.1020 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 11 integer bits and 53 fractional bits (resolution 2⁻⁵³). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 7.70×10⁻¹⁵, max 2.30×10⁻¹⁴; float64: median 2.49×10⁻¹⁴, max 5.07×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 2.84×10⁻¹⁴, max 4.97×10⁻¹³ |
| Netlist check | the 283,241-gate netlist (depth 990) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0421 (noise floor 0.123) — indistinguishable |
| Density of x (relative Wasserstein) | 4.88×10⁻⁴ against float64 (noise floor 0.0063) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Moore, D. W., & Spiegel, E. A. (1966). A thermally excited non-linear oscillator. *The Astrophysical Journal*, 143, 871–887. [doi:10.1086/148562](https://doi.org/10.1086/148562)

Bibcode 1966ApJ...143..871M. Our jerk form x''' = −x'' − (T−R+Rx²)x' − Tx is the standard statement of the model. Ours uses T=6, R=20, the usual chaotic choice; not checked against the paper.

```bibtex
@article{MooreSpiegel1966,
  author  = {Moore, D. W. and Spiegel, E. A.},
  title   = {A thermally excited non-linear oscillator},
  journal = {The Astrophysical Journal},
  volume  = {143},
  pages   = {871--887},
  year    = {1966},
  doi     = {10.1086/148562}
}
```

<a id="hyper_r_ssler_4d__euler"></a>

### Hyper-Rössler (4D) (30-E)

**Equations:** ẋ = −y − z; ẏ = x + ay + w; ż = b + xz; ẇ = −cz + dw

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.25, b = 3, c = 0.5, d = 0.05 |
| Initial condition | x\_0 = −10, y\_0 = −6, z\_0 = 0, w\_0 = 10 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁸ |
| L(n) | ≈ 8.15n² − 22.3n − 392 |
| Gates at 64 bits | 31,566 |
| pJ/bit (32 / 64-bit) | 0.342 / 0.997 |
| Lyapunov exponent | 0.1177 (float64), 10.7292 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 12 integer bits and 52 fractional bits (resolution 2⁻⁵²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.55×10⁻¹⁴, max 5.11×10⁻¹⁴; float64: median 2.26×10⁻¹³, max 1.48×10⁻¹² |
| Circuit vs float64, one step ÷ dt | median 2.27×10⁻¹³, max 1.48×10⁻¹² |
| Netlist check | the 31,566-gate netlist (depth 313) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 90.15 (noise floor 0.142) |
| Density of x (relative Wasserstein) | 7.67 against float64 (noise floor 0.0652) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). **The 64-bit circuit leaves the attractor:** its trajectory runs into the edge of the 12-integer-bit range (±2¹¹) during the run, where float64 stays bounded, so its λ and density no longer describe the system._

#### Original reference

Rössler, O. E. (1979). An equation for hyperchaos. *Physics Letters A*, 71(2–3), 155–157. [doi:10.1016/0375-9601(79)90150-6](https://doi.org/10.1016/0375-9601(79)90150-6)

First hyperchaotic system: a four-variable oscillator with a single quadratic term. Ours (a=0.25, b=3, c=0.5, d=0.05) matches the parameters usually quoted from Rössler (1979); the paper itself was not opened.

```bibtex
@article{Rossler1979,
  author  = {R{\"o}ssler, Otto E.},
  title   = {An equation for hyperchaos},
  journal = {Physics Letters A},
  volume  = {71},
  number  = {2--3},
  pages   = {155--157},
  year    = {1979},
  doi     = {10.1016/0375-9601(79)90150-6}
}
```

<a id="hyper_r_ssler_4d__rk4"></a>

### Hyper-Rössler (4D) (30-R)

**Equations:** ẋ = −y − z; ẏ = x + ay + w; ż = b + xz; ẇ = −cz + dw

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.25, b = 3, c = 0.5, d = 0.05 |
| Initial condition | x\_0 = −10, y\_0 = −6, z\_0 = 0, w\_0 = 10 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁶ |
| L(n) | ≈ 71.2n² − 382n + … |
| Gates at 64 bits | 260,606 |
| pJ/bit (32 / 64-bit) | 2.485 / 7.866 |
| Lyapunov exponent | 0.0976 (float64), 0.1121 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 13 integer bits and 51 fractional bits (resolution 2⁻⁵¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.46×10⁻¹⁴, max 3.21×10⁻¹⁴; float64: median 8.02×10⁻¹⁴, max 2.28×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 8.53×10⁻¹⁴, max 2.27×10⁻¹³ |
| Netlist check | the 260,606-gate netlist (depth 957) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.148 (noise floor 0.231) — indistinguishable |
| Density of x (relative Wasserstein) | 0.314 against float64 (noise floor 0.146) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Rössler, O. E. (1979). An equation for hyperchaos. *Physics Letters A*, 71(2–3), 155–157. [doi:10.1016/0375-9601(79)90150-6](https://doi.org/10.1016/0375-9601(79)90150-6)

First hyperchaotic system: a four-variable oscillator with a single quadratic term. Ours (a=0.25, b=3, c=0.5, d=0.05) matches the parameters usually quoted from Rössler (1979); the paper itself was not opened.

```bibtex
@article{Rossler1979,
  author  = {R{\"o}ssler, Otto E.},
  title   = {An equation for hyperchaos},
  journal = {Physics Letters A},
  volume  = {71},
  number  = {2--3},
  pages   = {155--157},
  year    = {1979},
  doi     = {10.1016/0375-9601(79)90150-6}
}
```

<a id="lorenz_96_n_5_f_8__euler"></a>

### Lorenz 96 (31-E)

**Equations:** ẋ\_i = (x\_i+1 − x\_i−2) x\_i−1 − x\_i + F,   i = 1, …, N (cyclic)

*Plot (not reproduced in Markdown):* x₁–x₂ projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | N = 5, F = 8 |
| Initial condition | x\_1(0) = 8.01, x\_2(0) = 8, x\_3(0) = 8, x\_4(0) = 8, x\_5(0) = 8 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁸ |
| L(n) | 28.8n² − 57.5n − 155 |
| Gates at 64 bits | 113,925 |
| pJ/bit (32 / 64-bit) | 1.292 / 3.080 |
| Lyapunov exponent | 0.6260 (float64), 0.6187 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 10 integer bits and 54 fractional bits (resolution 2⁻⁵⁴). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 6.11×10⁻¹⁵, max 7.61×10⁻¹⁵; float64: median 9.31×10⁻¹⁴, max 2.24×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 9.95×10⁻¹⁴, max 2.27×10⁻¹³ |
| Netlist check | the 113,925-gate netlist (depth 322) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0116 (noise floor 0.098) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0238 against float64 (noise floor 0.0198) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Lorenz, E. N. (1996). Predictability: a problem partly solved. In *Proceedings of the Seminar on Predictability, 4–8 September 1995* (Vol. 1, pp. 1–18). ECMWF, Reading. Reprinted in T. Palmer & R. Hagedorn (Eds.), *Predictability of Weather and Climate* (2006, pp. 40–58). Cambridge University Press. <https://www.cambridge.org/core/books/predictability-of-weather-and-climate/predictability-a-problem-partly-solved/3221BDE379DEB669BA52C66263AF3206>

Report or seminar paper. Seminar paper held in 1995, proceedings dated 1996 (ECMWF lists it as 1995). The model is also published in Lorenz, E. N., & Emanuel, K. A. (1998), Optimal sites for supplementary weather observations: simulation with a small model, J. Atmos. Sci., 55, 399–414, doi:10.1175/1520-0469(1998)055<0399:OSFSWO>2.0.CO;2 (DOI confirmed). The page range of the 2006 reprint is from memory. Ours uses N=5 and F=8; Lorenz used N=36 (1996) and N=40 (1998) with F=8, so our N is much smaller.

```bibtex
@inproceedings{Lorenz1996,
  author    = {Lorenz, Edward N.},
  title     = {Predictability: a problem partly solved},
  booktitle = {Proceedings of the Seminar on Predictability, 4--8 September 1995},
  volume    = {1},
  pages     = {1--18},
  publisher = {ECMWF},
  address   = {Reading, UK},
  year      = {1996}
}
```

<a id="lorenz_96_n_5_f_8__rk4"></a>

### Lorenz 96 (31-R)

**Equations:** ẋ\_i = (x\_i+1 − x\_i−2) x\_i−1 − x\_i + F,   i = 1, …, N (cyclic)

*Plot (not reproduced in Markdown):* x₁–x₂ projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | N = 5, F = 8 |
| Initial condition | x\_1(0) = 8.01, x\_2(0) = 8, x\_3(0) = 8, x\_4(0) = 8, x\_5(0) = 8 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁶ |
| L(n) | ≈ 165n² − 695n + … |
| Gates at 64 bits | 628,095 |
| pJ/bit (32 / 64-bit) | 7.129 / 17.373 |
| Lyapunov exponent | 0.5214 (float64), 0.5221 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 10 integer bits and 54 fractional bits (resolution 2⁻⁵⁴). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.03×10⁻¹⁵, max 4.58×10⁻¹⁵; float64: median 2.24×10⁻¹⁴, max 5.61×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 2.13×10⁻¹⁴, max 5.68×10⁻¹⁴ |
| Netlist check | the 628,095-gate netlist (depth 1,010) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00125 (noise floor 0.133) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0203 against float64 (noise floor 0.0263) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Lorenz, E. N. (1996). Predictability: a problem partly solved. In *Proceedings of the Seminar on Predictability, 4–8 September 1995* (Vol. 1, pp. 1–18). ECMWF, Reading. Reprinted in T. Palmer & R. Hagedorn (Eds.), *Predictability of Weather and Climate* (2006, pp. 40–58). Cambridge University Press. <https://www.cambridge.org/core/books/predictability-of-weather-and-climate/predictability-a-problem-partly-solved/3221BDE379DEB669BA52C66263AF3206>

Report or seminar paper. Seminar paper held in 1995, proceedings dated 1996 (ECMWF lists it as 1995). The model is also published in Lorenz, E. N., & Emanuel, K. A. (1998), Optimal sites for supplementary weather observations: simulation with a small model, J. Atmos. Sci., 55, 399–414, doi:10.1175/1520-0469(1998)055<0399:OSFSWO>2.0.CO;2 (DOI confirmed). The page range of the 2006 reprint is from memory. Ours uses N=5 and F=8; Lorenz used N=36 (1996) and N=40 (1998) with F=8, so our N is much smaller.

```bibtex
@inproceedings{Lorenz1996,
  author    = {Lorenz, Edward N.},
  title     = {Predictability: a problem partly solved},
  booktitle = {Proceedings of the Seminar on Predictability, 4--8 September 1995},
  volume    = {1},
  pages     = {1--18},
  publisher = {ECMWF},
  address   = {Reading, UK},
  year      = {1996}
}
```

<a id="hadley_circulation__euler"></a>

### Hadley circulation (32-E)

**Equations:** ẋ = −y^2 − z^2 − ax + aF; ẏ = xy − bxz − y + G; ż = bxy + xz − z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.25, b = 4, F = 8, G = 1 |
| Initial condition | x\_0 = 0, y\_0 = 0, z\_0 = 1.3 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁹ |
| L(n) | 23n² − 15.1n + 84 |
| Gates at 64 bits | 93,330 |
| pJ/bit (32 / 64-bit) | 1.983 / 4.352 |
| Lyapunov exponent | 0.0382 (float64), 0.0383 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.62×10⁻¹⁶, max 5.78×10⁻¹⁶; float64: median 2.80×10⁻¹⁴, max 1.13×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 2.80×10⁻¹⁴, max 1.14×10⁻¹³ |
| Netlist check | the 93,330-gate netlist (depth 334) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00116 (noise floor 0.161) — indistinguishable |
| Density of x (relative Wasserstein) | 1.19×10⁻⁶ against float64 (noise floor 7.11×10⁻⁴) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Lorenz, E. N. (1984). Irregularity: a fundamental property of the atmosphere. *Tellus A*, 36(2), 98–110. [doi:10.1111/j.1600-0870.1984.tb00230.x](https://doi.org/10.1111/j.1600-0870.1984.tb00230.x)

Crafoord Prize Lecture (Stockholm, 1983); introduces the three-variable general-circulation model now called Lorenz-84 or the Hadley circulation model. Ours uses a=1/4, b=4, F=8, G=1, the standard chaotic values used for this model.

```bibtex
@article{Lorenz1984,
  author  = {Lorenz, Edward N.},
  title   = {Irregularity: a fundamental property of the atmosphere},
  journal = {Tellus A},
  volume  = {36},
  number  = {2},
  pages   = {98--110},
  year    = {1984},
  doi     = {10.1111/j.1600-0870.1984.tb00230.x}
}
```

<a id="hadley_circulation__rk4"></a>

### Hadley circulation (32-R)

**Equations:** ẋ = −y^2 − z^2 − ax + aF; ẏ = xy − bxz − y + G; ż = bxy + xz − z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.25, b = 4, F = 8, G = 1 |
| Initial condition | x\_0 = 0, y\_0 = 0, z\_0 = 1.3 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁷ |
| L(n) | ≈ 120n² − 117n + … |
| Gates at 64 bits | 477,716 |
| pJ/bit (32 / 64-bit) | 9.566 / 22.047 |
| Lyapunov exponent | 0.1837 (float64), 0.1683 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 6 integer bits and 58 fractional bits (resolution 2⁻⁵⁸). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.66×10⁻¹⁵, max 2.29×10⁻¹⁵; float64: median 7.16×10⁻¹⁵, max 2.78×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 7.99×10⁻¹⁵, max 2.71×10⁻¹⁴ |
| Netlist check | the 477,716-gate netlist (depth 1,055) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0839 (noise floor 0.153) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0118 against float64 (noise floor 0.0643) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Lorenz, E. N. (1984). Irregularity: a fundamental property of the atmosphere. *Tellus A*, 36(2), 98–110. [doi:10.1111/j.1600-0870.1984.tb00230.x](https://doi.org/10.1111/j.1600-0870.1984.tb00230.x)

Crafoord Prize Lecture (Stockholm, 1983); introduces the three-variable general-circulation model now called Lorenz-84 or the Hadley circulation model. Ours uses a=1/4, b=4, F=8, G=1, the standard chaotic values used for this model.

```bibtex
@article{Lorenz1984,
  author  = {Lorenz, Edward N.},
  title   = {Irregularity: a fundamental property of the atmosphere},
  journal = {Tellus A},
  volume  = {36},
  number  = {2},
  pages   = {98--110},
  year    = {1984},
  doi     = {10.1111/j.1600-0870.1984.tb00230.x}
}
```

<a id="rucklidge__euler"></a>

### Rucklidge (33-E)

**Equations:** ẋ = −κx + λy − yz; ẏ = x; ż = −z + y^2

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | κ = 2, λ = 6.7 |
| Initial condition | x\_0 = 1, y\_0 = 0, z\_0 = 4.5 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | ≈ 13.7n² − 13n − 418 |
| Gates at 64 bits | 54,734 |
| pJ/bit (32 / 64-bit) | 1.034 / 2.508 |
| Lyapunov exponent | 0.1966 (float64), 0.2041 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 9 integer bits and 55 fractional bits (resolution 2⁻⁵⁵). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.47×10⁻¹⁵, max 2.99×10⁻¹⁵; float64: median 2.95×10⁻¹⁴, max 1.09×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 2.84×10⁻¹⁴, max 1.10×10⁻¹³ |
| Netlist check | the 54,734-gate netlist (depth 318) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0385 (noise floor 0.0555) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0521 against float64 (noise floor 0.0891) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Rucklidge, A. M. (1992). Chaos in models of double convection. *Journal of Fluid Mechanics*, 237, 209–229. [doi:10.1017/S0022112092003392](https://doi.org/10.1017/S0022112092003392)

Author's version at White Rose eprints; the record gives this DOI. Ours uses κ=2, λ=6.7, the values usually quoted for chaos in this model; not checked against the paper.

```bibtex
@article{Rucklidge1992,
  author  = {Rucklidge, A. M.},
  title   = {Chaos in models of double convection},
  journal = {Journal of Fluid Mechanics},
  volume  = {237},
  pages   = {209--229},
  year    = {1992},
  doi     = {10.1017/S0022112092003392}
}
```

<a id="rucklidge__rk4"></a>

### Rucklidge (33-R)

**Equations:** ẋ = −κx + λy − yz; ẏ = x; ż = −z + y^2

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | κ = 2, λ = 6.7 |
| Initial condition | x\_0 = 1, y\_0 = 0, z\_0 = 4.5 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 78.6n² + 204n + … |
| Gates at 64 bits | 324,625 |
| pJ/bit (32 / 64-bit) | 5.855 / 14.408 |
| Lyapunov exponent | 0.1979 (float64), 0.2009 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 9 integer bits and 55 fractional bits (resolution 2⁻⁵⁵). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.31×10⁻¹⁵, max 6.73×10⁻¹⁵; float64: median 6.93×10⁻¹⁵, max 2.93×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 7.99×10⁻¹⁵, max 2.93×10⁻¹⁴ |
| Netlist check | the 324,625-gate netlist (depth 823) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0153 (noise floor 0.0467) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0202 against float64 (noise floor 0.063) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Rucklidge, A. M. (1992). Chaos in models of double convection. *Journal of Fluid Mechanics*, 237, 209–229. [doi:10.1017/S0022112092003392](https://doi.org/10.1017/S0022112092003392)

Author's version at White Rose eprints; the record gives this DOI. Ours uses κ=2, λ=6.7, the values usually quoted for chaos in this model; not checked against the paper.

```bibtex
@article{Rucklidge1992,
  author  = {Rucklidge, A. M.},
  title   = {Chaos in models of double convection},
  journal = {Journal of Fluid Mechanics},
  volume  = {237},
  pages   = {209--229},
  year    = {1992},
  doi     = {10.1017/S0022112092003392}
}
```

<a id="thomas_b_0_208186__euler"></a>

### Thomas (34-E)

**Equations:** ẋ = sin y − bx; ẏ = sin z − by; ż = sin x − bz

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | b = 0.208186 |
| Initial condition | x\_0 = 0.1, y\_0 = 0, z\_0 = −0.1 |
| Type | flow |
| Class | Transcendental |
| Scheme | Euler, dt = 2⁻⁶ |
| L(n) | ≈ 0.782n³ + 272n² − 7.8e+03n + 77533 |
| Gates at 64 bits | 893,994 |
| pJ/bit (32 / 64-bit) | 10.642 / 40.584 |
| Lyapunov exponent | 0.0453 (float64), 0.0452 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.86×10⁻¹⁶, max 2.34×10⁻¹⁶; float64: median 1.02×10⁻¹⁴, max 1.41×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 1.02×10⁻¹⁴, max 1.43×10⁻¹⁴ |
| Netlist check | the 893,994-gate netlist (depth 2,765) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 4.44×10⁻⁴ (noise floor 0.12) — indistinguishable |
| Density of x (relative Wasserstein) | 1.06×10⁻⁶ against float64 (noise floor 0.0642) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Thomas, R. (1999). Deterministic chaos seen in terms of feedback circuits: analysis, synthesis, "labyrinth chaos". *International Journal of Bifurcation and Chaos*, 9(10), 1889–1905. [doi:10.1142/S0218127499001383](https://doi.org/10.1142/S0218127499001383)

Introduces the cyclically symmetric system x' = sin y − bx (and cyclic permutations). Ours uses b=0.208186, the value at the onset of chaos quoted by Sprott and later papers, not a value from Thomas (1999).

```bibtex
@article{Thomas1999,
  author  = {Thomas, Ren{\'e}},
  title   = {Deterministic chaos seen in terms of feedback circuits: analysis, synthesis, ``labyrinth chaos''},
  journal = {International Journal of Bifurcation and Chaos},
  volume  = {9},
  number  = {10},
  pages   = {1889--1905},
  year    = {1999},
  doi     = {10.1142/S0218127499001383}
}
```

<a id="thomas_b_0_208186__rk4"></a>

### Thomas (34-R)

**Equations:** ẋ = sin y − bx; ẏ = sin z − by; ż = sin x − bz

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0625 time units, 250 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | b = 0.208186 |
| Initial condition | x\_0 = 0.1, y\_0 = 0, z\_0 = −0.1 |
| Type | flow |
| Class | Transcendental |
| Scheme | RK4, dt = 2⁻⁴ |
| L(n) | ≈ 2.11n³ + 1.22e+03n² + … |
| Gates at 64 bits | 3,682,854 |
| pJ/bit (32 / 64-bit) | 29.789 / 144.762 |
| Lyapunov exponent | 0.0450 (float64), 0.0451 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.28×10⁻¹⁶, max 1.46×10⁻¹⁶; float64: median 2.42×10⁻¹⁵, max 3.62×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 2.46×10⁻¹⁵, max 3.72×10⁻¹⁵ |
| Netlist check | the 3,682,854-gate netlist (depth 11,002) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00201 (noise floor 0.197) — indistinguishable |
| Density of x (relative Wasserstein) | 1.92×10⁻⁶ against float64 (noise floor 0.0451) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Thomas, R. (1999). Deterministic chaos seen in terms of feedback circuits: analysis, synthesis, "labyrinth chaos". *International Journal of Bifurcation and Chaos*, 9(10), 1889–1905. [doi:10.1142/S0218127499001383](https://doi.org/10.1142/S0218127499001383)

Introduces the cyclically symmetric system x' = sin y − bx (and cyclic permutations). Ours uses b=0.208186, the value at the onset of chaos quoted by Sprott and later papers, not a value from Thomas (1999).

```bibtex
@article{Thomas1999,
  author  = {Thomas, Ren{\'e}},
  title   = {Deterministic chaos seen in terms of feedback circuits: analysis, synthesis, ``labyrinth chaos''},
  journal = {International Journal of Bifurcation and Chaos},
  volume  = {9},
  number  = {10},
  pages   = {1889--1905},
  year    = {1999},
  doi     = {10.1142/S0218127499001383}
}
```

<a id="halvorsen_a_1_4__euler"></a>

### Halvorsen (35-E)

**Equations:** ẋ = −ax − 4y − 4z − y^2; ẏ = −ay − 4z − 4x − z^2; ż = −az − 4x − 4y − x^2

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 1.4 |
| Initial condition | x\_0 = −1.48, y\_0 = −1.51, z\_0 = 2.04 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁹ |
| L(n) | 24.75n² − 99n − 381 |
| Gates at 64 bits | 94,659 |
| pJ/bit (32 / 64-bit) | 1.675 / 4.237 |
| Lyapunov exponent | 0.7490 (float64), 0.7339 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 10 integer bits and 54 fractional bits (resolution 2⁻⁵⁴). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.20×10⁻¹⁴, max 2.22×10⁻¹⁴; float64: median 1.46×10⁻¹³, max 4.40×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 1.42×10⁻¹³, max 4.55×10⁻¹³ |
| Netlist check | the 94,659-gate netlist (depth 320) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0202 (noise floor 0.0271) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0165 against float64 (noise floor 0.0169) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (2003). *Chaos and time-series analysis*. Oxford University Press. <https://global.oup.com/academic/product/chaos-and-time-series-analysis-9780198508397>

Book source. The system was proposed by Arne Dehli Halvorsen on the sci.fractals newsgroup; Sprott's page credits it and points to this book as the published description. No DOI is used for the book. Sprott shows the attractor at a=1.27 (b=c=4); ours uses a=1.4, a value common in later work, so it differs from Sprott.

```bibtex
@book{Sprott2003,
  author    = {Sprott, Julien Clinton},
  title     = {Chaos and Time-Series Analysis},
  publisher = {Oxford University Press},
  address   = {Oxford},
  year      = {2003},
  isbn      = {9780198508397}
}
```

<a id="halvorsen_a_1_4__rk4"></a>

### Halvorsen (35-R)

**Equations:** ẋ = −ax − 4y − 4z − y^2; ẏ = −ay − 4z − 4x − z^2; ż = −az − 4x − 4y − x^2

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 1.4 |
| Initial condition | x\_0 = −1.48, y\_0 = −1.51, z\_0 = 2.04 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁷ |
| L(n) | ≈ 118n² + 295n + … |
| Gates at 64 bits | 485,118 |
| pJ/bit (32 / 64-bit) | 9.387 / 22.406 |
| Lyapunov exponent | 0.6764 (float64), 0.6873 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 10 integer bits and 54 fractional bits (resolution 2⁻⁵⁴). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.56×10⁻¹⁵, max 8.88×10⁻¹⁵; float64: median 3.98×10⁻¹⁴, max 1.22×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 4.26×10⁻¹⁴, max 1.21×10⁻¹³ |
| Netlist check | the 485,118-gate netlist (depth 1,009) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0161 (noise floor 0.0263) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00785 against float64 (noise floor 0.00695) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (2003). *Chaos and time-series analysis*. Oxford University Press. <https://global.oup.com/academic/product/chaos-and-time-series-analysis-9780198508397>

Book source. The system was proposed by Arne Dehli Halvorsen on the sci.fractals newsgroup; Sprott's page credits it and points to this book as the published description. No DOI is used for the book. Sprott shows the attractor at a=1.27 (b=c=4); ours uses a=1.4, a value common in later work, so it differs from Sprott.

```bibtex
@book{Sprott2003,
  author    = {Sprott, Julien Clinton},
  title     = {Chaos and Time-Series Analysis},
  publisher = {Oxford University Press},
  address   = {Oxford},
  year      = {2003},
  isbn      = {9780198508397}
}
```

<a id="sprott_linz_a_nose_hoover__euler"></a>

### Sprott-Linz A (Nose-Hoover) (36-E)

**Equations:** ẋ = y; ẏ = −x + yz; ż = 1 − y^2

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case A) |
| Initial condition | x\_0 = 0, y\_0 = 5, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁹ |
| L(n) | 11.5n² − 16n − 20 |
| Gates at 64 bits | 46,060 |
| pJ/bit (32 / 64-bit) | 0.750 / 1.973 |
| Lyapunov exponent | 0.0109 (float64), 0.0109 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 7 integer bits and 57 fractional bits (resolution 2⁻⁵⁷). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.44×10⁻¹⁵, max 2.00×10⁻¹⁵; float64: median 3.55×10⁻¹⁴, max 1.11×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 3.55×10⁻¹⁴, max 1.10×10⁻¹³ |
| Netlist check | the 46,060-gate netlist (depth 326) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 5.71×10⁻⁴ (noise floor 5.64×10⁻⁴) |
| Density of x (relative Wasserstein) | 8.29×10⁻¹³ against float64 (noise floor 8.36×10⁻⁶) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). The circuit and float64 trajectories stayed together for the whole run (small exponent, slow divergence), so the λ and density differences reflect rounding, not two independent samples of the attractor._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Case A is the Nosé–Hoover oscillator: Posch, H. A., Hoover, W. G., & Vesely, F. J. (1986). Canonical dynamics of the Nosé oscillator: stability, order, and chaos. *Physical Review A*, 33(6), 4253–4265. [doi:10.1103/PhysRevA.33.4253](https://doi.org/10.1103/PhysRevA.33.4253)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_a_nose_hoover__rk4"></a>

### Sprott-Linz A (Nose-Hoover) (36-R)

**Equations:** ẋ = y; ẏ = −x + yz; ż = 1 − y^2

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case A) |
| Initial condition | x\_0 = 0, y\_0 = 5, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁷ |
| L(n) | ≈ 73.6n² − 114n + … |
| Gates at 64 bits | 290,209 |
| pJ/bit (32 / 64-bit) | 4.874 / 12.753 |
| Lyapunov exponent | 0.0321 (float64), 0.0321 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 7 integer bits and 57 fractional bits (resolution 2⁻⁵⁷). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.24×10⁻¹⁵, max 4.26×10⁻¹⁵; float64: median 8.49×10⁻¹⁵, max 2.74×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 7.99×10⁻¹⁵, max 3.02×10⁻¹⁴ |
| Netlist check | the 290,209-gate netlist (depth 1,033) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 6.72×10⁻⁵ (noise floor 0.0706) — indistinguishable |
| Density of x (relative Wasserstein) | 4.16×10⁻⁹ against float64 (noise floor 0.00332) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). The circuit and float64 trajectories stayed together for the whole run (small exponent, slow divergence), so the λ and density differences reflect rounding, not two independent samples of the attractor._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Case A is the Nosé–Hoover oscillator: Posch, H. A., Hoover, W. G., & Vesely, F. J. (1986). Canonical dynamics of the Nosé oscillator: stability, order, and chaos. *Physical Review A*, 33(6), 4253–4265. [doi:10.1103/PhysRevA.33.4253](https://doi.org/10.1103/PhysRevA.33.4253)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_b__euler"></a>

### Sprott-Linz B (37-E)

**Equations:** ẋ = yz; ẏ = x − y; ż = 1 − xy

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case B) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | 11.5n² − 12n − 8 |
| Gates at 64 bits | 46,328 |
| pJ/bit (32 / 64-bit) | 0.791 / 2.007 |
| Lyapunov exponent | 0.2035 (float64), 0.2037 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 6 integer bits and 58 fractional bits (resolution 2⁻⁵⁸). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.73×10⁻¹⁶, max 2.48×10⁻¹⁶; float64: median 7.25×10⁻¹⁵, max 3.23×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 7.11×10⁻¹⁵, max 3.24×10⁻¹⁴ |
| Netlist check | the 46,328-gate netlist (depth 324) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 8.02×10⁻⁴ (noise floor 0.0369) — indistinguishable |
| Density of x (relative Wasserstein) | 0.059 against float64 (noise floor 0.143) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_b__rk4"></a>

### Sprott-Linz B (37-R)

**Equations:** ẋ = yz; ẏ = x − y; ż = 1 − xy

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case B) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 69.8n² + 241n + … |
| Gates at 64 bits | 292,828 |
| pJ/bit (32 / 64-bit) | 6.036 / 13.826 |
| Lyapunov exponent | 0.2059 (float64), 0.2143 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 6 integer bits and 58 fractional bits (resolution 2⁻⁵⁸). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 4.29×10⁻¹⁶, max 1.00×10⁻¹⁵; float64: median 2.01×10⁻¹⁵, max 1.33×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 2.11×10⁻¹⁵, max 1.30×10⁻¹⁴ |
| Netlist check | the 292,828-gate netlist (depth 1,023) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0408 (noise floor 0.03) |
| Density of x (relative Wasserstein) | 0.0701 against float64 (noise floor 0.109) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_c__euler"></a>

### Sprott-Linz C (38-E)

**Equations:** ẋ = yz; ẏ = x − y; ż = 1 − x^2

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case C) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | 11.5n² − 11n − 12 |
| Gates at 64 bits | 46,388 |
| pJ/bit (32 / 64-bit) | 0.936 / 2.137 |
| Lyapunov exponent | 0.1807 (float64), 0.1752 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 6 integer bits and 58 fractional bits (resolution 2⁻⁵⁸). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.78×10⁻¹⁶, max 2.47×10⁻¹⁶; float64: median 6.50×10⁻¹⁵, max 2.54×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 6.66×10⁻¹⁵, max 2.53×10⁻¹⁴ |
| Netlist check | the 46,388-gate netlist (depth 324) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0305 (noise floor 0.0459) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0842 against float64 (noise floor 0.0648) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_c__rk4"></a>

### Sprott-Linz C (38-R)

**Equations:** ẋ = yz; ẏ = x − y; ż = 1 − x^2

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case C) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 71.6n² + 71.1n + … |
| Gates at 64 bits | 291,736 |
| pJ/bit (32 / 64-bit) | 4.029 / 10.942 |
| Lyapunov exponent | 0.1465 (float64), 0.1547 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 7 integer bits and 57 fractional bits (resolution 2⁻⁵⁷). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 8.55×10⁻¹⁶, max 1.39×10⁻¹⁵; float64: median 2.43×10⁻¹⁵, max 2.87×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 2.66×10⁻¹⁵, max 2.91×10⁻¹⁴ |
| Netlist check | the 291,736-gate netlist (depth 1,017) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0561 (noise floor 0.158) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0396 against float64 (noise floor 0.137) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_e__euler"></a>

### Sprott-Linz E (39-E)

**Equations:** ẋ = yz; ẏ = x^2 − y; ż = 1 − 4x

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case E) |
| Initial condition | x\_0 = 1, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | 11.5n² − 7n + 5 |
| Gates at 64 bits | 46,661 |
| pJ/bit (32 / 64-bit) | 0.916 / 2.138 |
| Lyapunov exponent | 0.0727 (float64), 0.0663 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 8.38×10⁻¹⁷, max 1.16×10⁻¹⁶; float64: median 9.30×10⁻¹⁵, max 5.24×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 9.33×10⁻¹⁵, max 5.24×10⁻¹⁴ |
| Netlist check | the 46,661-gate netlist (depth 327) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0872 (noise floor 0.0535) |
| Density of x (relative Wasserstein) | 0.0107 against float64 (noise floor 0.0149) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_e__rk4"></a>

### Sprott-Linz E (39-R)

**Equations:** ẋ = yz; ẏ = x^2 − y; ż = 1 − 4x

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case E) |
| Initial condition | x\_0 = 1, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 67.9n² + 412n + … |
| Gates at 64 bits | 294,152 |
| pJ/bit (32 / 64-bit) | 6.132 / 13.916 |
| Lyapunov exponent | 0.0515 (float64), 0.0512 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.33×10⁻¹⁶, max 5.26×10⁻¹⁶; float64: median 2.62×10⁻¹⁵, max 1.38×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 2.50×10⁻¹⁵, max 1.40×10⁻¹⁴ |
| Netlist check | the 294,152-gate netlist (depth 1,031) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00693 (noise floor 0.488) — indistinguishable |
| Density of x (relative Wasserstein) | 1.79×10⁻⁴ against float64 (noise floor 0.0279) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_f__euler"></a>

### Sprott-Linz F (40-E)

**Equations:** ẋ = y + z; ẏ = −x + 0.5y; ż = x^2 − z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case F) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | 5.75n² + 14.5n + 12 |
| Gates at 64 bits | 24,492 |
| pJ/bit (32 / 64-bit) | 0.509 / 1.155 |
| Lyapunov exponent | 0.1317 (float64), 0.1146 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 6 integer bits and 58 fractional bits (resolution 2⁻⁵⁸). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.75×10⁻¹⁶, max 2.36×10⁻¹⁶; float64: median 4.68×10⁻¹⁵, max 2.75×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 4.66×10⁻¹⁵, max 2.75×10⁻¹⁴ |
| Netlist check | the 24,492-gate netlist (depth 325) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.13 (noise floor 0.265) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0777 against float64 (noise floor 0.108) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_f__rk4"></a>

### Sprott-Linz F (40-R)

**Equations:** ẋ = y + z; ẏ = −x + 0.5y; ż = x^2 − z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case F) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 46.8n² + 347n + … |
| Gates at 64 bits | 205,404 |
| pJ/bit (32 / 64-bit) | 4.079 / 9.392 |
| Lyapunov exponent | 0.1132 (float64), 0.1115 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 6 integer bits and 58 fractional bits (resolution 2⁻⁵⁸). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 4.12×10⁻¹⁶, max 6.59×10⁻¹⁶; float64: median 1.31×10⁻¹⁵, max 1.42×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 1.28×10⁻¹⁵, max 1.44×10⁻¹⁴ |
| Netlist check | the 205,404-gate netlist (depth 699) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.015 (noise floor 0.13) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0123 against float64 (noise floor 0.0415) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_g__euler"></a>

### Sprott-Linz G (41-E)

**Equations:** ẋ = 0.4x + z; ẏ = xz − y; ż = −x + y

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case G) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | ≈ 7.94n² + 21n − 347 |
| Gates at 64 bits | 33,429 |
| pJ/bit (32 / 64-bit) | 0.654 / 1.520 |
| Lyapunov exponent | 0.0585 (float64), 0.0583 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 8.88×10⁻¹⁷, max 1.67×10⁻¹⁶; float64: median 4.99×10⁻¹⁵, max 2.59×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 5.00×10⁻¹⁵, max 2.60×10⁻¹⁴ |
| Netlist check | the 33,429-gate netlist (depth 327) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00333 (noise floor 0.114) — indistinguishable |
| Density of x (relative Wasserstein) | 2.36×10⁻⁴ against float64 (noise floor 0.0186) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_g__rk4"></a>

### Sprott-Linz G (41-R)

**Equations:** ẋ = 0.4x + z; ẏ = xz − y; ż = −x + y

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case G) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 48.7n² + 929n + … |
| Gates at 64 bits | 241,576 |
| pJ/bit (32 / 64-bit) | 5.510 / 11.519 |
| Lyapunov exponent | 0.0281 (float64), 0.0281 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.23×10⁻¹⁶, max 3.95×10⁻¹⁶; float64: median 1.32×10⁻¹⁵, max 6.88×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 1.33×10⁻¹⁵, max 7.05×10⁻¹⁵ |
| Netlist check | the 241,576-gate netlist (depth 752) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 4.70×10⁻⁶ (noise floor 0.0361) — indistinguishable |
| Density of x (relative Wasserstein) | 3.82×10⁻⁸ against float64 (noise floor 0.00329) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). The circuit and float64 trajectories stayed together for the whole run (small exponent, slow divergence), so the λ and density differences reflect rounding, not two independent samples of the attractor._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_h__euler"></a>

### Sprott-Linz H (42-E)

**Equations:** ẋ = −y + z^2; ẏ = x + 0.5y; ż = x − z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case H) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | 5.75n² + 14.5n + 12 |
| Gates at 64 bits | 24,492 |
| pJ/bit (32 / 64-bit) | 0.491 / 1.112 |
| Lyapunov exponent | 0.0894 (float64), 0.1068 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 6 integer bits and 58 fractional bits (resolution 2⁻⁵⁸). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.81×10⁻¹⁶, max 2.43×10⁻¹⁶; float64: median 6.22×10⁻¹⁵, max 5.19×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 6.22×10⁻¹⁵, max 5.20×10⁻¹⁴ |
| Netlist check | the 24,492-gate netlist (depth 323) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.195 (noise floor 0.122) |
| Density of x (relative Wasserstein) | 0.0221 against float64 (noise floor 0.0385) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_h__rk4"></a>

### Sprott-Linz H (42-R)

**Equations:** ẋ = −y + z^2; ẏ = x + 0.5y; ż = x − z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case H) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 46.8n² + 347n + … |
| Gates at 64 bits | 205,404 |
| pJ/bit (32 / 64-bit) | 4.328 / 9.574 |
| Lyapunov exponent | 0.0984 (float64), 0.1120 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 6 integer bits and 58 fractional bits (resolution 2⁻⁵⁸). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 4.22×10⁻¹⁶, max 6.30×10⁻¹⁶; float64: median 1.43×10⁻¹⁵, max 1.22×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 1.44×10⁻¹⁵, max 1.27×10⁻¹⁴ |
| Netlist check | the 205,404-gate netlist (depth 699) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.138 (noise floor 0.1) |
| Density of x (relative Wasserstein) | 0.0564 against float64 (noise floor 0.0361) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_i__euler"></a>

### Sprott-Linz I (43-E)

**Equations:** ẋ = −0.2y; ẏ = x + z; ż = x + y^2 − z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case I) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | ≈ 7.63n² + 50.4n − 609 |
| Gates at 64 bits | 33,695 |
| pJ/bit (32 / 64-bit) | 0.737 / 1.589 |
| Lyapunov exponent | 0.0294 (float64), 0.0294 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.22×10⁻¹⁷, max 4.44×10⁻¹⁷; float64: median 1.88×10⁻¹⁵, max 7.11×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 1.89×10⁻¹⁵, max 7.11×10⁻¹⁵ |
| Netlist check | the 33,695-gate netlist (depth 331) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 9.75×10⁻⁷ (noise floor 0.0739) — indistinguishable |
| Density of x (relative Wasserstein) | 2.75×10⁻¹¹ against float64 (noise floor 0.0133) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). The circuit and float64 trajectories stayed together for the whole run (small exponent, slow divergence), so the λ and density differences reflect rounding, not two independent samples of the attractor._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_i__rk4"></a>

### Sprott-Linz I (43-R)

**Equations:** ẋ = −0.2y; ẏ = x + z; ż = x + y^2 − z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case I) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 44.9n² + 1.24e+03n + … |
| Gates at 64 bits | 242,164 |
| pJ/bit (32 / 64-bit) | 5.424 / 11.444 |
| Lyapunov exponent | 0.0192 (float64), 0.0192 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 5.48×10⁻¹⁷, max 8.28×10⁻¹⁷; float64: median 4.51×10⁻¹⁶, max 1.71×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 4.86×10⁻¹⁶, max 1.67×10⁻¹⁵ |
| Netlist check | the 242,164-gate netlist (depth 715) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 1.06×10⁻⁶ (noise floor 0.0463) — indistinguishable |
| Density of x (relative Wasserstein) | 2.25×10⁻¹³ against float64 (noise floor 6.42×10⁻⁴) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). The circuit and float64 trajectories stayed together for the whole run (small exponent, slow divergence), so the λ and density differences reflect rounding, not two independent samples of the attractor._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_j__euler"></a>

### Sprott-Linz J (44-E)

**Equations:** ẋ = 2z; ẏ = −2y + z; ż = −x + y + y^2

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case J) |
| Initial condition | x\_0 = 2, y\_0 = 2, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | 5.75n² + 9.5n + 1 |
| Gates at 64 bits | 24,161 |
| pJ/bit (32 / 64-bit) | 0.512 / 1.116 |
| Lyapunov exponent | 0.0837 (float64), 0.0836 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 8 integer bits and 56 fractional bits (resolution 2⁻⁵⁶). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 7.77×10⁻¹⁶, max 8.88×10⁻¹⁶; float64: median 2.71×10⁻¹⁴, max 2.20×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 2.75×10⁻¹⁴, max 2.20×10⁻¹³ |
| Netlist check | the 24,161-gate netlist (depth 319) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00223 (noise floor 0.0742) — indistinguishable |
| Density of x (relative Wasserstein) | 0.013 against float64 (noise floor 0.0137) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_j__rk4"></a>

### Sprott-Linz J (44-R)

**Equations:** ẋ = 2z; ẏ = −2y + z; ż = −x + y + y^2

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case J) |
| Initial condition | x\_0 = 2, y\_0 = 2, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 48.6n² + 191n + … |
| Gates at 64 bits | 205,199 |
| pJ/bit (32 / 64-bit) | 4.300 / 9.570 |
| Lyapunov exponent | 0.0751 (float64), 0.0792 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 7 integer bits and 57 fractional bits (resolution 2⁻⁵⁷). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.08×10⁻¹⁵, max 2.04×10⁻¹⁵; float64: median 8.91×10⁻¹⁵, max 5.76×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 8.55×10⁻¹⁵, max 5.64×10⁻¹⁴ |
| Netlist check | the 205,199-gate netlist (depth 695) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0547 (noise floor 0.12) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00377 against float64 (noise floor 0.00571) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_k__euler"></a>

### Sprott-Linz K (45-E)

**Equations:** ẋ = xy − z; ẏ = x − y; ż = x + 0.3z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case K) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | ≈ 7.94n² + 19.9n − 347 |
| Gates at 64 bits | 33,365 |
| pJ/bit (32 / 64-bit) | 0.682 / 1.533 |
| Lyapunov exponent | 0.0021 (float64), 0.0021 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 8.56×10⁻¹⁷, max 1.53×10⁻¹⁶; float64: median 5.88×10⁻¹⁵, max 2.78×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 5.77×10⁻¹⁵, max 2.78×10⁻¹⁴ |
| Netlist check | the 33,365-gate netlist (depth 327) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 5.87×10⁻⁵ (noise floor 0.00387) — indistinguishable |
| Density of x (relative Wasserstein) | 8.18×10⁻¹⁴ against float64 (noise floor 9.19×10⁻⁵) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). The circuit and float64 trajectories stayed together for the whole run (small exponent, slow divergence), so the λ and density differences reflect rounding, not two independent samples of the attractor._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_k__rk4"></a>

### Sprott-Linz K (45-R)

**Equations:** ẋ = xy − z; ẏ = x − y; ż = x + 0.3z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case K) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 49.9n² + 817n + … |
| Gates at 64 bits | 240,368 |
| pJ/bit (32 / 64-bit) | 5.402 / 11.414 |
| Lyapunov exponent | 0.0316 (float64), 0.0316 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.30×10⁻¹⁶, max 3.21×10⁻¹⁶; float64: median 1.31×10⁻¹⁵, max 6.74×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 1.33×10⁻¹⁵, max 7.05×10⁻¹⁵ |
| Netlist check | the 240,368-gate netlist (depth 1,031) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 2.76×10⁻⁵ (noise floor 0.326) — indistinguishable |
| Density of x (relative Wasserstein) | 9.23×10⁻⁹ against float64 (noise floor 0.0128) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). The circuit and float64 trajectories stayed together for the whole run (small exponent, slow divergence), so the λ and density differences reflect rounding, not two independent samples of the attractor._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_l__euler"></a>

### Sprott-Linz L (46-E)

**Equations:** ẋ = y + 3.9z; ẏ = 0.9x^2 − y; ż = 1 − x

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case L) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | 10.8n² − 51.1n − 223 |
| Gates at 64 bits | 40,543 |
| pJ/bit (32 / 64-bit) | 0.741 / 1.861 |
| Lyapunov exponent | 0.0523 (float64), 0.0528 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 9 integer bits and 55 fractional bits (resolution 2⁻⁵⁵). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.11×10⁻¹⁵, max 7.86×10⁻¹⁵; float64: median 8.98×10⁻¹⁴, max 4.49×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 8.88×10⁻¹⁴, max 4.51×10⁻¹³ |
| Netlist check | the 40,543-gate netlist (depth 422) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00895 (noise floor 0.0578) — indistinguishable |
| Density of x (relative Wasserstein) | 2.03×10⁻⁴ against float64 (noise floor 9.55×10⁻⁴) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_l__rk4"></a>

### Sprott-Linz L (46-R)

**Equations:** ẋ = y + 3.9z; ẏ = 0.9x^2 − y; ż = 1 − x

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case L) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 61.8n² + 480n + … |
| Gates at 64 bits | 268,792 |
| pJ/bit (32 / 64-bit) | 5.620 / 12.748 |
| Lyapunov exponent | 0.0574 (float64), 0.0607 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 9 integer bits and 55 fractional bits (resolution 2⁻⁵⁵). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.52×10⁻¹⁵, max 5.82×10⁻¹⁵; float64: median 2.12×10⁻¹⁴, max 1.13×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 2.13×10⁻¹⁴, max 1.15×10⁻¹³ |
| Netlist check | the 268,792-gate netlist (depth 966) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0576 (noise floor 0.16) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00134 against float64 (noise floor 0.00279) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_m__euler"></a>

### Sprott-Linz M (47-E)

**Equations:** ẋ = −z; ẏ = −x^2 − y; ż = 1.7 + 1.7x + y

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case M) |
| Initial condition | x\_0 = 0, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁹ |
| L(n) | 8.25n² − 8.68n − 97 |
| Gates at 64 bits | 33,147 |
| pJ/bit (32 / 64-bit) | 0.601 / 1.482 |
| Lyapunov exponent | 0.0606 (float64), 0.0602 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 6 integer bits and 58 fractional bits (resolution 2⁻⁵⁸). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 6.66×10⁻¹⁶, max 1.20×10⁻¹⁵; float64: median 5.23×10⁻¹⁴, max 2.15×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 5.24×10⁻¹⁴, max 2.15×10⁻¹³ |
| Netlist check | the 33,147-gate netlist (depth 330) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0054 (noise floor 0.0905) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00121 against float64 (noise floor 0.00385) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_m__rk4"></a>

### Sprott-Linz M (47-R)

**Equations:** ẋ = −z; ẏ = −x^2 − y; ż = 1.7 + 1.7x + y

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case M) |
| Initial condition | x\_0 = 0, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁷ |
| L(n) | ≈ 52.4n² + 619n + … |
| Gates at 64 bits | 241,056 |
| pJ/bit (32 / 64-bit) | 5.077 / 11.236 |
| Lyapunov exponent | 0.0474 (float64), 0.0474 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 8.82×10⁻¹⁶, max 1.21×10⁻¹⁵; float64: median 1.25×10⁻¹⁴, max 5.11×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 1.24×10⁻¹⁴, max 5.02×10⁻¹⁴ |
| Netlist check | the 241,056-gate netlist (depth 685) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 9.24×10⁻⁵ (noise floor 0.115) — indistinguishable |
| Density of x (relative Wasserstein) | 9.65×10⁻⁷ against float64 (noise floor 0.0079) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). The circuit and float64 trajectories stayed together for the whole run (small exponent, slow divergence), so the λ and density differences reflect rounding, not two independent samples of the attractor._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_n__euler"></a>

### Sprott-Linz N (48-E)

**Equations:** ẋ = −2y; ẏ = x + z^2; ż = 1 + y − 2z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case N) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | 5.75n² + 7n + 17 |
| Gates at 64 bits | 24,017 |
| pJ/bit (32 / 64-bit) | 0.520 / 1.135 |
| Lyapunov exponent | 0.0870 (float64), 0.0838 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 7 integer bits and 57 fractional bits (resolution 2⁻⁵⁷). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.33×10⁻¹⁶, max 4.44×10⁻¹⁶; float64: median 2.92×10⁻¹⁴, max 2.24×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 2.93×10⁻¹⁴, max 2.24×10⁻¹³ |
| Netlist check | the 24,017-gate netlist (depth 321) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0367 (noise floor 0.0509) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0153 against float64 (noise floor 0.0238) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_n__rk4"></a>

### Sprott-Linz N (48-R)

**Equations:** ẋ = −2y; ẏ = x + z^2; ż = 1 + y − 2z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case N) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 48.6n² + 163n + … |
| Gates at 64 bits | 203,496 |
| pJ/bit (32 / 64-bit) | 4.289 / 9.629 |
| Lyapunov exponent | 0.0803 (float64), 0.0739 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 7 integer bits and 57 fractional bits (resolution 2⁻⁵⁷). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 9.73×10⁻¹⁶, max 2.47×10⁻¹⁵; float64: median 8.67×10⁻¹⁵, max 5.67×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 8.88×10⁻¹⁵, max 5.46×10⁻¹⁴ |
| Netlist check | the 203,496-gate netlist (depth 695) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0806 (noise floor 0.245) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0118 against float64 (noise floor 0.016) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_o__euler"></a>

### Sprott-Linz O (49-E)

**Equations:** ẋ = y; ẏ = x − z; ż = x + xz + 2.7y

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case O) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | ≈ 7.31n² + 73.4n − 885 |
| Gates at 64 bits | 33,531 |
| pJ/bit (32 / 64-bit) | 0.685 / 1.522 |
| Lyapunov exponent | 0.0532 (float64), 0.0529 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 4.91×10⁻¹⁷, max 2.06×10⁻¹⁶; float64: median 2.36×10⁻¹⁵, max 1.35×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 2.39×10⁻¹⁵, max 1.34×10⁻¹⁴ |
| Netlist check | the 33,531-gate netlist (depth 381) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00652 (noise floor 0.217) — indistinguishable |
| Density of x (relative Wasserstein) | 2.61×10⁻⁴ against float64 (noise floor 0.0499) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_o__rk4"></a>

### Sprott-Linz O (49-R)

**Equations:** ẋ = y; ẏ = x − z; ż = x + xz + 2.7y

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case O) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 44.4n² + 1.25e+03n + … |
| Gates at 64 bits | 240,853 |
| pJ/bit (32 / 64-bit) | 5.784 / 11.547 |
| Lyapunov exponent | 0.0614 (float64), 0.0615 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.06×10⁻¹⁶, max 1.56×10⁻¹⁶; float64: median 6.56×10⁻¹⁶, max 3.42×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 7.08×10⁻¹⁶, max 3.36×10⁻¹⁵ |
| Netlist check | the 240,853-gate netlist (depth 1,261) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00146 (noise floor 0.0614) — indistinguishable |
| Density of x (relative Wasserstein) | 1.11×10⁻⁴ against float64 (noise floor 0.0101) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_p__euler"></a>

### Sprott-Linz P (50-E)

**Equations:** ẋ = 2.7y + z; ẏ = −x + y^2; ż = x + y

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case P) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | ≈ 7.31n² + 73.4n − 884 |
| Gates at 64 bits | 33,532 |
| pJ/bit (32 / 64-bit) | 0.719 / 1.555 |
| Lyapunov exponent | 0.0859 (float64), 0.0940 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 5.55×10⁻¹⁷, max 2.22×10⁻¹⁶; float64: median 2.58×10⁻¹⁵, max 2.54×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 2.61×10⁻¹⁵, max 2.54×10⁻¹⁴ |
| Netlist check | the 33,532-gate netlist (depth 327) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0952 (noise floor 0.198) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00955 against float64 (noise floor 0.0276) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_p__rk4"></a>

### Sprott-Linz P (50-R)

**Equations:** ẋ = 2.7y + z; ẏ = −x + y^2; ż = x + y

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case P) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 44.3n² + 1.26e+03n + … |
| Gates at 64 bits | 241,296 |
| pJ/bit (32 / 64-bit) | 5.752 / 11.736 |
| Lyapunov exponent | 0.1015 (float64), 0.0937 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.32×10⁻¹⁶, max 2.47×10⁻¹⁶; float64: median 7.79×10⁻¹⁶, max 5.68×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 7.91×10⁻¹⁶, max 5.58×10⁻¹⁵ |
| Netlist check | the 241,296-gate netlist (depth 1,045) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0762 (noise floor 0.112) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0175 against float64 (noise floor 0.0471) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_r__euler"></a>

### Sprott-Linz R (51-E)

**Equations:** ẋ = 0.9 − y; ẏ = 0.4 + z; ż = xy − z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case R) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | 5.75n² + 5.09n − 53 |
| Gates at 64 bits | 23,821 |
| pJ/bit (32 / 64-bit) | 0.468 / 1.086 |
| Lyapunov exponent | 0.0682 (float64), 0.0688 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 8 integer bits and 56 fractional bits (resolution 2⁻⁵⁶). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 7.45×10⁻¹⁶, max 9.38×10⁻¹⁶; float64: median 1.37×10⁻¹⁴, max 9.27×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 1.42×10⁻¹⁴, max 9.24×10⁻¹⁴ |
| Netlist check | the 23,821-gate netlist (depth 321) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00784 (noise floor 0.0699) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00706 against float64 (noise floor 0.0144) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_r__rk4"></a>

### Sprott-Linz R (51-R)

**Equations:** ẋ = 0.9 − y; ẏ = 0.4 + z; ż = xy − z

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case R) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 50.5n² − 5.78n + … |
| Gates at 64 bits | 202,238 |
| pJ/bit (32 / 64-bit) | 3.967 / 9.425 |
| Lyapunov exponent | 0.0647 (float64), 0.0683 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 8 integer bits and 56 fractional bits (resolution 2⁻⁵⁶). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.64×10⁻¹⁵, max 2.83×10⁻¹⁵; float64: median 2.76×10⁻¹⁵, max 1.73×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 3.55×10⁻¹⁵, max 1.55×10⁻¹⁴ |
| Netlist check | the 202,238-gate netlist (depth 691) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0556 (noise floor 0.0251) |
| Density of x (relative Wasserstein) | 0.00902 against float64 (noise floor 0.0148) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_s__euler"></a>

### Sprott-Linz S (52-E)

**Equations:** ẋ = −x − 4y; ẏ = x + z^2; ż = 1 + x

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case S) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁹ |
| L(n) | 5.75n² + 13n + 26 |
| Gates at 64 bits | 24,410 |
| pJ/bit (32 / 64-bit) | 0.502 / 1.135 |
| Lyapunov exponent | 0.2021 (float64), 0.1917 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.48×10⁻¹⁶, max 4.58×10⁻¹⁶; float64: median 2.62×10⁻¹⁴, max 2.13×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 2.58×10⁻¹⁴, max 2.13×10⁻¹³ |
| Netlist check | the 24,410-gate netlist (depth 329) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0513 (noise floor 0.0781) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0233 against float64 (noise floor 0.00901) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_linz_s__rk4"></a>

### Sprott-Linz S (52-R)

**Equations:** ẋ = −x − 4y; ẏ = x + z^2; ż = 1 + x

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | all coefficients as written (Sprott 1994, case S) |
| Initial condition | x\_0 = 0.05, y\_0 = 0.05, z\_0 = 0.05 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁷ |
| L(n) | ≈ 48.7n² + 178n + … |
| Gates at 64 bits | 205,027 |
| pJ/bit (32 / 64-bit) | 4.205 / 9.681 |
| Lyapunov exponent | 0.1735 (float64), 0.2003 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 8.72×10⁻¹⁶, max 1.13×10⁻¹⁵; float64: median 7.90×10⁻¹⁵, max 5.55×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 7.77×10⁻¹⁵, max 5.62×10⁻¹⁴ |
| Netlist check | the 205,027-gate netlist (depth 676) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.154 (noise floor 0.0927) |
| Density of x (relative Wasserstein) | 0.0105 against float64 (noise floor 0.0151) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (1994). Some simple chaotic flows. *Physical Review E*, 50(2), R647–R650. [doi:10.1103/PhysRevE.50.R647](https://doi.org/10.1103/PhysRevE.50.R647)

Covers all 19 cases A–S in Table I (case A is the Nosé–Hoover oscillator). Coefficients in our SL dict follow Table I as usually reproduced; not checked case by case against the paper.

```bibtex
@article{Sprott1994,
  author  = {Sprott, J. C.},
  title   = {Some simple chaotic flows},
  journal = {Physical Review E},
  volume  = {50},
  number  = {2},
  pages   = {R647--R650},
  year    = {1994},
  doi     = {10.1103/PhysRevE.50.R647}
}
```

<a id="sprott_jerk_circuit__euler"></a>

### Sprott jerk circuit (53-E)

**Equations:** ẋ = y; ẏ = z; ż = −az − y + \|x\| − 1

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.6 |
| Initial condition | x\_0 = 0.1, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁶ |
| L(n) | ≈ 1.57n² + 86n − 1258 |
| Gates at 64 bits | 10,524 |
| pJ/bit (32 / 64-bit) | 0.286 / 0.537 |
| Lyapunov exponent | 0.0775 (float64), 0.0737 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. \|x\| in one's complement (1 ulp off for negative x). Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.22×10⁻¹⁷, max 5.55×10⁻¹⁷; float64: median 3.55×10⁻¹⁵, max 1.41×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 3.55×10⁻¹⁵, max 1.41×10⁻¹⁴ |
| Netlist check | the 10,524-gate netlist (depth 189) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0489 (noise floor 0.0265) |
| Density of x (relative Wasserstein) | 0.0136 against float64 (noise floor 0.00893) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sprott, J. C. (2000). Simple chaotic systems and circuits. *American Journal of Physics*, 68(8), 758–763. [doi:10.1119/1.19538](https://doi.org/10.1119/1.19538)

Original paper; the jerk circuit with an absolute-value nonlinearity is one of the circuits it describes. Ours uses A=0.6, the value used for this circuit in Sprott's work.

```bibtex
@article{Sprott2000,
  author  = {Sprott, J. C.},
  title   = {Simple chaotic systems and circuits},
  journal = {American Journal of Physics},
  year    = {2000},
  volume  = {68},
  number  = {8},
  pages   = {758--763},
  doi     = {10.1119/1.19538}
}
```

<a id="sprott_jerk_circuit__rk4"></a>

### Sprott jerk circuit (53-R)

**Equations:** ẋ = y; ẏ = z; ż = −az − y + \|x\| − 1

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0625 time units, 250 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.6 |
| Initial condition | x\_0 = 0.1, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁴ |
| L(n) | ≈ 22.1n² + 1.25e+03n + … |
| Gates at 64 bits | 149,588 |
| pJ/bit (32 / 64-bit) | 4.013 / 7.509 |
| Lyapunov exponent | 0.0391 (float64), 0.0391 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. \|x\| in one's complement (1 ulp off for negative x). Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.06×10⁻¹⁶, max 1.65×10⁻¹⁶; float64: median 9.97×10⁻¹⁶, max 3.48×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 9.85×10⁻¹⁶, max 3.51×10⁻¹⁵ |
| Netlist check | the 149,588-gate netlist (depth 676) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 4.82×10⁻⁶ (noise floor 0.109) — indistinguishable |
| Density of x (relative Wasserstein) | 1.04×10⁻¹⁰ against float64 (noise floor 0.00349) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). The circuit and float64 trajectories stayed together for the whole run (small exponent, slow divergence), so the λ and density differences reflect rounding, not two independent samples of the attractor._

#### Original reference

Sprott, J. C. (2000). Simple chaotic systems and circuits. *American Journal of Physics*, 68(8), 758–763. [doi:10.1119/1.19538](https://doi.org/10.1119/1.19538)

Original paper; the jerk circuit with an absolute-value nonlinearity is one of the circuits it describes. Ours uses A=0.6, the value used for this circuit in Sprott's work.

```bibtex
@article{Sprott2000,
  author  = {Sprott, J. C.},
  title   = {Simple chaotic systems and circuits},
  journal = {American Journal of Physics},
  year    = {2000},
  volume  = {68},
  number  = {8},
  pages   = {758--763},
  doi     = {10.1119/1.19538}
}
```

<a id="genesio_tesi__euler"></a>

### Genesio-Tesi (54-E)

**Equations:** ẋ = y; ẏ = z; ż = −cx − by − az + x^2

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.44, b = 1.1, c = 1 |
| Initial condition | x\_0 = 0.1, y\_0 = 0.1, z\_0 = 0.1 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | ≈ 8.58n² + 80.7n − 1130 |
| Gates at 64 bits | 38,792 |
| pJ/bit (32 / 64-bit) | 0.752 / 1.771 |
| Lyapunov exponent | 0.0972 (float64), 0.0918 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.79×10⁻¹⁷, max 8.12×10⁻¹⁷; float64: median 2.68×10⁻¹⁵, max 1.21×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 2.66×10⁻¹⁵, max 1.21×10⁻¹⁴ |
| Netlist check | the 38,792-gate netlist (depth 329) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0559 (noise floor 0.198) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0151 against float64 (noise floor 0.0233) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Genesio, R., & Tesi, A. (1992). Harmonic balance methods for the analysis of chaotic dynamics in nonlinear systems. *Automatica*, 28(3), 531–548. [doi:10.1016/0005-1098(92)90177-H](https://doi.org/10.1016/0005-1098(92)90177-H)

Original paper. Ours uses x''' = -0.44x'' - 1.1x' - x + x^2, the usual literature values; not checked against the original paper.

```bibtex
@article{GenesioTesi1992,
  author  = {Genesio, Roberto and Tesi, Alberto},
  title   = {Harmonic balance methods for the analysis of chaotic dynamics in nonlinear systems},
  journal = {Automatica},
  year    = {1992},
  volume  = {28},
  number  = {3},
  pages   = {531--548},
  doi     = {10.1016/0005-1098(92)90177-H}
}
```

<a id="genesio_tesi__rk4"></a>

### Genesio-Tesi (54-R)

**Equations:** ẋ = y; ẏ = z; ż = −cx − by − az + x^2

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.44, b = 1.1, c = 1 |
| Initial condition | x\_0 = 0.1, y\_0 = 0.1, z\_0 = 0.1 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 44.9n² + 1.65e+03n + … |
| Gates at 64 bits | 262,578 |
| pJ/bit (32 / 64-bit) | 6.094 / 12.387 |
| Lyapunov exponent | 0.0992 (float64), 0.0960 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 5.40×10⁻¹⁷, max 1.06×10⁻¹⁶; float64: median 5.11×10⁻¹⁶, max 2.96×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 5.20×10⁻¹⁶, max 2.90×10⁻¹⁵ |
| Netlist check | the 262,578-gate netlist (depth 816) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0323 (noise floor 0.146) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00856 against float64 (noise floor 0.033) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Genesio, R., & Tesi, A. (1992). Harmonic balance methods for the analysis of chaotic dynamics in nonlinear systems. *Automatica*, 28(3), 531–548. [doi:10.1016/0005-1098(92)90177-H](https://doi.org/10.1016/0005-1098(92)90177-H)

Original paper. Ours uses x''' = -0.44x'' - 1.1x' - x + x^2, the usual literature values; not checked against the original paper.

```bibtex
@article{GenesioTesi1992,
  author  = {Genesio, Roberto and Tesi, Alberto},
  title   = {Harmonic balance methods for the analysis of chaotic dynamics in nonlinear systems},
  journal = {Automatica},
  year    = {1992},
  volume  = {28},
  number  = {3},
  pages   = {531--548},
  doi     = {10.1016/0005-1098(92)90177-H}
}
```

<a id="newton_leipnik__euler"></a>

### Newton-Leipnik (55-E)

**Equations:** ẋ = −ax + y + 10yz; ẏ = −x − 0.4y + 5xz; ż = bz − 5xy

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.4, b = 0.175 |
| Initial condition | x\_0 = 0.349, y\_0 = 0, z\_0 = −0.16 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁸ |
| L(n) | ≈ 22.9n² + 119n − 1792 |
| Gates at 64 bits | 99,041 |
| pJ/bit (32 / 64-bit) | 1.886 / 4.452 |
| Lyapunov exponent | 0.1398 (float64), 0.1391 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 2 integer bits and 62 fractional bits (resolution 2⁻⁶²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.26×10⁻¹⁷, max 4.17×10⁻¹⁷; float64: median 3.15×10⁻¹⁵, max 1.34×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 3.14×10⁻¹⁵, max 1.34×10⁻¹⁴ |
| Netlist check | the 99,041-gate netlist (depth 334) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00485 (noise floor 0.0935) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0424 against float64 (noise floor 0.0655) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Leipnik, R. B., & Newton, T. A. (1981). Double strange attractors in rigid body motion with linear feedback control. *Physics Letters A*, 86(2), 63–67. [doi:10.1016/0375-9601(81)90165-1](https://doi.org/10.1016/0375-9601(81)90165-1)

DOI built from the ScienceDirect PII 0375960181901651, which the search confirms belongs to this paper; the DOI string itself could not be resolved here. Ours uses a=0.4, b=0.175, the original values; the initial condition (0.349, 0, −0.16) is the one commonly quoted for the upper attractor.

```bibtex
@article{LeipnikNewton1981,
  author  = {Leipnik, R. B. and Newton, T. A.},
  title   = {Double strange attractors in rigid body motion with linear feedback control},
  journal = {Physics Letters A},
  volume  = {86},
  number  = {2},
  pages   = {63--67},
  year    = {1981},
  doi     = {10.1016/0375-9601(81)90165-1}
}
```

<a id="newton_leipnik__rk4"></a>

### Newton-Leipnik (55-R)

**Equations:** ẋ = −ax + y + 10yz; ẏ = −x − 0.4y + 5xz; ż = bz − 5xy

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.4, b = 0.175 |
| Initial condition | x\_0 = 0.349, y\_0 = 0, z\_0 = −0.16 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁶ |
| L(n) | ≈ 97.8n² + 2.11e+03n + … |
| Gates at 64 bits | 501,366 |
| pJ/bit (32 / 64-bit) | 11.517 / 23.912 |
| Lyapunov exponent | 0.1309 (float64), 0.1396 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 3 integer bits and 61 fractional bits (resolution 2⁻⁶¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.07×10⁻¹⁶, max 1.38×10⁻¹⁶; float64: median 7.69×10⁻¹⁶, max 3.49×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 7.77×10⁻¹⁶, max 3.52×10⁻¹⁵ |
| Netlist check | the 501,366-gate netlist (depth 1,063) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0659 (noise floor 0.0991) — indistinguishable |
| Density of x (relative Wasserstein) | 0.133 against float64 (noise floor 0.165) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Leipnik, R. B., & Newton, T. A. (1981). Double strange attractors in rigid body motion with linear feedback control. *Physics Letters A*, 86(2), 63–67. [doi:10.1016/0375-9601(81)90165-1](https://doi.org/10.1016/0375-9601(81)90165-1)

DOI built from the ScienceDirect PII 0375960181901651, which the search confirms belongs to this paper; the DOI string itself could not be resolved here. Ours uses a=0.4, b=0.175, the original values; the initial condition (0.349, 0, −0.16) is the one commonly quoted for the upper attractor.

```bibtex
@article{LeipnikNewton1981,
  author  = {Leipnik, R. B. and Newton, T. A.},
  title   = {Double strange attractors in rigid body motion with linear feedback control},
  journal = {Physics Letters A},
  volume  = {86},
  number  = {2},
  pages   = {63--67},
  year    = {1981},
  doi     = {10.1016/0375-9601(81)90165-1}
}
```

<a id="burke_shaw__euler"></a>

### Burke-Shaw (56-E)

**Equations:** ẋ = −s(x + y); ẏ = −y − sxz; ż = sxy + v

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | s = 10, v = 4.272 |
| Initial condition | x\_0 = 0.6, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁹ |
| L(n) | ≈ 11.5n² + 26.6n + 74 |
| Gates at 64 bits | 48,856 |
| pJ/bit (32 / 64-bit) | 1.048 / 2.245 |
| Lyapunov exponent | 0.5649 (float64), 0.5302 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.30×10⁻¹⁶, max 4.52×10⁻¹⁶; float64: median 1.90×10⁻¹⁴, max 1.07×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 1.91×10⁻¹⁴, max 1.07×10⁻¹³ |
| Netlist check | the 48,856-gate netlist (depth 330) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0615 (noise floor 0.0773) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0106 against float64 (noise floor 0.009) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Shaw, R. (1981). Strange attractors, chaotic behavior, and information flow. *Zeitschrift für Naturforschung A*, 36(1), 80–112. [doi:10.1515/zna-1981-0115](https://doi.org/10.1515/zna-1981-0115)

The system is credited to Bill Burke and Robert Shaw; this is the usual citation. The exact equations were not found in the paper's abstract. Ours uses s=10, v=4.272, the values on Paul Bourke's page; not checked against Shaw (1981).

```bibtex
@article{Shaw1981,
  author  = {Shaw, Robert},
  title   = {Strange Attractors, Chaotic Behavior, and Information Flow},
  journal = {Zeitschrift f{\"u}r Naturforschung A},
  year    = {1981},
  volume  = {36},
  number  = {1},
  pages   = {80--112},
  doi     = {10.1515/zna-1981-0115}
}
```

<a id="burke_shaw__rk4"></a>

### Burke-Shaw (56-R)

**Equations:** ẋ = −s(x + y); ẏ = −y − sxz; ż = sxy + v

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | s = 10, v = 4.272 |
| Initial condition | x\_0 = 0.6, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁷ |
| L(n) | ≈ 73.5n² − 13.1n + … |
| Gates at 64 bits | 295,492 |
| pJ/bit (32 / 64-bit) | 5.808 / 13.539 |
| Lyapunov exponent | 0.6964 (float64), 0.6893 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 7 integer bits and 57 fractional bits (resolution 2⁻⁵⁷). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.34×10⁻¹⁵, max 5.96×10⁻¹⁵; float64: median 5.08×10⁻¹⁵, max 1.41×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 6.22×10⁻¹⁵, max 1.78×10⁻¹⁴ |
| Netlist check | the 295,492-gate netlist (depth 1,027) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0103 (noise floor 0.00421) |
| Density of x (relative Wasserstein) | 0.00874 against float64 (noise floor 0.0159) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Shaw, R. (1981). Strange attractors, chaotic behavior, and information flow. *Zeitschrift für Naturforschung A*, 36(1), 80–112. [doi:10.1515/zna-1981-0115](https://doi.org/10.1515/zna-1981-0115)

The system is credited to Bill Burke and Robert Shaw; this is the usual citation. The exact equations were not found in the paper's abstract. Ours uses s=10, v=4.272, the values on Paul Bourke's page; not checked against Shaw (1981).

```bibtex
@article{Shaw1981,
  author  = {Shaw, Robert},
  title   = {Strange Attractors, Chaotic Behavior, and Information Flow},
  journal = {Zeitschrift f{\"u}r Naturforschung A},
  year    = {1981},
  volume  = {36},
  number  = {1},
  pages   = {80--112},
  doi     = {10.1515/zna-1981-0115}
}
```

<a id="aizawa__euler"></a>

### Aizawa (57-E)

**Equations:** ẋ = (z − b)x − dy; ẏ = dx + (z − b)y; ż = c + az − z^3/3 − (x^2 + y^2)(1 + ez) + fzx^3

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.95, b = 0.7, c = 0.6, d = 3.5, e = 0.25, f = 0.1 |
| Initial condition | x\_0 = 0.1, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | ≈ 58.3n² − 68.5n − 1094 |
| Gates at 64 bits | 233,130 |
| pJ/bit (32 / 64-bit) | 4.312 / 10.456 |
| Lyapunov exponent | 0.1124 (float64), 0.1117 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.86×10⁻¹⁶, max 3.88×10⁻¹⁶; float64: median 4.43×10⁻¹⁵, max 1.95×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 4.33×10⁻¹⁵, max 1.98×10⁻¹⁴ |
| Netlist check | the 233,130-gate netlist (depth 807) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00553 (noise floor 0.0322) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00791 against float64 (noise floor 0.0114) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Langford, W. F. (1984). Numerical studies of torus bifurcations. In T. Küpper, H. D. Mittelmann, & H. Weber (Eds.), *Numerical methods for bifurcation problems* (International Series of Numerical Mathematics, Vol. 70, pp. 285–295). Birkhäuser. [doi:10.1007/978-3-0348-6256-1\_19](https://doi.org/10.1007/978-3-0348-6256-1_19)

Book source. We credit Langford (1984): he derived the system by truncating the normal form of a Hopf–cusp (fold–Hopf) bifurcation. A 2019 study (arXiv:1905.08828) notes the equations do not appear in Yoji Aizawa's work, so the name 'Aizawa' is a misnomer. A related paper by Aizawa & Uezu (1982) is sometimes cited instead. Ours uses a=0.95, b=0.7, c=0.6, d=3.5, e=0.25, f=0.1, the usual 'Aizawa' values; not checked against Langford.

```bibtex
@incollection{Langford1984,
  author    = {Langford, William F.},
  title     = {Numerical Studies of Torus Bifurcations},
  booktitle = {Numerical Methods for Bifurcation Problems},
  editor    = {K{\"u}pper, T. and Mittelmann, H. D. and Weber, H.},
  series    = {International Series of Numerical Mathematics},
  volume    = {70},
  pages     = {285--295},
  publisher = {Birkh{\"a}user},
  address   = {Basel},
  year      = {1984},
  doi       = {10.1007/978-3-0348-6256-1_19}
}
```

<a id="aizawa__rk4"></a>

### Aizawa (57-R)

**Equations:** ẋ = (z − b)x − dy; ẏ = dx + (z − b)y; ż = c + az − z^3/3 − (x^2 + y^2)(1 + ez) + fzx^3

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.95, b = 0.7, c = 0.6, d = 3.5, e = 0.25, f = 0.1 |
| Initial condition | x\_0 = 0.1, y\_0 = 0, z\_0 = 0 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 242n² + 1.24e+03n + … |
| Gates at 64 bits | 1,039,344 |
| pJ/bit (32 / 64-bit) | 22.197 / 48.659 |
| Lyapunov exponent | 0.0860 (float64), 0.0988 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.65×10⁻¹⁶, max 4.97×10⁻¹⁶; float64: median 1.17×10⁻¹⁵, max 3.55×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 1.22×10⁻¹⁵, max 3.66×10⁻¹⁵ |
| Netlist check | the 1,039,344-gate netlist (depth 2,572) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.148 (noise floor 0.0438) |
| Density of x (relative Wasserstein) | 0.00511 against float64 (noise floor 0.00776) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Langford, W. F. (1984). Numerical studies of torus bifurcations. In T. Küpper, H. D. Mittelmann, & H. Weber (Eds.), *Numerical methods for bifurcation problems* (International Series of Numerical Mathematics, Vol. 70, pp. 285–295). Birkhäuser. [doi:10.1007/978-3-0348-6256-1\_19](https://doi.org/10.1007/978-3-0348-6256-1_19)

Book source. We credit Langford (1984): he derived the system by truncating the normal form of a Hopf–cusp (fold–Hopf) bifurcation. A 2019 study (arXiv:1905.08828) notes the equations do not appear in Yoji Aizawa's work, so the name 'Aizawa' is a misnomer. A related paper by Aizawa & Uezu (1982) is sometimes cited instead. Ours uses a=0.95, b=0.7, c=0.6, d=3.5, e=0.25, f=0.1, the usual 'Aizawa' values; not checked against Langford.

```bibtex
@incollection{Langford1984,
  author    = {Langford, William F.},
  title     = {Numerical Studies of Torus Bifurcations},
  booktitle = {Numerical Methods for Bifurcation Problems},
  editor    = {K{\"u}pper, T. and Mittelmann, H. D. and Weber, H.},
  series    = {International Series of Numerical Mathematics},
  volume    = {70},
  pages     = {285--295},
  publisher = {Birkh{\"a}user},
  address   = {Basel},
  year      = {1984},
  doi       = {10.1007/978-3-0348-6256-1_19}
}
```

<a id="hyper_lorenz_4d__euler"></a>

### Hyper-Lorenz (4D) (58-E)

**Equations:** ẋ = a(y − x) + w; ẏ = cx − y − xz; ż = xy − bz; ẇ = −yz + rw

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 10, b = 8/3, c = 28, r = −1 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 1, w\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁹ |
| L(n) | ≈ 16.8n² + 213n − 6335 |
| Gates at 64 bits | 76,644 |
| pJ/bit (32 / 64-bit) | 1.048 / 2.600 |
| Lyapunov exponent | 0.3845 (float64), 0.4169 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 12 integer bits and 52 fractional bits (resolution 2⁻⁵²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.38×10⁻¹³, max 2.35×10⁻¹³; float64: median 8.22×10⁻¹³, max 5.41×10⁻¹² |
| Circuit vs float64, one step ÷ dt | median 9.09×10⁻¹³, max 5.46×10⁻¹² |
| Netlist check | the 76,644-gate netlist (depth 365) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0845 (noise floor 0.0422) |
| Density of x (relative Wasserstein) | 0.00853 against float64 (noise floor 0.00816) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Wang, X., & Wang, M. (2008). A hyperchaos generated from Lorenz system. *Physica A: Statistical Mechanics and its Applications*, 387(14), 3751–3758. [doi:10.1016/j.physa.2008.02.020](https://doi.org/10.1016/j.physa.2008.02.020)

Introduces x' = a(y−x)+w, y' = cx−y−xz, z' = xy−bz, w' = −yz+rw, which is exactly the form in our code. Ours uses a=10, b=8/3, c=28, r=−1; r=−1 lies inside the hyperchaotic range reported for this system (about −1.52 < r < −0.06 in the original; a later paper quotes −6.43 < r < 0.17), so it matches up to the choice of r.

```bibtex
@article{WangWang2008,
  author  = {Wang, Xingyuan and Wang, Mingjun},
  title   = {A hyperchaos generated from {Lorenz} system},
  journal = {Physica A: Statistical Mechanics and its Applications},
  volume  = {387},
  number  = {14},
  pages   = {3751--3758},
  year    = {2008},
  doi     = {10.1016/j.physa.2008.02.020}
}
```

<a id="hyper_lorenz_4d__rk4"></a>

### Hyper-Lorenz (4D) (58-R)

**Equations:** ẋ = a(y − x) + w; ẏ = cx − y − xz; ż = xy − bz; ẇ = −yz + rw

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 10, b = 8/3, c = 28, r = −1 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 1, w\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁷ |
| L(n) | ≈ 112n² − 29.5n + … |
| Gates at 64 bits | 439,084 |
| pJ/bit (32 / 64-bit) | 6.083 / 15.320 |
| Lyapunov exponent | 0.3681 (float64), 0.3508 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 12 integer bits and 52 fractional bits (resolution 2⁻⁵²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.52×10⁻¹⁴, max 3.07×10⁻¹⁴; float64: median 2.06×10⁻¹³, max 1.83×10⁻¹² |
| Circuit vs float64, one step ÷ dt | median 1.99×10⁻¹³, max 1.85×10⁻¹² |
| Netlist check | the 439,084-gate netlist (depth 1,092) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.047 (noise floor 0.0556) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00679 against float64 (noise floor 0.00646) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Wang, X., & Wang, M. (2008). A hyperchaos generated from Lorenz system. *Physica A: Statistical Mechanics and its Applications*, 387(14), 3751–3758. [doi:10.1016/j.physa.2008.02.020](https://doi.org/10.1016/j.physa.2008.02.020)

Introduces x' = a(y−x)+w, y' = cx−y−xz, z' = xy−bz, w' = −yz+rw, which is exactly the form in our code. Ours uses a=10, b=8/3, c=28, r=−1; r=−1 lies inside the hyperchaotic range reported for this system (about −1.52 < r < −0.06 in the original; a later paper quotes −6.43 < r < 0.17), so it matches up to the choice of r.

```bibtex
@article{WangWang2008,
  author  = {Wang, Xingyuan and Wang, Mingjun},
  title   = {A hyperchaos generated from {Lorenz} system},
  journal = {Physica A: Statistical Mechanics and its Applications},
  volume  = {387},
  number  = {14},
  pages   = {3751--3758},
  year    = {2008},
  doi     = {10.1016/j.physa.2008.02.020}
}
```

<a id="hyperchaotic_chen_4d__euler"></a>

### Hyperchaotic Chen (4D) (59-E)

**Equations:** ẋ = a(y − x) + w; ẏ = dx − xz + cy; ż = xy − bz; ẇ = yz + rw

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 35, b = 3, c = 12, d = 7, r = 0.5 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 1, w\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻¹⁰ |
| L(n) | ≈ 14.1n² + 283n − 6611 |
| Gates at 64 bits | 69,789 |
| pJ/bit (32 / 64-bit) | 0.947 / 2.337 |
| Lyapunov exponent | 0.5745 (float64), 0.5898 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 12 integer bits and 52 fractional bits (resolution 2⁻⁵²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 9.58×10⁻¹⁴, max 1.43×10⁻¹³; float64: median 1.27×10⁻¹², max 1.03×10⁻¹¹ |
| Circuit vs float64, one step ÷ dt | median 1.36×10⁻¹², max 1.02×10⁻¹¹ |
| Netlist check | the 69,789-gate netlist (depth 322) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0266 (noise floor 0.0428) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0201 against float64 (noise floor 0.0199) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Li, Y., Tang, W. K. S., & Chen, G. (2005). Generating hyperchaos via state feedback control. *International Journal of Bifurcation and Chaos*, 15(10), 3367–3375. [doi:10.1142/S0218127405013988](https://doi.org/10.1142/S0218127405013988)

Hyperchaotic Chen system x' = a(y−x)+w, y' = dx−xz+cy, z' = xy−bz, w' = yz+rw, the form in our code. Title, journal, volume, pages and DOI confirmed; author names come from memory and were not shown in the search results. Ours uses a=35, b=3, c=12, d=7, r=0.5, the values usually quoted for this system (r in roughly 0.085–0.798 is hyperchaotic); the paper itself was not opened.

```bibtex
@article{Li2005HyperChen,
  author  = {Li, Yuxia and Tang, Wallace K. S. and Chen, Guanrong},
  title   = {Generating hyperchaos via state feedback control},
  journal = {International Journal of Bifurcation and Chaos},
  volume  = {15},
  number  = {10},
  pages   = {3367--3375},
  year    = {2005},
  doi     = {10.1142/S0218127405013988}
}
```

<a id="hyperchaotic_chen_4d__rk4"></a>

### Hyperchaotic Chen (4D) (59-R)

**Equations:** ẋ = a(y − x) + w; ẏ = dx − xz + cy; ż = xy − bz; ẇ = yz + rw

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 35, b = 3, c = 12, d = 7, r = 0.5 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 1, w\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁸ |
| L(n) | ≈ 95.3n² + 713n + … |
| Gates at 64 bits | 405,516 |
| pJ/bit (32 / 64-bit) | 5.205 / 13.610 |
| Lyapunov exponent | 0.5274 (float64), 0.5243 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 12 integer bits and 52 fractional bits (resolution 2⁻⁵²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.94×10⁻¹⁴, max 6.25×10⁻¹⁴; float64: median 3.11×10⁻¹³, max 1.76×10⁻¹² |
| Circuit vs float64, one step ÷ dt | median 3.13×10⁻¹³, max 1.71×10⁻¹² |
| Netlist check | the 405,516-gate netlist (depth 1,006) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00601 (noise floor 0.0334) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00588 against float64 (noise floor 0.00828) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Li, Y., Tang, W. K. S., & Chen, G. (2005). Generating hyperchaos via state feedback control. *International Journal of Bifurcation and Chaos*, 15(10), 3367–3375. [doi:10.1142/S0218127405013988](https://doi.org/10.1142/S0218127405013988)

Hyperchaotic Chen system x' = a(y−x)+w, y' = dx−xz+cy, z' = xy−bz, w' = yz+rw, the form in our code. Title, journal, volume, pages and DOI confirmed; author names come from memory and were not shown in the search results. Ours uses a=35, b=3, c=12, d=7, r=0.5, the values usually quoted for this system (r in roughly 0.085–0.798 is hyperchaotic); the paper itself was not opened.

```bibtex
@article{Li2005HyperChen,
  author  = {Li, Yuxia and Tang, Wallace K. S. and Chen, Guanrong},
  title   = {Generating hyperchaos via state feedback control},
  journal = {International Journal of Bifurcation and Chaos},
  volume  = {15},
  number  = {10},
  pages   = {3367--3375},
  year    = {2005},
  doi     = {10.1142/S0218127405013988}
}
```

<a id="hyper_lu_4d__euler"></a>

### Hyper-Lu (4D) (60-E)

**Equations:** ẋ = a(y − x) + w; ẏ = −xz + cy; ż = xy − bz; ẇ = xz + rw

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 36, b = 3, c = 20, r = 1.3 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 1, w\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁹ |
| L(n) | ≈ 12.1n² + 144n − 4272 |
| Gates at 64 bits | 54,668 |
| pJ/bit (32 / 64-bit) | 0.706 / 1.829 |
| Lyapunov exponent | 0.9728 (float64), 0.9473 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 13 integer bits and 51 fractional bits (resolution 2⁻⁵¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.16×10⁻¹³, max 4.27×10⁻¹³; float64: median 7.74×10⁻¹³, max 3.64×10⁻¹² |
| Circuit vs float64, one step ÷ dt | median 6.82×10⁻¹³, max 3.87×10⁻¹² |
| Netlist check | the 54,668-gate netlist (depth 361) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0262 (noise floor 0.0269) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0156 against float64 (noise floor 0.0257) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). 1 of the 3 nearby float64 starts diverged, so the noise floor uses the others; the attractor coexists with escaping orbits at this step._

#### Original reference

Chen, A., Lu, J., Lü, J., & Yu, S. (2006). Generating hyperchaotic Lü attractor via state feedback control. *Physica A: Statistical Mechanics and its Applications*, 364, 103–110. [doi:10.1016/j.physa.2005.09.039](https://doi.org/10.1016/j.physa.2005.09.039)

Introduces x' = a(y−x)+w, y' = −xz+cy, z' = xy−bz, w' = xz+rw, the form in our code. Ours uses a=36, b=3, c=20, r=1.3; these are the standard values for this system (r=1.3 is at the upper end of the hyperchaotic range commonly quoted, −0.35 < r ≤ 1.3); the paper itself was not opened.

```bibtex
@article{Chen2006HyperLu,
  author  = {Chen, Aimin and Lu, Junan and L{\"u}, Jinhu and Yu, Simin},
  title   = {Generating hyperchaotic {L\"u} attractor via state feedback control},
  journal = {Physica A: Statistical Mechanics and its Applications},
  volume  = {364},
  pages   = {103--110},
  year    = {2006},
  doi     = {10.1016/j.physa.2005.09.039}
}
```

<a id="hyper_lu_4d__rk4"></a>

### Hyper-Lu (4D) (60-R)

**Equations:** ẋ = a(y − x) + w; ẏ = −xz + cy; ż = xy − bz; ẇ = xz + rw

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 36, b = 3, c = 20, r = 1.3 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 1, w\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁷ |
| L(n) | ≈ 84.6n² + 445n + … |
| Gates at 64 bits | 349,680 |
| pJ/bit (32 / 64-bit) | 4.651 / 12.241 |
| Lyapunov exponent | 0.9885 (float64), 0.9116 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 13 integer bits and 51 fractional bits (resolution 2⁻⁵¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.20×10⁻¹⁴, max 6.16×10⁻¹⁴; float64: median 1.82×10⁻¹³, max 9.22×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 1.71×10⁻¹³, max 9.66×10⁻¹³ |
| Netlist check | the 349,680-gate netlist (depth 1,034) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0777 (noise floor 0.0398) |
| Density of x (relative Wasserstein) | 0.0443 against float64 (noise floor 0.0358) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). 1 of the 3 nearby float64 starts diverged, so the noise floor uses the others; the attractor coexists with escaping orbits at this step._

#### Original reference

Chen, A., Lu, J., Lü, J., & Yu, S. (2006). Generating hyperchaotic Lü attractor via state feedback control. *Physica A: Statistical Mechanics and its Applications*, 364, 103–110. [doi:10.1016/j.physa.2005.09.039](https://doi.org/10.1016/j.physa.2005.09.039)

Introduces x' = a(y−x)+w, y' = −xz+cy, z' = xy−bz, w' = xz+rw, the form in our code. Ours uses a=36, b=3, c=20, r=1.3; these are the standard values for this system (r=1.3 is at the upper end of the hyperchaotic range commonly quoted, −0.35 < r ≤ 1.3); the paper itself was not opened.

```bibtex
@article{Chen2006HyperLu,
  author  = {Chen, Aimin and Lu, Junan and L{\"u}, Jinhu and Yu, Simin},
  title   = {Generating hyperchaotic {L\"u} attractor via state feedback control},
  journal = {Physica A: Statistical Mechanics and its Applications},
  volume  = {364},
  pages   = {103--110},
  year    = {2006},
  doi     = {10.1016/j.physa.2005.09.039}
}
```

<a id="chen_lee__euler"></a>

### Chen-Lee (61-E)

**Equations:** ẋ = ax − yz; ẏ = by + xz; ż = cz + xy/3

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 5, b = −10, c = −0.38 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻¹⁰ |
| L(n) | ≈ 18.5n² + 134n − 6082 |
| Gates at 64 bits | 78,442 |
| pJ/bit (32 / 64-bit) | 1.097 / 3.289 |
| Lyapunov exponent | 0.3580 (float64), 0.3666 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 12 integer bits and 52 fractional bits (resolution 2⁻⁵²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.49×10⁻¹³, max 1.39×10⁻¹²; float64: median 2.96×10⁻¹³, max 1.62×10⁻¹² |
| Circuit vs float64, one step ÷ dt | median 2.27×10⁻¹³, max 1.36×10⁻¹² |
| Netlist check | the 78,442-gate netlist (depth 409) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0243 (noise floor 0.0346) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00837 against float64 (noise floor 0.0368) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Chen, H.-K., & Lee, C.-I. (2004). Anti-control of chaos in rigid body motion. *Chaos, Solitons & Fractals*, 21(4), 957–965. [doi:10.1016/j.chaos.2003.12.034](https://doi.org/10.1016/j.chaos.2003.12.034)

Original paper (rigid body with feedback gains). Ours uses a=5, b=-10, c=-0.38, the values usually quoted from this paper; not checked directly.

```bibtex
@article{ChenLee2004,
  author  = {Chen, Hsien-Keng and Lee, Ching-I},
  title   = {Anti-control of chaos in rigid body motion},
  journal = {Chaos, Solitons \& Fractals},
  year    = {2004},
  volume  = {21},
  number  = {4},
  pages   = {957--965},
  doi     = {10.1016/j.chaos.2003.12.034}
}
```

<a id="chen_lee__rk4"></a>

### Chen-Lee (61-R)

**Equations:** ẋ = ax − yz; ẏ = by + xz; ż = cz + xy/3

*Plot (not reproduced in Markdown):* x–z projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 5, b = −10, c = −0.38 |
| Initial condition | x\_0 = 1, y\_0 = 1, z\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁸ |
| L(n) | ≈ 99.8n² + 664n + … |
| Gates at 64 bits | 419,333 |
| pJ/bit (32 / 64-bit) | 5.213 / 17.201 |
| Lyapunov exponent | 0.1518 (float64), 0.1383 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 12 integer bits and 52 fractional bits (resolution 2⁻⁵²). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.70×10⁻¹⁴, max 7.37×10⁻¹⁴; float64: median 7.65×10⁻¹⁴, max 2.33×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 5.68×10⁻¹⁴, max 2.27×10⁻¹³ |
| Netlist check | the 419,333-gate netlist (depth 1,209) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0887 (noise floor 0.0942) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00263 against float64 (noise floor 0.00627) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Chen, H.-K., & Lee, C.-I. (2004). Anti-control of chaos in rigid body motion. *Chaos, Solitons & Fractals*, 21(4), 957–965. [doi:10.1016/j.chaos.2003.12.034](https://doi.org/10.1016/j.chaos.2003.12.034)

Original paper (rigid body with feedback gains). Ours uses a=5, b=-10, c=-0.38, the values usually quoted from this paper; not checked directly.

```bibtex
@article{ChenLee2004,
  author  = {Chen, Hsien-Keng and Lee, Ching-I},
  title   = {Anti-control of chaos in rigid body motion},
  journal = {Chaos, Solitons \& Fractals},
  year    = {2004},
  volume  = {21},
  number  = {4},
  pages   = {957--965},
  doi     = {10.1016/j.chaos.2003.12.034}
}
```

<a id="finance_a_0_001_b_0_2_c_1_1__euler"></a>

### Finance (62-E)

**Equations:** ẋ = z + (y − a)x; ẏ = 1 − by − x^2; ż = −x − cz

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.001, b = 0.2, c = 1.1 |
| Initial condition | x\_0 = 0.1, y\_0 = 4, z\_0 = 0.5 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁷ |
| L(n) | ≈ 16.2n² − 31.2n − 447 |
| Gates at 64 bits | 63,795 |
| pJ/bit (32 / 64-bit) | 1.056 / 2.769 |
| Lyapunov exponent | 0.0797 (float64), 0.1180 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 7 integer bits and 57 fractional bits (resolution 2⁻⁵⁷). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 3.71×10⁻¹⁶, max 6.27×10⁻¹⁶; float64: median 6.47×10⁻¹⁵, max 2.54×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 6.22×10⁻¹⁵, max 2.58×10⁻¹⁴ |
| Netlist check | the 63,795-gate netlist (depth 323) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.48 (noise floor 0.457) |
| Density of x (relative Wasserstein) | 0.0108 against float64 (noise floor 0.0243) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Ma, J.-H., & Chen, Y.-S. (2001). Study for the bifurcation topological structure and the global complicated character of a kind of nonlinear finance system (I). *Applied Mathematics and Mechanics*, 22(11), 1240–1251. [doi:10.1023/A:1016313804297](https://doi.org/10.1023/A:1016313804297)

Part I; Part II is Appl. Math. Mech. 22(12), 1375–1382, doi 10.1007/BF02435540. Page numbers differ between the English and Chinese editions. Ours uses a=0.001, b=0.2, c=1.1; not checked against the original paper.

```bibtex
@article{MaChen2001,
  author  = {Ma, Jun-hai and Chen, Yu-shu},
  title   = {Study for the bifurcation topological structure and the global complicated character of a kind of nonlinear finance system ({I})},
  journal = {Applied Mathematics and Mechanics},
  year    = {2001},
  volume  = {22},
  number  = {11},
  pages   = {1240--1251},
  doi     = {10.1023/A:1016313804297}
}
```

<a id="finance_a_0_001_b_0_2_c_1_1__rk4"></a>

### Finance (62-R)

**Equations:** ẋ = z + (y − a)x; ẏ = 1 − by − x^2; ż = −x − cz

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.001, b = 0.2, c = 1.1 |
| Initial condition | x\_0 = 0.1, y\_0 = 4, z\_0 = 0.5 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁵ |
| L(n) | ≈ 81.7n² + 721n + … |
| Gates at 64 bits | 362,948 |
| pJ/bit (32 / 64-bit) | 7.185 / 16.524 |
| Lyapunov exponent | 0.0794 (float64), 0.0867 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 7 integer bits and 57 fractional bits (resolution 2⁻⁵⁷). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 8.31×10⁻¹⁶, max 9.79×10⁻¹⁶; float64: median 1.57×10⁻¹⁵, max 6.23×10⁻¹⁵ |
| Circuit vs float64, one step ÷ dt | median 1.89×10⁻¹⁵, max 6.88×10⁻¹⁵ |
| Netlist check | the 362,948-gate netlist (depth 1,025) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0912 (noise floor 0.108) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0172 against float64 (noise floor 0.0209) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Ma, J.-H., & Chen, Y.-S. (2001). Study for the bifurcation topological structure and the global complicated character of a kind of nonlinear finance system (I). *Applied Mathematics and Mechanics*, 22(11), 1240–1251. [doi:10.1023/A:1016313804297](https://doi.org/10.1023/A:1016313804297)

Part I; Part II is Appl. Math. Mech. 22(12), 1375–1382, doi 10.1007/BF02435540. Page numbers differ between the English and Chinese editions. Ours uses a=0.001, b=0.2, c=1.1; not checked against the original paper.

```bibtex
@article{MaChen2001,
  author  = {Ma, Jun-hai and Chen, Yu-shu},
  title   = {Study for the bifurcation topological structure and the global complicated character of a kind of nonlinear finance system ({I})},
  journal = {Applied Mathematics and Mechanics},
  year    = {2001},
  volume  = {22},
  number  = {11},
  pages   = {1240--1251},
  doi     = {10.1023/A:1016313804297}
}
```

<a id="windmi_a_0_7_b_2_5__euler"></a>

### WINDMI (63-E)

**Equations:** ẋ = y; ẏ = z; ż = −az − y + b − e^x

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0254 time units, 102 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.7, b = 2.5 |
| Initial condition | x\_0 = 0, y\_0 = 0.8, z\_0 = 0 |
| Type | flow |
| Class | Transcendental |
| Scheme | Euler, dt = 2⁻⁹ |
| L(n) | ≈ 0.314n³ + 109n² − 3.49e+03n + 31499 |
| Gates at 64 bits | 334,429 |
| pJ/bit (32 / 64-bit) | 3.774 / 16.195 |
| Lyapunov exponent | 0.0738 (float64), 0.0788 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 8 integer bits and 56 fractional bits (resolution 2⁻⁵⁶). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. exp: 2^y split into integer and fractional parts, polynomial for 2^f and a barrel shifter. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 2.91×10⁻¹⁵, max 7.83×10⁻¹⁵; float64: median 1.28×10⁻¹³, max 9.07×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 1.28×10⁻¹³, max 9.09×10⁻¹³ |
| Netlist check | the 334,429-gate netlist (depth 3,092) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0671 (noise floor 0.195) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0213 against float64 (noise floor 0.0272) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Horton, W., & Doxas, I. (1998). A low-dimensional dynamical model for the solar wind driven geotail-ionosphere system. *Journal of Geophysical Research: Space Physics*, 103(A3), 4561–4572. [doi:10.1029/97JA02417](https://doi.org/10.1029/97JA02417)

The original WINDMI model is six-dimensional. The three-variable jerk form x''' = −a x'' − x' + b − eˣ used here is Sprott's reduction (J. C. Sprott, Elegant Chaos: Algebraically Simple Chaotic Flows, World Scientific, 2010). Issue number and pages are from memory; volume and DOI were confirmed. Ours uses a=0.7, b=2.5, the values Sprott gives for the jerk form (from memory, not confirmed in a source seen here).

```bibtex
@article{HortonDoxas1998,
  author  = {Horton, W. and Doxas, I.},
  title   = {A low-dimensional dynamical model for the solar wind driven geotail-ionosphere system},
  journal = {Journal of Geophysical Research: Space Physics},
  volume  = {103},
  number  = {A3},
  pages   = {4561--4572},
  year    = {1998},
  doi     = {10.1029/97JA02417}
}
```

<a id="windmi_a_0_7_b_2_5__rk4"></a>

### WINDMI (63-R)

**Equations:** ẋ = y; ẏ = z; ż = −az − y + b − e^x

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.7, b = 2.5 |
| Initial condition | x\_0 = 0, y\_0 = 0.8, z\_0 = 0 |
| Type | flow |
| Class | Transcendental |
| Scheme | RK4, dt = 2⁻⁷ |
| L(n) | ≈ 0.831n³ + 509n² + … |
| Gates at 64 bits | 1,442,498 |
| pJ/bit (32 / 64-bit) | 16.048 / 68.487 |
| Lyapunov exponent | 0.0902 (float64), 0.1027 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 8 integer bits and 56 fractional bits (resolution 2⁻⁵⁶). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. exp: 2^y split into integer and fractional parts, polynomial for 2^f and a barrel shifter. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 6.98×10⁻¹⁵, max 1.28×10⁻¹⁴; float64: median 3.07×10⁻¹⁴, max 2.14×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 3.38×10⁻¹⁴, max 2.20×10⁻¹³ |
| Netlist check | the 1,442,498-gate netlist (depth 6,261) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.139 (noise floor 0.199) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0165 against float64 (noise floor 0.0514) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Horton, W., & Doxas, I. (1998). A low-dimensional dynamical model for the solar wind driven geotail-ionosphere system. *Journal of Geophysical Research: Space Physics*, 103(A3), 4561–4572. [doi:10.1029/97JA02417](https://doi.org/10.1029/97JA02417)

The original WINDMI model is six-dimensional. The three-variable jerk form x''' = −a x'' − x' + b − eˣ used here is Sprott's reduction (J. C. Sprott, Elegant Chaos: Algebraically Simple Chaotic Flows, World Scientific, 2010). Issue number and pages are from memory; volume and DOI were confirmed. Ours uses a=0.7, b=2.5, the values Sprott gives for the jerk form (from memory, not confirmed in a source seen here).

```bibtex
@article{HortonDoxas1998,
  author  = {Horton, W. and Doxas, I.},
  title   = {A low-dimensional dynamical model for the solar wind driven geotail-ionosphere system},
  journal = {Journal of Geophysical Research: Space Physics},
  volume  = {103},
  number  = {A3},
  pages   = {4561--4572},
  year    = {1998},
  doi     = {10.1029/97JA02417}
}
```

<a id="sakarya__euler"></a>

### Sakarya (64-E)

**Equations:** ẋ = −x + y + yz; ẏ = −x − y + axz; ż = z − bxy

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0234 time units, 94 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.4, b = 0.3 |
| Initial condition | x\_0 = 1, y\_0 = −1, z\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | Euler, dt = 2⁻⁸ |
| L(n) | ≈ 22.2n² − 105n − 400 |
| Gates at 64 bits | 84,001 |
| pJ/bit (32 / 64-bit) | 1.370 / 3.678 |
| Lyapunov exponent | 0.2926 (float64), 0.6787 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 10 integer bits and 54 fractional bits (resolution 2⁻⁵⁴). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Forward Euler; multiplying by dt = 2^−k is wiring. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 7.58×10⁻¹⁵, max 3.93×10⁻¹⁴; float64: median 7.46×10⁻¹⁴, max 4.52×10⁻¹³ |
| Circuit vs float64, one step ÷ dt | median 7.11×10⁻¹⁴, max 4.55×10⁻¹³ |
| Netlist check | the 84,001-gate netlist (depth 417) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 1.32 (noise floor 0.0858) |
| Density of x (relative Wasserstein) | 2.42 against float64 (noise floor 0.0492) |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean). **The 64-bit circuit leaves the attractor:** its trajectory runs into the edge of the 10-integer-bit range (±2⁹) during the run, where float64 stays bounded, so its λ and density no longer describe the system. 1 of the 3 nearby float64 starts diverged, so the noise floor uses the others; the attractor coexists with escaping orbits at this step._

#### Original reference

Sakarya attractor. In *List of chaotic maps*. Wikipedia. Original journal source not verified. <https://en.wikipedia.org/wiki/List_of_chaotic_maps>

Web source; no journal paper found. Could not find the original paper. The name points to Sakarya University (İ. Pehlivan and Y. Uyaroğlu publish many such systems, e.g. Pehlivan & Uyaroğlu 2010, Turk. J. Elec. Eng. & Comp. Sci. 18(2), 171–184, doi:10.3906/elk-0906-67), and a 2025 IET paper credits the Sakarya system to Pehlivan, but no source seen ties our equations (x' = −x+y+yz, y' = −x−y+0.4xz, z' = z−0.3xy) to a specific paper.

```bibtex
@misc{SakaryaWeb,
  title        = {Sakarya attractor},
  howpublished = {\url{https://en.wikipedia.org/wiki/List_of_chaotic_maps}},
  note         = {Original journal source not verified}
}
```

<a id="sakarya__rk4"></a>

### Sakarya (64-R)

**Equations:** ẋ = −x + y + yz; ẏ = −x − y + axz; ż = z − bxy

*Plot (not reproduced in Markdown):* x–y projection: 4,000 consecutive points every 0.0312 time units, 125 time units after a 20-unit transient; each side from its own transient.

| Field | Value |
|---|---|
| Parameters | a = 0.4, b = 0.3 |
| Initial condition | x\_0 = 1, y\_0 = −1, z\_0 = 1 |
| Type | flow |
| Class | Polynomial |
| Scheme | RK4, dt = 2⁻⁶ |
| L(n) | ≈ 114n² − 206n + … |
| Gates at 64 bits | 445,265 |
| pJ/bit (32 / 64-bit) | 8.425 / 20.723 |
| Lyapunov exponent | 0.2233 (float64), 0.2619 (64-bit circuit), per unit time |
| Implementation | 64-bit two's-complement fixed point with 10 integer bits and 54 fractional bits (resolution 2⁻⁵⁴). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Classical fourth-order Runge–Kutta; dt/2, dt/3 and dt/6 are folded into the constants. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact ÷ dt | 64-bit circuit: median 1.75×10⁻¹⁵, max 3.84×10⁻¹⁵; float64: median 1.51×10⁻¹⁴, max 8.61×10⁻¹⁴ |
| Circuit vs float64, one step ÷ dt | median 1.42×10⁻¹⁴, max 8.53×10⁻¹⁴ |
| Netlist check | the 445,265-gate netlist (depth 1,428) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.172 (noise floor 0.179) — indistinguishable |
| Density of x (relative Wasserstein) | 0.0347 against float64 (noise floor 0.0641) — indistinguishable |

_Runs: 500 time units after a 20-unit transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Sakarya attractor. In *List of chaotic maps*. Wikipedia. Original journal source not verified. <https://en.wikipedia.org/wiki/List_of_chaotic_maps>

Web source; no journal paper found. Could not find the original paper. The name points to Sakarya University (İ. Pehlivan and Y. Uyaroğlu publish many such systems, e.g. Pehlivan & Uyaroğlu 2010, Turk. J. Elec. Eng. & Comp. Sci. 18(2), 171–184, doi:10.3906/elk-0906-67), and a 2025 IET paper credits the Sakarya system to Pehlivan, but no source seen ties our equations (x' = −x+y+yz, y' = −x−y+0.4xz, z' = z−0.3xy) to a specific paper.

```bibtex
@misc{SakaryaWeb,
  title        = {Sakarya attractor},
  howpublished = {\url{https://en.wikipedia.org/wiki/List_of_chaotic_maps}},
  note         = {Original journal source not verified}
}
```

<a id="2d_lorenz_map_a_1_25_b_0_75__map"></a>

### 2D Lorenz map (65)

**Equations:** x\_k+1 = (1 + ab)x\_k − bx\_ky\_k,   y\_k+1 = (1 − b)y\_k + bx\_k^2

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | a = 1.25, b = 0.75 |
| Initial condition | x\_0 = 0.1, y\_0 = 0.1 |
| Type | map |
| Class | Polynomial |
| Scheme | map iteration |
| L(n) | 11.5n² + 1n − 4 |
| Gates at 64 bits | 47,164 |
| pJ/bit (32 / 64-bit) | 1.626 / 3.347 |
| Lyapunov exponent | 0.3401 (float64), 0.3426 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 1.08×10⁻¹⁸, max 2.12×10⁻¹⁸; float64: median 7.32×10⁻¹⁷, max 9.92×10⁻¹⁶ |
| Circuit vs float64, one step | median 7.37×10⁻¹⁷, max 9.92×10⁻¹⁶ |
| Netlist check | the 47,164-gate netlist (depth 316) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00735 (noise floor 0.00577) |
| Density of x (relative Wasserstein) | 0.00944 against float64 (noise floor 0.00597) |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Lorenz, E. N. (1989). Computational chaos—a prelude to computational instability. *Physica D: Nonlinear Phenomena*, 35(3), 299–317. [doi:10.1016/0167-2789(89)90072-9](https://doi.org/10.1016/0167-2789(89)90072-9)

Lorenz obtained this map as the Euler discretisation (time step b) of a 2D ODE and showed chaos appearing as the step grows ('computational chaos'). Revisited by Frouzakis, Kevrekidis & Peckham (2003), Physica D 177, 101. Lorenz fixed a = 0.36 and varied the step; our a = 1.25, b = 0.75 is the value used in Sprott's catalogue, so it differs from Lorenz's.

```bibtex
@article{lorenz1989computational,
  author  = {Lorenz, Edward N.},
  title   = {Computational chaos---a prelude to computational instability},
  journal = {Physica D: Nonlinear Phenomena},
  volume  = {35},
  number  = {3},
  pages   = {299--317},
  year    = {1989},
  doi     = {10.1016/0167-2789(89)90072-9}
}
```

<a id="gumowski_mira_mu_0_7__map"></a>

### Gumowski-Mira (66)

**Equations:** x\_k+1 = y\_k + αy\_k(1 − σy\_k^2) + f(x\_k),   y\_k+1 = −x\_k + f(x\_k+1); f(x) = μx + 2(1 − μ)x^2/(1 + x^2)

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | μ = −0.7, α = 0.008, σ = 0.05 |
| Initial condition | x\_0 = 0.1, y\_0 = 0.1 |
| Type | map |
| Class | Division / square root |
| Scheme | map iteration |
| L(n) | ≈ 51.3n² − 77.7n − 2878 |
| Gates at 64 bits | 201,611 |
| pJ/bit (32 / 64-bit) | 6.175 / 14.221 |
| Lyapunov exponent | 0.1832 (float64), 0.1886 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 13 integer bits and 51 fractional bits (resolution 2⁻⁵¹). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Division: restoring division of one's-complement magnitudes. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 1.10×10⁻¹⁵, max 2.89×10⁻¹⁵; float64: median 6.63×10⁻¹⁶, max 3.25×10⁻¹⁵ |
| Circuit vs float64, one step | median 1.33×10⁻¹⁵, max 3.55×10⁻¹⁵ |
| Netlist check | the 201,611-gate netlist (depth 17,753) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.0294 (noise floor 0.00678) |
| Density of x (relative Wasserstein) | 0.00928 against float64 (noise floor 0.00441) |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Gumowski, I., & Mira, C. (1980). *Recurrences and Discrete Dynamic Systems* (Lecture Notes in Mathematics, Vol. 809). Springer, Berlin. [doi:10.1007/BFb0089135](https://doi.org/10.1007/BFb0089135)

Book source. Book (Springer lecture notes). The map arose from their earlier work at CERN on particle-accelerator dynamics. Our form x' = y + a(1 - 0.05y^2)y + f(x) with a = 0.008, mu = -0.7 is the common Sprott variant; not checked against the book.

```bibtex
@book{gumowski1980recurrences,
  author    = {Gumowski, Igor and Mira, Christian},
  title     = {Recurrences and Discrete Dynamic Systems},
  series    = {Lecture Notes in Mathematics},
  volume    = {809},
  publisher = {Springer},
  address   = {Berlin},
  year      = {1980},
  doi       = {10.1007/BFb0089135}
}
```

<a id="hopalong_a_7_17_b_8_44_c_2_56__map"></a>

### Hopalong (67)

**Equations:** x\_k+1 = y\_k − sign(x\_k) √\|bx\_k − c\|,   y\_k+1 = a − x\_k

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | a = 7.17, b = 8.44, c = 2.56 |
| Initial condition | x\_0 = 0.1, y\_0 = 0.1 |
| Type | map |
| Class | Division / square root |
| Scheme | map iteration |
| L(n) | ≈ 10.6n² − 32.8n − 539 |
| Gates at 64 bits | 40,739 |
| pJ/bit (32 / 64-bit) | 1.132 / 2.471 |
| Lyapunov exponent | 0.0633 (float64), 0.0254 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 10 integer bits and 54 fractional bits (resolution 2⁻⁵⁴). Products: radix-4 Booth multipliers that keep only the needed columns (exact floor of the product). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. Square root: restoring (digit-by-digit) square root. \|x\| in one's complement (1 ulp off for negative x). |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 2.88×10⁻¹⁶, max 4.89×10⁻¹⁶; float64: median 5.39×10⁻¹⁶, max 2.50×10⁻¹⁵ |
| Circuit vs float64, one step | median 5.55×10⁻¹⁶, max 2.50×10⁻¹⁵ |
| Netlist check | the 40,739-gate netlist (depth 7,436) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.599 (noise floor 0.363) |
| Density of x (relative Wasserstein) | 0.718 against float64 (noise floor 0.81) — indistinguishable |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Dewdney, A. K. (1986). Computer recreations: Wallpaper for the mind: computer images that are almost, but not quite, repetitive. *Scientific American*, 255(3), 14–23. [doi:10.1038/scientificamerican0986-14](https://doi.org/10.1038/scientificamerican0986-14)

Popular (magazine) source. Magazine column. The map is due to Barry Martin (Aston University, Birmingham), popularised by Dewdney; reprinted in Dewdney's The Armchair Universe (1988). Values a = 7.17, b = 8.44, c = 2.56 not found in the column or other sources; not checked.

```bibtex
@article{dewdney1986wallpaper,
  author  = {Dewdney, A. K.},
  title   = {Computer Recreations: Wallpaper for the mind: computer images that are almost, but not quite, repetitive},
  journal = {Scientific American},
  volume  = {255},
  number  = {3},
  pages   = {14--23},
  year    = {1986},
  doi     = {10.1038/scientificamerican0986-14}
}
```

<a id="clifford__map"></a>

### Clifford (68)

**Equations:** x\_k+1 = sin(ay\_k) + c cos(ax\_k),   y\_k+1 = sin(bx\_k) + d cos(by\_k)

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | a = −1.4, b = 1.6, c = 1.0, d = 0.7 |
| Initial condition | x\_0 = 0.1, y\_0 = 0.1 |
| Type | map |
| Class | Transcendental |
| Scheme | map iteration |
| L(n) | ≈ 0.708n³ + 400n² − 1.14e+04n + 111749 |
| Gates at 64 bits | 1,207,509 |
| pJ/bit (32 / 64-bit) | 25.433 / 85.831 |
| Lyapunov exponent | 0.2930 (float64), 0.2920 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 1.33×10⁻¹⁶, max 4.73×10⁻¹⁶; float64: median 1.08×10⁻¹⁶, max 4.20×10⁻¹⁶ |
| Circuit vs float64, one step | median 1.18×10⁻¹⁶, max 3.38×10⁻¹⁶ |
| Netlist check | the 1,207,509-gate netlist (depth 2,948) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00344 (noise floor 0.00643) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00513 against float64 (noise floor 0.00459) |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Bourke, P. (n.d.). *Clifford Attractors* [Web page]. paulbourke.net. Attributed to Clifford A. Pickover. <https://paulbourke.net/fractals/clifford/>

Web source; no journal paper found. Web page (no DOI). The name 'Clifford attractor' comes from Bourke's page, which attributes the map x' = sin(ay) + c cos(ax), y' = sin(bx) + d cos(by) to Clifford Pickover (see also Pickover, Chaos in Wonderland, 1994). Bourke's page itself could not be fetched here; attribution confirmed through secondary sources only. Our a = -1.4, b = 1.6, c = 1.0, d = 0.7 is the widely used example set; not checked against Bourke's page.

```bibtex
@misc{bourke_clifford,
  author       = {Bourke, Paul},
  title        = {Clifford Attractors},
  howpublished = {\url{https://paulbourke.net/fractals/clifford/}},
  note         = {Attractor attributed to Clifford A. Pickover}
}
```

<a id="de_jong__map"></a>

### De Jong (69)

**Equations:** x\_k+1 = sin(ay\_k) − cos(bx\_k),   y\_k+1 = sin(cx\_k) − cos(dy\_k)

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | a = 1.641, b = 1.902, c = 0.316, d = 1.525 |
| Initial condition | x\_0 = 0.1, y\_0 = 0.1 |
| Type | map |
| Class | Transcendental |
| Scheme | map iteration |
| L(n) | ≈ 0.869n³ + 380n² − 1.09e+04n + 107947 |
| Gates at 64 bits | 1,191,312 |
| pJ/bit (32 / 64-bit) | 24.390 / 84.293 |
| Lyapunov exponent | 0.2820 (float64), 0.2829 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 4 integer bits and 60 fractional bits (resolution 2⁻⁶⁰). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 2.48×10⁻¹⁷, max 2.04×10⁻¹⁶; float64: median 1.10×10⁻¹⁶, max 3.18×10⁻¹⁶ |
| Circuit vs float64, one step | median 1.24×10⁻¹⁶, max 5.16×10⁻¹⁶ |
| Netlist check | the 1,191,312-gate netlist (depth 2,843) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00323 (noise floor 0.00156) |
| Density of x (relative Wasserstein) | 0.00297 against float64 (noise floor 0.00252) |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Bourke, P. (1989, images updated 2014). *Peter de Jong Attractors* [Web page]. paulbourke.net. <https://paulbourke.net/fractals/peterdejong/>

Web source; no journal paper found. Web page. Bourke credits the first publication to A. K. Dewdney, Computer Recreations, Scientific American 257(1), 108 (July 1987), 'Probing the strange attractions of chaos', doi:10.1038/scientificamerican0787-108 (verified on scientificamerican.com); cite that column for a printed source. Our a = 1.641, b = 1.902, c = 0.316, d = 1.525 is the first parameter set on Bourke's page; matches.

```bibtex
@misc{bourke_dejong,
  author       = {Bourke, Paul},
  title        = {Peter de Jong Attractors},
  howpublished = {\url{https://paulbourke.net/fractals/peterdejong/}},
  year         = {1989},
  note         = {Images updated February 2014}
}
```

<a id="fractal_dream__map"></a>

### Fractal-Dream (70)

**Equations:** x\_k+1 = sin(by\_k) + c sin(bx\_k),   y\_k+1 = sin(ax\_k) + d sin(ay\_k)

*Plot (not reproduced in Markdown):* x–y attractor: 1,500 points sampled evenly over 10⁵ iterations after a 10³-step transient.

| Field | Value |
|---|---|
| Parameters | a = −0.966918, b = 2.879879, c = 0.765145, d = 0.744728 |
| Initial condition | x\_0 = 0.1, y\_0 = 0.1 |
| Type | map |
| Class | Transcendental |
| Scheme | map iteration |
| L(n) | ≈ 3.7n³ + 64.5n² − 825n + 7907 |
| Gates at 64 bits | 1,182,677 |
| pJ/bit (32 / 64-bit) | 22.965 / 82.192 |
| Lyapunov exponent | 0.3369 (float64), 0.3392 (64-bit circuit), per iteration |
| Implementation | 64-bit two's-complement fixed point with 5 integer bits and 59 fractional bits (resolution 2⁻⁵⁹). Constants: canonical signed-digit shift-and-add chains with 4 guard bits, rounded once per linear combination; non-dyadic constants come from float64, so they carry 53 significant bits. sin and cos: argument in turns, folded to a quarter turn, odd Taylor polynomial by Horner with the degree set for F + 1 bits. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 3.82×10⁻¹⁷, max 8.31×10⁻¹⁷; float64: median 8.61×10⁻¹⁷, max 4.16×10⁻¹⁶ |
| Circuit vs float64, one step | median 7.55×10⁻¹⁷, max 4.23×10⁻¹⁶ |
| Netlist check | the 1,182,677-gate netlist (depth 2,894) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 0.00678 (noise floor 0.00712) — indistinguishable |
| Density of x (relative Wasserstein) | 0.00641 against float64 (noise floor 0.00365) |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (200-digit mpmath). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Pickover, C. A. (1994). *Chaos in Wonderland: Visual Adventures in a Fractal World*. St. Martin's Press, New York. ISBN 0-312-10743-9. <https://publishersweekly.com/9780312107437>

Book source. Popular book (no DOI). The 'Fractal Dream' form x' = sin(by) + c sin(bx), y' = sin(ax) + d sin(ay) is attributed to this book by the HoloViz attractor gallery. Our a = -0.966918, b = 2.879879, c = 0.765145, d = 0.744728 come from Jason Rampe's presets (via HoloViz), not checked against the book.

```bibtex
@book{pickover1994chaos,
  author    = {Pickover, Clifford A.},
  title     = {Chaos in Wonderland: Visual Adventures in a Fractal World},
  publisher = {St. Martin's Press},
  address   = {New York},
  year      = {1994},
  isbn      = {0-312-10743-9}
}
```

<a id="mdcs_nepomuceno_et_al_2019__map"></a>

### Minimal Digital Chaotic System (MDCS) (71)

**Equations:** x\_k+1 = r · x\_k · x̄\_k,   x̄\_k = 1 − 2^−n − x\_k  (digit complement)

*Plot (not reproduced in Markdown):* Return map x(k+1) against x(k): 1,500 consecutive iterates after the 10³-step transient.

| Field | Value |
|---|---|
| Parameters | r = 4; unsigned fixed point, n fractional bits (Q0.n) |
| Initial condition | x\_0 = 0.3 |
| Type | map |
| Class | Polynomial |
| Scheme | map iteration |
| L(n) | ≈ 1.50n² + 4.7n − 26 |
| Gates at 64 bits | 6,432 |
| pJ/bit (32 / 64-bit) | 0.704 / 1.353 |
| Lyapunov exponent | 0.6931 (float64), 0.6931 (64-bit circuit), per iteration |
| Implementation | XOR-pair partial products (x\_ix̄\_j + x\_jx̄\_i = x\_i ⊕ x\_j), column compression, truncated to 2 guard columns with a bias constant; ×4 is wiring. Unsigned Q0.64. |

#### 64-bit gate level vs float64

| Metric | Value |
|---|---|
| One-step error vs exact | 64-bit circuit: median 1.47×10⁻¹⁹, max 2.63×10⁻¹⁹; float64: median 1.27×10⁻¹⁷, max 1.44×10⁻¹⁶ |
| Circuit vs float64, one step | median 1.28×10⁻¹⁷, max 1.45×10⁻¹⁶ |
| Netlist check | the 6,432-gate netlist (depth 2,169) and the integer model used for the long runs agree bit for bit on all 200 states |
| Lyapunov exponent (relative error) | 5.83×10⁻⁵ (noise floor 1.95×10⁻⁵) |
| Density of x (relative Wasserstein) | 0.00306 against float64 (noise floor 0.00538) — indistinguishable; against the exact arcsine on [0,1] density: circuit 0.00225, float64 0.00128 |

_Runs: 10⁵ iterations after a 10³-step transient; both sides use the same scheme and step. One-step errors from 200 states on the float64 attractor, against exact arithmetic (rational numbers). Noise floors: float64 against float64 from three initial conditions shifted by 10⁻⁶ to 3×10⁻⁶ (mean)._

#### Original reference

Nepomuceno, E. G., Lima, A. M., Arias-García, J., Perc, M., & Repnik, R. (2019). Minimal digital chaotic system. *Chaos, Solitons & Fractals*, 120, 62–66. [doi:10.1016/j.chaos.2019.01.019](https://doi.org/10.1016/j.chaos.2019.01.019)

```bibtex
@article{Nepomuceno2019minimal,
  author  = {Nepomuceno, Erivelton G. and Lima, Arthur M. and Arias-Garc{\'i}a, Janier and Perc, Matja{\v{z}} and Repnik, Robert},
  title   = {Minimal digital chaotic system},
  journal = {Chaos, Solitons \& Fractals},
  volume  = {120},
  pages   = {62--66},
  year    = {2019},
  doi     = {10.1016/j.chaos.2019.01.019}
}
```
