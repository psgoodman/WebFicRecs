$("#jsGrid").jsGrid({
    width: "1500",
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
        {
            name:"title",
            title: "Title",
            type: "text",
            headercss: "title-header",
            css: "title-cell",
            width: 150,
            itemTemplate: function(value, item) {
                var html = '<a href="' + item.url + '">' + value + '</a>'
                return html
            }
        },
        { name:"url", title: "URL", type: "text", visible: false, sorting: false },
        { name:"synopsis", title: "Synopsis", type: "text", width: 300, sorting: false },
        {
            name:"rating",
            title: "Rating",
            type: "number",
            headercss: "rating-header",
            css: "rating-cell",
            width: 70,
            itemTemplate: function(value, item) {
                var ratings = ["A+", "A", "A-","B+", "B", "B-","C+", "C", "C-"]
                return ratings[value]
            }
        },
        { name:"comments", title: "Comments", type: "text", width: 300, sorting: false },
        {
            name: "length",
            title: "Length",
            type: "number",
            width: 70
        },
        { name:"author", title: "Author", type: "text", width: 100 },
        { name:"complete", title: "Complete", type: "text", width: 70 },
        { name:"mood", title: "Mood", type: "text", width: 120 },
        {
            name: "tvtropes",
            title: "TV Tropes",
            type: "text",
            width: 150,
            sorting: false,
            itemTemplate: function(value, item) {
                if (value === "") {return ""}
                var html = '<a href="' + value + '">' + item.title + '</a>'
                return html
            }
        }
    ]
});
