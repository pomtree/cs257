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

    var search_players_go = document.getElementById('player_search_bar_go');
    search_players_go.onclick = SearchPlayers;

    var instant_compare = document.getElementById('instant_compare');
    instant_compare.onclick = InstantCompare;


    var players_by_assists = document.getElementById('players_by_assists');
    var players_by_blocks = document.getElementById('players_by_blocks');
    var players_by_fouls = document.getElementById('players_by_fouls');

    var players_by_threes = document.getElementById('players_by_threes');

    var players_by_violations = document.getElementById('players_by_violations');

    console.log(players_by_violations);
    console.log(players_by_assists);

    var players_by_turnovers_caused = document.getElementById('players_by_turnovers_caused');

    players_by_assists.onclick = Assists;
    players_by_blocks.onclick = Blocks;
    players_by_fts.onclick = FTs;
    players_by_threes.onclick = Threes;
    players_by_fouls.onclick = Fouls;
    players_by_violations.onclick = Violations;
    players_by_turnovers_caused.onclick = TOsCaused;
    players_by_threes = Threes;


    var compare_bar = document.getElementById('compare_bar');
    compare_bar.onclick = CompareGo;

}

// Returns the base URL of the API, onto which endpoint components can be appended.
function getAPIBaseURL() {
    var baseURL = window.location.protocol + '//' + window.location.hostname + ':' + window.location.port + '/api';
    return baseURL;
}
function Blocks() {
    var url = getAPIBaseURL() + '/players/search?sort=blocks';
    playerQuery('Blocks', url, 'blocks');
}
function Assists() {
    console.log('sort by assists clicked...');
    var url = getAPIBaseURL() + '/players/search?sort=assists';
    playerQuery('Assists', url, 'assists');
}
function FTs() {
    var url = getAPIBaseURL() + '/players/search?sort=blocks';
    playerQuery('Free Throw %', url, 'ft_makes', 'ft_attempts');
}
function Threes() {
    console.log("thre query start");
    var url = getAPIBaseURL() + '/players/search?sort=threes';
    playerQuery('Three %', url, 'three_makes', 'three_attempts');
}
function Fouls() {
    var url = getAPIBaseURL() + '/players/search?sort=fouls';
    playerQuery('Fouls', url, 'fouls');
}
function Violations() {
    console.log("violations called");
    var url = getAPIBaseURL() + '/players/search?sort=vs';
    playerQuery('Violations', url, 'vs');
}
function TOsCaused() {
    var url = getAPIBaseURL() + '/players/search?sort=tos_caused';
    playerQuery('Turnovers Caused', url, 'tos_caused');
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
    if (compare_ids.length > 5) {
        //too many elements
        window.alert('The maximum number of players to compare is 5. You provided ' + compare_ids.length);
        compare_ids.length = 5;
    }
    console.log(compare_ids);
    if (compare_ids.length == 0) {
        window.alert('Please select players to compare');
        return;
    }
    console.log('querrying...');
    comparePlayers(compare_ids);
}
function InstantCompare() {
    search_input = document.getElementById("search");
    console.log(search_input.value);
    url = getAPIBaseURL() + '/players/search?q=' + search_input.value;
    fetch(url, { method: 'get' })
        .then((response) => response.json())


        .then(function (playerResults) {

            ids = [];
            for(var k = 0; k < playerResults.length; k++) {
                ids.push(playerResults[k]['id']);
            }
            console.log(ids);
            comparePlayers(ids);

        })
        .catch(function (error) {
            console.log(error);
        });

}

