function send_jopa_data()
{
    $.ajax(
    {
        type: 'GET',
        url: '/get_jopa',
        dataType: 'json',
        connectType: 'application/json',
        data:
        {

        },
        success: function (response)
        {
            document.getElementById("jopa_out").value = document.getElementById("jopaID").value
        }
    })
}