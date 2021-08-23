$(document).ready(function () {
    $(".addcart").click(function () {
        let identifier = $(this).data("identifier");

        $.ajax({
            method: 'post',
            url: '/product/add-cart',
            data: {
                'identifier': identifier,
            },
            dataType: 'json',
            statusCode: {
                302: function(responseObject, textStatus, errorThrown) {
                    window.location.href = responseObject['responseJSON']['redirect'];
                }
            },
            success: function (responseObject) {
                alert(responseObject['msg']);
            },
            error: function (data, statusText, xhr) {

            }
        })
    })
})