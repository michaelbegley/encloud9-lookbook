// Stage 1: Prospecting. D minor (Aeolian with a Phrygian bII colour), 104 bpm, 4/4, 16-bar loop.
// The calmest track: half-time drums, long pads, a slow-breathing arp and a sparse lead on the back half.
SONGS[1]={
  name:'Prospecting',
  title:'First Light on the Wire',
  bpm:104,
  steps:256,
  n:0,
  // one chord per two bars: bass root, voicing (absolute MIDI, 57..76)
  ch:[
    {b:38,v:[62,65,69,72,76]},   // Dm9
    {b:34,v:[58,62,65,69,72]},   // Bbmaj9
    {b:41,v:[60,64,65,69,72]},   // Fmaj9
    {b:36,v:[60,64,67,72,74]},   // Cadd9
    {b:43,v:[58,62,65,69,74]},   // Gm9
    {b:39,v:[58,63,67,70,74]},   // Ebmaj7 (bII colour)
    {b:34,v:[58,62,65,69,72]},   // Bbmaj9
    {b:33,v:[57,62,64,67,69]}    // A7sus4 (bar 15 resolves to A7)
  ],
  a7:[57,61,64,67,69],
  // lead phrases: bar -> [[step,midi,len],...]
  back:{8:[[0,70,6],[6,69,2],[8,67,8]],9:[[0,65,4],[4,67,4],[8,69,8]],
        10:[[0,67,4],[4,70,4],[8,74,8]],11:[[0,72,6],[6,70,2],[8,67,8]],
        12:[[0,69,8],[8,65,4],[12,67,4]],13:[[0,72,8],[8,69,8]],
        14:[[0,67,6],[6,64,2],[8,62,8]],15:[[0,61,12],[12,64,4]]},
  front:{0:[[0,69,12],[12,72,4]],1:[[0,69,8],[8,65,8]],2:[[0,65,12],[12,69,4]],3:[[0,72,16]],
         4:[[0,72,6],[6,69,2],[8,67,8]],5:[[0,64,16]],6:[[0,67,8],[8,64,4],[12,62,4]],7:[[0,64,16]]},
  // keep every bass note inside MIDI 28..48: fold by octaves, and if the jump folds onto the root use the fifth instead
  bn:function(r,o){var n=r+o;while(n>48)n-=12;while(n<28)n+=12;if(n===r&&o!==0)n=(r+7>48)?r-5:r+7;return n},
  arp:[0,2,4,1,3,2,4,3],
  play:function(i,t,d,h){
    var S=SONGS[1];if(i===0)S.n++;
    var bar=i>>4,s=i&15,ci=bar>>1,I=h.intensity||0,c=S.ch[ci],v=(bar===15)?S.a7:c.v,k,p;
    // chord to the game, pad underneath
    if(s===0&&(bar%2===0||bar===15)){
      h.chord(v.slice());
      var plen=(bar>=14)?16:32;
      for(k=0;k<v.length;k++)h.synth(v[k],t,d*plen,.021,{pad:true,cut:650+650*I,att:.7,q:2,detune:12,bus:'pump',pan:(k-2)*.25});
      h.synth(c.b+12,t,d*plen,.03,{pad:true,wave:'triangle',voices:1,cut:500,att:.5,bus:'pump'}); // warm low octave
    }
    // bass: slow, thick, filtered saw
    var bp=[[0,0,6],[6,0,2],[10,0,3],[14,12,2]];
    if(I>.45)bp.push([3,0,1],[12,7,2]);
    for(k=0;k<bp.length;k++)if(bp[k][0]===s)h.synth(S.bn(c.b,bp[k][1]),t,d*bp[k][2],.1,{cut:240+420*I,q:8,detune:9});
    // drums: half time, opening up a little with intensity
    if(s===0)h.hit(t,'kick',.42);
    if(s===10)h.hit(t,'kick',.3);
    if(I>.55&&s===7&&bar%2===1)h.hit(t,'kick',.22);
    if(s===8)h.hit(t,'clap',.065);
    if(s%4===2)h.hit(t,'hat',.024);
    if(I>.6&&s%2===1)h.hit(t,'hat',.01);
    if(s===14&&bar%4===3)h.hit(t,'openhat',.03);
    if(bar===15&&(s===12||s===13||s===14))h.hit(t,'tom',.16-(s-12)*.03);
    // arp: eighths while calm, sixteenths once the pipe grows; accents every third step for a slow cross-rhythm
    var sixteenths=I>.3||S.n>2;
    if(sixteenths||s%2===0){
      k=(i+S.n*2)%8;p=v[S.arp[k]%v.length];if(p>69)p-=12;
      h.synth(p,t,d*.9,(i%3===0)?.034:.022,{voices:1,cut:600+1000*I,q:7,bus:'fx',pan:(i%2)?.3:-.3});
    }
    // lead: back half every loop, the front phrase joins from loop 2 or when intensity builds
    var ph=S.back[bar]||((S.n%2===0||I>.4)?S.front[bar]:null);
    if(ph)for(k=0;k<ph.length;k++)if(ph[k][0]===s)
      h.synth(ph[k][1],t,d*ph[k][2]*.95,.05,{voices:2,detune:10,cut:1000+500*I,q:3,att:.03,bus:'fx'});
    // deal: a soft, bright triangle counter-arp rising through the chord
    if(h.deal&&s%2===1){k=(s>>1)%v.length;h.synth(v[(k*2)%v.length],t,d*1.4,.045,{wave:'triangle',voices:1,cut:2600,q:1,bus:'fx',pan:.4})}
  }
};
