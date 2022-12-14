$(".nav_search-btn").click(
    function () {
    if ($(".nav_search-input").hasClass("d-none")) {
        event.preventDefault();
        $(".nav_search-input")
            .animate({
                left: "-1000px"
            },
                "1000000"
            )
            .removeClass("d-none");
    }
    else {
        $(".nav_search-input")
            .animate({
                left: "0px"
            },
                "1000000"
            )
            .addClass("d-none");
    }
});