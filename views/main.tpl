<html>
 <head>
  <title>Wavemeter Server</title>
  <script type="text/javascript" src="/static/scripts/jquery.min.js"></script>
  <script>
    $(document).ready( function() {
       $.ajax({
	       type: "GET",
	       url: "/api/wavelength/1",
	      }).done(function( msg ) {
		var text = "";
		if (msg.count > 0) {
			text = "<h3>"+msg.channels[0].wavelength +" : "+msg.status+"</h3>";
		} else {
                  text = "<h3>"+msg.status+"</h3>";
	        }
				    
		  $("#results").html(text);
                });
				   
    });
  </script>
 </head>
 <body>
 <h1>Why not??</h1>
 <div id="results"></div>
 </body>
</html>
