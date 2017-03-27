$("#jsGrid").jsGrid({
        width: "100%",
        // height: "400px",
 
        inserting: false,
        editing: false,
        sorting: true,
        paging: false,
        controller: {
            // loadData: 
        }
 
        fields: [
            { name: "Name", type: "text", width: 150, validate: "required" },
            { name: "Age", type: "number", width: 50 },
            { name: "Address", type: "text", width: 200 },
            { name: "Country", type: "select", items: countries, valueField: "Id", textField: "Name" },
            { name: "Married", type: "checkbox", title: "Is Married", sorting: false },
            { type: "control" }
        ]
    });