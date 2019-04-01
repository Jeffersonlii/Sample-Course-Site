function greyOut(){
	if(document.getElementById('0').value==="" ||
    document.getElementById('1').value===""||
    document.getElementById('2').value==="" ||
    document.getElementById('3').value===""){
		document.getElementById("submitButton").disabled=true;
	}
	else{
		document.getElementById("submitButton").disabled=false;
	}
}