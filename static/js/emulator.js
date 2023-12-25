
setInterval(connection, 3000)

function connection()
{
    refresh_govno1()
}

function refresh_govno1()
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
        document.getElementById('n_1').value = response['n_1']
        document.getElementById('n_2').value = response['n_2']
        },
    })
}