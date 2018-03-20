let riskTableAttribute = $("#datatables").attr("modelslug")
let table = $('#datatables').DataTable({
    // "processing": true,    //comment out to cancel server side
    // "serverSide": true,    //comment out to cancel server side
    "ajax": {
        "url": "/api/risk/" + riskTableAttribute + "/",
        "type": "GET",
    },
    "columns": [
        {"data": "id"},
        { "data": "title"
//        { "data": "title",
//       "fnCreatedCell": function (nTd, sData, oData, iRow, iCol) {
//            $(nTd).html("<a href='" + window.location.href + oData.slug + "/'>" + oData.title+ "</a>");
//            }
        },
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
    let url = '/api/risk/';
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
        url: '/api/risk/' + id + '/',
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

let responseTableAttribute = $("#datatables2").attr("modelslug")
let responseTable = $('#datatables2').DataTable({
    // "processing": true,    //comment out to cancel server side
    // "serverSide": true,    //comment out to cancel server side
    "ajax": {
        "url": "/api/responses/" + responseTableAttribute + "/",
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

$('#datatables2 tbody').on('click', 'button', function () {
    let data = responseTable.row($(this).parents('tr')).data();
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