btnVal = "run";
var editor = ace.edit("editor");
editor.setTheme("ace/theme/twilight");
editor.session.setMode("ace/mode/c_cpp");

function setSubmit() {
    btnVal = "submit";
    console.log("submit value setted");
}
$(document).on('submit', '#ide-form', function(e) {
    document.getElementsByClassName('output')[0].innerHTML = '';
    console.log($('#chk_input').val());
    e.preventDefault();
    console.log('{% url "run" %}');
    $.ajax({
        type: 'POST',
        // url: '{% url "run" %}',
        url: '/IDEApp/run/',
        data: {
            title: $('#id_title').val(),
            code: editor.getValue(),
            chk_input: $('#chk_input').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
            inp: $('#id_input').val(),
            action: 'post'
        },
        success: function(json) {
            $(".output").prepend('<div class="col-md-6">' +
                '<div class="row no-gutters border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">' +
                '<div class="col p-4 d-flex flex-column position-static">' +
                '<p class="mb-auto">' + json.out + '</p>' +
                '</div>' +
                '</div>' +
                '</div>'
            );
        },
        error: function(xhr, errmsg, err) {
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
    function() {
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