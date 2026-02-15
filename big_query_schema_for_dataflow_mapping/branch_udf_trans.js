function transform(line) {
    var values = line.split(',');

    // Check if the line is the header by checking the first value
    if (values[0].toLowerCase() === 'branch_id') {
        return null; // Ignore the header row
    }

    var obj = new Object();
    obj.branch_id = values[0];
    obj.branch_name = values[1];
    obj.location = values[2];
    obj.manager_name = values[3];
    obj.opened_date = values[4];
    obj.region = values[5];
	obj.branch_type = values[6];
    obj.contact_number = values[7];
    var jsonString = JSON.stringify(obj);
    return jsonString;
}
