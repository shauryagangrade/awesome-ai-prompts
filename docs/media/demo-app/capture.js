const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

// Default covers the chat scene (8.4s) plus a little headroom.
const DURATION_MS = Number(process.argv[2] || 9500);

(async () => {
  const outDir = path.join(__dirname, 'out');
  fs.rmSync(outDir, { recursive: true, force: true });
  fs.mkdirSync(outDir, { recursive: true });

  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1200, height: 800 },
    recordVideo: {
      dir: outDir,
      size: { width: 1200, height: 800 },
    },
  });

  const page = await context.newPage();

  await page.goto('http://localhost:3099');

  await page.waitForTimeout(DURATION_MS);

  // Closing the context flushes Playwright's webm to disk.
  await context.close();
  await browser.close();

  const written = fs.readdirSync(outDir).filter((f) => f.endsWith('.webm'));
  console.log('Capture complete:', written.map((f) => path.join(outDir, f)).join(', '));
})();
