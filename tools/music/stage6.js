// Stage 6: Negotiation. "Counteroffer". C minor, 134 bpm, 4/4, 16 bars.
// A (bars 0-7): Cm | Ab | Fm | G, two bars each; a low saw "offer" answered by a square "counter".
// B (bars 8-15): Eb Bb Ab Db Fm Ab Gsus G, one per bar, one long lead line over a sixteenth gallop.
SONGS[6]={
  name:'Negotiation',
  title:'Counteroffer',
  bpm:134,
  steps:256,
  play:(function(){
    var CM=[36,[60,63,67]],AB=[32,[60,63,68]],FM=[29,[60,65,68]],G=[31,[59,62,67]],
        EB=[39,[58,63,67]],BB=[34,[58,62,65]],DB=[37,[61,65,68]],GSUS=[31,[60,62,67]];
    var BARS=[CM,CM,AB,AB,FM,FM,G,G, EB,BB,AB,DB,FM,AB,GSUS,G];
    // [bar, step, midi, len, voice] voice 0 = offer (low saw), 1 = counter (square), 2 = section B lead
    var LEAD=[
      [0,0,60,3,0],[0,3,63,3,0],[0,6,67,2,0],[0,8,65,2,0],[0,10,63,2,0],[0,12,62,4,0],[1,0,63,3,0],[1,3,60,3,0],[1,6,58,2,0],[1,8,60,8,0],
      [2,0,72,3,1],[2,3,70,3,1],[2,6,68,2,1],[2,8,67,6,1],[2,14,68,2,1],[3,0,70,3,1],[3,3,72,3,1],[3,6,75,2,1],[3,8,72,8,1],
      [4,0,65,3,0],[4,3,68,3,0],[4,6,72,2,0],[4,8,70,2,0],[4,10,68,2,0],[4,12,67,4,0],[5,0,68,3,0],[5,3,65,3,0],[5,6,63,2,0],[5,8,65,8,0],
      [6,0,71,3,1],[6,3,74,3,1],[6,6,71,2,1],[6,8,67,6,1],[6,14,68,2,1],[7,0,67,3,1],[7,3,65,3,1],[7,6,62,2,1],[7,8,59,4,1],[7,12,62,4,1],
      [8,0,67,6,2],[8,6,70,4,2],[8,10,75,6,2],
      [9,0,74,6,2],[9,6,70,4,2],[9,10,65,6,2],
      [10,0,72,6,2],[10,6,68,4,2],[10,10,63,6,2],
      [11,0,65,6,2],[11,6,68,4,2],[11,10,73,6,2],
      [12,0,72,8,2],[12,8,68,4,2],[12,12,65,4,2],
      [13,0,67,4,2],[13,4,68,4,2],[13,8,72,4,2],[13,12,75,4,2],
      [14,0,74,8,2],[14,8,72,8,2],
      [15,0,71,12,2],[15,12,67,4,2]];
    var LM={};for(var k=0;k<LEAD.length;k++)LM[LEAD[k][0]*16+LEAD[k][1]]=LEAD[k];
    // sixteenth gallop: 0 rest, 1 root, 2 octave/high; accents on the beat
    var GAL=[1,1,2,1, 1,0,2,1, 1,1,2,1, 1,2,1,2];
    var n=-1;
    return function(i,t,d,h){
      if(i===0)n++;
      var bar=i>>4,s=i&15,Bc=BARS[bar],r=Bc[0],c=Bc[1],I=h.intensity||0,secB=bar>=8;
      var hiN=r+12>48?r+7:r+12;
      if(s===0&&(bar===0||BARS[bar-1]!==Bc)){
        h.chord(c);
        var len=1;while(bar+len<16&&BARS[bar+len]===Bc)len++;
        for(var v=0;v<3;v++)h.synth(c[v],t,d*16*len-d,secB?.026:.02,{pad:true,att:.2,cut:600+800*I,q:3,bus:'pump',pan:(v-1)*.6});
      }
      var intro=(n===0&&bar<2);
      // drums
      if(s%4===0)h.hit(t,'kick',.46);
      if(s===14&&(secB||I>.5))h.hit(t,'kick',.28);
      if(!intro&&(s===4||s===12)){h.hit(t,'snare',.11);h.hit(t,'clap',.06)}
      if(!intro){if(s%4===2)h.hit(t,'openhat',.03);else h.hit(t,'hat',s%2?.014:.022)}
      if(bar===15&&s>=8)h.hit(t,'snare',.04+.012*(s-8));
      if(bar===7&&s>=12)h.hit(t,'tom',.16);
      if(s===0&&(bar===8||(bar===0&&n>0)))h.hit(t,'crash',.055);
      // bass gallop (in the intro it plays on the beats only, filter closed)
      var g=GAL[s];
      if(g&&(!intro||s%4===0))h.synth(g===2?hiN:r,t,d*.75,s%4===0?.1:.075,{voices:3,detune:9,cut:(intro?260:340)+600*I+(secB?120:0),q:9});
      // offbeat stab on the chord: the push and pull of the deal
      if(!intro&&(s===3||s===10))for(var v2=0;v2<3;v2++)h.synth(c[v2],t,d*1.2,.018,{voices:2,detune:12,cut:900+700*I,q:4,bus:'fx'});
      // leads
      var L=LM[i];
      if(L){
        if(L[4]===0)h.synth(L[2],t,d*L[3]*.92,.055,{voices:3,detune:12,cut:850+450*I,q:5,att:.01,bus:'fx',pan:-.3});
        else if(L[4]===1)h.synth(L[2],t,d*L[3]*.92,.042,{wave:'square',voices:2,detune:6,cut:1300+400*I,q:3,att:.01,bus:'fx',pan:.3});
        else{h.synth(L[2],t,d*L[3]*.95,.055,{voices:3,detune:11,cut:1300+600*I,q:3,att:.02,bus:'fx',glide:L[3]>=6?-1:0});
          if(I>.5&&L[2]-12>=52)h.synth(L[2]-12,t,d*L[3]*.95,.03,{wave:'square',voices:1,cut:900,q:2,bus:'fx'});}
      }
      // section B: a quiet sixteenth arpeggio under the lead once the pipe is long
      if(secB&&I>.35){var an=[c[0],c[1],c[2],c[1]][s%4];h.synth(an,t,d*.7,.022,{voices:1,cut:1100,q:5,bus:'fx',pan:s%2?.35:-.35});}
      // deal: bright sixteenth arpeggio an octave up, rising and falling
      if(h.deal){
        var dn=[c[0]+12,c[1]+12,c[2]+12,c[1]+12,c[0]+12,c[2]+12,c[1]+12,c[2]+12][s%8];if(dn>79)dn-=12;
        if(s%4!==0)h.synth(dn,t,d*.6,.027,{wave:'square',voices:1,cut:2200,q:4,bus:'fx',pan:.5});
      }
    };
  })()
};
