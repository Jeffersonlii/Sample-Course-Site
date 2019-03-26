$(document).ready(function(){


	//reg button
	$('#register').click(function(){
		$('.popUpReg').css('display', 'flex');
	});
	$('#register').hover(function(){
		$('#register').css("background","Silver");
	},function(){
		$('#register').css("background","white");
	})
	//close popup button
	$('#close').click(function(){
		$('.popUpReg').css('display', 'none');
	});
	$('#close').hover(function(){
		$('#close').css("background","Silver");
	},function(){
		$('#close').css("background","white");
	})
	

})