// Stage 8: Closing. "Seven Signatures". F# minor, 144 bpm, 7/8 (grouped 2+2+3), 16-bar loop.
// The prog stage: everything leans forward and trips over the short bar. A 7-step bass engine, a 4-note arp that drifts
// against the 7/8 so it lands differently every bar, chord stabs, and a soaring theme in the second half that climbs
// to a C# major (dominant) turnaround which throws the loop back to the top.
SONGS[8]={
  name:'Closing',
  title:'Seven Signatures',
  bpm:144,
  steps:224,           // 16 bars of 7/8 = 16 x 14 sixteenths
  n:-1,
  prog:[
    {r:30,c:[57,61,64,68]},        // F#m9      A C# E G#
    {r:38,c:[57,62,66,73]},        // Dmaj7     A D F# C#
    {r:40,c:[59,64,66,68]},        // Eadd9     B E F# G#
    {r:37,c:[59,61,64,68]},        // C#m7      B C# E G#
    {r:30,c:[61,66,69,73]},        // F#m       C# F# A C#
    {r:35,c:[59,62,66,73]},        // Bm(add9)  B D F# C#
    {r:38,c:[62,66,68,73]},        // Dmaj7#11  D F# G# C#
    {r:37,c:[59,61,65,68]}         // C#7       B C# E# G#
  ],
  // 14-step bass figure (null = rest); 12 folds to a fifth if it would leave the bass range
  bassPat:[0,null,0,12, 0,null,12,0, 0,null,0,7,12,7],
  bassAcc:[1,0,0,0, 1,0,0,0, 1,0,0,0,1,0],
  theme:[ // section B lead, steps from bar 9 (bars are 14 steps)
    [0,69,4],[4,73,4],[8,71,3],[11,69,3],
    [14,68,4],[18,66,10],
    [28,66,4],[32,69,4],[36,74,6],
    [42,73,4],[46,71,4],[50,69,6],
    [56,68,4],[60,69,4],[64,73,6],
    [70,76,8],[78,74,6],
    [84,73,4],[88,77,4],[92,73,6],
    [98,68,4],[102,65,4],[106,61,8]
  ],
  play:function(i,t,d,h){
    var S=SONGS[8],bar=Math.floor(i/14),s=i%14,P=S.prog[bar>>1],r=P.r,k=h.intensity||0;
    if(i===0)S.n++;
    var loop=S.n,secB=bar>=8,last=(bar&1)===1;
    if(s===0&&(bar&1)===0)h.chord(P.c);
    // ---- drums: K . . . S . . . K . K . S .  (2+2+3)
    if(s===0||s===8)h.hit(t,'kick',.47);
    if(s===10&&(k>.25||secB))h.hit(t,'kick',.36);
    if(s===4||s===12)h.hit(t,'snare',.1);
    if(s===12)h.hit(t,'clap',.07);
    if(s%2===0&&s!==4&&s!==12)h.hit(t,'hat',.032);
    if(k>.3&&s%2===1)h.hit(t,'hat',.01+k*.012);
    if(s===6)h.hit(t,'openhat',.025);
    if(last&&bar%4===3&&s>=8)h.hit(t,'tom',.15+(s-8)*.025);   // fills into every 4th bar
    if(s===0&&(bar===0||bar===8))h.hit(t,'crash',.055);
    // ---- bass
    var o=S.bassPat[s];
    if(o!==null){if(r+o>48)o=o===12?7:0;if(r+o>48)o=0;
      var a=S.bassAcc[s];
      h.synth(r+o,t,d*(a?1.3:.75),a?.11:.085,{cut:280+k*800+(a?160:0),q:10,voices:3,detune:10,glide:(s===0&&bar%4===0)?-12:0});}
    if(s===0)h.synth(r,t,d*4,.05,{wave:'sine',voices:1,cut:180});
    // ---- pad
    if(s===0&&(bar&1)===0)for(var p=0;p<4;p++)h.synth(P.c[p],t,d*26,.022,{pad:true,att:.3,cut:750+k*850,q:2,voices:2,detune:12,bus:'pump',pan:p%2?.35:-.35});
    // ---- drifting arp: 4-note cycle against the 7-step bar, so it lands in a new place each bar
    var ac=[P.c[0],P.c[1],P.c[2],P.c[3]],an=ac[[0,1,2,3,2,1][i%6]];
    if(s%2===0||k>.2)h.synth(an,t,d*.85,.026+k*.012,{voices:1,cut:1000+k*1000,q:6,bus:'fx',pan:(i%2?.3:-.3)});
    // ---- chord stabs on the 3-group in section A (later loops or rising intensity)
    if(!secB&&(loop>0||k>.3)&&(s===8||s===11)&&last)
      for(var q=1;q<4;q++)h.synth(P.c[q],t,d*1.4,.022,{voices:2,detune:10,cut:1500,q:3,bus:'fx'});
    // ---- section B theme (first pass at low intensity plays only its long notes)
    if(secB){
      var full=loop>0||k>.4,rel=i-112,T=S.theme;
      for(var j=0;j<T.length;j++)if(T[j][0]===rel){
        if(full||T[j][2]>=6)h.synth(T[j][1],t,d*T[j][2]*.95,.058,{voices:2,detune:9,cut:1400+k*500,q:4,bus:'fx',att:.01,glide:T[j][2]>=8?-1:0});
        if(full&&k>.55)h.synth(T[j][1]-12,t,d*T[j][2]*.95,.032,{wave:'square',voices:1,cut:1000,q:2,bus:'fx'});
      }
    }
    // ---- deal: bright counter-line in threes (3 against 7), an octave up
    if(h.deal&&i%3===0){
      var dn=P.c[(i/3)%4|0]+12;while(dn>79)dn-=12;
      h.synth(dn,t,d*1.1,.028,{wave:'square',voices:1,cut:2400,q:3,bus:'fx',pan:(i%2?.5:-.5)});
    }
  }
};
