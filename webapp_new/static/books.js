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
    var players_by_blocks = document.getElementById('players_by_blocks');

    players_by_assists.onclick = Assists;
    players_by_blocks.onclick = Blocks;
    players_by_fts.onclick = FTs;

}

// Returns the base URL of the API, onto which endpoint components can be appended.
function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}
function Blocks() {
    var url = getAPIBaseURL() + '/authors?sort=blocks';
    playerQuery(url, 'blocks');
}
function Assists() {
    console.log('sort by assists clicked...');
    var url = getAPIBaseURL() + '/authors?sort=assists';
    playerQuery(url, 'assists');
}
function FTs() {
    var url = getAPIBaseURL() + '/authors?sort=blocks';
    playerQuery(url, 'ft_makes', 'ft_attempts');
}



function playerQuery(url, sort_by_arg) {
    fetch(url, { method: 'get' })

        .then((response) => response.json())


        .then(function (authorsList) {

            console.log('resonce found');
            console.log(authorsList.length);
            var tableBody = '<tr><td><h1>Rank</h1></td><td><h1>Team</h1></td><td><h1>Player</h1></td><td><h1 class = \"capitalize\">' + sort_by_arg + '</h1></td></tr>';
            rank = 1;
            for (var k = 0; k < authorsList.length; k++) {
                tableBody += '<tr>';



                if (k > 0) {
                    if (authorsList[k][sort_by_arg] < authorsList[k - 1][sort_by_arg]) {
                        rank = 1;
                    }
                    else {
                        rank++;
                    }
                }
                else {
                    rank = 1;
                }
                if (rank <= 1) {
                    if (k == authorsList.length - 1) {
                        tableBody += '<td>' + (k - rank + 2) + '</td>';
                    }
                    else {
                        if (authorsList[k][sort_by_arg] == authorsList[k + 1][sort_by_arg]) {
                            tableBody += '<td>=' + (k - rank + 2) + '</td>';
                        }
                        else {

                            tableBody += '<td>' + (k - rank + 2) + '</td>';
                        }
                    }
                }
                else {
                    //tableBody += '<td>=' + (k - rank + 2) + '</td>';
                    tableBody += '<td></td>';
                }
                //tableBody += '<td>=' + rank + ' | ' + k + '</td>';
                tableBody += '<td>' + authorsList[k]['team'] + '</td>';

                tableBody += '<td><a onclick="getAuthor([' + authorsList[k]['id'] + ",111,112,113,114,115,116],'"
                    + authorsList[k]['name'] + ' ' + authorsList[k]['name'] + "')\">"
                    + authorsList[k]['name'] + '</a></td>';


                //tableBody += "<td>" + authorsList[k]['id'] + '</td>';


                tableBody += '<td>' + authorsList[k][sort_by_arg] + '</td>';

                //console.log(authorsList[k]['blocks']);

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

            tableBody += '<tr><td>Assists</td>' + basic_stat_row_gen(booksList, "assists");

            tableBody += '<tr><td>Blocks</td>' + basic_stat_row_gen(booksList, "blocks");

            tableBody += '<tr><td>Fouls</td>' + basic_stat_row_gen(booksList, "fouls", true);

            //broken rows commented out
            //tableBody += '<tr><td>Fouled</td>' + basic_stat_row_gen(booksList, "fouled");

            //tableBody += '<tr><td>Rebounds</td>' + basic_stat_row_gen(booksList, "rbs");

            tableBody += '<tr><td>Violations</td>' + basic_stat_row_gen(booksList, "vs", true);

            //tableBody += '<tr><td>Turnovers</td>' + basic_stat_row_gen(booksList, "tos", true);

            tableBody += '<tr><td>Turnovers Caused</td>' + basic_stat_row_gen(booksList, "tos_caused");


            tableBody += "</tr><tr><td>3 point % </td>";
            tableBody += pct_gen(booksList, "three");

            tableBody += "</tr><tr><td>layup % </td>";
            tableBody += pct_gen(booksList, "layup");

            tableBody += "</tr><tr><td>jump % </td>";
            tableBody += pct_gen(booksList, "jumper");

            //currently broken: (see to do)
            // tableBody += "</tr><tr><td>hook % </td>";
            // tableBody += pct_gen(booksList, "hook");

            // tableBody += "</tr><tr><td>dunk % </td>";
            // tableBody += pct_gen(booksList, "dunk");            

            //tableBody += "</tr><tr><td>free throw % </td>";
            //tableBody += pct_gen(booksList, "ft");


            var resultsTableElement = document.getElementById('results_table');
            if (resultsTableElement) {
                resultsTableElement.innerHTML = tableBody;
            }
        })

        .catch(function (error) {
            console.log(error);
        });
}
function basic_stat_row_gen(booksList, stat, reverse = false) {
    output = "";
    stat_list = [];
    for (k = 0; k < booksList.length; k++) {
        stat_list.push(booksList[k][stat])
    }
    if (reverse) {
        console.log("reverse" + stat);
        min_arr = max(stat_list);
        max_arr = min(stat_list);
    }
    else {
        max_arr = max(stat_list);
        min_arr = min(stat_list);
    }
    for (var k = 0; k < booksList.length; k++) {
        if (max_arr.includes(k)) {
            output += "<td class = \"winner\">" + stat_list[k] + "</td>";
        }
        else if (min_arr.includes(k) || stat[k] == 0) {
            console.log(min_arr);
            output += "<td class = \"loser\">" + stat_list[k] + "</td>";
        }
        else {
            output += "<td>" + stat_list[k] + "</td>";
        }
    }
    return output;
}

function pct_gen(booksList, type) {
    attempts = type + "_attempts";
    makes = type + "_makes";
    tableBody = "";
    var pcts = [];
    var pcts_strings = [];
    for (var k = 0; k < booksList.length; k++) {

        var pct;

        if (booksList[k][attempts] > 0) {
            var pct = booksList[k][makes] / booksList[k][attempts] * 100;
            //cts.push(parseInt(pct));
            pcts.push(pct);
            pct = pct + "";
            pct = pct.substring(0, 5) + "%";
            pct.replace(' ', '');
            //pct = "" + booksList[k]['makes'] + "/" + booksList[k]['attempts'] + " (" + pct + ")";
            pct = pct + " (" + booksList[k][makes] + "/" + booksList[k][attempts] + ")";
        }
        else {
            pcts.push(0);
            pct = "" + booksList[k][makes] + "/" + booksList[k][attempts];
        }
        pcts_strings.push(pct);


    }
    max_arr = max(pcts);
    min_arr = min(pcts);
    for (var k = 0; k < booksList.length; k++) {
        if (max_arr.includes(k)) {
            tableBody += "<td class = \"winner\">" + pcts_strings[k] + "</td>";
        }
        else if (min_arr.includes(k) || pcts[k] == 0) {
            console.log(min_arr);
            tableBody += "<td class = \"loser\">" + pcts_strings[k] + "</td>";
        }
        else {
            tableBody += "<td>" + pcts_strings[k] + "</td>";
        }
        //tableBody += "<td>" + Math.max(pcts) + ' | ' + pcts[k] + "</td>";
        //console.log(Math.max(float_array));
        //console.log(pcts);
        //console.log(max(pcts));
        //console.log(float_array);
    }
    return tableBody;

}



function max(array) {
    var current_max = -1;
    var max_pos = [];
    var i = 0;
    while (i < array.length) {
        if (array[i] > current_max) {
            max_pos = [i];
            current_max = array[i];
        }
        else if (array[i] == current_max) {
            max_pos.push(i);
        }
        i++;
    }
    return max_pos;
}
function min(array) {
    var current_min = Infinity;
    var min_pos = [];
    var i = 0;
    while (i < array.length) {
        if (array[i] == 0) {
            min_pos.push(i);
        }
        else if (array[i] < current_min) {
            console.log("reset min");
            min_pos = [];
            min_pos.push(i);
            current_min = array[i];
        }
        else if (array[i] == current_min) {
            console.log("min equal");
            min_pos.push(i);
        }
        i++;
    }
    return min_pos;
}