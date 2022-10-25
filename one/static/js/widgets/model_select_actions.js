function appendModalWithId(selector = 'body', idModal = 'modal_fake', content = '', target_input = '') {
    $(selector).append(`
            <div class="modal fade" tabindex="-1" id="${idModal}" modal-quick-action="" target-input="${target_input}">
                <div class="modal-dialog modal-dialog-scrollable">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Modal title</h5>

                            <!--begin::Close-->
                            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                            <!--end::Close-->
                        </div>

                        <div class="modal-body">
                            ${content}
                        </div>

                        <div class="modal-footer">
<!--                            <button type="button" class="btn btn-light" data-bs-dismiss="modal">Close</button>-->
<!--                            <button type="button" class="btn btn-primary">Save changes</button>-->
                        </div>
                    </div>
                </div>
            </div>
    `)
}

$(document).ready(function () {
    $(document).on('click', '[quick-create-button]', function () {
        const action_url = $(this).data('action-url')
        const target_input = $(this).data('target-input')
        $.ajax({
            url: action_url,
            method: "get",
            data: null,
            success: function (response) {
                // get form html return success
                console.log('-----', response)
                let idModal = 'abc_fake'; // TODO: generate id modal here
                appendModalWithId('body', idModal, response, target_input)
                $('#' + idModal).modal('show')
            },
            error: function (request, status, error) {
                alert(`${JSON.stringify(request)}\n${status}\n${error}`)
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
            url,
            method,
            contentType: false,
            processData: false,
            data: formData,
            success: function (response) {
                // get form html return success
                console.log('-----', response)
                $modal.modal('hide')
                $('#' + $modal.attr('target-input')).prepend(`<option value="${response['id']}">${response['name']}</option>`).val([response['id']])
                $modal.remove();
            },
            error: function (request, status, error) {
                alert(`${JSON.stringify(request)}\n${status}\n${error}`)
            }
        });
    })
})
