var IndexAPI = {
	// Auth
	checkAuth: function(login, password, quite) {
		$.ajax({
			type: 'GET',
			url: 'api/checkAuth',
			data: "login=" + login + "&password=" + password,
			success: function(data) {
				console.log(data);
				if(quite) {
					console.log("quite: " + quite);
					if(data == "True") {
						IndexUI.switchBlock("Account");
						// load account data
					} else {
						IndexUI.switchBlock("Main");
					}
				} else {
					if(data == "True") {
						Cookies.set("login", $("#MainAuthFormLoginInput").val(), {expires: 3});
						Cookies.set("password", $("#MainAuthFormPasswordInput").val(), {expires: 3});
						IndexUI.switchBlock("Account");
					} else {
						alert("Неверный логин/пароль!");
						$("#MainAuthFormLoginInput").val("");
						$("#MainAuthFormPasswordInput").val("");
					}
				}
			}
		});
	},
	// Get info
	getConfirmedReviews: function() {
		$.ajax({
			type: 'GET',
			url: 'api/getConfirmedReviews',
			data: "login=" + Cookies.get("login") + "&password=" + Cookies.get("password"),
			success: function(data) {
				console.log(data);
				for(var i=0;i<10000;i++)
					data = data.replace("'", '"');
				if(data != "err") {
					console.log("getConfirmedReviews -> OK");
					IndexUI.loadConfirmedReviews(JSON.parse(data));
				} else {
					alert("Ошибка при получении подтверждённых отзывов!");
				}
			}
		});
	},
	getNotConfirmedReviews: function() {
		$.ajax({
			type: 'GET',
			url: 'api/getNotConfirmedReviews',
			data: "login=" + Cookies.get("login") + "&password=" + Cookies.get("password"),
			success: function(data) {
				console.log(data);
				for(var i=0;i<10000;i++)
					data = data.replace("'", '"');
				if(data != "err") {
					console.log("getNotConfirmedReviews -> OK");
					IndexUI.loadNotConfirmedReviews(JSON.parse(data));
				} else {
					alert("Ошибка при получении неподтверждённых отзывов!");
				}
			}
		});
	},
	getInfoUpdateTime: function() {
		$.ajax({
			type: 'GET',
			url: 'api/getInfoUpdateTime',
			data: "login=" + Cookies.get("login") + "&password=" + Cookies.get("password"),
			success: function(data) {
				console.log(data);
				if(data != "err") {
					console.log("getInfoUpdateTime -> OK");
				} else {
					alert("Ошибка при получении информации о периоде автообновления данных!");
				}
			}
		});
	},
	getKidsFaq: function() {
		$.ajax({
			type: 'GET',
			url: 'api/getKidsFaq',
			data: "login=" + Cookies.get("login") + "&password=" + Cookies.get("password"),
			success: function(data) {
				console.log(data);
				if(data != "err") {
					console.log("getKidsFaq -> OK");
					IndexUI.loadKidsFaq(JSON.parse(data));
				} else {
					alert("Ошибка при получении информации о FAQ(Kids)!");
				}
			}
		});
	},
	getAdultFaq: function() {
		$.ajax({
			type: 'GET',
			url: 'api/getAdultFaq',
			data: "login=" + Cookies.get("login") + "&password=" + Cookies.get("password"),
			success: function(data) {
				console.log(data);
				if(data != "err") {
					console.log("getAdultFaq -> OK");
					IndexUI.loadAdultFaq(JSON.parse(data));
				} else {
					alert("Ошибка при получении информации о FAQ(Adult)!");
				}
			}
		});
	},
	getLastInfoUpdateTime: function() {
		$.ajax({
			type: 'GET',
			url: 'api/getLastInfoUpdateTime',
			data: "login=" + Cookies.get("login") + "&password=" + Cookies.get("password"),
			success: function(data) {
				console.log(data);
				if(data != "err") {
					console.log("getLastInfoUpdateTime -> OK");
					$("#LastUpdateTimeText").html(data);
				} else {
					alert("Ошибка при получении информации о FAQ(Adult)!");
				}
			}
		});
	},
	getBotStats: function() {
		$.ajax({
			type: 'GET',
			url: 'api/getBotStats',
			data: "login=" + Cookies.get("login") + "&password=" + Cookies.get("password"),
			success: function(data) {
				console.log(data);
				if(data != "err") {
					console.log("getBotStats -> OK");
					$("#BotStatsText").html("Количество запросов с момента запуска: " + data + "<br><br>Статус: неисправности отсутствуют.");
				} else {
					alert("Ошибка при получении информации о статистике бота!");
				}
			}
		});
	},
	// Set info
	setInfoUpdateTime: function(timeInSeconds) {
		$.ajax({
			type: 'GET',
			url: 'api/setInfoUpdateTime',
			data: "login=" + Cookies.get("login") + "&password=" + Cookies.get("password") + "&time=" + timeInSeconds,
			success: function(data) {
				console.log(data);
				if(data != "err") {
					alert("Период автообновления данных успешно изменён!");
				} else {
					alert("Ошибка при изменении периода автообновления данных!");
				}
			}
		});
	},
	setNewAdultFaq: function(question, answer) {
		$.ajax({
			type: 'GET',
			url: 'api/setNewAdultFaq',
			data: "login=" + Cookies.get("login") + "&password=" + Cookies.get("password") + "&question=" + question + "&answer=" + answer,
			success: function(data) {
				console.log(data);
				if(data != "err") {
					console.log("setNewFaq -> OK");
				} else {
					alert("Ошибка при изменении информации FAQ!");
				}
			}
		});
	},
	setNewKidsFaq: function(question, answer) {
		$.ajax({
			type: 'GET',
			url: 'api/setNewKidsFaq',
			data: "login=" + Cookies.get("login") + "&password=" + Cookies.get("password") + "&question=" + question + "&answer=" + answer,
			success: function(data) {
				console.log(data);
				if(data != "err") {
					console.log("setNewFaq -> OK");
				} else {
					alert("Ошибка при изменении информации FAQ!");
				}
			}
		});
	},
	acceptReview: function(reviewFileName) {
		$.ajax({
			type: 'GET',
			url: 'api/acceptReview',
			data: "login=" + Cookies.get("login") + "&password=" + Cookies.get("password") + "&name=" + reviewFileName,
			success: function(data) {
				console.log(data);
				if(data != "err") {
					console.log("acceptReview -> OK");
					IndexUI.loadAllData();
				} else {
					alert("Ошибка при одобрении отзыва!");
				}
			}
		});
	},
	declineReview: function(reviewFileName) {
		$.ajax({
			type: 'GET',
			url: 'api/declineReview',
			data: "login=" + Cookies.get("login") + "&password=" + Cookies.get("password") + "&name=" + reviewFileName,
			success: function(data) {
				console.log(data);
				if(data != "err") {
					console.log("declineReview -> OK");
					IndexUI.loadAllData();
				} else {
					alert("Ошибка при отклонении отзыва!");
				}
			}
		});
	},
}