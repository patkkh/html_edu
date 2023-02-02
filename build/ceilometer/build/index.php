<html>
<head></head>
<script src="node_modules/jquery/dist/jquery.min.js"></script> 
<script>

var j = new Array("option1","option2","option3","option4","option5"),    
var options = '';

for (var i = 0; i < j.length; i++) {
   options += '<option value="' + j[i]+ '">' + j[i] + '</option>';
}
$("#vars").html(options);


</script>
<body>
<form>
<label for="start">Start date:</label>
<input type="date" id="start" name="trip-start"
       value="2018-07-22"
       min="2018-01-01" max="2018-12-31">
<input type="date" id="end" name="trip-end"
       value="2018-07-23"
       min="2018-01-01" max="2018-12-31">
<select id="vars"> </select> 
</form>
</body>
</html>
