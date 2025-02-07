// var h = new(d("WebBloksScriptTokens").WebBloksBooleanToken)(!0),
//     i = new(d("WebBloksScriptTokens").WebBloksBooleanToken)(!1),
var j = /^-?(?:0|[1-9]\d*)(?:\.\d+)?(?:[eE][+-]?\d+)?$/;

function k(a) {
    switch (a) {
    case " ":
    case "\n":
    case "\r":
    case "\t":
    case ",":
        return !0;
    default:
        return !1
    }
}

function a(a) {
    var b = a;
    a = [];
    var c = [a],
    e = 0;

    function f() {
        while (k(b[e])) e++
    }
    while (e < b.length) {
        f();
        var g = b[e];
        switch (g) {
            case "(":
                a = [];
                c.push(a);
                e++;
                break;
            case ")":
                g = c.pop();
                a = c[c.length - 1];
                if (!a) throw new Error(e, "Unexpected ')'");
                a.push(g);
                e++;
                break;
            case '"':
                g = ++e;
                var h = !1;
                while (!0) {
                    var i = b.indexOf('"', e);
                    if (i === -1) throw new Error(g, "Unterminated string");
                    var j = b.indexOf("\\", e);
                    if (i < j || j === -1) {
                    e = i;
                    break
                    }
                    e = j + 2;
                    h = !0
                }
                i = b.substring(g, e);
                a.push(h ? l(g, i) : i);
                e++;
                break;
            default:
                j = e;
                while (!0) {
                    h = b[++e];
                    if (k(h) || h === ")" || h === "(" || h === void 0) {
                    a.push(m(b.substring(j, e)));
                    break
                }
            }
        }
        if (c.length === 1) break
    }
    g = a[0];
    return g
}

function l(a, b) {
    return JSON.parse('"' + b + '"')
}

function m(a) {
    if (a === "true") return h;
    else if (a === "false") return i;
    else if (j.test(a)) {
        var b = parseFloat(a);
        if (b.toString() === a) return b // new(d("WebBloksScriptTokens").WebBloksNumberToken)(b);
        else return a // new(d("WebBloksScriptTokens").WebBloksStringToken)(a)
    }
    return a // new(d("WebBloksScriptTokens").WebBloksIdentifierToken)(a)
}

console.log(a(" (bk.action.core.TakeLast, (bk.fx.action.OpenURLInIAB, \"https:\\/\\/help.instagram.com\\/697961817256175\"), (bk.action.logging.LogEvent, \"ig_about_this_account\", \"\", (bk.action.map.Make, (bk.action.array.Make, \"target_ig_user_id\", \"event_name\", \"referer_type\", \"surface\", \"bloks_app_id\"), (bk.action.array.Make, 317404151, \"ata_help_center_click\", \"ProfileUsername\", \"Landing\", \"com.bloks.www.ig.about_this_account\"))))"))