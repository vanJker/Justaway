function addRow() {
    let table = document.getElementById('dataTable');
    let newRow = table.insertRow(table.rows.length);
    console.log(table.rows.length);

    let nameCell = newRow.insertCell(0);
    let emailCell = newRow.insertCell(1);
    let actionCell = newRow.insertCell(2);

    nameCell.innerHTML = 'New User';
    emailCell.innerHTML = 'newuser@example.com';
    actionCell.innerHTML = '<button onclick="editRow(this)">Edit</button>' +
                            '<button onclick="deleteRow(this)">Delete</button>';
}

function deleteRow(button) {
    let row = button.parentNode.parentNode;
    row.parentNode.removeChild(row);
}

function editRow(button) {
    let row = button.parentNode.parentNode;
    let nameCell = row.cells[0];
    let emailCell = row.cells[1];

    let newName = prompt('Enter new name', nameCell.innerHTML);
    let newEmail = prompt('Enter new rmail', emailCell.innerHTML);

    if (newName !== null && newEmail !== null) {
        nameCell.innerHTML = newName;
        emailCell.innerHTML = newEmail;
    }
}