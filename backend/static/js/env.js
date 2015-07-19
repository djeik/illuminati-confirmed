$("input[type='file']").on("change",function(event){
    var file = event.target.files[0];
    var reader = new FileReader();
    reader.onload = function(event){
        $("#photo").attr("src", event.target.result);
        $("#photo").show();
        $("#upload-icon").hide();
        $("#spinner").fadeIn(5000);
        $("#title").text("Confirming Illuminati...");
    }
    reader.readAsDataURL(file);

    var data = new FormData();
    data.append("illuminati", file);

    $.ajax({
        url: "/api/confirm",
        type: "POST",
        data: data,
        cache: false,
        dataType: "string",
        processData: false,
        contentType: false,
        success: function(data, textStatus, jqXHR){
            $("#title").text("Illuminati Confirmed!");
            $("#photo2").load(function(){
                $("photo").hide();
            });
            $("#photo2").attr("src", data.url);
            $("spinner").fadeOut(5000);
        }
    });
});
