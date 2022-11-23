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

function appendDrawerWithId(selector = 'body', idDrawer = 'drawer_fake', idForm = '', content = '', target_input = '', close_label = '', save_changes_label = 'Save') {
    $(selector).append(`
            <!--begin::Chat drawer-->
<div id="${idDrawer}" class="bg-body"
    quick-action
     data-kt-drawer="true"
     data-kt-drawer-name="user-menu"
     data-kt-drawer-activate="true"
     data-kt-drawer-overlay="true"
     data-kt-drawer-width="{default:'300px', 'md': '500px'}"
     data-kt-drawer-direction="end"
     data-kt-drawer-toggle="#kt_drawer_user_menu_toggle"
     data-kt-drawer-close="#kt_drawer_user_menu_close">
  <!--begin::Messenger-->
  <div class="card rounded-0 w-100">
			<!--begin::Card header-->
			<div class="card-header bgi-position-y-bottom bgi-position-x-end bgi-size-cover bgi-no-repeat rounded-0 border-0 min-h-75px">
				<!--begin::Title-->
				<div class="card-title m-0 pe-5">
					<!--begin::User-->
					<span class="span_title text-gray-200"></span>
					<!--end::User-->
				</div>
				<!--end::Title-->
				<!--begin::Card toolbar-->
				<div class="card-toolbar">
					<!--begin::Close-->
					<div class="btn btn-sm btn-icon btn-active-light-primary" id="kt_drawer_example_dismiss_close" data-kt-drawer-dismiss="true">
						<!--begin::Svg Icon | path: icons/duotune/arrows/arr061.svg-->
						<span class="svg-icon svg-icon-2">
															<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
																<rect opacity="0.5" x="6" y="17.3137" width="16" height="2" rx="1" transform="rotate(-45 6 17.3137)" fill="currentColor"></rect>
																<rect x="7.41422" y="6" width="16" height="2" rx="1" transform="rotate(45 7.41422 6)" fill="currentColor"></rect>
															</svg>
														</span>
						<!--end::Svg Icon-->
					</div>
					<!--end::Close-->
				</div>
				<!--end::Card toolbar-->
			</div>

			<!--end::Card header-->
			<!--begin::Card body-->
			<div class="card-body pt-5 hover-scroll-overlay-y">
				<form id="${idForm}" enctype="multiple/data">
				    ${content}
                </form>
			</div>
			<!--end::Card body-->
			<!--begin::Card footer-->
			<div class="card-footer text-center">
				<!--begin::Dismiss button-->
			    <button class="btn btn-light-danger me-2" data-kt-drawer-dismiss="true">Close</button>
			    <!--end::Dismiss button-->
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
        console.log('action_url', action_url)
        const self = this;

        if (action_url.indexOf('popup') === -1) {
            window.location.href = action_url;
            return false;
        }

        $.ajax({
            url: action_url, method: "get", data: null, success: function (response) {
                // get form html return success
                // console.log('-----', response)
                const timestamp = Date.now();
                const theme = $(self).data('theme');
                console.log('theme', theme)
                if (theme === 'drawer') {

                    var idDrawer = "kt_drawer_fake_" + timestamp
                    var idDrawerForm = "kt_form_drawer_fake_" + timestamp

                    appendDrawerWithId('body', idDrawer, idDrawerForm, response, target_input, $('#id_btn_close_label').val(), $('#id_btn_save_changes_label').val(),)
                    $('.span_title').text($('#' + idDrawerForm + ' #id_form_title').val());
                    let selectorHeader = '#' + idDrawer + ' .card-header'
                    console.log('selectorHeader', selectorHeader)
                    $(selectorHeader).css('background-image', 'url(' + $('#' + 'trans_label_div' + ' #id_drawer_header_bg').val() + ')');

                    KTDrawer.createInstances();
                    var drawerElement = document.querySelector('#' + idDrawer);
                    var drawer = KTDrawer.getInstance(drawerElement);
                    drawer.show();

                    drawer.on("kt.drawer.after.hidden", function () {
                        console.log("kt.drawer.after.hidden event is fired");
                        $('#' + idDrawer).remove();
                    });
                } else {
                    const idModal = 'modal_fake_' + timestamp;
                    const idForm = 'form_fake_' + timestamp;
                    appendModalWithId('body', idModal, idForm, response, target_input, $('#id_btn_close_label').val(), $('#id_btn_save_changes_label').val(),)
                    $('#id_modal_title').text($('#id_form_title').val())
                    $('#' + idModal).modal('show')
                    $('#' + idModal).find('form').attr('id', idForm)

                    reInitAllWidget();
                }

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
            url, method, contentType: false, processData: false, data: formData, success: function (response) {
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

    $(document).on('submit', '.drawer[quick-action] form', function (e) {
        e.preventDefault();
        const method = $(this).attr('method')
        const url = $(this).attr('action')
        const formData = new FormData(this)
        // const $modal = $(this).closest('.modal')
        const $drawer = $(this).closest('.drawer')
        $.ajax({
            url, method, contentType: false, processData: false, data: formData, success: function (response) {
                // get form html return success
                // console.log('-----', response)
                var drawerElement = document.querySelector('#' + $drawer.attr('id'));
                var drawer = KTDrawer.getInstance(drawerElement);
                drawer.hide();
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
