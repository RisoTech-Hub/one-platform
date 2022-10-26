"use strict";
function initFileUploader(fileUploader_url, template_strings, fileTemplate_strings, token, messages, size) {
  new qq.FileUploader({
    element: $('#file-uploader > div').get(0),
    action: fileUploader_url,

    template: '<div class="qq-uploader">' +
      '<div class="qq-upload-drop-area"><span>'+template_strings.drop_area+'</span></div>' +
      '<div class="qq-upload-button">'+template_strings.upload_btn+'</div>' +
      '<div class="qq-upload-list"></div>' +
      '</div>',

    fileTemplate: '<div>' +
      '<span class="qq-upload-file"></span>' +
      '<span class="qq-upload-spinner"></span>' +
      '<span class="qq-upload-size"></span>' +
      '<a class="qq-upload-cancel" href="#">'+fileTemplate_strings.cancel+'</a>' +
      '<span class="qq-upload-failed-text">'+fileTemplate_strings.failed+'</span>' +
      '<span class="qq-upload-complete"></span>' +
      '<div class="progress-bar"><div class="content"></div></div>' +
      '</div>',

    params: {
      'csrf_token': token,
      'csrf_name': 'csrfmiddlewaretoken',
      'csrf_xname': 'X-CSRFToken',
      'folder': '',
    },

    allowedExtensions: ['.jpg', '.jpeg', '.gif', '.png', '.tif', '.tiff', '.pdf', '.doc', '.rtf', '.txt', '.xls', '.csv', '.docx', '.mov', '.mp4', '.m4v', '.webm', '.wmv', '.mpeg', '.mpg', '.avi', '.rm', '.mp3', '.wav', '.aiff', '.midi', '.m4p'],
    sizeLimit: size,
    minSizeLimit: 0,
    debug: false,
    // messages
    messages: messages,

    getItem: function (id) {
      var items = $(this.element).find('.qq-upload-list > div').get();
      var item = items.pop();

      while (typeof item != "undefined") {
        if (item.qqFileId == id) {
          return $(item);
        }
        item = items.pop();
      }
    },
    onProgress: function (id, fileName, loaded, total) {
      var bar = this.getItem(id).find('.progress-bar .content');
      var new_width = '' + (loaded / total * 100) + '%';
      bar.css('width', new_width);
    },
    onComplete: function (id, fileName, resp) {
      if (resp.success) {
        this.getItem(id).find('.qq-upload-file').html('<a href="' + resp.url + '">' + resp.filename + '</a>');
      }
    },
    showMessage: function (message) {
      alert(message);
    }
  });
}
