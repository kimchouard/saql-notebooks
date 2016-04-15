from IPython.core import display

# ================================
#    Main
# ================================

js_init = """
function getCookie(cname) {
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1);
        if (c.indexOf(name) == 0) return decodeURIComponent(c.substring(name.length,c.length));
    }
    return "";
}

var command = "sid = '" + getCookie('sid') + "'\\norg = '" + getCookie('org') + "'\\nusername = '" + getCookie('username') + "'";
console.log("Executing Command: " + command);

var kernel = IPython.notebook.kernel;
kernel.execute(command);
"""

js = display.Javascript(data=js_init)
display.display_javascript(js)