let table = $('#datatables').DataTable({
    "processing": true,    //comment out to cancel server side
    "serverSide": true,    //comment out to cancel server side
    "ajax": {
        "url": "/api/hazard/",
        "type": "GET"
    },
    "columns": [
        {"data": "id"},
        {"data": "title"},
        {"data": "parent"},
        {"data": "description"},
        {"data": "slug"},        
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

$('#datatables tbody').on('click', 'button', function () {
    let data = table.row($(this).parents('tr')).data();
    let class_name = $(this).attr('class');
    if (class_name == 'btn btn-info') {
        // EDIT button
        $('#title').val(data['title']);
        $('#parent').val(data['parent']);
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
    let url = '/api/hazard/';
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
        url: '/api/hazard/' + id + '/',
        method: 'DELETE'
    }).success(function (data, textStatus, jqXHR) {
        location.reload();
    }).error(function (jqXHR, textStatus, errorThrown) {
        console.log(jqXHR)
    });
});


$('#new').on('click', function (e) {
    $('#title').val('');
    $('#parent').val('');
    $('#description').val('');
    $('#slug').val('');    
    $('#type').val('new');
    $('#modal_title').text('NEW');
    $("#myModal").modal();
});


