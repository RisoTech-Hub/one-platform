const debounce = (func, delay) => {

    let debounceTimer
    return function () {
        const context = this
        const args = arguments
        clearTimeout(debounceTimer)
        debounceTimer = setTimeout(() => func.apply(context, args), delay)
    }
}


function parseErrorAjax(responseJSON) {
    $.each(responseJSON, function (key, value) {
        $.each(value, function (_key, _value) {
            if (key === "__all__") {
                toastr.error(_value, "{% translate 'Error' %}");
            } else {
                console.log('_value', _value);
                if (Array.isArray(_value)) {
                    _value.map(function (item) {
                        toastr.error(item.replace(/field/g, _key));
                    })
                } else {
                    toastr.error(_value.replace(/field/g, _key));
                }
            }
        });
    });
}
