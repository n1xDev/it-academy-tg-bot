var allInfoUpdater;

$(document).ready(function() {
	// Init
	//IndexUI.switchBlock("Preload");
	IndexAPI.checkAuth(Cookies.get("login"), Cookies.get("password"), true);
	IndexUI.switchBlock("Main");
	IndexUI.loadAllData();
	initBotStatsPlot();
	// Updaters
	allInfoUpdater = setInterval(function() {
		IndexUI.loadAllData();
	}, 3000);
	// Clicks
	$(".NavbarOneBtn").click(function() {
		switch($(this).attr("id")) {
			case "NavbarMainBtn": {
				IndexUI.switchPanel("Main");
				break;
			};
			case "NavbarFaqBtn": {
				IndexUI.switchPanel("Faq");
				break;
			};
			case "NavbarReviewsBtn": {
				IndexUI.switchPanel("Reviews");
				break;
			};
			case "NavbarSettingsBtn": {
				IndexUI.switchPanel("Settings");
				break;
			};
			case "NavbarExitBtn": {
				forgetMe();
				break;
			};
			default: {
				break;
			};
		}
		IndexUI.switchNavbarBtn(this);
	});
	$("#MainAuthFormAuthBtn").click(function() {
		IndexAPI.checkAuth($("#MainAuthFormLoginInput").val(), $("#MainAuthFormPasswordInput").val(), false);
		//IndexUI.switchBlock("Account");
	});
	// FAQ
	$("#AccountFaqAdultAddNewBtn").click(function() {
		IndexAPI.setNewAdultFaq($("#AccountFaqAdultNewQuestionInput").val(), $("#AccountFaqAdultNewAnswerInput").val());
		$("#AccountFaqAdultNewQuestionInput").val("");
		$("#AccountFaqAdultNewAnswerInput").val("");
	});
	$("#AccountFaqKidsAddNewBtn").click(function() {
		IndexAPI.setNewKidsFaq($("#AccountFaqKidsNewQuestionInput").val(), $("#AccountFaqKidsNewAnswerInput").val());
		$("#AccountFaqKidsNewQuestionInput").val("");
		$("#AccountFaqKidsNewAnswerInput").val("");
	});
	// Dynamic buttons clicks
	$('body').on('click', 'button.MainDeclineReviewBtn', function() {
		console.log($(this).attr("data-reviewname"));
		IndexAPI.declineReview($(this).attr("data-reviewname"));
	});
	$('body').on('click', 'button.MainAcceptReviewBtn', function() {
		console.log($(this).attr("data-reviewname"));
		IndexAPI.acceptReview($(this).attr("data-reviewname"));
	});
	$('body').on('click', 'button.ReviewsDeclineReviewBtn', function() {
		console.log($(this).attr("data-reviewname"));
		IndexAPI.declineReview($(this).attr("data-reviewname"));
	});
	$('body').on('click', 'button.ReviewsAcceptReviewBtn', function() {
		console.log($(this).attr("data-reviewname"));
		IndexAPI.acceptReview($(this).attr("data-reviewname"));
	});
});

function forgetMe() {
	Cookies.remove("login");
	Cookies.remove("password");
	IndexUI.switchBlock("Main");
}

function initBotStatsPlot() {
	//AccountMainBotStatsPlot
}