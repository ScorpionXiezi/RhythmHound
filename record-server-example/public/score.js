// const Vex = require("vexflow");

const Http = new XMLHttpRequest();
const url = "https://jsonplaceholder.typicode.com/posts";
Http.open("GET", url);
Http.send();

Http.onreadystatechange = e => {
  console.log(Http.responseText);
};

VF = Vex.Flow;
var WorkspaceInformation = {
  div: document.getElementById("notes"),
  canvasWidth: 1000,
  canvasHeight: 150
};
var renderer = new VF.Renderer(
  WorkspaceInformation.div,
  VF.Renderer.Backends.SVG
);
renderer.resize(
  WorkspaceInformation.canvasWidth,
  WorkspaceInformation.canvasHeight
);
var context = renderer.getContext();
context.setFont("Arial", 10, "").setBackgroundFillStyle("#eed");

var stave = new VF.Stave(10, 40, 1000);
stave.addClef("treble").addTimeSignature("4/4");
stave.setContext(context).draw();

var notes = [
  new VF.StaveNote({ clef: "treble", keys: ["c/4"], duration: "q" }),
  new VF.StaveNote({ clef: "treble", keys: ["d/4"], duration: "q" }),
  new VF.StaveNote({ clef: "treble", keys: ["b/4"], duration: "qr" }),
  new VF.StaveNote({
    clef: "treble",
    keys: ["c/4", "e/4", "g/4"],
    duration: "q"
  }),
  new VF.StaveNote({
    clef: "treble",
    keys: ["c/4", "e/4", "g/4"],
    duration: "q"
  })
];
var voice = new VF.Voice({ num_beats: 5, beat_value: 4 });
voice.addTickables(notes);

var formatter = new VF.Formatter().joinVoices([voice]).format([voice], 400);

voice.draw(context, stave);
