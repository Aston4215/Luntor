async function fetchHtmlAsText(url) {
    return await (await fetch(url)).text();
}

async function importPage(target) {
    document.querySelector('#' + target).innerHTML = await fetchHtmlAsText('https://teamcrypto.netlify.app/resources/' + target + '.html');
}

importPage('header_' + document.documentElement.lang);
importPage('footer_' + document.documentElement.lang);