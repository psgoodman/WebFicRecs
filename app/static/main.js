$("#jsGrid").jsGrid({
    width: "auto",
    // height: "400px",
    autoload: true,
    inserting: false,
    editing: false,
    sorting: true,
    paging: false,
    controller: {
        loadData: function(filter) {
            return $.ajax({
                type: "GET",
                url: "/data",
                data: filter
            });
        }
    },

    fields: [
        { name:"title", title: "Title", type: "text", width: 150 },
        { name:"url", title: "URL", type: "text", visible: false, sorting: false },
        { name:"synopsis", title: "Synopsis", type: "text", width: 300, sorting: false },
        { name:"rating", title: "Rating", type: "number", width: 50 },
        { name:"comments", title: "Comments", type: "text", width: 300, sorting: false },
        {
            name: "length",
            title: "Length",
            type: "number",
            width: 50
        },
        { name:"author", title: "Author", type: "text", width: 80 },
        { name:"complete", title: "Complete", type: "text", width: 50 },
        { name:"mood", title: "Mood", type: "text", width: 150 },
        { name: "tvtropes", title: "TV Tropes", type: "text", width: 150,
            sorting: false }
    ]
});
