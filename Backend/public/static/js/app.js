/*  Template Name: Wozia - Minimal Portfolio & Shop Template
    Author: Pichforest  
    File Description: Main JS file of the template
*/

//  Window scroll sticky class add
function windowScroll() {
    const navbar = document.getElementById("navbar");
    if (navbar) {
        if (
            document.body.scrollTop >= 50 ||
            document.documentElement.scrollTop >= 50
        ) {
            navbar.classList.add("nav-sticky");
        } else {
            navbar.classList.remove("nav-sticky");
        }
    }
}

window.addEventListener('scroll', (ev) => {
    ev.preventDefault();
    windowScroll();
})

// feather icon
feather.replace()



//Menu Active
function getClosest(elem, selector) {
    // Element.matches() polyfill
    if (!Element.prototype.matches) {
        Element.prototype.matches =
            Element.prototype.matchesSelector ||
            Element.prototype.mozMatchesSelector ||
            Element.prototype.msMatchesSelector ||
            Element.prototype.oMatchesSelector ||
            Element.prototype.webkitMatchesSelector ||
            function (s) {
                var matches = (this.document || this.ownerDocument).querySelectorAll(s),
                    i = matches.length;
                while (--i >= 0 && matches.item(i) !== this) { }
                return i > -1;
            };
    }
    // Get the closest matching element
    for (; elem && elem !== document; elem = elem.parentNode) {
        if (elem.matches(selector)) return elem;
    }
    return null;
};
function activateMenu() {
    var menuItems = document.getElementsByClassName("sub-menu-item");
    if (menuItems) {
        var matchingMenuItem = null;
        for (var idx = 0; idx < menuItems.length; idx++) {
            if (menuItems[idx].href === window.location.href) {
                matchingMenuItem = menuItems[idx];
            }
        }
        if (matchingMenuItem) {
            matchingMenuItem.classList.add('active');
            var immediateParent = getClosest(matchingMenuItem, 'li');
            if (immediateParent) {
                immediateParent.classList.add('active');
            }
            var parent = getClosest(matchingMenuItem, '.parent-menu-item');
            if (parent) {
                parent.classList.add('active');
                var parentMenuitem = parent.querySelector('.menu-item');
                if (parentMenuitem) {
                    parentMenuitem.classList.add('active');
                }
                var parentOfParent = getClosest(parent, '.parent-parent-menu-item');
                if (parentOfParent) {
                    parentOfParent.classList.add('active');
                }
            } else {
                var parentOfParent = getClosest(matchingMenuItem, '.parent-parent-menu-item');
                if (parentOfParent) {
                    parentOfParent.classList.add('active');
                }
            }
        }
    }
}

window.onload = function loader() {
    // Menus
    activateMenu();
}
// Contact Form
$(document).ready(function(){
$('#contect_form').on('submit',function(e){
    e.preventDefault();
    $("#simple-msg").empty();
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var subject = document.getElementById("subject").value;
    var comments = document.getElementById("comments").value;
 
    console.log(name,email,subject,comments);
    document.getElementById("error-msg").style.opacity = 0;
    document.getElementById('error-msg').innerHTML = "";
    if (name == "" || name == null) {
        document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning error_message'>Please enter a name</div>";
        fadeIn();
    }
    else if (email == "" || email == null) {
        document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning error_message'>Please enter a email</div>";
        fadeIn();
    }
    else if (subject == "" || subject == null) {
        document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning error_message'>Please enter a subject</div>";
        fadeIn();
    }
    else if (comments == "" || comments == null) {
        document.getElementById('error-msg').innerHTML = "<div class='alert alert-warning error_message'>Please enter a comments</div>";
        fadeIn();
    }
    else{
     const csrftoken = document.querySelector(
        "[name=csrfmiddlewaretoken]"
    ).value;
    console.log("daaaataaaaa :::",name,email,subject,comments);
    $.ajax({
        type: "POST",
        url: "contact",
        headers: {
            "X-CSRFToken": csrftoken,
        },
        data: {
            name: name,
            email: email,
            subject: subject,
            comments:comments,
            csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
        },
        success: function (data) {
            if (data.success_message) {
                $("#contect_form").trigger("reset");

                $("#simple-msg").append("<fieldset><div id='success_page'><h5 class='text-success'>Email Sent Successfully.</h5><p>Thank you <strong>admin</strong>, your message has been submitted to us.</p></div></fieldset>");
            } else {
            }
        },
        error: function (error) {
            // handle error
        },
    });
}
});
       
}); 

function fadeIn() {
    var fade = document.getElementById("error-msg");
    var opacity = 0;
    var intervalID = setInterval(function () {
        if (opacity < 1) {
            opacity = opacity + 0.5
            fade.style.opacity = opacity;
        } else {
            clearInterval(intervalID);
        }
    }, 200);
}

// Set Default Mode
defaultMode();
function defaultMode(e) {
    if (window.localStorage.getItem('mode') == null) {
        var mode = 'light'
    }else{
        var mode = window.localStorage.getItem('mode');
    }


    if (mode == "dark") {
        var x = document.getElementById("app-css");  
        var y = document.getElementById("mode");  
        x.setAttribute('href', '../static/css/style-dark.css')
        y.setAttribute('data-class', mode)
    }else{
        var x = document.getElementById("app-css");
        var y = document.getElementById("mode");  
        x.setAttribute('href', '../static/css/style.css')
        y.setAttribute('data-class', mode)
    }    
}

// light/dark mode button
function changeMode(event) {
    var currentMode = event.currentTarget.dataset.class;
    var x = document.getElementById("app-css");
    var y = document.getElementById("mode");

    if (currentMode === "light") {
        x.setAttribute('href', '../static/css/style-dark.css');
        y.setAttribute('data-class', 'dark');
        window.localStorage.removeItem('mode');
        window.localStorage.setItem("mode", "dark");
    } else {
        x.setAttribute('href', '../static/css/style.css');
        y.setAttribute('data-class', 'light');
        window.localStorage.removeItem('mode');
        window.localStorage.setItem("mode", "light");
    }
}

// Swicher
function toggleSwitcher() {
    var i = document.getElementById('style-switcher');
    if (i.style.left === "-189px") {
        i.style.left = "-0px";
    } else {
        i.style.left = "-189px";
    }
};

function setColor(theme) {
    window.localStorage.removeItem('color');
    window.localStorage.setItem("color", theme);
    document.getElementById('color-opt').href = '../static/css/colors/' + theme + '.css';
    toggleSwitcher(false);
};

// Set Default  Color
defaultColor();
function defaultColor(e) {
    if (window.localStorage.getItem('color') == null) {
        color = 'default'
    }else{
        color = window.localStorage.getItem('color');
    }
    document.getElementById('color-opt').href = '../static/css/colors/' + color + '.css';
}