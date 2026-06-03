# Young Docents of the Southern Branch · 南院小小英語導覽員

A place-based **bilingual course** (English primary, Chinese supplementary) for the English teachers and students of **嘉義縣立永慶高級中學 · Yung Ching Senior High School (YCSH)** in Taibao City, Chiayi County.

The course turns the **National Palace Museum · Southern Branch** — the world-class Asian art museum a few minutes from the school — into an English classroom. Students train to give a **2-minute English gallery tour**, lesson by lesson, gallery by gallery.

Built and donated by [My Culture Connect 人師教育協會](https://www.mycultureconnect.org/), a Taiwanese non-profit. It also serves as a **live demo of "making bilingual teaching materials with AI"** for a teacher workshop at the school.

**Live**: <https://lukelin7429.github.io/ycsh-bilingual/>

## Pages

| URL | Lesson | Gallery / theme |
|---|---|---|
| `/` | Course Home | Hero, course intro, the five-step lesson model, the 8-lesson map, a "made-with-AI" note for teachers, museum + school info |
| `/welcome/` | L1 · Welcome to the Southern Branch | Orientation; what an Asian art museum is; basic museum & welcome English |
| `/building/` | L2 · Reading the Building | Kris Yao's calligraphy architecture — solid ink / flying white / wash; dragon·elephant·horse = China·India·Persia |
| `/blue-and-white/` | L3 · Blue-and-White | 青花 ceramics — cobalt, glaze, firing, Asian trade |
| `/textiles/` | L4 · Threads of Splendour | 至極富麗 textiles — silk, embroidery, motifs as meaning |
| `/tea/` | L5 · The Art of Tea | 東亞茶文化 — ritual, utensils, the senses |
| `/buddha/` | L6 · Images of the Buddha | 亞洲佛教藝術 — sculpture, posture/mudra, respectful guiding |
| `/wisdom-craft/` | L7 · Wisdom & Craft | 生命的指南 classics + 近代亞洲工藝 — exchange & connection |
| `/docent/` | L8 · Become a Young Docent | Capstone: a 5-step frame + rubric for a 2-minute English tour |

Every lesson uses the same five blocks: **Read** (bilingual story) → **Word of the Day** (vocab with 🔊) → **Docent Phrase Bank** (guiding lines with 🔊) → **Quick Check** (English-only quiz) → **Your Turn** (a short task).

## Build

Static HTML generated from one template + per-lesson content:

```bash
python3 build.py        # regenerates index.html + the 8 lesson folders
```

To add or change a lesson, edit the `LESSONS` list in `build.py` and rebuild. Swap the content for a different landmark and the same machine produces a new course — that is the workshop's point.

## Design

- **Primary**: ink charcoal `#23262b` — the museum's calligraphic "ink-wash" architecture (solid ink / flying white / wash)
- **Accent**: cinnabar seal red `#b5392e` — the red signature seal on an ink painting
- **Type**: Playfair Display (English display) + Lato (English body) + PingFang TC (Chinese)
- **Background**: pure white throughout
- **Pattern**: inline single-page per lesson — no click-outs, no popups; 🔊 pronunciation via the Web Speech API; self-made quiz (no third-party forms)
- Deliberately distinct from the sister cross-county sites: Taibao Elementary ink-blue `#1F3A5F` · Taibao JHS garnet `#7A2A3A` · KangLang Elementary coastal-teal `#1E5963`

## Assets still needed

See `photos/README.md`. Heroes currently render as ink-wash gradients (no broken images). Pending confirmation:

- **Gallery photos** — the museum's images are copyrighted; confirm licensing with NPM Southern Branch, or keep the text-and-gradient treatment and have students observe on site.
- **Course fit** — which class slot this runs in (bilingual experimental class / international education / self-directed learning / club).
- **Field visit** — whether students can rehearse a live tour at the museum (walking distance).

## To bind a custom domain (when the school is ready)

GitHub Pages serves this at `lukelin7429.github.io/ycsh-bilingual/`. To put it on a domain the school controls:

1. Use a **subdomain** (e.g. `bilingual.<domain>`), **not** an apex/naked domain — subdomains provision their HTTPS certificate cleanly on GitHub Pages.
2. In the school's DNS console, add a `CNAME` record pointing the chosen hostname to `lukelin7429.github.io`.
3. Add a `CNAME` file (one line: the hostname) to the repo root and set the custom domain in **Settings → Pages**. Wait for the certificate before enforcing HTTPS.
