
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
        url: '/load_govno',
        dataType: 'json',
        connectType: 'application/json',
        data:
        {
        'id1': document.getElementById('id1').value,
        'id2': document.getElementById('id2').value,
        },
        success: function (response)
        {

        },
    })
}

function create_chart() {
    $.ajax({
        type: 'GET',
        url: '/get_chart',
        dataType: 'json',
        contentType: 'application/json',
        data: {},
        success: function (response) {
            new Chart(
                document.querySelector('.chart'),{
                    type: 'line',
                    data: {
                        labels: response['time_data'],
                        datasets: [
                            {
                                borderColor:'blue',
                                backgroundColor:'skyblue',
                                label: "Динамика изменения говна",
                                data: response['temp_data'],
                                cubicInterpolationMode: 'monotone',
                                fill: true
                            }
                        ]
                    },
                    options: {
                        backgroundColor:'skyblue',
                        responsive: false
                    }
                }
            );
        }
    });
}
