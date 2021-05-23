
$("input[type=submit]").click(function () { 
    $.ajax({
        type: $("form").attr("method"),
        url: $("form").attr("action"),
        data: JSON.stringify({n1:$("input[name=n1]").val(),
        n2:$("input[name=n2]").val(),
        operation:$("input[name=operation]").val()}),
        dataType: "json"
       });
});