function SearchPlayers() {
    search_input = document.getElementById("search");
    console.log(search_input.value);
    url = getAPIBaseURL() + '/players/search?q=' + search_input.value;
    fetch(url, { method: 'get' })
        .then((response) => response.json())


        .then(function (playerResults) {

            console.log('resonce found');
            console.log(playerResults.length);
            tableBody = "<tr><td><h1>Team</h1></td><td><h1>Player</h1></td><td>Compare</td></tr>";

            //tableBody += '<td>=' + rank + ' | ' + k + '</td>';
            for (k = 0; k < playerResults.length; k++) {
                tableBody += '<td>' + playerResults[k]['team'] + '</td>';

                tableBody += '<td><a onclick="comparePlayers([' + playerResults[k]['id'] + "],'"
                    + playerResults[k]['name'] + ' ' + playerResults[k]['name'] + "')\">"
                    + playerResults[k]['name'] + '</a></td>';


                tableBody += '<td><center><input type=checkbox id=CBID_' + playerResults[k].id + ' class="compare_box"></td ></center ></tr > ';
            }

            tableBody += '<ul class="vertical-navbar"><li><a id="compare_bar">(broken compare)</a></li></ul>';

            var resultsTableElement = document.getElementById('results_table');
            if (resultsTableElement) {
                resultsTableElement.innerHTML = tableBody;
            }

        })
        .catch(function (error) {
            console.log(error);
        });

}




function playerQuery(title, url, sort_by_arg, sort_by_arg2 = false) {

    console.log('pq nm 1: ' + sort_by_arg + ' 2 ' + sort_by_arg2);

    playerQueryMain(title, url, sort_by_arg, sort_by_arg2);


    var compare_bar = document.getElementById('compare_bar');
    compare_bar.onclick = CompareGo;

}

function playerQueryMain(title, url, sort_by_arg, sort_by_arg2) {
    fetch(url, { method: 'get' })

        .then((response) => response.json())


        .then(function (playerList) {

            console.log('resonce found' + sort_by_arg + ' 2:' + sort_by_arg2);
            console.log(playerList.length);
            data = [];
            tableBody = "<tr><td><h1>Rank</h1></td><td><h1>Team</h1></td><td><h1>Player</h1></td>";
            for (k = 0; k < playerList.length; k++) {
                if (sort_by_arg2) {
                    console.log('2 sorting args...');
                    data.push(playerList[k][sort_by_arg] / playerList[k][sort_by_arg2]);
                }
                else {
                    data.push(playerList[k][sort_by_arg]);
                }
            }
            if (sort_by_arg2) {
                tableBody += '<td><h1 class = \"capitalize\">' + sort_by_arg.replace('_makes', ' %') + '</h1></td><td>Makes</td><td>Attempts</td><td>Compare</td></tr>';
            }
            else {
                tableBody += '<td><h1 class = \"capitalize\">' + title + '</h1></td><td>Compare</td></tr>';
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
                tableBody += '<td>' + playerList[k]['team'] + '</td>';

                tableBody += '<td><a onclick="comparePlayers([' + playerList[k]['id'] + "],'"
                    + playerList[k]['name'] + ' ' + playerList[k]['name'] + "')\">"
                    + playerList[k]['name'] + '</a></td>';

                if (sort_by_arg2) {
                    pct = ((data[k] * 100) + "").substring(0, 5) + "%";
                    tableBody += '<td>' + pct + '</td>';
                    tableBody += '<td>' + playerList[k][sort_by_arg] + '</td>';
                    tableBody += '<td>' + playerList[k][sort_by_arg2] + '</td>';
                }
                else {
                    tableBody += '<td>' + data[k] + '</td>';
                }


                tableBody += '<td><center><input type=checkbox id=CBID_' + playerList[k].id + ' class="compare_box"></td ></center ></tr > ';
            }
            tableBody += '<ul class="vertical-navbar"><li><a id="compare_bar">(broken compare)</a></li></ul>';
            var resultsTableElement = document.getElementById('results_table');
            if (resultsTableElement) {
                resultsTableElement.innerHTML = tableBody;
            }

        })
        .catch(function (error) {
            console.log(error);
        });
}


