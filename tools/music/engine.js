/* Pipeline music engine (shared by the game and the test renderer).
   A song is a plain object in SONGS[stage]; the engine calls song.play(i, t, d, h) once per sixteenth note,
   ahead of time, on the AudioContext clock. Everything is synthesized: no audio files. */
function PipelineAudio(ac, destination){
  var A={ac:ac};
  var master=ac.createGain();master.gain.value=.8;
  var comp=ac.createDynamicsCompressor();comp.threshold.value=-14;comp.ratio.value=4;comp.attack.value=.004;comp.release.value=.2;
  master.connect(comp).connect(destination||ac.destination);
  var music=ac.createGain();music.gain.value=0;music.connect(master);             // the song (faded in and out by the game)
  var dry=ac.createGain();dry.connect(music);                                         // bus 'dry'
  var pump=ac.createGain();pump.connect(music);                                       // bus 'pump': ducks on every kick (sidechain feel)
  var dl=ac.createDelay(1),fb=ac.createGain(),wf=ac.createBiquadFilter(),wet=ac.createGain();
  dl.delayTime.value=.3;fb.gain.value=.33;wf.type='lowpass';wf.frequency.value=2400;wet.gain.value=.36;
  dl.connect(fb).connect(dl);dl.connect(wf).connect(wet).connect(music);
  var fx=ac.createGain();fx.connect(pump);fx.connect(dl);                             // bus 'fx': pumped, with echo
  var jingle=ac.createGain();jingle.gain.value=.9;jingle.connect(master);jingle.connect(dl);   // effects and fanfares, never muted with the song
  var noise=ac.createBuffer(1,ac.sampleRate,ac.sampleRate);var nd=noise.getChannelData(0);for(var i=0;i<nd.length;i++)nd[i]=Math.random()*2-1;
  var BUS={dry:dry,pump:pump,fx:fx,jingle:jingle};
  var hz=function(m){return 440*Math.pow(2,(m-69)/12)};
  var ok=function(v){return typeof v==='number'&&isFinite(v)};

  // synth(midi, time, length, volume, opts)
  // opts: wave 'sawtooth'|'square'|'triangle'|'sine' (default saw), voices 1..3 (default 2), detune cents (default 7),
  //       cut Hz (default 1400), q (default 6), pad true = slow filter opening and long release, att seconds,
  //       glide semitones (pitch slides from midi+glide to midi), bus 'dry'|'pump'|'fx'|'jingle' (default 'dry'), pan -1..1
  A.synth=function(m,t,len,vol,o){
    o=o||{};if(!ok(m)||!ok(t)||!ok(len)||!ok(vol)||len<=0)return;
    vol=Math.min(vol,.16);m=Math.max(24,Math.min(88,m));
    var f=ac.createBiquadFilter(),g=ac.createGain(),cut=o.cut||1400,att=o.att||.006,pad=!!o.pad,out=g;
    f.type='lowpass';f.Q.value=o.q==null?6:o.q;f.frequency.setValueAtTime(pad?cut*.35:cut*2.2,t);
    if(pad)f.frequency.linearRampToValueAtTime(cut,t+Math.max(.05,len*.5));else f.frequency.setTargetAtTime(cut*.5,t+.01,.08);
    g.gain.setValueAtTime(0,t);g.gain.linearRampToValueAtTime(vol,t+att);
    g.gain.setTargetAtTime(pad?vol*.8:vol*.5,t+att,.12);g.gain.setTargetAtTime(0,t+len,pad?.25:.05);
    if(o.pan&&ac.createStereoPanner){var p=ac.createStereoPanner();p.pan.value=Math.max(-1,Math.min(1,o.pan));g.connect(p);out=p}
    var n=o.voices||2,det=o.detune==null?7:o.detune,stop=t+len+(pad?1.4:.4);
    for(var v=0;v<n;v++){var x=ac.createOscillator();x.type=o.wave||'sawtooth';
      if(o.glide){x.frequency.setValueAtTime(hz(m+o.glide),t);x.frequency.exponentialRampToValueAtTime(hz(m),t+Math.min(len,.12))}else x.frequency.setValueAtTime(hz(m),t);
      x.detune.value=n===1?0:(v/(n-1)*2-1)*det;x.connect(f);x.start(t);x.stop(stop)}
    f.connect(g);out.connect(BUS[o.bus]||dry);
  };
  // hit(time, kind, volume, bus): kick, snare, clap, hat, openhat, tom, crash, riser (riser takes length via vol? no: fixed 1 bar feel)
  A.hit=function(t,kind,vol,bus){
    if(!ok(t)||!ok(vol))return;vol=Math.min(vol,.6);var b=BUS[bus]||dry;
    if(kind==='kick'||kind==='tom'){var o=ac.createOscillator(),g=ac.createGain(),hi=kind==='kick'?150:220,lo=kind==='kick'?42:90;
      o.frequency.setValueAtTime(hi,t);o.frequency.exponentialRampToValueAtTime(lo,t+.13);g.gain.setValueAtTime(vol,t);g.gain.exponentialRampToValueAtTime(.001,t+(kind==='kick'?.22:.3));
      o.connect(g).connect(b);o.start(t);o.stop(t+.35);
      if(kind==='kick'){pump.gain.cancelScheduledValues(t);pump.gain.setValueAtTime(.35,t);pump.gain.linearRampToValueAtTime(1,t+.18)}
      return}
    var s=ac.createBufferSource(),f=ac.createBiquadFilter(),g2=ac.createGain();s.buffer=noise;
    var cfg={snare:['bandpass',1800,.14],clap:['bandpass',1200,.1],hat:['highpass',7500,.035],openhat:['highpass',6500,.22],crash:['highpass',4000,1.2]}[kind]||['highpass',7000,.04];
    f.type=cfg[0];f.frequency.value=cfg[1];g2.gain.setValueAtTime(vol,t);g2.gain.exponentialRampToValueAtTime(.001,t+cfg[2]);
    if(kind==='clap'){g2.gain.setValueAtTime(vol*.6,t+.012);g2.gain.setValueAtTime(vol,t+.024)}
    s.connect(f).connect(g2).connect(b);s.start(t,Math.random()*.4);s.stop(t+cfg[2]+.05);
  };
  A.bus=BUS;A.music=music;A.master=master;
  return A;
}
