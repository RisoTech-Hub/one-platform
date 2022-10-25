function appendModalWithId(selector = 'body', idModal = 'modal_fake', content = '') {
    $(selector).append(`
            <div class="modal fade" tabindex="-1" id="${idModal}">
                <div class="modal-dialog modal-dialog-scrollable">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Modal title</h5>

                            <!--begin::Close-->
                            <div class="btn btn-icon btn-sm btn-active-light-primary ms-2" data-bs-dismiss="modal" aria-label="Close">
                                <span class="svg-icon svg-icon-2x"></span>
                            </div>
                            <!--end::Close-->
                        </div>

                        <div class="modal-body">
                            ${content}
                        </div>

                        <div class="modal-footer">
                            <button type="button" class="btn btn-light" data-bs-dismiss="modal">Close</button>
                            <button type="button" class="btn btn-primary">Save changes</button>
                        </div>
                    </div>
                </div>
            </div>
`)
}

$(document).ready(function () {
    $(document).on('click', '[quick-create-button]', function () {
        const action_url = $(this).data('action-url')
        $.ajax({
            url: action_url,
            method: "get",
            data: null,
            success: function (response) {
                // get form html return success

                appendModalWithId('body', response)
            },
            error: function (request, status, error) {
                alert(`${JSON.stringify(request)}\n${status}\n${error}`)
            }
        });
    })
})
