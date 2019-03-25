$(document).ready(function(){


	// popup reg login button
	$('#login').click(function(){
		window.location.href = "home.html";
	});
	$('#login').hover(function(){
		$('#login').css("background","Silver");
	},function(){
		$('#login').css("background","white");
	})
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

	//register button
	$('#Register').click(function(){
		$('.popUpReg').css('display', 'none');
	});
	$('#Register').hover(function(){
		$('#Register').css("background","Silver");
	},function(){
		$('#Register').css("background","white");
	})
	

})