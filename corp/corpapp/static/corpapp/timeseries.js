function renderChart(country, dom) {
	// State should be confirmed, deaths, or recovered

	var state = "confirmed";
	url = "https://covid.ourworldindata.org/data/ecdc/total_cases.csv";

	$.get(url).done(function (response) {
		data = $.csv.toObjects(response);
		dates = data.map(function(x){ return x.date; });
		vals = data.map(function(x){ return parseInt(x[country]); });
		world = data.map(function(x){ return parseInt(x.World); });

		scale = Math.max(...vals) / Math.max(...world);
		world = world.map(function(x){ return x*scale; });

		let chart = new frappe.Chart("#chart", {
			data: {
				labels: dates,
				datasets: [
	   			   { name: "World (Normalized)", chartType: 'line', values: world },
   				   { name: country, chartType: 'line', values: vals },
				],
			},

			title: state+" cases in "+country,
			type: 'axis-mixed', // or 'bar', 'line', 'pie', 'percentage'
			//height: 300,
			colors: ['#bbb', '#800080'],

			tooltipOptions: {
			   formatTooltipX: d => (d + '').toUpperCase(),
			   formatTooltipY: d => d,
			}
			});
	});
}
