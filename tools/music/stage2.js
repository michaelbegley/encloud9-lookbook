// Stage 2: Qualifying. E minor, 114 bpm, 4/4, 16-bar loop.
// Four on the floor arrives; a plucked sixteenth bass ostinato does the sorting, offbeat chord stabs and a call-and-answer hook.
SONGS[2]={
  name:'Qualifying',
  title:'Signal Over Noise',
  bpm:114,
  steps:256,
  n:0,
  ch:[
    {b:40,v:[59,62,66,67,71]},   // Em9
    {b:36,v:[59,62,64,67,71]},   // Cmaj9
    {b:33,v:[60,62,64,67,72]},   // Am11
    {b:35,v:[59,64,66,69,71]},   // Bsus4 (bar 7 turns to B7)
    {b:43,v:[62,66,67,71,74]},   // Gmaj7
    {b:38,v:[57,62,64,66,69]},   // Dadd9
    {b:36,v:[59,64,66,67,71]},   // Cmaj7#11
    {b:33,v:[60,64,67,69,72]}    // Am9 colour (bar 15 turns to B7)
  ],
  b7:[59,63,66,69,71],
  // hook: call over bars 4-7, answer over bars 12-15
  hook:{4:[[0,64,3],[3,67,3],[6,69,2],[8,71,4],[12,69,2],[14,67,2]],5:[[0,72,6],[6,71,2],[8,69,8]],
        6:[[0,71,3],[3,69,3],[6,66,2],[8,64,4],[12,66,4]],7:[[0,63,6],[6,66,2],[8,71,8]],
        12:[[0,67,3],[3,71,3],[6,74,2],[8,71,4],[12,66,4]],13:[[0,67,8],[8,64,4],[12,66,4]],
        14:[[0,72,3],[3,71,3],[6,67,2],[8,64,8]],15:[[0,63,4],[4,66,4],[8,69,4],[12,71,4]]},
  // low counter-line on alternate loops, bars 0-3 and 8-11
  low:{0:[[0,55,8],[8,59,8]],1:[[0,57,6],[6,55,2],[8,54,8]],2:[[0,52,8],[8,55,8]],3:[[0,57,16]],
       8:[[0,55,8],[8,59,8]],9:[[0,62,6],[6,59,2],[8,57,8]],10:[[0,57,8],[8,54,8]],11:[[0,57,16]]},
  // keep every bass note inside MIDI 28..48: fold by octaves, and if the jump folds onto the root use the fifth instead
  bn:function(r,o){var n=r+o;while(n>48)n-=12;while(n<28)n+=12;if(n===r&&o!==0)n=(r+7>48)?r-5:r+7;return n},
  bass:[0,-1,12,0, -1,0,12,-1, 0,-1,12,0, 7,-1,12,0],
  play:function(i,t,d,h){
    var S=SONGS[2];if(i===0)S.n++;
    var bar=i>>4,s=i&15,ci=bar>>1,I=h.intensity||0,c=S.ch[ci],k,p;
    var v=(bar===7||bar===15)?S.b7:c.v,root=(bar===15)?35:c.b;
    if(s===0&&(bar%2===0||bar===7||bar===15)){
      h.chord(v.slice());
      var plen=(bar===6||bar===7||bar>=14)?16:32;
      for(k=0;k<v.length;k++)h.synth(v[k],t,d*plen,.016,{pad:true,cut:700+500*I,att:.4,q:2,detune:14,bus:'pump',pan:(k-2)*.25});
    }
    // bass: plucked sixteenth ostinato; eighths only while the pipe is short
    var o=S.bass[s];if(bar%4===3&&s>=12)o=[7,12,7,12][s-12];   // turnaround fill every fourth bar
    if(o>=0&&(I>.2||s%2===0||S.n>1)){
      var acc=(s%4===0)?.1:.075;
      h.synth(S.bn(root,o),t,d*.85,acc,{cut:300+700*I+(s%4===2?150:0),q:9,detune:8});
    }
    // drums
    if(s%4===0)h.hit(t,'kick',.44);
    if(s===4||s===12)h.hit(t,'clap',.075);
    h.hit(t,'hat',s%4===2?.03:.012);
    if(I>.45&&s===14)h.hit(t,'openhat',.035);
    if(bar===15&&s>=12)h.hit(t,'tom',.15-(s-12)*.025);
    if(bar===7&&s===14)h.hit(t,'snare',.05);
    // offbeat chord stabs (pumped), arrive as the pipe grows
    if((I>.25||S.n>1)&&(s===3||s===6||s===11)){
      for(k=1;k<v.length;k++)h.synth(v[k]-12>=52?v[k]-12:v[k],t,d*1.2,.017,{cut:900+900*I,q:4,voices:2,detune:10,bus:'pump'});
    }
    // hook lead
    var ph=S.hook[bar];
    if(ph)for(k=0;k<ph.length;k++)if(ph[k][0]===s)
      h.synth(ph[k][1],t,d*ph[k][2]*.92,.055,{voices:2,detune:9,cut:1100+600*I,q:4,att:.01,glide:(ph[k][2]<=3?-2:0),bus:'fx',pan:-.1});
    // low counter-line (alternate loops, or once intensity is up)
    var lo=(S.n%2===0||I>.5)?S.low[bar]:null;
    if(lo)for(k=0;k<lo.length;k++)if(lo[k][0]===s)
      h.synth(lo[k][1],t,d*lo[k][2]*.95,.04,{wave:'square',voices:1,cut:800+300*I,q:2,att:.04,bus:'fx',pan:.25});
    // deal: bright up-and-over arpeggio in sixteenths
    if(h.deal){p=v[[0,2,4,2,1,3,4,3][s%8]];h.synth(p+(s>=8&&p<67?12:0),t,d*.8,.03,{wave:'square',voices:1,cut:2600,q:2,bus:'fx',pan:.45})}
  }
};
