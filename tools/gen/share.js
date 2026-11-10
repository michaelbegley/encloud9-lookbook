const {chromium}=require('playwright');const path=require('path');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1200,height:630}});
const root='file://'+path.resolve('.');
require('fs').writeFileSync('_share.html',`<html><head><link rel="stylesheet" href="assets/fonts/fonts.css"><style>
body{margin:0;width:1200px;height:630px;background:#355DA6;color:#fff;font-family:"Hanken Grotesk",sans-serif;display:flex;flex-direction:column;justify-content:center;padding:0 96px;box-sizing:border-box}
img{height:72px;width:auto;margin-bottom:44px;align-self:flex-start}
h1{font-size:56px;line-height:1.08;margin:0 0 28px;letter-spacing:-.015em;max-width:960px}
p{font-size:28px;margin:0;opacity:.92}</style></head><body>
<img src="assets/brand/enCloud9-wordmark-white.svg" alt="">
<h1>Dynamics 365, Copilot and Power Platform for US small businesses</h1>
<p>Microsoft Partner since 2008, Bellevue, Nebraska. 1-844-264-0729</p></body></html>`);await p.goto(root+'/_share.html');
await p.waitForTimeout(800);await p.screenshot({path:'assets/brand/share-card.png'});await b.close()})();
