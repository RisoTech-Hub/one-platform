$(document).ready(function () {

    $(document).on('click', '[data-kt-element="remove-item"]', function (e) {
        const targetElement = $(this).attr('kt-target-element');
        $(targetElement).prop('checked', true).trigger('change');

        const $parent = $(this).parents('[data-kt-element="items"]');
        $parent.find(':input').prop('required', false);
        $parent.addClass('d-none')
    })

    $(document).on('click', '[kt-add-line-formset="true"]', function (e) {
        e.preventDefault();
        const $targetAppend = $($(this).attr('kt-target-append'));
        const $targetTotal = $($(this).attr('kt-target-total'));
        let counter = parseInt($targetTotal.val());
        const cloneElement = $($(this).attr('kt-target-element')).html().replace(/__prefix__/g, counter);
        $targetTotal.val(counter + 1);
        const html = $.parseHTML(cloneElement)
        console.log('cloneElement', cloneElement, html);

        $targetAppend.append(html);
    })
})
