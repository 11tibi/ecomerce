$(document).ready(function () {
    $("#id_county").change(function () {
        let county_id = $(this).val()

        $.ajax({
            method: 'post',
            url: '/cart/detalii-comanda/city',
            data: {
                'county_id': county_id,
            },
            dataType: 'json',
            success: function(response) {
                $('#id_city').replaceWith(response['html']);
                $('#id_city').prop('disabled', false);
            },
            error: function (response) {
                $('#id_city').replaceWith('<select name="city" class="form-control" disabled="" id="id_city"></select>');
                $('#id_city').prop('disabled', true);
            }
        })
    });
    $('input[name=customer_type]').on('change', function() {
        let input = $('input[name=customer_type]:checked', '#checkout-form').val();
        if (input === 'C' && $('#company').length === 0) {
            $.ajax({
                method: 'post',
                url: '/cart/detalii-comanda/customer-type',
                data: {
                    'customer_type': input,
                },
                dataType: 'json',
                success: function(response) {
                    $('#select-customer').after(response['html']);
                },
            })
        } else {
            $('#company').remove()
        }
    });
})