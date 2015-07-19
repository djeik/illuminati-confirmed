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
                console.log('Ajax succeeded');
                $("#title").text("Illuminati Confirmed!");
                $("#photo2").load(function(){
                    console.log('photo2 loaded');
                    $("#photo").hide();
                    $("#photo2").show();
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
