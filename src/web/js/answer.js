$(document).ready(function () {
    $.ajax({
        url: '/answer',
        type: 'GET',
        dataType: 'json',
        success: function (data) {
            $('#result-container').text(JSON.stringify(data, null, 2));
        },
        error: function (error) {
            console.error('Error fetching data:', error);
            $('#result-container').text('Error fetching data. Check console for details.');
        }
    });
});