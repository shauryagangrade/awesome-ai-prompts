const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({
    viewport: { width: 1200, height: 800 },
    recordVideo: {
      dir: '/Users/shwetag/Projects/awesome-ai-prompts/docs/media/demo-app/out',
      size: { width: 1200, height: 800 },
    },
  });

  const page = await context.newPage();

  await page.goto('http://localhost:3099');

  // Wait for all animations to complete
  // Scene 1: ~10.5s, transition: ~0.8s, Scene 2: ~12s
  await page.waitForTimeout(30000);

  // Close browser to finalize video
  await context.close();
  await browser.close();

  console.log('Capture complete.');
})();
