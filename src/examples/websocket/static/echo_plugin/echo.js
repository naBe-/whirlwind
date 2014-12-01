
var log = null
var ws = null

window.onload = function() {
    log = document.getElementById('log');

    if("WebSocket" in window) {
        var loc = window.location, new_uri;
        if (loc.protocol === "https:") {
                ws_uri = "wss:";
        } else {
                ws_uri = "ws:";
        }
        ws_uri += "//"+loc.host;
        ws_uri += loc.pathname+'echows'
        var message = document.getElementById("message")
        var ws = new WebSocket(ws_uri);
        ws.onopen = function() {
            log.innerHTML += "Connection open...<br>"
        };
        ws.onmessage = function(evt) {
            log.innerHTML += evt.data+"<br>"
        };
        ws.onclose = function() {
            log.innerHTML += "Connection closed! Refresh this page to reconnect or click <a href=\"#\" onclick=\"window.location.reload()\">here</a>.<br>"
            message.style.display='none'
        };
        message.onkeydown = function(evt) {
            if(evt.keyCode == 13) {
                ws.send(message.value)
                message.value = ""
            }
        }
    } else {
        log.innerHTML = "WebSockets are not supported in your browser. This demo is useless.";
    }
}

