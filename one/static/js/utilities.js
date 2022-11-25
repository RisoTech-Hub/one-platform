const debounce = (func, delay) => {

    let debounceTimer
    return function () {
        const context = this
        const args = arguments
        clearTimeout(debounceTimer)
        debounceTimer
            = setTimeout(() => func.apply(context, args), delay)
    }
}


function parseErrorAjax(responseJSON) {
    $.each(responseJSON, function (key, value) {
        $.each(value, function (index, _value) {
            if (key === "__all__") {
                toastr.error(_value, "{% translate 'Error' %}");
            } else {
                toastr.error(_value.replace(/field/g, key));
            }
        });
    });
}
