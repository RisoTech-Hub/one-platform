function appendModalWithId(
    selector = 'body',
    idModal = 'modal_fake',
    idForm = '',
    content = '',
    target_input = '',
    close_label = '',
    save_changes_label = '') {
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

function appendDrawerWithId(
    selector = 'body',
    idDrawer = 'drawer_fake',
    idForm = '',
    content = '',
    target_input = '',
    close_label = '',
    save_changes_label = 'Save') {
    $(selector).append(`
            <!--begin::Chat drawer-->
            <div id="${idDrawer}" class="bg-body"
                 quick-action
                 data-kt-drawer="true"
                 data-kt-drawer-name="${idDrawer}"
                 data-kt-drawer-activate="true"
                 data-kt-drawer-overlay="true"
                 data-kt-drawer-width="{default:'300px', 'md': '500px'}"
                 data-kt-drawer-direction="end"
                 data-kt-drawer-toggle="#${idDrawer}_toggle"
                 data-kt-drawer-close="#${idDrawer}_close">
                <!--begin::Messenger-->
                <div class="card w-100 rounded-0 border-0" id="${idDrawer}" >
                    <!--begin::Card header-->
                    <div class="card-header bgi-position-y-bottom bgi-position-x-end bgi-size-cover bgi-no-repeat rounded-0 border-0 py-4"
                         id="${idDrawer}_header">
                        <!--begin::Title-->
                        <div class="card-title m-0">
                            <div class="menu-item">
                              <div class="menu-content d-flex align-items-center px-3">
                                <!--begin::Title-->
                                <h3 class="card-title fs-3 fw-bold text-white flex-column m-0 span_title">
                                </h3>
                                <!--end::Title-->
                              </div>
                            </div>
                        </div>
                        <!--end::Title-->
                        <!--begin::Card toolbar-->
                        <div class="card-toolbar">
                            <!--begin::Close-->
                            <div class="btn btn-sm btn-icon bg-white bg-opacity-25 btn-color-white p-0 w-20px h-20px rounded-1"
                                 id="${idDrawer}_close"
                                 data-kt-drawer-dismiss="true">
                                <span class="svg-icon svg-icon-2">
                                    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                        <rect opacity="0.5" x="6" y="17.3137" width="16" height="2" rx="1" transform="rotate(-45 6 17.3137)" fill="currentColor"></rect>
                                        <rect x="7.41422" y="6" width="16" height="2" rx="1" transform="rotate(45 7.41422 6)" fill="currentColor"></rect>
                                    </svg>
                                </span>
                            </div>
                            <!--end::Close-->
                        </div>
                        <!--end::Card toolbar-->
                    </div>
                    <!--end::Card header-->
                    <!--begin::Card body-->
                    <div class="card-body pt-5" id="${idDrawer}_body">
                        ${content}
                    </div>
                    <!--end::Card body-->
                    <!--begin::Card footer-->
                    <div class="card-footer text-center" id="${idDrawer}_footer">
                        <button type="submit" form="${idForm}" class="btn btn-primary">${save_changes_label}</button>
                    </div>
                    <!--end::Card footer-->
                </div>
                <!--end::Messenger-->
            </div>
            <!--end::Chat drawer-->
        `)
}

$(document).ready(function () {
    $(document).on('click', '[quick-create-button], [quick-update-button], [quick-add-button]', function () {
        const action_url = $(this).data('action-url')
        const target_input = $(this).data('target-input')
        const self = this;

        if (action_url.indexOf('popup') === -1) {
            window.location.href = action_url;
            return false;
        }

        $.ajax({
            url: action_url,
            method: "get",
            data: null,
            success: function (response) {
                // get form html return success
                const timestamp = Date.now();
                const theme = $(self).data('theme');
                if (theme === 'drawer') {

                    var idDrawer = "kt_drawer_fake_" + timestamp
                    var idDrawerForm = "kt_form_drawer_fake_" + timestamp

                    appendDrawerWithId('body', idDrawer, idDrawerForm, response, target_input, $('#id_btn_close_label').val(), $('#id_btn_save_changes_label').val(),)
                    $('#' + idDrawer).find('form').attr('id', idDrawerForm)

                    $('.span_title').text($('#' + idDrawerForm + ' #id_form_title').val());
                    let selectorHeader = '#' + idDrawer + ' .card-header'
                    $(selectorHeader).css('background-image', 'url(' + $('#' + 'trans_label_div' + ' #id_drawer_header_bg').val() + ')');


                    KTDrawer.createInstances();
                    var drawerElement = document.querySelector('#' + idDrawer);
                    var drawer = KTDrawer.getInstance(drawerElement);
                    drawer.show();

                    drawer.on("kt.drawer.after.hidden", function () {
                        $('#' + idDrawer).remove();
                    });

                    reInitAllWidget();
                } else {
                    const idModal = 'modal_fake_' + timestamp;
                    const idForm = 'form_fake_' + timestamp;
                    appendModalWithId('body', idModal, idForm, response, target_input, $('#id_btn_close_label').val(), $('#id_btn_save_changes_label').val(),)
                    $('#id_modal_title').text($('#id_form_title').val())
                    $('#' + idModal).modal('show')
                    $('#' + idModal).find('form').attr('id', idForm)


                    $('#' + idModal).on('hidden.bs.modal', function () {
                        $('#' + idModal).remove();
                    });

                    reInitAllWidget();
                }

            },
            error: function (request, status, error) {
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
            url,
            method,
            contentType: false,
            processData: false,
            data: formData,
            success: function (response) {
                // get form html return success
                $modal.modal('hide')
                if ($modal.attr('target-input') && $('#' + $modal.attr('target-input'))) {
                    $('#' + $modal.attr('target-input')).prepend(`<option value="${response['id']}" selected>${response['name']}</option>`)
                }
                $modal.remove();

                toastr.success('Successfully');
                redrawTable();

            },
            error: function (request, status, error) {
                $.each(request.responseJSON, function (key, value) {
                    $.each(value, function (index, _value) {
                        if (key === "__all__") {
                            toastr.error(_value, "{% translate 'Error' %}");
                        } else {
                            toastr.error(_value, key.toUpperCase());
                        }
                    });
                });
            }
        });
    })

    $(document).on('submit', '.drawer[quick-action] form', function (e) {
        e.preventDefault();
        const method = $(this).attr('method')
        const url = $(this).attr('action')
        const formData = new FormData(this)
        // const $modal = $(this).closest('.modal')
        const $drawer = $(this).closest('.drawer')
        $.ajax({
            url,
            method,
            contentType: false,
            processData: false,
            data: formData,
            success: function (response) {
                // get form html return success
                var drawerElement = document.querySelector('#' + $drawer.attr('id'));
                var drawer = KTDrawer.getInstance(drawerElement);
                drawer.hide();
                toastr.success('Successfully');
            },
            error: function (request, status, error) {
                $.each(request.responseJSON, function (key, value) {
                    $.each(value, function (index, _value) {
                        if (key === "__all__") {
                            toastr.error(_value, "{% translate 'Error' %}");
                        } else {
                            toastr.error(_value, key.toUpperCase());
                        }
                    });
                });
            }
        });
    })
})