function comparePlayers(playerIDs) {
    // Very similar pattern to onAuthorsButtonClicked, so I'm not
    // repeating those comments here. Read through this code
    // and see if it makes sense to you.
    var url = getAPIBaseURL() + '/players/details/' + playerIDs;

    fetch(url, { method: 'get' })

        .then((response) => response.json())

        .then(function (playersList) {

            var tableBody = '<tr><th>Name</th>';
            for (var k = 0; k < playersList.length; k++) {
                tableBody += "<th>" + playersList[k]['name'] + "</th>";
            }

            tableBody += '<tr><td>Team</td>';
            for (var k = 0; k < playersList.length; k++) {
                tableBody += "<td>" + playersList[k]['team'] + "</td>";
            }

            tableBody += '<tr><td>Assists</td>' + basic_stat_row_gen(playersList, "assists");

            tableBody += '<tr><td>Blocks</td>' + basic_stat_row_gen(playersList, "blocks");

            tableBody += '<tr><td>Fouls</td>' + basic_stat_row_gen(playersList, "fouls", true);

            //broken rows commented out
            //tableBody += '<tr><td>Fouled</td>' + basic_stat_row_gen(playersList, "fouled");

            //tableBody += '<tr><td>Rebounds</td>' + basic_stat_row_gen(playersList, "rbs");

            tableBody += '<tr><td>Violations</td>' + basic_stat_row_gen(playersList, "vs", true);

            //tableBody += '<tr><td>Turnovers</td>' + basic_stat_row_gen(playersList, "tos", true);

            tableBody += '<tr><td>Turnovers Caused</td>' + basic_stat_row_gen(playersList, "tos_caused");


            tableBody += "</tr><tr><td>3 point % </td>";
            tableBody += pct_gen(playersList, "three");

            tableBody += "</tr><tr><td>Layup % </td>";
            tableBody += pct_gen(playersList, "layup");

            tableBody += "</tr><tr><td>Jump % </td>";
            tableBody += pct_gen(playersList, "jumper");

            //currently broken: (see to do)
            // tableBody += "</tr><tr><td>hook % </td>";
            // tableBody += pct_gen(playersList, "hook");

            // tableBody += "</tr><tr><td>dunk % </td>";
            // tableBody += pct_gen(playersList, "dunk");            

            //tableBody += "</tr><tr><td>free throw % </td>";
            //tableBody += pct_gen(playersList, "ft");


            var resultsTableElement = document.getElementById('results_table');
            if (resultsTableElement) {
                resultsTableElement.innerHTML = tableBody;
            }
        })

        .catch(function (error) {
            console.log(error);
        });
}
function basic_stat_row_gen(playersList, stat, reverse = false) {
    output = "";
    stat_list = [];
    for (k = 0; k < playersList.length; k++) {
        stat_list.push(playersList[k][stat])
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
    for (var k = 0; k < playersList.length; k++) {
        if (max_arr.includes(k) && playersList.length > 1) {
            output += "<td class = \"winner\">" + stat_list[k] + "</td>";
        }
        else if ((min_arr.includes(k) || stat[k] == 0) && playersList.length > 1) {
            console.log(min_arr);
            output += "<td class = \"loser\">" + stat_list[k] + "</td>";
        }
        else {
            output += "<td>" + stat_list[k] + "</td>";
        }
    }
    return output;
}

function pct_gen(playersList, type) {
    attempts = type + "_attempts";
    makes = type + "_makes";
    tableBody = "";
    var pcts = [];
    var pcts_strings = [];
    for (var k = 0; k < playersList.length; k++) {

        var pct;

        if (playersList[k][attempts] > 0) {
            var pct = playersList[k][makes] / playersList[k][attempts] * 100;
            //cts.push(parseInt(pct));
            pcts.push(pct);
            pct = pct + "";
            pct = pct.substring(0, 5) + "%";
            pct.replace(' ', '');
            //pct = "" + playersList[k]['makes'] + "/" + playersList[k]['attempts'] + " (" + pct + ")";
            pct = pct + " (" + playersList[k][makes] + "/" + playersList[k][attempts] + ")";
        }
        else {
            pcts.push(0);
            pct = "" + playersList[k][makes] + "/" + playersList[k][attempts];
        }
        pcts_strings.push(pct);


    }
    max_arr = max(pcts);
    min_arr = min(pcts);
    for (var k = 0; k < playersList.length; k++) {
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