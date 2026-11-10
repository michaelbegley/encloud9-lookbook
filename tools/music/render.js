// Render one stage's song offline and report on it.  node /tmp/songs/render.js <stage 1-9> [seconds=32] [--deal]
// Writes $OUT (default /tmp/songs/out)/stageN.wav and .mp3, prints JSON stats. Needs PLAYWRIGHT_BROWSERS_PATH=/opt/pw-browsers.
const {chromium}=require('playwright');const fs=require('fs');const {execSync}=require('child_process');
const OUT=process.env.OUT||'/tmp/songs/out';const n=+process.argv[2],secs=+(process.argv[3]||32),deal=process.argv.includes('--deal');
(async()=>{
  const b=await chromium.launch();const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
  await p.setContent('<html><body></body></html>');
  await p.addScriptTag({content:'var SONGS={};'});
  await p.addScriptTag({path:''+require('path').join(__dirname,'engine.js')+''});
  await p.addScriptTag({path:require('path').join(__dirname,'stage'+n+'.js')});
  const r=await p.evaluate(async([n,secs,deal])=>{
    const song=SONGS[n];if(!song)return {error:'SONGS['+n+'] not defined'};
    const sr=44100,ac=new OfflineAudioContext(2,sr*(secs+2),sr),A=PipelineAudio(ac,ac.destination);A.music.gain.value=1;
    const notes={count:0,lo:999,hi:0,bad:0},chords=[];const synth=A.synth;
    const h={synth:function(m,t,len,vol,o){notes.count++;if(!isFinite(m)||!isFinite(t)||!isFinite(len)||!isFinite(vol))notes.bad++;else{notes.lo=Math.min(notes.lo,m);notes.hi=Math.max(notes.hi,m)}synth(m,t,len,vol,o)},
      hit:A.hit,chord:function(c){chords.push(c)},deal:deal,intensity:0};
    const d=15/song.bpm;let i=0,errors=[];
    for(let t=.05;t<secs;t+=d,i++){h.intensity=Math.min(1,t/secs);try{song.play(i%song.steps,t,d,h)}catch(e){errors.push(String(e));break}}
    const buf=await ac.startRendering();const a=buf.getChannelData(0),c=buf.getChannelData(1),N=a.length;
    let peak=0;for(let k=0;k<N;k++)peak=Math.max(peak,Math.abs(a[k]),Math.abs(c[k]));
    const rms=[],bright=[];for(let s=0;s+2<=secs;s+=2){let e=0,hp=0,prev=0;for(let k=s*sr;k<(s+2)*sr;k+=2){const x=a[k];e+=x*x;const y=x-prev;hp+=y*y;prev=x}rms.push(+Math.sqrt(e/sr).toFixed(3));bright.push(e?+(hp/e).toFixed(3):0)}
    // 16-bit stereo WAV, normalised to -1 dBFS
    const g=.89/Math.max(peak,1e-4),out=new DataView(new ArrayBuffer(44+N*4));const w=(o,s)=>{for(let k=0;k<s.length;k++)out.setUint8(o+k,s.charCodeAt(k))};
    w(0,'RIFF');out.setUint32(4,36+N*4,true);w(8,'WAVE');w(12,'fmt ');out.setUint32(16,16,true);out.setUint16(20,1,true);out.setUint16(22,2,true);out.setUint32(24,sr,true);out.setUint32(28,sr*4,true);out.setUint16(32,4,true);out.setUint16(34,16,true);w(36,'data');out.setUint32(40,N*4,true);
    for(let k=0;k<N;k++){out.setInt16(44+k*4,Math.max(-1,Math.min(1,a[k]*g))*32767,true);out.setInt16(46+k*4,Math.max(-1,Math.min(1,c[k]*g))*32767,true)}
    const u=new Uint8Array(out.buffer);let s2='';for(let k=0;k<u.length;k+=32768)s2+=String.fromCharCode.apply(null,u.subarray(k,k+32768));
    return {name:song.name,title:song.title,bpm:song.bpm,steps:song.steps,loopSeconds:+(song.steps*d).toFixed(2),errors,notes,chordCalls:chords.length,peakRaw:+peak.toFixed(3),rmsPer2s:rms,brightnessPer2s:bright,b64:btoa(s2)};
  },[n,secs,deal]);
  await b.close();
  if(r.b64){fs.writeFileSync(`${OUT}/stage${n}.wav`,Buffer.from(r.b64,'base64'));delete r.b64;try{execSync(`ffmpeg -y -loglevel error -i ${OUT}/stage${n}.wav -b:a 160k ${OUT}/stage${n}.mp3`)}catch(e){}}
  r.pageErrors=errs;console.log(JSON.stringify(r,null,1));
})();
