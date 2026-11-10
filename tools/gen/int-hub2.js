const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1440,height:900}});
await p.goto('file:///home/claude/lb/pages/nine-dynamics-365.html');await p.waitForTimeout(2500);
for(const i of [0,4,8,2,6]){const bb=await p.locator('.pk .cell').nth(i).boundingBox();const x=bb.x+bb.width/2,y=bb.y+bb.height/2;
await p.mouse.move(x,y,{steps:8});await p.waitForTimeout(700);
const at=await p.evaluate(([x,y])=>{const e=document.elementFromPoint(x,y);return e&&e.closest('.cell')?.getAttribute('data-k')},[x,y]);
await p.mouse.down();await p.mouse.up();await p.waitForTimeout(200);
console.log(i,'at',at,'on',await p.evaluate(()=>document.querySelector('#pick-d .pd.on').getAttribute('data-k')))}
await b.close()})();
