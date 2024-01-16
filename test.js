const axios = require('axios');

const accessToken = 'e4962e96-cd4a-32d0-ab13-ab9f131c03e0';
const apiUrl = 'https://api.vonage.com/t/vbc.prod/reports/accounts/190230/call-logs';

// Example query parameters
const params = {
  'start:gte': '2024-01-15 00:00:00',
  'start:lte': '2024-01-15 17:00:00',
  page_size: '10000',
  page: '1'
};

// Convert params to a query string with percent-encoded names and values
const queryString = Object.entries(params)
  .map(([key, value]) => `${encodeURIComponent(key)}=${encodeURIComponent(value)}`)
  .join('&');

axios.get(apiUrl + '?' + queryString, {
  headers: {
    'Authorization': `Bearer ${accessToken}`,
  }
})

.then(response => {
  const jsonData = response.data._embedded.call_logs;

  const fs = require('fs');

  // Convert JSON to string
  const jsonString = JSON.stringify(jsonData, null, 2); // The third parameter (2) specifies the number of spaces to use for indentation

  // Specify the file path
  const filePath = 'output.json';

  // Write the JSON data to the file
  fs.writeFile(filePath, jsonString, 'utf-8', (err) => {
  if (err) {
    console.error('Error writing JSON to file:', err);
  } else {
      console.log('JSON data has been written to', filePath);
  }
});

  
/*   // Iterate through each call log object
  callLogs.forEach((callLog, index) => {
    console.log(`Call Log ${index + 1}:`, callLog);
    // Access specific properties within each call log object if needed
    // Example: console.log('Call Duration:', callLog.duration);
  });

  // You can also access pagination details
  console.log('Pagination Details:', response.data._links);

})
.catch(error => {
  console.error('Error details:', error.message);
}); */
});
