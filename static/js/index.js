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
function send_govno_data()
{
    $.ajax(
    {
        type: 'GET',
        url: '/get_govno',
        dataType: 'json',
        connectType: 'application/json',
        data:
        {

        },
        success: function (response)
        {
            document.getElementById("n_1").value = document.getElementById("id1").value
            document.getElementById("n_2").value = document.getElementById("id2").value
        }
    })
}