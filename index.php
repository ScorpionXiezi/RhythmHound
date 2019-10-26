<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="baidu-site-verification" content="GR6ucPEbeL" />
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <script src="https://npmcdn.com/vexflow@1.2.84/releases/vexflow-debug.js"></script>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <script src="/js/jquery.js"></script>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <link href="assets/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="css/font-awesome.min.css">
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" type="text/css" href="http://js.api.here.com/v3/3.0/mapsjs-ui.css" />
    <title>Rhythm Hunter - let's find the rhythm</title>
</head>
<body data-spy="scroll" data-target=".main-nav">
<a href= "#section-story" class = "navbar-brand" style = "white-space: normal;">🎵🎵🎵🎵</a>
<div class="container"></div>
<section id="section-story" class="section-padding">
    <div class="row">
        <div class="col-md-12 col-sm-12" style="text-align: center; margin-top:5px; padding-right: 0px;padding-left: 0px;">
            <div class="container" style = "text-align: center;">
                <div id="notes_render"></div>
            </div>
            <script type="text/javascript" src="js/map.js" charset="UTF-8" ></script>
        </div>
    </div>
</section>
<footer id="section-footer">
    <div class="container">
        <div class="row">
            <div class="col-md-12 text-center">
                <ul class="socail-link list-inline">
                    <li><a href="images/wechat.jpg"><i class="fa fa-weixin"></i></a></li>
                    <li><a href="#"><i class="fa fa-facebook"></i></a></li>
                    <li><a href="https://github.com/camppp"><i class="fa fa-github"></i></a></li>
                    <li><a href="http://www.linkedin.com/in/%E5%AE%87%E8%BD%A9-%E5%88%98-669839a5/"><i class="fa fa-linkedin"></i></a></li>
                </ul>
            </div>
        </div>
    </div>
</footer>
<!-- jQuery (necessary for Bootstrap JavaScript plugins) -->
<script src="js/jquery.js"></script>
<!-- Include all compiled plugins (below), or include individual files as needed -->
<!-- initialize jQuery Library -->
<script type="text/javascript" src="js/jquery.js"></script>
<!-- Bootstrap jQuery -->
<script type="text/javascript" src="assets/js/bootstrap.min.js"></script>
<!-- PrettyPhoto -->
<script type="text/javascript" src="js/jquery.prettyPhoto.js"></script>
<!-- Wow Animation -->
<script type="text/javascript" src="js/wow.min.js"></script>
<!-- singlepagenav -->
<script src="js/jquery.singlePageNav.js"></script>
<!-- Eeasing -->
<script type="text/javascript" src="js/jquery.easing.1.3.js"></script>
<!-- Sticky Menu -->
<script src="js/jquery.sticky.js"></script>
<script type="text/javascript" src="js/custom.js"></script>
<script>
    $(".main-nav").sticky();
</script>
<!-- Matomo -->
<script type="text/javascript">
    var _paq = _paq || [];
    /* tracker methods like "setCustomDimension" should be called before "trackPageView" */
    _paq.push(['trackPageView']);
    _paq.push(['enableLinkTracking']);
    (function() {
        var u="//lyuxuan.com/statistics/";
        _paq.push(['setTrackerUrl', u+'piwik.php']);
        _paq.push(['setSiteId', '1']);
        var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
        g.type='text/javascript'; g.async=true; g.defer=true; g.src=u+'piwik.js'; s.parentNode.insertBefore(g,s);
    })();
</script>
<script>
  VF = Vex.Flow;

  // Create an SVG renderer and attach it to the DIV element named "boo".
  var div = document.getElementById("boo")
  var renderer = new VF.Renderer(div, VF.Renderer.Backends.SVG);

  // Configure the rendering context.
  renderer.resize(500, 500);
  var context = renderer.getContext();
  context.setFont("Arial", 10, "").setBackgroundFillStyle("#eed");

  // Create a stave of width 400 at position 10, 40 on the canvas.
  var stave = new VF.Stave(10, 40, 400);

  // Add a clef and time signature.
  stave.addClef("treble").addTimeSignature("4/4");

  // Connect it to the rendering context and draw!
  stave.setContext(context).draw();

  // Create the notes
  var notes = [
      // A quarter-note C.
      new VF.StaveNote({ keys: ["c/4"], duration: "q" }),

      // A quarter-note D.
      new VF.StaveNote({ keys: ["d/4"], duration: "q" }),

      // A quarter-note rest. Note that the key (b/4) specifies the vertical
      // position of the rest.
      new VF.StaveNote({ keys: ["b/4"], duration: "qr" }),

      // A C-Major chord.
      new VF.StaveNote({ keys: ["c/4", "e/4", "g/4"], duration: "q" })
  ];

  // Create a voice in 4/4 and add above notes
  var voice = new VF.Voice({num_beats: 4,  beat_value: 4});
  voice.addTickables(notes);

  // Format and justify the notes to 400 pixels.
  var formatter = new VF.Formatter().joinVoices([voice]).format([voice], 400);

  // Render voice
  voice.draw(context, stave);

</script>
<!-- End Matomo Code -->
<script>
    new WOW().init();
</script>
</body>
</html>