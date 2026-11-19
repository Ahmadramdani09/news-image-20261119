// Entry program for make.fun's news-image-20261119 competition.
//
// The picture of the day lives beside this file as entry.png (a JPEG in a
// .png-named file, which the gate accepts: it tells PNG from JPEG by the
// first bytes). Grading runs this program with no network and reads only
// /output/entry.png, so the whole job is to place the image there.
//
// Locally, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync, statSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const target = join(outDir, "entry.png");

mkdirSync(outDir, { recursive: true });
copyFileSync(source, target);

const bytes = statSync(target).size;
console.log(`entry.png written to ${target} (${bytes} bytes)`);
