$(document).ready(function () {

    $(document).on('click', '[data-kt-element="remove-item"]', function (e) {

    })

    $(document).on('click', '[kt-add-line-formset="true"]', function (e) {
        e.preventDefault();
        const $targetAppend = $($(this).attr('kt-target-append'));
        const $targetTotal = $($(this).attr('kt-target-total'));
        let counter = parseInt($targetTotal.val());
        $targetTotal.val(counter + 1);
        const cloneElement = $($(this).attr('kt-target-element')).html().replace(/__index__/g, counter++);
        const html = $.parseHTML(cloneElement)
        console.log('cloneElement', cloneElement, html);

        $targetAppend.append(html);
    })
})
