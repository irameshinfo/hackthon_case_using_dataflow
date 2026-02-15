function transform(line) {
    var values = line.split(',');

    // Check if the line is the header by checking the first value
    if (values[0].toLowerCase() === 'account_id') {
        return null; // Ignore the header row
    }

    var obj = new Object();
    obj.account_id = values[0];
    obj.account_name = values[1];
    obj.email = values[2];
    obj.phone_number = values[3];
    obj.address = values[4];
    obj.created_date = values[5];
    var jsonString = JSON.stringify(obj);
    return jsonString;
}
