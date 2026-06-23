# A1 — Qovaid (grammatika) testlari (viewer JSON)

A0 qovaid formatining aynan o'zi: har dars uchun yengil `a1_N_qovaid.json`.
Bitta `viewer.html` (repodagi mavjud) ularni o'qiydi — alohida HTML kerak emas.

## Fayllar
`a1_1_qovaid.json` … `a1_12_qovaid.json` (12 dars)

Har fayl sxemasi A0 bilan bir xil:
`{ "title", "otish": 80, "vaqt": <daqiqa>, "questions": [ { "q", "opts", "correct", "izoh" } ] }`

- `correct` — to'g'ri javob indeksi (0–3). Bu **kalit** faqat tekshirish uchun; viewer
  o'quvchi javob bergandan keyingina ishlatadi, savol matnida ko'rinmaydi.
- `izoh` — javobdan keyin chiqadigan qisqa grammatik tushuntirish.

| Dars | Savol | Vaqt (daq) | O'tish | Mavzu |
|-----:|------:|-----------:|:------:|:------|
| 1 | 25 | 25 | 80% | Ko'rsatish/kishilik olmoshlari, so'roq, salomlashish |
| 2 | 30 | 30 | 80% | Ikkilik (musanno), oila, iboralar |
| 3 | 29 | 29 | 80% | Ko'plik (jam' salim/taksir), g'ayri aqliy qoida |
| 4 | 35 | 35 | 80% | Ismiy gap (mubtado/xabar), bog'langan olmoshlar |
| 5 | 35 | 35 | 80% | O'tgan zamon, fe'liy gap, uy-joy iboralari |
| 6 | 35 | 35 | 80% | Hozirgi zamon, o'rin/vaqt zarflari, yo'nalish |
| 7 | 35 | 35 | 80% | So'roq olmoshlari, predloglar (harfi jar) |
| 8 | 35 | 35 | 80% | O'tgan zamon tuslanishi, son va ma'dud (3–10, 11–99) |
| 9 | 35 | 35 | 80% | Kelasi zamon (سـ/سوف), muzori' tuslanishi, bozor lug'ati |
| 10 | 40 | 40 | 80% | Fe'liy gap (foil/maf'ul), jar harflar, zarf, inkor |
| 11 | 40 | 40 | 80% | Ko'rsatkich olmoshlari (uzoq/yaqin), sifat-mavsuf |
| 12 | 30 | 30 | 80% | Ismut-tafzil, bog'lovchilar, buyruq/taqiq fe'llari |

Jami: **404 savol**.

## Manba va tozalash
Savollar siz bergan `a1 qovaid testlari.docx` (12 tab) dan olingan. Quyidagilar bajarildi:
- «Tab N», bo'lim sarlavhalari, AI izohlari va «Снимок экрана …jpg» havolalari olib tashlandi;
- LaTeX belgilari (`$…$`, `\leftarrow`, `\rightarrow`) tozalandi;
- lotinchada qolib ketgan arabcha so'zlar arab yozuviga o'tkazildi (masalan: Anta→أَنْتَ, Tuffah→التُّفَّاحُ, kilo→كِيلُو);
- imloviy xatolar to'g'rilandi (arabcha: مَإ→مَا, غَنِ→عَنِ; o'zbekcha: muzakkas→muzakkar, sifa-mavsuf→sifat-mavsuf va h.k.);
- to'g'ri javoblar grammatik tahlil asosida aniqlandi (8, 11, 12-darslarda docdagi kalitlardan ham foydalanildi).

## GitHub'ga qo'yish (A0 dagidek)
Bu 12 faylni `Azam2111/bayyina-test` repozitoriyasining **`testlar/`** papkasiga yuklang
(A0 qovaid fayllari yonidagi joyga). `viewer.html` allaqachon repoda — qayta yuklash shart emas.

Botdagi havola shakli:
`https://azam2111.github.io/bayyina-test/viewer.html?dars=a1_1_qovaid`
(har dars uchun `a1_2_qovaid`, `a1_3_qovaid` … deb almashtiriladi)

> Eslatma: nusxalari `_QIROAT_GENERATOR/testlar/` ichiga ham qo'yildi — A0 va boshqa
> a1 fayllari bilan birga turibdi.
