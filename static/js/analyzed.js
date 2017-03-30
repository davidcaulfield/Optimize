$(document).ready(function(){

	var chartButton = $('#chart_button');
	chartButton.on('click', function() {

		var graph = $('.graph');
		graph.css('display', 'block');
		var ticker = $('.chart_button').data('ticker');
		$.ajax(
        {
            url: '/chart-data/'+ticker,
            method: 'GET',
            success: function(result){
                console.log(result)
                // data = JSON.parse(result);
                // // console.log('data')
                // // console.log(data)
                // $('.loader').css('display','none')
                // tesla_info = data['result']['tesla']
                // coke_info = data['result']['coke']
                // snap_info = data['result']['snap']
                // // return data
            }
        }
)




	});
	console.log(chartButton);




});