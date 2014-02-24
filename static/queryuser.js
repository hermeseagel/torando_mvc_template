function queryexist(str) {
	var email = $("#emaila").val();
	if (email.length  > 2 ) 
	 {
		$('#Loading').show();
		$.post("/checkid")
	 }
	
}