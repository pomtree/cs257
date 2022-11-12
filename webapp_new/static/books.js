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

    var compare_bar = document.getElementById('compare_bar');


    var players_by_assists = document.getElementById('players_by_assists');
    var players_by_blocks = document.getElementById('players_by_blocks');
    var players_by_fouls = document.getElementById('players_by_fouls');
    var players_by_threes = document.getElementById('players_by_threes');
    //var players_by_violations = document.getElementById('players_by_violations');
    //var players_by_turnovers_caused = document.getElementById('players_by_turnovers_caused');

    players_by_assists.onclick = Assists;
    players_by_blocks.onclick = Blocks;
    players_by_fts.onclick = FTs;
    players_by_threes.onclick = Threes;
    players_by_fouls.onclick = Fouls;
    players_by_violations = Violations;
    players_by_turnovers_caused = TOsCaused;
    players_by_threes = Threes;

    compare_bar.onclick = CompareGo;

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
function Threes() {
    console.log("thre query start");
    var url = getAPIBaseURL() + '/authors?sort=threes';
    playerQuery(url, 'three_makes', 'three_attempts');
}
function Fouls() {
    var url = getAPIBaseURL() + '/authors?sort=fouls';
    playerQuery(url, 'fouls');
}
function Violations() {
    console.log("violations called");
    var url = getAPIBaseURL() + '/authors?sort=vs';
    playerQuery(url, 'vs');
}
function TOsCaused() {
    var url = getAPIBaseURL() + '/authors?sort=tos_caused';
    playerQuery(url, 'tos_caused');
}
function CompareGo() {
    console.log("compare --");
    checkboxes = document.getElementsByClassName('compare_box');
    console.log(checkboxes.length);
    compare_ids = [];
    for (k = 0; k < checkboxes.length; k++) {
        if (checkboxes[k].checked) {
            //console.log(k);
            //console.log(checkboxes[k].id);
            compare_ids.push(parseInt(checkboxes[k].id.replace('CBID_', '')));
        }
    }
    console.log(compare_ids);
    if(compare_ids.length > 5) {
        //too many elements
        window.alert('The maximum number of players to compare is 5. You provided ' + compare_ids.length);
        compare_ids.length = 5;
    }
    console.log(compare_ids);
    if(compare_ids.length == 0) {
        window.alert('Please select players to compare');
        return;
    }
    console.log('querrying...');
    getAuthor(compare_ids);
}



function playerQuery(url, sort_by_arg, sort_by_arg2 = false) {
    fetch(url, { method: 'get' })

        .then((response) => response.json())


        .then(function (authorsList) {

            console.log('resonce found');
            console.log(authorsList.length);
            data = [];
            tableBody = "<tr><td><h1>Rank</h1></td><td><h1>Team</h1></td><td><h1>Player</h1></td>";
            for (k = 0; k < authorsList.length; k++) {
                if (sort_by_arg2) {
                    console.log('2 sorting args...');
                    data.push(authorsList[k][sort_by_arg] / authorsList[k][sort_by_arg2]);
                }
                else {
                    data.push(authorsList[k][sort_by_arg]);
                }
            }
            if (sort_by_arg2) {
                tableBody += '<td><h1 class = \"capitalize\">' + sort_by_arg.replace('_makes', ' %') + '</h1></td><td>Makes</td><td>Attempts</td><td>Compare</td></tr>';
            }
            else {
                tableBody += '<td><h1 class = \"capitalize\">' + sort_by_arg + '</h1></td><td>Compare</td></tr>';
            }

            rank = 1;
            for (var k = 0; k < data.length; k++) {
                tableBody += '<tr>';



                if (k > 0) {
                    if (data[k] < data[k - 1]) {
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
                    if (k == data.length - 1) {
                        tableBody += '<td>' + (k - rank + 2) + '</td>';
                    }
                    else {
                        if (data[k] == data[k + 1]) {
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


                if (sort_by_arg2) {
                    pct = ((data[k] * 100) + "").substring(0, 5) + "%";
                    tableBody += '<td>' + pct + '</td>';
                    tableBody += '<td>' + authorsList[k][sort_by_arg] + '</td>';
                    tableBody += '<td>' + authorsList[k][sort_by_arg2] + '</td>';
                }
                else {
                    tableBody += '<td>' + data[k] + '</td>';
                }
                //console.log(authorsList[k]['blocks']);

                tableBody += '<td><center><input type=checkbox id=CBID_' + authorsList[k].id + ' class="compare_box"></td ></center ></tr > ';
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