
$(document).ready(function() {
    $("button.add-medal").click(function () {
      var id = $(this).attr("id");
      var medal_id = "#medal_" + id;

        $.ajax({
            url: id + "/medal/",
            data: {},
            dataType: "json",
            success: function(data) {
              if (data.flag == true) {
                $(medal_id).html('<img src="/media/png/starfull.png" hspace="700">');
              }
              else if (data.flag == false) {
                $(medal_id).text("");
              }
            },
            error: function(data) {
              console.log(data);
              alert("status code: " + data.status)
            }
        });
    });
});



$(document).ready(function() {
    function ajax_setup(e){
        e.preventDefault();
        var href = $(this).attr("href");
        $.ajax({
          url: href,
          data: {},
          dataType: "json",
          success: function(data) {
            if (data.id) {
              var id = "#rat_r_" + data.id;
            }
            else {
              var id = "#rat_q";
            }
            $(id).text(data.rating);
          },
          error: function(data) {
            console.log(data);
            alert("status code: " + data.status);
          }
        });
    }
$("a.evaluate-score").click(ajax_setup);
})

