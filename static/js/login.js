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
	$('#newReg').hover(function(){
		$('#newReg').css("background","Silver");
	},function(){
		$('#newReg').css("background","white");
	})
	$('#login').hover(function(){
		$('#login').css("background","Silver");
	},function(){
		$('#login').css("background","white");
	})
	

})
