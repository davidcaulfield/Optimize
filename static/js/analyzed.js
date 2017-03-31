$(document).ready(function(){

    var createGraph = function(result, div){

        require.config({
            baseUrl: '/js',
            paths: {
            d3: "http://d3js.org/d3.v3.min"
              }
        });
        
        require(["d3", "c3"], function(d3, c3){
            
            var data = JSON.parse(result)
            var cdate = data['date_list']
            cdate.unshift('Dates')
            var date = data['date_list']
            console.log(cdate[0])
            date.shift()
            var sp = data['adj_list']
            var stock = data['ticker']
            var chart = c3.generate({
                bindto: '#'+div.attr('id'),
                data: {
                    x: cdate[0],
                    columns: [cdate,
                        sp,
                        stock

                    ],
                },
                axis: {
                    y:{
                        label: {
                            text:"Percent Change",
                            position:'inner-middle'
                        }
                    },
                    x: {
                        type: 'timeseries',
                        tick: {
                            format: '%Y-%m-%d'
                        }
                   
                    }
                }
            });
        });
    }; 

	var chartButton = $('#chart_button');
	chartButton.on('click', function() {

		var graph = $('.chart_title');
		graph.css('display', 'block');
		var ticker = $('.chart_button').data('ticker');
		$.ajax(
        {
            url: '/chart-data/'+ticker,
            method: 'GET',
            success: function(result){
                var data = result
                var date = result['date_list']
                var sp = result['adj_list']
                var stock = result['ticker']
                createGraph(data, $('#graph'))
                $('.close_graph').on('click', function(){
                    graph.css('display','none')
                })  
            }
        }
        )




	});
	console.log(chartButton);




});





