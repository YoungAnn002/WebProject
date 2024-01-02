var lastScrollTop = 0;
navbar = document.getElementById("theHeader");
window.addEventListener("scroll", function(){
    var scrollTop = window.scrollY || this.document.documentElement.scrollTop;
    if (scrollTop > lastScrollTop){
        navbar.style.top = "-130px";
    }
    else{
        navbar.style.top = "0";
    }
    lastScrollTop = scrollTop
})
