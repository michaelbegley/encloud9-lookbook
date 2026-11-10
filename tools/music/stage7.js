// Stage 7: Contract. "Fine Print". D minor, 136 bpm, 4/4, 16-bar loop.
// Tight, mechanical and dark: a rolling 3+3+2 saw bass, a Neapolitan (Eb) turn in the second half, and a lead that only
// arrives once the deal gets serious. Section A (bars 1-8) sets the machine running, section B (bars 9-16) brings the theme.
SONGS[7]={
  name:'Contract',
  title:'Fine Print',
  bpm:136,
  steps:256,
  n:-1,
  // two bars per chord: root (bass MIDI) and pad voicing (57-76)
  prog:[
    {r:38,c:[57,62,64,65]},        // Dm(add9)  A D E F
    {r:34,c:[57,58,62,65],b7:11},        // Bbmaj7    A Bb D F
    {r:31,c:[58,62,65,69]},        // Gm9       Bb D F A
    {r:33,c:[57,62,64,69]},        // Asus4     A D E A  (resolves to A on bar 2)
    {r:38,c:[57,60,62,65]},        // Dm7       A C D F
    {r:36,c:[57,60,65,67]},        // F/C add9  A C F G
    {r:39,c:[58,62,63,67],b7:11},        // Ebmaj7    Bb D Eb G  (the dark bII turn)
    {r:33,c:[57,61,64,67]}         // A7        A C# E G
  ],
  // bass: 3+3+2 accent shape, offsets from root (12 folds to a fifth if it would leave the bass range)
  arpIdx:[0,1,2, 0,1,2, 3,2, 1,2,3, 1,2,3, 2,1],
  bassPat:[0,0,12, 0,0,12, 0,7, 0,0,12, 0,0,12, 10,12],
  theme:[ // section B lead: [step from bar 9, midi, length in steps]
    [0,69,6],[6,67,2],[8,65,4],[12,64,2],[14,65,2],
    [16,62,8],[26,64,2],[28,65,4],
    [32,67,6],[38,69,2],[40,72,8],[48,70,4],[52,69,4],[56,67,4],[60,65,4],
    [64,70,8],[72,67,4],[76,70,2],[78,72,2],[80,74,12],[92,72,2],[94,70,2],
    [96,69,4],[100,73,4],[104,76,8],[112,73,6],[118,69,2],[120,64,4],[124,61,4]
  ],
  play:function(i,t,d,h){
    var S=SONGS[7],bar=i>>4,s=i&15,P=S.prog[bar>>1],r=P.r,k=h.intensity||0;
    if(i===0)S.n++;
    var loop=S.n,secB=bar>=8;
    // chord calls: once per change, plus the Asus4 and A7 resolving to their major third on their second bar
    if(s===0&&(bar&1)===0)h.chord(P.c);
    if(s===0&&bar===7)h.chord([57,61,64,69]);
    if(s===0&&bar===15)h.chord([57,61,64,67]);
    // ---- drums
    if(s%4===0)h.hit(t,'kick',.46);
    if(s===4||s===12)h.hit(t,'clap',.11);
    if(s===12&&secB)h.hit(t+d*.5,'snare',.05);
    if(s%4===2)h.hit(t,'hat',.035);
    if(k>.35&&(s%4===1||s%4===3))h.hit(t,'hat',.012+k*.012);
    if(s===14&&(bar&1))h.hit(t,'openhat',.03);
    if((bar===7||bar===15)&&s>=12)h.hit(t,'tom',.16+(s-12)*.03);
    if(s===0&&(bar===0||bar===8))h.hit(t,'crash',.05);
    // ---- bass: thick filtered saw, filter opens with intensity, accent on the 3+3+2 heads
    var o=S.bassPat[s];if(o===10&&P.b7)o=P.b7;if(r+o>48)o=o===12?7:0;
    var acc=(s===0||s===3||s===6||s===8||s===11||s===14);
    h.synth(r+o,t,d*(acc?1.1:.7),acc?.105:.08,{cut:300+k*700+(acc?140:0),q:9,voices:3,detune:9});
    if(s===0)h.synth(r-12>=28?r-12:r,t,d*3.5,.05,{wave:'sine',voices:1,cut:200});
    // ---- pad: two-bar swells on the pump bus
    if(s===0&&(bar&1)===0)for(var p=0;p<4;p++)h.synth(P.c[p],t,d*30,.022,{pad:true,att:.35,cut:700+k*800,q:2,voices:2,detune:11,bus:'pump',pan:p%2?.3:-.3});
    // ---- arp: chord tones in 3s across the 4/4 grid, so the accent rolls round the bar
    var arpC=P.c.slice(1).concat(P.c[1]+12),ai=S.arpIdx[s];
    var an=arpC[ai];
    if(loop>0||k>.15||secB)h.synth(an,t,d*.8,.028+k*.01,{wave:'sawtooth',voices:1,cut:900+k*900,q:5,bus:'fx',pan:ai===1?.35:-.2});
    // ---- section B theme; on the first pass at low intensity only its outline plays
    if(secB){
      var full=loop>0||k>.45,rel=i-128,T=S.theme;
      for(var j=0;j<T.length;j++)if(T[j][0]===rel){
        if(full||T[j][2]>=6)h.synth(T[j][1],t,d*T[j][2]*.95,.055,{voices:2,detune:8,cut:1300+k*500,q:4,bus:'fx',att:.012});
        if(full&&k>.6)h.synth(T[j][1]-12,t,d*T[j][2]*.95,.03,{wave:'square',voices:1,cut:900,q:2,bus:'fx'});
      }
    }else if(loop>0&&(bar&1)===1&&(s===8||s===10||s===14)){
      // section A answer motif on later loops: a short falling call
      var call={8:P.c[3]+0,10:P.c[2],14:P.c[1]}[s];h.synth(call,t,d*1.6,.04,{wave:'square',voices:1,cut:1100,q:3,bus:'fx'});
    }
    // ---- deal: a bright counter-line in dotted eighths, an octave over the chord
    if(h.deal&&s%3===0&&s<15){
      var dn=P.c[(s/3+bar)%4]+12;while(dn>79)dn-=12;
      h.synth(dn,t,d*1.2,.03,{wave:'square',voices:1,cut:2400,q:3,bus:'fx',pan:(s%2?.45:-.45)});
    }
  }
};
