$(document).ready(function(){


// ============================Single Stock Graph==========================================
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
// ====================================================================================


// ============================Portfolio Graph==========================================
    
    var createPortfolioGraph = function(port, div){
        require.config({
            baseUrl: '/js',
            paths: {
            d3: "http://d3js.org/d3.v3.min"
            }
        });
        console.log(div)
        require(["d3", "c3"], function(d3, c3){
            var date_with_title = port['date_list']
            var dates_only = port['date_list']
            dates_only.shift()
            var sp = port['adj_list']
            console.log(sp)
            var portfolio = port['Portfolio']
            console.log(portfolio)
            var chart = c3.generate({
                bindto: '#'+div.attr('id'),
                data: {
                    x: date_with_title[0],
                    columns: [
                        date_with_title,
                        sp,
                        portfolio
                    ]
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
    
    var portfolioGraph = $("#portfolio_graph");
    var port_data = $('#portfolio_vs_sp').data('returns');
    createPortfolioGraph(port_data, $('#portfolio_vs_sp'))
// ====================================================================================

// =================================Portfolio 3yr===============================================
    
    var portfolioGraphThree = $("#portfolio_vs_sp_three");
    var port_data_three = $('#portfolio_vs_sp_three').data('returns');
    createPortfolioGraph(port_data_three, portfolioGraphThree)


// =================================Portfolio 5yr===============================================

    var portfolioGraphFive = $("#portfolio_vs_sp_five");
    var port_data_three = $('#portfolio_vs_sp_five').data('returns');
    createPortfolioGraph(port_data_three, portfolioGraphFive)


});





