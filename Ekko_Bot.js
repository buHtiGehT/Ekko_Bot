var Discord = require("discord.js");

var mybot = new Discord.Client();

mybot.setStatusOnline();
mybot.setPlayingGame("Back to the Future", callback);

mybot.on("message", function(message) {
	 if(message.content === "ding"){
	 mybot.reply(message, "dong");
	 }
});


mybot.on("message", function(message){
	var ekko = Math.floor((Math.random() * 14)+1);

	if(message.content === "!Ekko"){
		if(ekko === 1){
			mybot.reply(message,"It's not how much time you have, it's how you use it");
		}
		if(ekko === 2){
			mybot.reply(message,"Welcome to Zaun!");
		}
		if(ekko === 3){
			mybot.reply(message,"Someone's day's about to get wrecked.");
		}
		if(ekko === 4){
			mybot.reply(message,"Time to start some trouble.");
		}
		if(ekko === 5){
			mybot.reply(message,"Ah.. that fresh start smell.");
		}
		if(ekko === 6){
			mybot.reply(message,"Someone's day's about to get wrecked!");
		}
		if(ekko === 7){
			mybot.reply(message,"We'll do it the hard way!");
		}
		if(ekko === 8){
			mybot.reply(message,"I could make this hurt less");
		}
		if(ekko === 9){
			mybot.reply(message,"Make me repeat myself!");
		}
		if(ekko === 10){
			mybot.reply(message,"Time is not on your side");
		}
		if(ekko === 11){
			mybot.reply(message,"Should've walked away..");
		}
		if(ekko === 12){
			mybot.reply(message,"I like HITTING you!");
		}
		if(ekko === 13){
			mybot.reply(message,"Good a time to as any to act reckless");
		}
		if(ekko === 14){
			mybot.reply(message,"Come on! Show me something new!");
		}	
	}
});


	
mybot.loginWithToken("MjE3MDM0NTI2ODQzNjAwODk4.Cpuwsw.6enEptUU9FukjKWK-Ts3ZRLzmoM");