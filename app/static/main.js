$("#jsGrid").jsGrid({
        width: "auto",
        // height: "400px",
 
        inserting: false,
        editing: false,
        sorting: true,
        paging: false,
        controller: {
            loadData: function(filter) {
                return $.ajax({
                    type: "GET",
                    url: "data"
                });
            }
        },
 
        fields: [
            { name: "Title", type: "text", width: 150 },
            { name: "URL", type: "text", visible: false, sorting: false },
            { name: "Synopsis", type: "text", width: 300, sorting: false },
            { name: "Rating", type: "number", width: 50 },
            { name: "Comments", type: "text", width: 300, sorting: false },
            {
                name: "Length",
                title: "Length (in words, often a rough estimate",
                type: "number",
                width: 50
            },
            { name: "Author", type: "text", width: 80 },
            { name: "Complete", type: "text", width: 50 },
            { name: "Mood", type: "text", width: 150 },
            { name: "tvtropes", title: "TV Tropes", type: "text", width: 150,
                sorting: false }
        ]
    });