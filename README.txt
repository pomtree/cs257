AUTHORS: Doug Pham, Thomas Pree

DATA: A list of every play that occured in the NBA during the 2019-20 Season. We compiled it into player specific stats.

FEATURES CURRENTLY WORKING:
    + Sort players by certain statistics (Assists, Blocks, Fouls, Turnovers Caused, Violations, 3 %)
        + displays rank and ties properly
        + 3s show makes/misses and % (sorts by %)
        + limit can be adjusted
        + links to player details
        + has compare check boxes
    + View single player details
    + Compare players
        + loads players sucsessfully from either search or sort input
        + Highlights best/worst player in compare
        + limits the number of players compared at once (so as not to overflow the screen/table, and remain readable)
    + Search players by name
        + Displays players with matching names
        + Suports multi query (e.g., search for Stephen Curry and Russell Westbrook: enter "curry, westbrook")
    + Instant Compare
        + Same as search, but instead of basic results page, instantly loads comparision of all resulting players.


FEATURES NOT YET WORKING:
    -Some stats broken (convert.py needs to be updated to database)
    -General Design/style
        -Likley no side bars needed, could all be in header
        -Colors are ridicious
        -Homepage is just an empty search
    -Lacking data visualizations
    -Code is getting better but still largely very sloppy
    -DB lacks certain basic info
        -player's full first name (no way to differential S. (Steph) Cury and S. (Seth) Curry)
            -This is a limitation of our starting data
        -height/weight etc.