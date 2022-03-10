$.get("{% url 'api:users-list' %}", function (data) {
      console.log(data);
    });

    var arr_fields =  "{{ fields|safe }}";
    var columns = []

    Object.keys(arr_fields).map(key => {
      columns.push({
        data: arr_fields[key]['col']
      })
    })
    console.log('fields: ', arr_fields)
    console.log('columns: ', columns)
    var table;

    $(document).ready(function () {
      table = $('#table_fields').DataTable({
        'processing': true,
        'serverSide': true,
        'searching': true,
        'searchDelay': 350,
        "autoWidth": false,
        'serverMethod': 'get',
        'ajax': {
          'url': '{% url "api:users-list" %}',
          'dataSrc': 'results',
          'dataFilter': function (data) {
            let json = JSON.parse(data);
            json.recordsTotal = json['count'];
            json.recordsFiltered = json['count'];


            return JSON.stringify(json); // return JSON string
          },
          "data": function (D) {
            console.log('d-------------', D)
            let ordering = '';
            let page = D['start']/D['length']+1


            // TODO: viet cach duyet D['order'] neu sort multi
            if (Array.isArray(D['order']) && D['order'].length > 0) {
              ordering = (D['order'][0]['dir'] === 'desc' ? '-' : '') + arr_fields[D['order'][0]['column']]['col']
            }
            return $.extend(D, {
              ordering,
              limit: D['length'],
              offset: D['start'],
              start: D['start'],
            });
          }
        },
        columnDefs: [],
        order: [],
        columns
      });
    })
