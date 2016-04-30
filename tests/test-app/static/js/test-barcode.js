
function create_barcode_obj(s) {
	//$("#barcode").empty();
	var div = document.createElementNS("http://www.w3.org/1999/xhtml", "div");
	div.innerHTML = s;
	return $(div);
}

function post_barcode(barcode_format, barcode_string) {
	$.ajax({
		type: "POST",
		url: "/api/barcode",
		data: {
			"barcode_format": barcode_format,
			"barcode_string": barcode_string
		},
		dataType: "json"
	})
	.success(function(data) {
		var barcode = create_barcode_obj(data.barcode_svg);
		$("#barcode").append(barcode);
	})
	.fail(function(error) {
		console.log(error);
		console.log(error.responseText);
		$("#error").text(error.responseText);
	});
}

function barcode_button() {
	$("#barcode_button").on("click", function (e) {
		$("#error").empty();
		try {
			post_barcode($("#barcode_format").val(), $("#barcode_string").val());
		} catch(err) {
			console.log(err);
		}
		e.preventDefault();
	});
}

$(document).ready(function () {
	barcode_button();

});
