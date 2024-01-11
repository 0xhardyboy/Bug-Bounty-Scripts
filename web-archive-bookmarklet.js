javascript:(function() {
    var currentURL = encodeURIComponent(window.location.hostname.replace(/^www\./, ''));
    var newURL = 'https://web.archive.org/cdx/search/cdx?url=*.' + currentURL + '&fl=original&collapse=urlkey';
    window.open(newURL, '_blank');
})();
