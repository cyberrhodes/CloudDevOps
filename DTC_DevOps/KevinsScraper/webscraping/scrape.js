const request = require('request');
const cheerio = require('cheerio');


//request('https://rhodey35.github.io/candlesam/', (error,
request('https://dyterr.com/our-services/', (error, 
response, html) => {
  if (!error && response.statusCode == 200) {
	const $ = cheerio.load(html);
	
	$('.w3-top a').each((i, el) => {
	  const title = $(el)
	    .find('href')
	    .text()
		.replace(/\s\s+/g, '');
	  		
	  console.log(title);
	});
	
  }
}); 