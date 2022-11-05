function appendModalWithId(selector = 'body', idModal = 'modal_fake', idForm = '', content = '', target_input = '', close_label = '', save_changes_label = '') {
    $(selector).append(`
            <div class="modal fade" tabindex="-1" id="${idModal}" modal-quick-action="" target-input="${target_input}">
                <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable modal-xl">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="id_modal_title"></h5>

                            <!--begin::Close-->
                             <div class="btn btn-sm btn-icon btn-active-color-primary" data-bs-dismiss="modal">
                                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                    <rect opacity="0.5" x="6" y="17.3137" width="16" height="2" rx="1" transform="rotate(-45 6 17.3137)" fill="currentColor"></rect>
                                    <rect x="7.41422" y="6" width="16" height="2" rx="1" transform="rotate(45 7.41422 6)" fill="currentColor"></rect>
                                </svg>
                             </div>

                            <!--end::Close-->
                        </div>

                        <div class="modal-body py-10 px-lg-17">
                            ${content}
                        </div>

                        <div class="modal-footer flex-center">
                            <button type="button" class="btn btn-light" data-bs-dismiss="modal">${close_label}</button>
                            <button type="submit" form="${idForm}" class="btn btn-primary">${save_changes_label}</button>
                        </div>
                    </div>
                </div>
            </div>
        `)
}

$(document).ready(function () {
    $(document).on('click', '[quick-create-button], [quick-update-button], [quick-add-button]', function () {
        const action_url = $(this).data('action-url')
        const target_input = $(this).data('target-input')
        console.log('action_url', action_url)
        $.ajax({
            url: action_url, method: "get", data: null, success: function (response) {
                // get form html return success
                // console.log('-----', response)
                const timestamp = Date.now();
                const idModal = 'modal_fake_' + timestamp;
                const idForm = 'form_fake_' + timestamp;
                appendModalWithId('body', idModal, idForm, response, target_input, $('#id_btn_close_label').val(), $('#id_btn_save_changes_label').val(),)
                $('#id_modal_title').text($('#id_form_title').val())
                $('#' + idModal).modal('show')
                $('#' + idModal).find('form').attr('id', idForm)

                reInitAllWidget()

            }, error: function (request, status, error) {
                toastr.error(`${JSON.stringify(request)}\n${status}\n${error}`)
            }
        });
    })

    $(document).on('submit', '.modal[modal-quick-action] form', function (e) {
        e.preventDefault();
        const method = $(this).attr('method')
        const url = $(this).attr('action')
        const formData = new FormData(this)
        const $modal = $(this).closest('.modal')
        $.ajax({
            url, method, contentType: false, processData: false, data: formData,
            success: function (response) {
                // get form html return success
                // console.log('-----', response)
                $modal.modal('hide')
                if ($modal.attr('target-input') && $('#' + $modal.attr('target-input'))) {
                    $('#' + $modal.attr('target-input')).prepend(`<option value="${response['id']}" selected>${response['name']}</option>`)
                }
                $modal.remove();

                redrawTable();
            }, error: function (request, status, error) {
                console.log('error--------------', request, status, error)
                $.each(request.responseJSON, function (key, value) {
                    $.each(value, function (index, _value) {
                        if (key === "__all__") {
                            toastr.error(_value, "{% translate 'Error' %}");
                        } else {
                            toastr.error(_value, key.toUpperCase());
                        }
                    });
                });

                //toastr.error(`${JSON.stringify(request)}\n${status}\n${error}`)
            }
        });
    })
})
