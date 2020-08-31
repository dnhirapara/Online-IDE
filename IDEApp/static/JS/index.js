/* variable declaration */
btnVal = "run";
var editor = ace.edit("editor");
var _codeLang = "c";
var ini_snip_c = "#include<stdio.h>" +
    "int main(){" +
    "return 0;" +
    "}";
/* variable declaration end */

$(document).ready(function () {
    $('#output-card').hide();
    initilizeEditor();
    sleep(2000);
});

function initilizeEditor() {
    editor = ace.edit("editor");
    editor.resize("800px");
    editor.setAutoScrollEditorIntoView(true);
    editor.renderer.setScrollMargin(10, 10, 10, 10);
    editor.setOptions({
        wrap: true,
        autoScrollEditorIntoView: true,
        copyWithEmptySelection: true,
        showInvisibles: true,
        enableLiveAutocompletion: true,
        displayIndentGuides: true,
        showPrintMargin: false,
    });
    editor.setTheme("ace/theme/twilight");
    editor.session.setMode("ace/mode/c_cpp");
    editor.setValue("//enter c code\n");
    document.getElementById("editor").style.height = "500px";
    // editor.clearSelection();
}
/* settings */

document.getElementById("font-range").addEventListener("change", function () {
    let size = this.value;
    document.getElementById("span-font-range").innerHTML = size;
    console.log(size);
    changeFontSize(size);
});

document.getElementById("text-wrap").addEventListener("change", function () {
    changeTextWrap(this.checked);
});

document.getElementById("editor_theme").addEventListener("change", function () {
    editor.setTheme("ace/theme/" + document.getElementById("editor_theme").value);
    console.log("ace/theme/" + document.getElementById("editor_theme").value);
});


function changeFontSize(size) {
    editor.setFontSize(size);
}

function changeTextWrap(flag) {
    editor.session.setUseWrapMode(flag.value);
}

function selectLang() {
    _codeLang = document.getElementById("code_lang").value;
    if (_codeLang === "c") {
        editor.session.setMode("ace/mode/c_cpp");
        editor.setValue("//enter c code");
    } else if (_codeLang === "cpp") {
        editor.session.setMode("ace/mode/c_cpp");
        editor.setValue("//enter c++ code");
    } else if (_codeLang === "py") {
        editor.session.setMode("ace/mode/python");
        editor.setValue("#enter python code");
    }
    console.log("ace/mode/" + document.getElementById("code_lang").value);
}

function setSubmit(str) {
    btnVal = str;
    console.log("submit value setted");
}
/* settings end*/

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function setBtnInactive() {
    let data = document.getElementsByTagName("button");
    for (let i of data) {
        i.disabled = true;
    }
}

function setBtnActive() {
    let data = document.getElementsByTagName("button");
    for (let i of data) {
        i.disabled = false;
    }
}

$(document).on('submit', '#ide-form', function (e) {
    document.getElementById('textarea-output').innerHTML = '';
    console.log($('#chk_input').val());
    e.preventDefault();
    console.log(document.querySelector("button[value=" + btnVal + "]"));
    let btns = document.querySelector("button[value=" + btnVal + "]");
    btns.disabled = true;
    setBtnInactive();
    let spinner = document.createElement('div');
    spinner.setAttribute("class", "spinner-border text-dark m-1 my-1 mx-1");
    spinner.width = "1rem";
    spinner.height = "1rem";
    spinner.setAttribute("role", "status");
    btns.appendChild(spinner);
    console.log('{% url ' + btnVal + ' %}');
    console.log(btnVal);
    $.ajax({
        type: 'POST',
        url: '/IDEApp/' + btnVal + '/',
        data: {
            title: "hello",
            code: editor.getValue(),
            chk_input: $('#chk_input').val(),
            codeLang: _codeLang,
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            inp: $('#id_input').val(),
            action: 'post'
        },
        success: function (json) {
            $('#output-card').show();
            $('#textarea-output').val(json.out);
            $('#textarea-output').height($('#textarea-output')[0].scrollHeight);
            $('#textarea-output').css('#output');
            btns.removeChild(spinner);
            btns.disabled = false;
            setBtnActive();
            document.getElementById("id_btns").disabled = true;
            console.log(json.out);
            $('body, html').animate({ scrollTop: $("#textarea-output").offset().top }, 1000);/* To scroll display */
        },
        error: function (xhr, errmsg, err) {
            console.log("error");
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
});

function display() {
    console.log("changed");
    var inp = document.getElementById("input");
    if (document.getElementById("chk_input").checked == true) {
        inp.style.display = "block";
    } else {
        inp.style.display = "none";
    }
}

// editor.on('change',
//     function () {
//         console.log(editor.getValue());
//         document.getElementById("id_code").innerText = editor.getValue();
//     });

// function getValue() {
//     console.log(editor.getValue());
// }


/* clock */
function startTime() {
    var today = new Date();
    var h = today.getHours();
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    document.getElementById('txt').innerHTML =
        h + ":" + m + ":" + s;
    var t = setTimeout(startTime, 500);
}
function checkTime(i) {
    if (i < 10) { i = "0" + i };  // add zero in front of numbers < 10
    return i;
}
/* clock end */