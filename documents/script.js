window.onload=function(){
	document.getElementById("button").onclick = function(){
		var user_keyWords = document.getElementById("keyWords").value.replace(/，/ig,',');   //  get raw string of input
		var year_start = document.getElementById("year_start").value;
		var year_end = document.getElementById("year_end").value;
		var language = document.getElementById("language").value;
		var smoothing = document.getElementById("smoothing").value;
		var letter = "off";
		if (document.getElementById("case_insensitive").checked)
			letter = "on";
		// change the URL of this iframe
		document.getElementById("ngrams").src = "https://books.google.com/ngrams/interactive_chart?content=" + encodeURI(user_keyWords) + "&case_insensitive=" + letter + "&year_start=" + year_start + "&year_end=" + year_end + "&corpus=" + language.toString() + "&smoothing=" + smoothing.toString();
	}
}