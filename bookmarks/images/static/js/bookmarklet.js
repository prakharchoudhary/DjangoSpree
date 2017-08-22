(function) {
	var jquery_version = '2.1.4';
	var site_url = 'http://127.0.0.1:8000';
	var static_url = site_url + 'static/';
	var min_width = 100;
	var min_height = 100;

	function bookmarklet(msg) {
		// Here goes out bookmarklet code
	};
	// Check if jquery is loaded
	if (typeof window.jQuery != 'undefined') {
		bookmarklet();
	} else {
		// Check for conflicts
		var conflict = typeof window.$ != 'undefined';
		// Create the script and point to Google API
		var script = document.createElement('script');
		script.setAttribute('src', 'https://ajax.googleapis.com/ajax/libs/jquery'+jquery_version+'/jquery.min.js')
	}

}