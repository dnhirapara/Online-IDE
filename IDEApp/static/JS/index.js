btnVal = "run";


var editor = ace.edit("editor");
editor.resize();
// editor.setOption("maxLines", 100);
editor.setAutoScrollEditorIntoView(true);
editor.renderer.setScrollMargin(10, 10, 10, 10);
// editor.setOption("maxLines", 15);

editor.setOptions({
    wrap: true,
    autoScrollEditorIntoView: true,
    copyWithEmptySelection: true,
    showInvisibles: true,
    enableLiveAutocompletion: true,
    displayIndentGuides: true,
    showPrintMargin: false, // hides the vertical limiting strip
    // maxLines: Infinity,
});
editor.setTheme("ace/theme/twilight");
editor.session.setMode("ace/mode/c_cpp");
// editor.session.setOption("wrap", true);
document.getElementById("editor_theme").addEventListener("change", function () {
    editor.setTheme("ace/theme/" + document.getElementById("editor_theme").value);
    console.log("ace/theme/" + document.getElementById("editor_theme").value);
});
function selectLang() {
    editor.session.setMode("ace/mode/" + document.getElementById("code_lang").value);
    console.log("ace/mode/" + document.getElementById("code_lang").value);
}

function setSubmit(str) {
    btnVal = str;
    console.log("submit value setted");
}

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
    document.getElementById('output').innerHTML = '';
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
        // url: '{% url "run" %}',
        url: '/IDEApp/' + btnVal + '/',
        data: {
            title: "hello", //$('#id_title').val(),
            code: editor.getValue(),
            chk_input: $('#chk_input').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            inp: $('#id_input').val(),
            action: 'post'
        },
        success: function (json) {
            // $("#output").prepend('<div class="col-md-6">' +
            //     '<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">' +
            //     '<div class="col p-4 d-flex flex-column position-static">' +
            //     '<p class="mb-auto">' + json.out + '</p>' +
            //     '</div>' +
            //     '</div>' +
            //     '</div>'
            // );
            $('#output').val(json.out);
            btns.removeChild(spinner);
            btns.disabled = false;
            setBtnActive();
            document.getElementById("id_btns").disabled = true;
            // $('#output').innerText = "// $('#output').prepend('<div class='col-md-6'>" +
            //     "//     '<div class=/row no-gutters border rounded overflow-hidden flex-md-row /mb-4 shadow-sm h-md-250 position-relative/>' +" +
            //     "//     '<div class='col p-4 d-flex flex-column position-static'>' +" +
            //     "//     '<p class='mb-auto'>' + json.out + '<//p>' +" +
            //     "//     '</div>' +" +
            //     "//     '</div>' +" +
            //     "//     '</div>'+" +
            //     "// )";
            console.log(json.out);
        },
        error: function (xhr, errmsg, err) {
            console.log("error");
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
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

// document.getElementById("editor").innerText = code;
editor.on('change',
    function () {
        console.log(editor.getValue());
        document.getElementById("id_code").innerText = editor.getValue();
    });

function getValue() {
    console.log(editor.getValue());

}
// $(document).ready(function() {
//     //code here...
//     var code = $("#id_code")[0];
//     temp = document.getElementById("id_code");

//     // console.log(temp);
//     console.log(code);
//     var editor = CodeMirror.fromTextArea(code, {
//         mode: "application/xml",
//         htmlMode: true,
//         matchClosing: true,
//         lineNumbers: true,
//         spellcheck: true,
//         indentUnit: 4,
//         mode: 'clike',
//         keymap: "sublime",
//         autocorrect: true,
//         matchBrackets: true,
//         lineWrapping: true,
//         theme: 'monokai',
//     });
//     editor.on('change', function(cMirror) {
//         // get value right from instance
//         temp.value = editor.getValue();
//     });
//     editor.getTextArea();
// });