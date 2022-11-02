function appendModalWithId(selector = 'body', idModal = 'modal_fake', idForm = '', content = '', target_input = '', close_label = '', save_changes_label = '') {
    $(selector).append(`
            <div class="modal fade" tabindex="-1" id="${idModal}" modal-quick-action="" target-input="${target_input}">
                <div class="modal-dialog modal-dialog-scrollable">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="id_modal_title"></h5>

                            <!--begin::Close-->
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            <!--end::Close-->
                        </div>

                        <div class="modal-body">
                            ${content}
                        </div>

                        <div class="modal-footer">
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

                redrawTable();
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
                toastr.error(`${JSON.stringify(request)}\n${status}\n${error}`)
            }
        });
    })
})
