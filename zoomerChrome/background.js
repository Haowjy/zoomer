console.log("from background")
chrome.identity.getAuthToken({ 'interactive': true }, function(token) {
  console.log(token)
});