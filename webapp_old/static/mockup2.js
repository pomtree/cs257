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
            + team['abbreviation'] //+ ': ' + team['full_name']
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
    // let element = document.getElementById('team_selector');
    // if (!element) {
    //     return;
    // }
    let teamID = this.value;
    let url = getAPIBaseURL() + '/teams/team_stat/' + teamID;

    fetch(url, {method: 'get'})

    .then((response) => response.json())

    .then(function(teams){
        let tableBody = '';
        for (let k = 0; k < teams.length; k++) {
            let team = teams[k];
            tableBody +=    '<tr> <td> 2019-20 Team Stats <td> <tr>\n'
                            + '<tr>'
                            + '<td> Name </td>'
                            + '<td> Overall Record </td>'
                            + '<td> Home Record </td>'
                            + '<td> Away Record </td>'
                            + '<td> OT Record </td>'
                            + '<td> Points </td>'
                            + '<td> Rebound</td>'
                            + '<td> Assists </td>'
                            + '</tr>\n' + 
                            '<tr>'
                            + '<td>' + team['name'] + '</td>'
                            + '<td>' + team['total_wins'] + ' - ' + team['total_losses']+ '</td>'
                            + '<td>' + team['h_wins'] + ' - ' + team['h_losses'] + '</td>'
                            + '<td>' + team['a_wins'] + ' - ' + team['a_losses'] + '</td>'
                            + '<td>' + team['ot_wins'] + ' - ' + team['ot_losses'] + '</td>'
                            + '<td>' + team['points_per_game'] + '</td>'
                            + '<td>' + team['rebounds_per_game'] + '</td>'
                            + '<td>' + team['assists_per_game'] + '</td>'
                            + '</tr>\n';

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


