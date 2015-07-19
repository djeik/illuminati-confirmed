$("input[type='file']").on("change",function(event){
    var file = event.target.files[0];
    var reader = new FileReader();
    reader.onload = function(event){
        $("#photo").attr("src", event.target.result);
        $("#photo").show();
        $("#upload-icon").hide();
        $("#spinner").fadeIn(5000);
        $("#title").text("Confirming Illuminati...");
        $("#file-upload-input").attr("disabled", "disabled");
    }
    reader.readAsDataURL(file);

    var data = new FormData();
    data.append("illuminati", file);

    $.ajax({
        url: "/api/confirm",
        type: "POST",
        data: data,
        cache: false,
        dataType: 'json',
        processData: false,
        contentType: false,
        success: function(data, textStatus, jqXHR) {
            $("#title").text("Illuminati Confirmed!");
            $("#photo2").load(function(){
                $("#photo").hide();
                $("#photo2").show();
            });
            $("#photo2").attr("src", data.url);
            $("meta[property='og:image']").attr("content", "www.illuminaticonfirmed.xyz" + data.url);
            $("#spinner").fadeOut(5000);
            FB.ui({
                  method: 'share',
                    href: 'http://www.illuminaticonfirmed.xyz',
            }, function(response){});
        },
        error: function(error) {
            console.log('error occurred', error);
        }
    });
});
