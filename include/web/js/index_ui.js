var IndexUI = {
	// UI actions
	hideAllBlocks: function() {
		$("body").css("background-color", "white");
		$("#MainBlock").hide();
		$("#PreloadBlock").hide();
		$("#AccountBlock").hide();
	},
	hideAllPanels: function() {
		$("#AccountMainBlockElem").hide();
		$("#AccountFaqBlockElem").hide();
		$("#AccountReviewsBlockElem").hide();
		$("#AccountSettingsBlockElem").hide();
	},
	switchBlock: function(blockName) {
		this.hideAllBlocks();
		switch(blockName) {
			case "Preload": {
				$("#PreloadBlock").show();
				break;
			};
			case "Main": {
				$("body").css("background-color", "#e8e8e8");
				$("#MainBlock").show();
				break;
			};
			case "Account": {
				$("#AccountBlock").show();
				break;
			};
			default: {
				break;
			};
		}
	},
	switchPanel: function(panelName) {
		this.hideAllPanels();
		switch(panelName) {
			case "Main": {
				$("#AccountMainBlockElem").show();
				break;
			};
			case "Faq": {
				$("#AccountFaqBlockElem").show();
				break;
			};
			case "Reviews": {
				$("#AccountReviewsBlockElem").show();
				break;
			};
			case "Settings": {
				$("#AccountSettingsBlockElem").show();
				break;
			};
			default: {
				break;
			};
		}
	},
	switchNavbarBtn: function(btnElem) {
		$(".NavbarOneBtnElem").removeClass("active");
		$(btnElem).parent().addClass("active");
	},
	// Data load actions
	loadConfirmedReviews: function(dataObj) {
		$("#AccountReviewsAllConfirmedListElem").html("");
		for(var i = 0; i < dataObj.length - 1; i++) {
			$("#AccountReviewsAllConfirmedListElem").append(`<div class="OneReviewElem"><p>` + dataObj[i][0] + `</p></div>`);
		}
	},
	loadNotConfirmedReviews: function(dataObj) {
		$("#AccountMainReviewsAllNotConfirmedListElem").html("");
		$("#AccountReviewsAllNotConfirmedListElem").html("");
		if(dataObj.length == 0)
			$("#AccountMainReviewsAllNotConfirmedListElem").html("<h3>Неподтверждённых отзывов нет.</h3>");
		for(var i = 0; i < dataObj.length; i++) {
			$("#AccountMainReviewsAllNotConfirmedListElem").append(`<div class="OneReviewElem"><p>` + dataObj[i][0] + `(от: ` + dataObj[i][1] + `)</p><button data-reviewname='` + dataObj[i][2] + `' class="MainDeclineReviewBtn btn btn-danger" style="margin-right: 15px;">Отклонить</button><button data-reviewname='` + dataObj[i][2] + `' class="MainAcceptReviewBtn btn btn-success">Одобрить</button></div>`);
			$("#AccountReviewsAllNotConfirmedListElem").append(`<div class="OneReviewElem"><p>` + dataObj[i][0] + `(от: ` + dataObj[i][1] + `)</p><button data-reviewname='` + dataObj[i][2] + `' class="ReviewsDeclineReviewBtn btn btn-danger" style="margin-right: 15px;">Отклонить</button><button data-reviewname='` + dataObj[i][2] + `' class="ReviewsAcceptReviewBtn btn btn-success">Одобрить</button></div>`);
		}
	},
	loadKidsFaq: function(dataObj) {
		$("#AccountFaqKidsListElem").html("");
		for(var i = 0; i < dataObj["kids"].length; i++) {
			$("#AccountFaqKidsListElem").append(`<div class='form-group'><label>` + dataObj["kids"][i][0] + `</label><p>` + dataObj["kids"][i][1] + `</p></div>`);
		}
	},
	loadAdultFaq: function(dataObj) {
		$("#AccountFaqAdultListElem").html("");
		for(var i = 0; i < dataObj["adult"].length; i++) {
			$("#AccountFaqAdultListElem").append(`<div class='form-group'><label>` + dataObj["adult"][i][0] + `</label><p>` + dataObj["adult"][i][1] + `</p></div>`);
		}
	},
	loadUpdateTimeInfo: function(dataObj) {
		//
	},
	loadAllData: function() {
		IndexAPI.getConfirmedReviews();
		IndexAPI.getNotConfirmedReviews();
		IndexAPI.getInfoUpdateTime();
		IndexAPI.getKidsFaq();
		IndexAPI.getAdultFaq();
		IndexAPI.getLastInfoUpdateTime();
		IndexAPI.getBotStats();
	},
}