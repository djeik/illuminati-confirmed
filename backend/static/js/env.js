(function() {

function playIlluminati() {
    document.getElementById('illuminati-music').play();
    console.log('playing illuminati music');
}

$(document).ready(function() {
    var input = $("input[type='file']");
    input.attr("disabled", false);

    // When the user selects an image.
    input.on("change", function(event) {
        // Extract the selected file
        var file = event.target.files[0];

        // Create a file reader to show the image
        var reader = new FileReader();

        // When the reader has loaded the image as a data URL, we set the src
        // attribute of the main image to that data url, which makes the
        // browser load that image.
        reader.onload = function(event){
            console.log('reader loaded');
            var photo = $("#photo");
            $("#upload-icon").hide();
            photo.load(function() {
                $("#spinner").fadeIn(5000);
                $("#title").text("Confirming Illuminati...");
                $("#file-upload-input").attr("disabled", "disabled");
            });
            photo.attr("src", event.target.result);
            photo.show();
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
                var shareURL = "https://www.facebook.com/dialog/share?" +
                    "app_id=982515815140018" +
                    "&display=popup" +
                    "&href=" + encodeURIComponent("http://www.illuminaticonfirmed.xyz:6501/") +
                    data.id +
                    "&redirect_uri=" + encodeURIComponent("http://www.illuminaticonfirmed.xyz");

                console.log('Ajax succeeded', JSON.stringify(data));
                // Change header text
                $("#title").text("Illuminati Confirmed!");

                // When the new image is loaded, replace the initial image with
                // the new image
                $("#photo2").load(function(){
                    console.log('photo2 loaded');
                    $("#photo").hide();
                    $("#photo2").show();
                    $("#new-share-link").on("click", function(){
                        event.preventDefault();
                        window.open(shareURL, target="_blank");
                    });
                });

                // Load the new image
                $("#photo2").attr("src", data.url);

                // Fade out the spinner for five seconds
                $("#spinner").fadeOut(5000);

                // Play the xfiles music
                playIlluminati();
            },
            error: function(error) {
                $("#title").text("Can't confirm!");
                $(".container").append($("<p>They're watching...</p>"));
            }
        });
    });
});

})();
