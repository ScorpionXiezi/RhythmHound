// const Vex = require("vexflow");
VF = Vex.Flow;
function httpGet() {
  const Http = new XMLHttpRequest();
  const url = "http://10.0.0.62:8000/";
  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange = e => {
    console.log(Http.responseText);
  };
}
// httpGet();

function httpPost(audio) {
  const Http = new XMLHttpRequest();
  const url = "http://10.0.0.62:8000/";
  Http.open("POST", url);
  Http.setRequestHeader("Access-Control-Allow-Origin", "*");
  Http.setRequestHeader("Access-Control-Allow-Credentials", "true");
  Http.setRequestHeader(
    "Access-Control-Allow-Methods",
    "GET,HEAD,OPTIONS,POST,PUT"
  );
  Http.setRequestHeader(
    "Access-Control-Allow-Headers",
    "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
  );
  Http.setRequestHeader("Content-Type", "multipart/form-data");

  Http.onreadystatechange = function() {
    console.log(this.readyState);
    if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
      // Request finished. Do processing here.
      console.log(Http.responseText);
    }
  };
  console.log(audio);
  Http.send(audio);
}

var json = [
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

function drawNotes(notes) {
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

  var voice = new VF.Voice({ num_beats: 5, beat_value: 4 });
  voice.addTickables(notes);

  var formatter = new VF.Formatter().joinVoices([voice]).format([voice], 400);

  voice.draw(context, stave);
}

drawNotes(json);

// while (true) {

// }

const recordAudio = () =>
  new Promise(async resolve => {
    const stream = await navigator.mediaDevices.getUserMedia({
      audio: true
    });
    const mediaRecorder = new MediaRecorder(stream);
    let audioChunks = [];

    mediaRecorder.addEventListener("dataavailable", event => {
      audioChunks.push(event.data);
    });

    const start = () => {
      audioChunks = [];
      mediaRecorder.start();
    };

    const stop = () =>
      new Promise(resolve => {
        mediaRecorder.addEventListener("stop", () => {
          const audioBlob = new Blob(audioChunks);
          const audioUrl = URL.createObjectURL(audioBlob);
          const audio = new Audio(audioUrl);
          const play = () => audio.play();
          resolve({ audioChunks, audioBlob, audioUrl, play });
        });

        mediaRecorder.stop();
      });

    resolve({ start, stop });
  });

const sleep = time => new Promise(resolve => setTimeout(resolve, time));

const recordButton = document.querySelector("#record");
const stopButton = document.querySelector("#stop");
const playButton = document.querySelector("#play");
const saveButton = document.querySelector("#save");
const savedAudioMessagesContainer = document.querySelector(
  "#saved-audio-messages"
);

let recorder;
let audio;

recordButton.addEventListener("click", async () => {
  recordButton.setAttribute("disabled", true);
  stopButton.removeAttribute("disabled");
  playButton.setAttribute("disabled", true);
  saveButton.setAttribute("disabled", true);
  if (!recorder) {
    recorder = await recordAudio();
  }
  recorder.start();
});

stopButton.addEventListener("click", async () => {
  recordButton.removeAttribute("disabled");
  stopButton.setAttribute("disabled", true);
  playButton.removeAttribute("disabled");
  saveButton.removeAttribute("disabled");
  audio = await recorder.stop();
});

playButton.addEventListener("click", () => {});

saveButton.addEventListener("click", () => {
  const reader = new FileReader();
  reader.readAsDataURL(audio.audioBlob);
  reader.onload = () => {
    console.log(reader.result);
    const base64AudioMessage = reader.result.split(",")[1];
    httpPost(reader.result);
    fetch("/messages", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: base64AudioMessage })
    }).then(res => {
      if (res.status === 201) {
        // return populateAudioMessages();
        return res;
      }
      console.log("Invalid status saving audio message: " + res.status);
    });
  };
});

// const populateAudioMessages = () => {
//   return fetch("/messages").then(res => {
//     if (res.status === 200) {
//       return res.json().then(json => {
//         json.messageFilenames.forEach(filename => {
//           let audioElement = document.querySelector(
//             `[data-audio-filename="${filename}"]`
//           );
//           if (!audioElement) {
//             audioElement = document.createElement("audio");
//             audioElement.src = `/messages/${filename}`;
//             audioElement.setAttribute("data-audio-filename", filename);
//             audioElement.setAttribute("controls", true);
//             savedAudioMessagesContainer.appendChild(audioElement);
//           }
//         });
//       });
//     }
//     console.log("Invalid status getting messages: " + res.status);
//   });
// };

// populateAudioMessages();
