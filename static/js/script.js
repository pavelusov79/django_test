$(document).ready(function () {
    $('#id_country').change(function() {
        var country = $(this).val();
        console.log('country = ', country)
        $.ajax({
            type: 'GET',
            url: '/load_regions/',
            data: {'country': country},
            success: function(response) {
                $('#id_region').html(response);
            }
        });
    });
});
