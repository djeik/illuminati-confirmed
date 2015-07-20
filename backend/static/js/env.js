(function() {

function playIlluminati() {
    document.getElementById('illuminati-music').play();
    console.log('playing illuminati music');
}

$(document).ready(function() {
    var input = $("input[type='file']");
    input.attr("disabled", false);

    input.on("change", function(event) {
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
                var shareUrl = "https://www.facebook.com/dialog/share?" +
                    "app_id=982515815140018" +
                    "&display=popup" +
                    "&href=" + "http%3A%2F%2Fwww.illuminaticonfirmed.xyz:6501" + encodeURIComponent(data.id) +
                    "&redirect_uri=" + encodeURIComponent(window.location.href); 

                console.log('Ajax succeeded');
                $("#title").text("Illuminati Confirmed!");
                $("#photo2").load(function(){
                    console.log('photo2 loaded');
                    $("#photo").hide();
                    $("#photo2").show();
                    $("pluginShareButtonLink").attr("href", "/sharer/sharer.php?app_id=982515815140018&amp;sdk=joey&amp;u=http%3A%2F%2Fwww.illuminaticonfirmed.xyz%3A6501%2F" +
                        data.id + "&amp;display=popup&amp;ref=plugin&amp;src=share_button"
                });
                $("#photo2").attr("src", data.url);
                $("#spinner").fadeOut(5000);
                playIlluminati();
            },
            error: function(error) {
                console.log('error occurred', error);
            }
        });
    });
});

})();
