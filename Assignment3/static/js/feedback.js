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

function replace(){
	document.body.innerHTML = document.body.innerHTML.replace(/&lt;br&gt;/g, '<br>');
}

function getTime(){
	var date = new Date(); 
	var year = date.getFullYear();
	var month = date.getMonth() + 1;
	var day = date.getDay();
	document.getElementById('hiddenDate').innerHTML = 
	year+' / '+month +' / ' +day;
}
