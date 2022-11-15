/*
    mockup2.js
    Doug Pham and Tom Pree
    November 11, 2022

    Add team button

*/
window.onload = initialize;

function initialize() {
    loadTeamSelector();

    let element = document.getElementById('team_selector');
    if (element) {
        element.onchange = onTeamSelectionChanged;
    }

    // var button = document.getElementById('addTeam');
    // button.onclick = compareTeam
    // var button2 = document.getElementById('backHome');
    // button.onclick = backToHome
}


// Returns the base URL of the API, onto which endpoint
// components can be appended.
function getAPIBaseURL() {
    let baseURL = window.location.protocol
                    + '//' + window.location.hostname
                    + ':' + window.location.port
                    + '/api';
    return baseURL;
}

function loadTeamSelector() {
    let url = getAPIBaseURL() + '/teams/';
    
    // Send the request to the books API /authors/ endpoint
    fetch(url, {method: 'get'})

    // When the results come back, transform them from a JSON string into
    // a Javascript object (in this case, a list of author dictionaries).
    .then((response) => response.json())

    // Once you have your list of author dictionaries, use it to build
    // an HTML table displaying the author names and lifespan.
    .then(function(teams) {
        // Add the <option> elements to the <select> element
        let selectorBody = '';
        for (let k = 0; k < teams.length; k++) {
            let team = teams[k];
            selectorBody += '<option value="' + team['abbreviation'] + '">'
            + team['abbreviation'] + ': ' + team['full_name']
            + '</option>\n'

        }
        let selector = document.getElementById('team_selector');
        if (selector) {
            selector.innerHTML = selectorBody;
        }
    })
    .catch(function(error) {
        console.log(error);
    });
}

function onTeamSelectionChanged() {
    let element = document.getElementById('team_selector');
    if (!element) {
        return;
    }
    let teamID = element.value;
    let url = getAPIBaseURL() + '/teams/team_stat/' + teamID;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(teams){
        let tableBody = '';
        for (let k = 0; k < teams.length; k++) {
            let team = teams[k];
            tableBody += '<tr>'
                            + '<td>' + team['full_name'] + '</td>'
                            + '<td>' + team['total_wins'] + ' - ' + team['total_losses']+ '</td>'
                            + '<td>' + team['h_wins'] + ' - ' + team['h_losses'] + '</td>'
                            + '<td>' + team['a_wins'] + ' - ' + team['a_losses'] + '</td>'
                            + '<td>' + team['ot_wins'] + ' - ' + team['ot_losses'] + '</td>'
                            + '<td>' + team['points_per_game'] + '</td>'
                            + '<td>' + team['rebounds_per_game'] + '</td>'
                            + '<td>' + team['assists_per_game'] + '</td>'
                            + '</tr>\n';
            // 'full_name':row[1], 'total_wins':row[2], 'total_losses':row[3], 'h_wins':row[4], 'h__losses':row[5], 'a_wins':row[6], 'a_losses':row[7], 'ot_wins':row[8], 'ot_losses':row[9], 'points_per_game':row[10], 'rebounds_per_game':row[11], 'assists_per_game':row[12]
        }
        let teamsTable = document.getElementById('teams_table')
        if (teamsTable) {
            teamsTable.innerHTML = tableBody;
        }
    })

    .catch(function(error) {
        console.log(error);
    });
}


