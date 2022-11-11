/*
 * books.js
 * Jeff Ondich, 27 April 2016
 * Updated, 5 November 2020
 *
 * A little bit of Javascript showing one small example of AJAX
 * within the "books and authors" sample for Carleton CS257.
 *
 * This example uses a very simple-minded approach to Javascript
 * program structure. We'll talk more about this after you get
 * a feel for some Javascript basics.
 */

window.onload = initialize;

function initialize() {
    var element = document.getElementById('authors_button');
    element.onclick = onAuthorsButtonClicked;

    var players_by_assists = document.getElementById('players_by_assists');
    players_by_assists.onclick = onPBAssistsClicked;
}

// Returns the base URL of the API, onto which endpoint components can be appended.
function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}
function onPBAssistsClicked() {
    console.log('sort by assists clicked...');
    var url = getAPIBaseURL() + '/authors?sort=assists';
    playerQuery(url, 'Assists');

}
function playerQuery(url, sort_by_arg) {
    fetch(url, { method: 'get' })

        .then((response) => response.json())


        .then(function (authorsList) {

            console.log('resonce found');
            console.log(authorsList.length);
            var tableBody = '<tr><td><h1>Team</h1></td><td><h1>Player</h1></td><td>' + sort_by_arg + '</td></tr>';

            for (var k = 0; k < authorsList.length; k++) {
                tableBody += '<tr>';

                tableBody += '<td>' + authorsList[k]['team'] + '</td>';

                tableBody += '<td><a onclick="getAuthor([' + authorsList[k]['id'] + ",111,112,113,114,115,116],'"
                    + authorsList[k]['name'] + ' ' + authorsList[k]['name'] + "')\">"
                    + authorsList[k]['name'] + '</a></td>';


                //tableBody += "<td>" + authorsList[k]['id'] + '</td>';


                tableBody += '<td>' + authorsList[k]['assists'] + '</td>';

                tableBody += '</tr>';
            }
            var resultsTableElement = document.getElementById('results_table');
            if (resultsTableElement) {
                resultsTableElement.innerHTML = tableBody;
            }

        })
        .catch(function (error) {
            console.log(error);
        });
}

function onAuthorsButtonClicked() {
    var url = getAPIBaseURL() + '/authors';
    playerQuery(url, 'default catogory');
}

function getAuthor(authorID, authorName) {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.
    var url = getAPIBaseURL() + '/books/author/' + authorID;

    fetch(url, { method: 'get' })

        .then((response) => response.json())

        .then(function (booksList) {
            //var tableBody = '<tr><th>' + authorName + '</th></tr>';



            var tableBody = '<tr><th>Name</th>';
            for (var k = 0; k < booksList.length; k++) {
                tableBody += "<th>" + booksList[k]['name'] + "</th>";
            }

            tableBody += '<tr><td>Team</td>';
            for (var k = 0; k < booksList.length; k++) {
                tableBody += "<td>" + booksList[k]['team'] + "</td>";
            }


            tableBody += "</tr><tr><td>3 point</td>";
            for (var k = 0; k < booksList.length; k++) {

                var three_pct;
                if (booksList[k]['three_attempts'] > 0) {
                    var three_pct = booksList[k]['three_makes'] / booksList[k]['three_attempts'] * 100;
                    three_pct = three_pct + " "
                    three_pct = three_pct.substring(0, 5) + "%";
                    three_pct = "" + booksList[k]['three_makes'] + "/" + booksList[k]['three_attempts'] + " (" + three_pct + ")";
                }
                else {
                    three_pct = "" + booksList[k]['three_makes'] + "/" + booksList[k]['three_attempts'];
                }

                tableBody += "<td>" + three_pct + "</td>";
            }


            var resultsTableElement = document.getElementById('results_table');
            if (resultsTableElement) {
                resultsTableElement.innerHTML = tableBody;
            }
        })

        .catch(function (error) {
            console.log(error);
        });
}

