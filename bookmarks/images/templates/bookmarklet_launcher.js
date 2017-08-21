(function() {
	if (window.myBookmarklet !== undefined) {
		myBookmarklet();
	}
	else {
		document.body.appendChild(document.createElement('script')).
		src='http://127.0.0.1:8000/static/js/bookmarklet.js?r='+Math.
		floor(Math.random()*99999999999999999999);
	}
}) ();

/*
This script discovers if the bookmarklet is already loaded by checking if the
myBookmarklet variable is defined. By doing so, we avoid loading it again if the
user clicks on the bookmarklet repeatedly. If myBookmarklet is not defined, we load
another JavaScript file adding a <script> element to the document.
*/