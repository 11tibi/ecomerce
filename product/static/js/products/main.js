$(document).ready(function () {
    // on hover
    $('#stars li').on('mouseover', function () {
        var onStar = parseInt($(this).data('value'), 10);
        $(this).parent().children('li.star').each(function (e) {
            if (e < onStar) {
                $(this).addClass('hover');
            } else {
                $(this).removeClass('hover');
            }
        });
    }).on('mouseout', function () {
        $(this).parent().children('li.star').each(function (e) {
            $(this).removeClass('hover');
        });
    });

    // on click
    $('#stars li').on('click', function () {
        var onStar = parseInt($(this).data('value'), 10);
        var stars = $(this).parent().children('li.star');
        for (i = 0; i < stars.length; i++) {
            $(stars[i]).removeClass('selected');
        }
        for (i = 0; i < onStar; i++) {
            $(stars[i]).addClass('selected');
        }
        $("#rating-hidden").val(onStar)
    });
});

$(document).ready(function () {
    $("#delete-review").click(function () {
        var id = $("#delete").data("id");

        $.ajax({
            method: 'post',
            url: "/product/delete-review",
            data: {
                "id": id,
            },
            dataType: 'json',
            success: function (response) {
                $("#exampleModal").modal("hide");
                $("#delete").parents().eq(3).remove();
                $("[id=reviews-number]").text($("#reviews-number").text() - 1);
                $("#add-review-section").attr('hidden', false);

                alert(response['responseJSON']['msg']);
            },
            error: function (response) {
                alert(response['responseJSON']['msg']);
            },
        });
    })
})