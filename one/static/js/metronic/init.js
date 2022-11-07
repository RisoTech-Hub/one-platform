function reInitAllWidget() {
    // https://preview.keenthemes.com/good/documentation/forms/image-input.html
    if (KTImageInput) {
        KTImageInput.createInstances();
    }

    let options = {selector: ".tinymce", height: "480"};

    if (KTThemeMode.getMode() === "dark") {
        options["skin"] = "oxide-dark";
        options["content_css"] = "dark";
    }

    tinymce.init(options);
}

function redrawTable() {
    if (table) {
        table.draw(false)
    }
}
