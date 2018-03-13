let table2 = $('#datatables2').DataTable({
    "processing": true,    //comment out to cancel server side
    "serverSide": true,    //comment out to cancel server side
    "ajax": {
        "url": "/api/responses/",
        "type": "GET"
    },
    "columns": [
        {"data": "id"},
        {"data": "risk"},        
        {"data": "responsesCategory"},
        {"data": "description"},        
        {"data": "last_modify_date"},
        {"data": "created"},

        {
            "data": null,
            "defaultContent": '<button type="button" class="btn btn-info">Edit</button>' + '&nbsp;&nbsp' +
            '<button type="button" class="btn btn-danger">Delete</button>'
        }
    ]
});

let id = 0;

$('#datatables2 tbody').on('click', 'button', function () {
    let data = table2.row($(this).parents('tr')).data();
    let class_name = $(this).attr('class');
    if (class_name == 'btn btn-info') {
        // EDIT button
        $('#risk').val(data['risk']);
        $('#responsesCategory').val(data['responsesCategory']);
        $('#description').val(data['description']);
        $('#slug').val(data['slug']);        
        $('#type').val('edit');
        $('#modal_title').text('EDIT');
        $("#myModal").modal();
    } else {
        // DELETE button
        $('#modal_title').text('DELETE');
        $("#confirm").modal();
    }

    id = data['id'];

});

$('form').on('submit', function (e) {
    e.preventDefault();
    let $this = $(this);
    let type = $('#type').val();
    let method = '';
    let url = '/api/responses/';
    if (type == 'new') {
        // new
        method = 'POST';
    } else {
        // edit
        url = url + id + '/';
        method = 'PUT';
    }

    $.ajax({
        url: url,
        method: method,
        data: $this.serialize()
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});

$('#confirm').on('click', '#delete', function (e) {
    $.ajax({
        url: '/api/responses/' + id + '/',
        method: 'DELETE'
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});


$('#new').on('click', function (e) {
    $('#risk').val('');    
    $('#responsesCategory').val('');
    $('#description').val('');  
    $('#type').val('new');
    $('#modal_title').text('NEW');
    $("#myModal").modal();

});


