function reInitAllWidget() {
    // https://preview.keenthemes.com/good/documentation/forms/image-input.html
    if (KTImageInput) {
        KTImageInput.createInstances();
    }
}

function redrawTable() {
    if(table){
        table.draw()
    }
}
