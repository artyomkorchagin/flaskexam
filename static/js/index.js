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
function get_govno_data()
{
    $.ajax(
    {
        type: 'GET',
        url: '/get_govno',
        dataType: 'json',
        connectType: 'application/json',
        data:
        {
        "id1": document.getElementById("id1").value,
        "id2": document.getElementById("id2").value,
        },
        success: function (response)
        {
        document.getElementById("n_1").value = response['n_1']
        document.getElementById("n_2").value = response['n_2']
        },
    })
}
