// Stage 9: Closed won. "Cloud Nine". A major (with borrowed F and G), 148 bpm, 4/4, 16-bar loop.
// The finale. Nine chord changes per loop, every chord voiced with its 9th, and a nine-note hook that climbs to the top.
// Trance-style rolling offbeat bass, a big pumping supersaw pad, four-on-the-floor, and a cinematic bVI-bVII lift
// (F to G) in the back half that lands home on A every time round. Triumphant, but still cool and synth-driven.
SONGS[9]={
  name:'Closed won',
  title:'Cloud Nine',
  bpm:148,
  steps:256,
  n:-1,
  // [start bar, bass root, pad voicing 57-76]: nine changes
  prog:[
    [0, 33,[57,61,64,71]],         // Aadd9      A C# E B
    [2, 37,[61,64,68,71]],         // C#m7       C# E G# B
    [4, 38,[62,66,69,73]],         // Dmaj7      D F# A C#
    [6, 35,[59,66,69,73]],         // Bm9        B F# A C#
    [8, 29,[60,64,65,69]],         // Fmaj7      C E F A
    [10,31,[59,62,64,69]],         // G6/9       B D E A
    [12,28,[59,64,69,71]],         // Esus4      B E A B  (to E on bar 2)
    [14,29,[60,65,67,69]],         // Fadd9      C F G A
    [15,31,[59,62,67,69]]          // Gadd9      B D G A
  ],
  hook:[ // lead over the whole loop: [step, midi, length]
    [0,64,2],[2,69,2],[4,71,2],[6,73,6],[12,71,2],[14,69,2],[16,71,4],[20,76,8],[28,73,4],   // the nine-note hook
    [32,68,4],[36,71,4],[40,73,8],[48,71,2],[50,68,2],[52,64,4],[56,66,8],
    [64,69,6],[70,73,2],[72,74,8],[80,73,4],[84,69,4],[88,66,8],
    [96,64,2],[98,66,2],[100,69,4],[104,73,8],[112,71,4],[116,69,2],[118,66,2],[120,64,8],
    [128,65,2],[130,69,2],[132,72,4],[136,76,12],[148,74,2],[150,72,2],[152,69,4],[156,72,4],
    [160,71,6],[166,74,2],[168,76,8],[176,74,4],[180,71,4],[184,67,8],
    [192,69,8],[200,71,4],[204,69,4],[208,68,8],[216,71,4],[220,76,4],
    [224,72,4],[228,76,4],[232,77,8],
    [240,74,4],[244,76,2],[246,74,2],[248,71,4],[252,73,4]
  ],
  // rolling bass: rest on the kick, roll the other three sixteenths (offset from root)
  bassPat:[null,0,0,12, null,0,0,12, null,0,0,12, null,0,12,7],
  chordAt:function(bar){var P=this.prog,c=P[0];for(var j=0;j<P.length;j++)if(P[j][0]<=bar)c=P[j];return c},
  play:function(i,t,d,h){
    var S=SONGS[9],bar=i>>4,s=i&15,k=h.intensity||0,C=S.chordAt(bar),r=C[1],v=C[2];
    if(i===0)S.n++;
    var loop=S.n,lift=bar>=8;
    if(bar===13)v=[59,64,68,71];                        // Esus4 resolves to E
    if(s===0&&(C[0]===bar||bar===13))h.chord(v);
    // ---- drums
    if(s%4===0)h.hit(t,'kick',.48);
    if(s===4||s===12)h.hit(t,'clap',.12);
    if(s===4||s===12)h.hit(t,'snare',.06);
    if(s%4===2)h.hit(t,'openhat',.028+k*.01);
    if(s%2===1)h.hit(t,'hat',.014+k*.01);
    if(bar===15&&s>=8)h.hit(t,'snare',.04+(s-8)*.012);  // snare roll into the top
    if(bar===7&&s>=12)h.hit(t,'tom',.16+(s-12)*.03);
    if(s===0&&(bar===0||bar===8))h.hit(t,'crash',.065);
    // ---- bass: saw roll with a sine sub under each kick
    var o=S.bassPat[s];
    if(o!==null){if(r+o>48)o=o===12?7:0;h.synth(r+o,t,d*.8,s%4===3?.11:.095,{cut:320+k*900+(s%4===3?150:0),q:8,voices:3,detune:10});}
    else h.synth(r,t,d*1.6,.06,{wave:'sine',voices:1,cut:200});
    // ---- pad: big supersaw on the pump bus, retriggered every bar so the pump breathes
    if(s===0)for(var p=0;p<4;p++)h.synth(v[p],t,d*15,.021+(lift?.004:0),{pad:true,att:.15,cut:900+k*900,q:2,voices:3,detune:14,bus:'pump',pan:[-.4,.4,-.15,.15][p]});
    // ---- arp: rising chord tones in sixteenths, folding over at the top
    var ar=[v[0],v[1],v[2],v[3],v[1]+12>79?v[1]:v[1]+12,v[3],v[2],v[1]],an=ar[s%8];
    h.synth(an,t,d*.8,.024+k*.014,{voices:1,cut:1100+k*900,q:6,bus:'fx',pan:(s%2?.35:-.35)});
    // ---- lead: the hook; doubled an octave below for weight on later loops and as intensity climbs
    var H=S.hook;
    for(var j=0;j<H.length;j++)if(H[j][0]===i){
      var n=H[j][1],L=H[j][2];
      h.synth(n,t,d*L*.95,.066,{voices:2,detune:9,cut:1500+k*600,q:4,bus:'fx',att:.01,glide:L>=8?-2:0});
      if(loop>0||k>.4)h.synth(n-12,t,d*L*.95,.035,{wave:'square',voices:1,cut:1100,q:2,bus:'fx'});
      if(lift&&k>.6&&L>=6)h.synth(n-5,t,d*L*.95,.025,{voices:1,cut:1200,q:2,bus:'fx'});   // a fourth below on the long notes
    }
    // ---- deal: a sparkling counter-arpeggio, an octave up, in eighth-note triplet feel (every 3 steps)
    if(h.deal&&i%3===0){
      var dn=v[(i/3|0)%4]+12;while(dn>79)dn-=12;
      h.synth(dn,t,d*1.2,.027,{wave:'square',voices:1,cut:2500,q:3,bus:'fx',pan:((i/3|0)%2?.5:-.5)});
    }
  }
};
