"use strict";

var DT = (function () {
    // Define shared variables
    var table;
    var datatable;
    var arr_selected = [];
    var toolbarBase;
    var toolbarSelected;
    var selectedCount;
    var totalCount = 0;

    // Private functions
    var initTable = function (
        tableId = "",
        options = {},
        endpoint = {},
        language = {}
    ) {
        table = document.getElementById(tableId);

        const iconDelete = (row) => `<a href="javascript:void(0);" data-bs-toggle="tooltip" data-bs-placement="top" title="Delete row" class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm text-hover-danger" data-id="${row["id"]}" data-kt-table-filter="delete_row">
                                        <!--begin::Svg Icon | path: icons/duotune/general/gen027.svg-->
                                        <span class="svg-icon svg-icon-3">
                                            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                                <path d="M5 9C5 8.44772 5.44772 8 6 8H18C18.5523 8 19 8.44772 19 9V18C19 19.6569 17.6569 21 16 21H8C6.34315 21 5 19.6569 5 18V9Z" fill="currentColor"/>
                                                <path opacity="0.5" d="M5 5C5 4.44772 5.44772 4 6 4H18C18.5523 4 19 4.44772 19 5V5C19 5.55228 18.5523 6 18 6H6C5.44772 6 5 5.55228 5 5V5Z" fill="currentColor"/>
                                                <path opacity="0.5" d="M9 4C9 3.44772 9.44772 3 10 3H14C14.5523 3 15 3.44772 15 4V4H9V4Z" fill="currentColor"/>
                                            </svg>
                                        </span>
                                        <!--end::Svg Icon-->
                                      </a>`

        const iconEdit = (row) => `<a href="javascript:void(0);" class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1" data-id="${row["id"]}" data-kt-table-filter="edit_row">
                                    <!--begin::Svg Icon | path: icons/duotune/art/art005.svg-->
                                    <span class="svg-icon svg-icon-3">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path opacity="0.3" d="M21.4 8.35303L19.241 10.511L13.485 4.755L15.643 2.59595C16.0248 2.21423 16.5426 1.99988 17.0825 1.99988C17.6224 1.99988 18.1402 2.21423 18.522 2.59595L21.4 5.474C21.7817 5.85581 21.9962 6.37355 21.9962 6.91345C21.9962 7.45335 21.7817 7.97122 21.4 8.35303ZM3.68699 21.932L9.88699 19.865L4.13099 14.109L2.06399 20.309C1.98815 20.5354 1.97703 20.7787 2.03189 21.0111C2.08674 21.2436 2.2054 21.4561 2.37449 21.6248C2.54359 21.7934 2.75641 21.9115 2.989 21.9658C3.22158 22.0201 3.4647 22.0084 3.69099 21.932H3.68699Z" fill="currentColor"/>
                                            <path d="M5.574 21.3L3.692 21.928C3.46591 22.0032 3.22334 22.0141 2.99144 21.9594C2.75954 21.9046 2.54744 21.7864 2.3789 21.6179C2.21036 21.4495 2.09202 21.2375 2.03711 21.0056C1.9822 20.7737 1.99289 20.5312 2.06799 20.3051L2.696 18.422L5.574 21.3ZM4.13499 14.105L9.891 19.861L19.245 10.507L13.489 4.75098L4.13499 14.105Z" fill="currentColor"/>
                                        </svg>
                                    </span>
                                    <!--end::Svg Icon-->
                                </a>`

        const iconView = (row) => `<a href="javascript:void(0);" class="btn btn-icon btn-bg-light btn-active-color-primary btn-sm me-1" data-id="${row["id"]}" data-kt-table-filter="view_row">
                                    <!--begin::Svg Icon | path: /var/www/preview.keenthemes.com/kt-products/docs/metronic/html/releases/2022-10-09-043348/core/html/src/media/icons/duotune/arrows/arr095.svg-->
                                    <span class="svg-icon svg-icon-3">
                                        <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                                            <path opacity="0.3" d="M4.7 17.3V7.7C4.7 6.59543 5.59543 5.7 6.7 5.7H9.8C10.2694 5.7 10.65 5.31944 10.65 4.85C10.65 4.38056 10.2694 4 9.8 4H5C3.89543 4 3 4.89543 3 6V19C3 20.1046 3.89543 21 5 21H18C19.1046 21 20 20.1046 20 19V14.2C20 13.7306 19.6194 13.35 19.15 13.35C18.6806 13.35 18.3 13.7306 18.3 14.2V17.3C18.3 18.4046 17.4046 19.3 16.3 19.3H6.7C5.59543 19.3 4.7 18.4046 4.7 17.3Z" fill="currentColor"/>
                                            <rect x="21.9497" y="3.46448" width="13" height="2" rx="1" transform="rotate(135 21.9497 3.46448)" fill="currentColor"/>
                                            <path d="M19.8284 4.97161L19.8284 9.93937C19.8284 10.5252 20.3033 11 20.8891 11C21.4749 11 21.9497 10.5252 21.9497 9.93937L21.9497 3.05029C21.9497 2.498 21.502 2.05028 20.9497 2.05028L14.0607 2.05027C13.4749 2.05027 13 2.52514 13 3.11094C13 3.69673 13.4749 4.17161 14.0607 4.17161L19.0284 4.17161C19.4702 4.17161 19.8284 4.52978 19.8284 4.97161Z" fill="currentColor"/>
                                        </svg>
                                    </span>
                                    <!--end::Svg Icon-->
                                </a>`

        const defaultOptions = {
            order: [],
            pageLength: 10,
            columnDefs: [
                {
                    orderable: false, // Disable ordering on column 0 (checkbox)
                    targets: 0,
                    render: function (data, type, full, meta) {
                        return `<div class="form-check form-check-sm form-check-custom form-check-solid">
                       <input class="form-check-input widget-9-check" type="checkbox" value="${data}">
                     </div>`;
                    },
                },
                {
                    orderable: false, // Disable ordering on column (actions)
                    targets: -1,
                    title: "Action",
                    className: "text-end",
                    render: function (data, type, row, meta) {
                        return `<div class="d-flex justify-content-end flex-shrink-0">
                        ${iconView(row)}
                        ${iconEdit(row)}
                        ${iconDelete(row)}
                    </div>`;
                    },
                },
            ],
            processing: true,
            language: {
                processing: "<div class='d-block'><span class='spinner-border w-15px h-15px text-muted align-middle me-2'></span></div>",
            },
            rowCallback: function (row, data) {
                $(row)
                    .find("input.asset-checkbox-select")
                    .prop(
                        "checked",
                        arr_selected.findIndex((item) => item === data["ID"]) > -1
                    );
            },
            drawCallback: function (settings) {
                // ?Initialize tooltip bootstrap
                const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
                const tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
                    return new bootstrap.Tooltip(tooltipTriggerEl)
                })

                if (settings && settings["json"]) {
                    totalCount = parseInt(settings["json"]["recordsFiltered"]);
                    if (settings["json"]["options"]) {
                        initFilterForm(settings["json"]["options"]);
                    }
                }

                $(document).on("change", tableId + 'td input[type="checkbox"]', function () {
                    if ($(this).is(":checked")) {
                        arr_selected.push($(this).val());
                    } else {
                        arr_selected.splice(arr_selected.indexOf($(this).val()), 1);
                    }
                    // console.log('arr_selected: ', arr_selected);

                    toggleToolbars();
                });

                // TODO: HANDLE META DATA FOR FORM FILTER WILL APPEND TO SELECT, RETURN FROM API
            },
        };

        // Init datatable --- more info on datatables: https://datatables.net/manual/
        datatable = $(table).DataTable({
            ...defaultOptions,
            ...options
        });

        // Re-init functions on every table re-draw -- more info: https://datatables.net/reference/event/draw
        datatable.on("draw", function () {
            initToggleToolbar(endpoint.delete, language);
            handleDeleteRows(endpoint.delete, language);
            toggleToolbars();
        });

        // $('input[data-kt-check="true"]').on("change", function () {
        //     if (this.checked) {
        //         $('tbody td [type="checkbox"]').prop("checked", true);
        //     } else {
        //         $('tbody td [type="checkbox"]').prop("checked", false);
        //     }
        //     toggleToolbars();
        // });

        // $('#kt_table_settings tbody td input[type="checkbox"]').on(
        //     "change",
        //     function () {
        //         toggleToolbars();
        //     }
        // );

        return datatable;
    };

    var handleViewRow = () => {
        $(document).on('click', 'td [data-kt-table-filter="edit_row"]', function () {
            const id = $(this).attr('data-id')
            console.log('click view in row with id: ', id)
        })
    }

    var handleEditRow = () => {
        $(document).on('click', 'td [data-kt-table-filter="edit_row"]', function () {
            const id = $(this).attr('data-id')
            console.log('click edit in row with id: ', id)
        })
    }

    // Search Datatable --- official docs reference: https://datatables.net/reference/api/search()
    var handleSearchDatatable = () => {
        const filterSearch = document.querySelector(
            '[data-kt-table-filter="search"]'
        );
        filterSearch.addEventListener("keyup", function (e) {
            datatable.search(e.target.value).draw();
        });
    };

    // init Filter Form
    const initFilterForm = (options) => {
        // const filterForm = document.querySelector('[data-kt-table-filter="form"]');
        // const filterBody = filterForm.querySelector(
        //     '[data-kt-table-filter="body"]'
        // );
        // options.forEach(function (item) {
        //     console.log(item);
        //     filterBody.append(item);
        // })
    }

    // Filter Datatable
    var handleFilterDatatable = () => {
        // Select filter options
        const filterForm = document.querySelector('[data-kt-table-filter="form"]');
        const filterButton = filterForm.querySelector(
            '[data-kt-table-filter="filter"]'
        );
        const selectOptions = filterForm.querySelectorAll("[name]");

        // Filter datatable on submit
        filterButton.addEventListener("click", function () {
            var filterString = "";

            // Get filter values
            selectOptions.forEach((item, index) => {
                if (item.value && item.value !== "") {
                    if (index !== 0) {
                        filterString += " ";
                    }

                    // Build filter value options
                    filterString += item.value;
                }
            });

            console.log("filterString: ", filterString);
            // Filter datatable --- official docs reference: https://datatables.net/reference/api/search()
            datatable.search(filterString).draw();
        });
    };

    // Reset Filter
    var handleResetForm = () => {
        // Select reset button
        const resetButton = document.querySelector(
            '[data-kt-table-filter="reset"]'
        );

        // Reset datatable
        resetButton.addEventListener("click", function () {
            // Select filter options
            const filterForm = document.querySelector(
                '[data-kt-table-filter="form"]'
            );
            const selectOptions = filterForm.querySelectorAll("select");

            // Reset select2 values -- more info: https://select2.org/programmatic-control/add-select-clear-items
            selectOptions.forEach((select) => {
                $(select).val("").trigger("change");
            });

            // Reset datatable --- official docs reference: https://datatables.net/reference/api/search()
            datatable.search("").draw();
        });
    };

    // Delete subscription
    var handleDeleteRows = (_url_delete = "", _language) => {
        // Select all delete buttons
        const deleteButtons = table.querySelectorAll(
            '[data-kt-table-filter="delete_row"]'
        );
        const url_delete = _url_delete;

        deleteButtons.forEach((d) => {
            // Delete button on click
            // console.log('url-delete', url_delete)
            $(d).attr("data-url", url_delete);
            d.addEventListener("click", function (e) {
                e.preventDefault();
                // Select parent row
                // const parent = e.target.closest('tr');

                let id = $(this).attr("data-id");
                // let url_delete = $(this).attr('data-url')

                // SweetAlert2 pop up --- official docs reference: https://sweetalert2.github.io/
                Swal.fire({
                    text: _language.confirmDelete ||
                        "Are you sure you want to delete this(these) record?",
                    icon: "warning",
                    showCancelButton: true,
                    buttonsStyling: false,
                    confirmButtonText: "Yes, delete!",
                    cancelButtonText: "No, cancel",
                    customClass: {
                        confirmButton: "btn fw-bold btn-danger",
                        cancelButton: "btn fw-bold btn-active-light-primary",
                    },
                }).then(function (result) {
                    if (result.value) {
                        $.ajax({
                            url: _url_delete,
                            headers: {
                                "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val(),
                                Authorization: "Basic cm9vdDox", // TODO: will receipt token
                                "Content-Type": "application/json",
                            },
                            method: "delete",
                            dataType: "text",
                            contentType: false,
                            processData: false,
                            data: JSON.stringify([id]),
                            success: function (response) {
                                Swal.fire({
                                    text: _language.delete_success || "You have deleted!",
                                    icon: "success",
                                    buttonsStyling: false,
                                    confirmButtonText: "Ok, got it!",
                                    customClass: {
                                        confirmButton: "btn fw-bold btn-primary",
                                    },
                                })
                                    .then(function () {
                                        // Remove current row
                                        // datatable.row($(parent)).remove().draw();
                                        datatable.draw();
                                    })
                                    .then(function () {
                                        // Detect checked checkboxes
                                        toggleToolbars();
                                    });
                            },
                            error: function (request, status, error) {
                                Swal.fire({
                                    title: "Notice",
                                    text: "Something is error: " + error,
                                    icon: "error",
                                    type: "error",
                                }).then(function () {
                                });
                            },
                        });
                    } else if (result.dismiss === "cancel") {
                        Swal.fire({
                            text: _language.delete_fail || "This record was not deleted.",
                            icon: "error",
                            buttonsStyling: false,
                            confirmButtonText: "Ok, got it!",
                            customClass: {
                                confirmButton: "btn fw-bold btn-primary",
                            },
                        });
                    }
                });
            });
        });
    };

    // Init toggle toolbar
    var initToggleToolbar = (_url_delete = "", _language = {}) => {
        // Toggle selected action toolbar
        // Select all checkboxes
        const checkboxes = table.querySelectorAll('[type="checkbox"]');

        // Select elements
        toolbarBase = document.querySelector('[data-kt-table-toolbar="base"]');
        toolbarSelected = document.querySelector(
            '[data-kt-table-toolbar="selected"]'
        );
        selectedCount = document.querySelector(
            '[data-kt-table-select="selected_count"]'
        );
        const deleteSelected = document.querySelector(
            '[data-kt-table-select="delete_selected"]'
        );

        // Toggle delete selected toolbar
        checkboxes.forEach((c) => {
            // Checkbox on click event
            c.addEventListener("click", function () {
                setTimeout(function () {
                    toggleToolbars();
                }, 50);
            });
        });

        // Deleted selected rows
        deleteSelected.addEventListener("click", function () {
            // SweetAlert2 pop up --- official docs reference: https://sweetalert2.github.io/
            Swal.fire({
                text: _language.confirm_delete || "Are you sure you want to delete selected records?",
                icon: "warning",
                showCancelButton: true,
                buttonsStyling: false,
                confirmButtonText: _language.confirm_btn_delete || "Yes, delete!",
                cancelButtonText: _language.cancel_btn_delete || "No, cancel",
                customClass: {
                    confirmButton: "btn fw-bold btn-danger",
                    cancelButton: "btn fw-bold btn-active-light-primary",
                },
            }).then(function (result) {
                if (result.value) {
                    $.ajax({
                        url: _url_delete,
                        headers: {
                            "X-CSRFToken": $('[name="csrfmiddlewaretoken"]').val(),
                            Authorization: "Basic cm9vdDox",
                            "Content-Type": "application/json",
                        },
                        method: "delete",
                        dataType: "text",
                        contentType: false,
                        processData: false,
                        data: JSON.stringify(arr_selected),
                        success: function (response) {
                            datatable.draw()
                            toastr.success(_language.delete_success || "You have deleted all selected records!.")
                            toastr.options.onHidden = function () {
                                console.log('goodbye');
                                // Remove all selected customers
                                checkboxes.forEach((c) => {
                                    if (c.checked) {
                                        datatable
                                            .row($(c.closest("tbody tr")))
                                            .remove()
                                            .draw();
                                    }
                                });

                                // Remove header checked box
                                const headerCheckbox = table.querySelectorAll('[type="checkbox"]')[0];
                                console.log('---------headerCheckbox', headerCheckbox)
                                headerCheckbox.checked = false;

                                arr_selected = [];
                                toggleToolbars(); // Detect checked checkboxes
                                initToggleToolbar(_url_delete, _language); // Re-init toolbar to recalculate checkboxes

                            }

                        },
                        error: function (request, status, error) {
                            toastr.error(_language.delete_fail || "This record was not deleted.")

                        },
                    });
                } else if (result.dismiss === "cancel") {
                    // Swal.fire({
                    //     text: "Selected customers was not deleted.",
                    //     icon: "error",
                    //     buttonsStyling: false,
                    //     confirmButtonText: "Ok, got it!",
                    //     customClass: {
                    //         confirmButton: "btn fw-bold btn-primary",
                    //     }
                    // });
                }
            });
        });
    };

    // Toggle toolbars
    const toggleToolbars = () => {
        // Select refreshed checkbox DOM elements
        const allCheckboxes = table.querySelectorAll('tbody td [type="checkbox"]');
        // console.log('all checkbox', allCheckboxes)
        // Detect checkboxes state & count
        let checkedState = false;
        let count = 0;

        // Count checked boxes
        allCheckboxes.forEach((c) => {
            if (c.checked) {
                checkedState = true;
                count++;
            }
        });

        // Toggle toolbars
        if (checkedState) {
            selectedCount.innerHTML = count;
            toolbarBase.classList.add("d-none");
            toolbarSelected.classList.remove("d-none");
        } else {
            toolbarBase.classList.remove("d-none");
            toolbarSelected.classList.add("d-none");
        }

        $('input[data-kt-check="true"]').prop("checked", totalCount === count);
    };

    return {
        // Public functions
        init: function (
            _tableId = "",
            _options = {},
            _endpoint = {
                delete: "",
            },
            _language = {},
            _extra_columundefs = [{
                searchable: false, // Disable ordering on column 0 (checkbox)
                targets: 1,

            },]
        ) {
            initTable(_tableId, _options, _endpoint, _language);
            handleSearchDatatable();
            handleViewRow();
            handleEditRow();
            handleResetForm();
            handleFilterDatatable();

            // initToggleToolbar(); // it called in event draw, comment it
            // handleDeleteRows(_endpoint.delete); // it called in event draw, comment it
            return datatable;
        },
    };
})();
